from django.shortcuts import render
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
# Create your views here.
from delivery.models import Delivery_Agent,Customer,Delivery
import numpy as np
from rest_framework.permissions import IsAuthenticated
import datetime
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.decorators import authentication_classes
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from django.contrib.gis.geos import Point
from django.contrib.gis.db.models.functions import Distance

from rest_framework.decorators import permission_classes

class Create_Delivery(APIView):
	permission_classes = (IsAuthenticated,) 
	"""
	A view that returns the count of active users in JSON.
	"""
	renderer_classes = [JSONRenderer]

	def post(self, request, format=None):
		agents = Delivery_Agent.objects.all().filter(on_delivery=False)
		node = Point(float(request.POST['x']),float(request.POST['y']), srid=4326)
		location_list = list()
		agent_list = list()
		selected_agent = Delivery_Agent.objects.annotate(distance=Distance('location', node)).order_by('distance').first()
		selected_agent.on_delivery = True
		selected_agent.save()
		delivery = Delivery()
		delivery.customer = Customer.objects.get(user=request.user)
		delivery.delivery_agent = selected_agent
		delivery.pickup_location = node
		delivery.location = selected_agent.location
		delivery.start_time = datetime.datetime.now()
		delivery.total_distance = selected_agent.location.distance(node) * 100
		delivery.save()
		content = {'agent': selected_agent.user.username}
		return Response(content)

@api_view(['POST']) 
@permission_classes([IsAuthenticated])
def reached_pickup(request):
	user = request.user
	try:
		agent = Delivery_Agent.objects.get(user=request.user)
		delivery = Delivery.objects.get(delivery_agent=agent)
		print(delivery)
		delivery.at_pickup = True
		delivery.save()
	except:
		return Response("error:no_agent")
	return Response('status:success')

@api_view(['POST']) 
@permission_classes([IsAuthenticated])
def get_location(request):
	user = request.user
	try:
		agent = Delivery_Agent.objects.get(user=request.user)
		delivery = Delivery.objects.get(delivery_agent=agent)
		content = {'agent':str(delivery.location) }
		return Response(content)
	except:
		return Response("error:no_agent")
	return Response('status:success')

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def delivery_completed(request):
	user = request.user
	try:
		agent = Delivery_Agent.objects.get(user=request.user)
		delivery = Delivery.objects.get(delivery_agent=agent)
		if delivery.completed==True:
			return Response("error:already_delivered")
		else:
			delivery.end_time = datetime.datetime.now()
			delivery.completed = True
			delivery.save()
	except:
		return Response("error:no_agent")
	return Response('status:success')
