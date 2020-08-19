from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status

from restapp.models import Tutorial
from restapp.serializers import TutorialSerializer
from restapp.models import MyService
from restapp.serializers import MyServiceSerializer
from restapp.models import SubService
from restapp.serializers import SubServiceSerializer
from restapp.models import Customer
from restapp.serializers import CustomerSerializer
from restapp.models import Expert
from restapp.serializers import ExpertSerializer
from restapp.models import Expert
from restapp.serializers import ExpertSerializer
from restapp.models import Expertise
from restapp.serializers import ExpertiseSerializer

from rest_framework.decorators import api_view

####################   Expertise       
      
@api_view(['GET', 'POST', 'DELETE'])
def expertise_list(request):
    # GET list of expertise, POST a new expertise, DELETE all expertise
    if request.method == 'GET':
        expertise = Expertise.objects.all()
        expertise_serializer = ExpertiseSerializer(expertise, many=True)
        return JsonResponse(expertise_serializer.data, safe=False)
        # 'safe=False' for objects serialization
 
    elif request.method == 'POST':
        expertise_data = JSONParser().parse(request)
        expertise_serializer = ExpertiseSerializer(data=expertise_data)
        if expertise_serializer.is_valid():
            expertise_serializer.save()
            return JsonResponse(expertise_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(expertise_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = Expertise.objects.all().delete()
        return JsonResponse({'message': '{} Expertises were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)         
        
        
@api_view(['GET', 'PUT', 'DELETE'])
def expertise_detail(request, pk):
    # find service by pk (id)
    try: 
        expertise = Expertise.objects.get(pk=pk) 
    except Expertise.DoesNotExist: 
        return JsonResponse({'message': 'The Expertise does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        expertise_serializer = ExpertiseSerializer(service) 
        return JsonResponse(expertise_serializer.data) 
 
    elif request.method == 'PUT': 
        expertise_data = JSONParser().parse(request) 
        expertise_serializer = ExpertiseSerializer(expertise, data=expertise_data) 
        if expertise_serializer.is_valid(): 
            expertise_serializer.save() 
            return JsonResponse(expertise_serializer.data) 
        return JsonResponse(expertise_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        expertise.delete() 
        return JsonResponse({'message': 'Expertise was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT) 
        
@api_view(['GET'])
def expert_expertices(request, pk):
    experts = Expert.objects.get(expert_id=pk) 

    if request.method == 'GET': 
        expertise_serializer = ExpertiseSerializer(expertise, many=True)
        return JsonResponse(expertise_serializer.data, safe=False)           
         
