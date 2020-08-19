from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status

from rest_framework.decorators import api_view

from restapp.models import City
from restapp.serializers import CitySerializer

from restapp.models import CityServiceSubservice
from restapp.serializers import CityServiceSubserviceSerializer

####################   City   
# TODO - Add Fixtures for city    
      
@api_view(['GET', 'POST', 'DELETE'])
def city_list(request):
    # GET list of cities, POST a new city, DELETE all cities
    if request.method == 'GET':
        cities= City.objects.all()
        city_serializer = CitySerializer(cities, many=True)
        return JsonResponse(city_serializer.data, safe=False)
        # 'safe=False' for objects serialization
    elif request.method == 'POST':
        #TODO : Replace with fixtures
        city_data = JSONParser().parse(request)
        city_serializer = CitySerializer(data=city_data)
        if city_serializer.is_valid():
            city_serializer.save()
            return JsonResponse(city_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(city_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
         #TODO : Comment out once fixtures are implemented
        count = City.objects.all().delete()
        return JsonResponse({'message': '{} Cities were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)         
        
@api_view(['GET', 'POST', 'DELETE'])
def city_services_list(request):
    if request.method == 'GET':
        citi_services= CityServiceSubservice.objects.all()
        city_id = request.GET.get('city_id', None)
        if(city_id != None):
            citi_services = citi_services.filter(city_id__exact=int(city_id)) 
        city_service_serializer = CityServiceSubserviceSerializer(citi_services, many=True)
        return JsonResponse(city_service_serializer.data, safe=False)
        # 'safe=False' for objects serialization
    elif request.method == 'POST':
        #TODO : Replace with fixtures
        city_service_data = JSONParser().parse(request)
        city_service_serializer = CityServiceSubserviceSerializer(data=city_service_data)
        if city_service_serializer.is_valid():
            city_service_serializer.save()
            return JsonResponse(city_service_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(city_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        #TODO : Comment out once fixtures are implemented
        count = CityServiceSubservice.objects.all().delete()
        return JsonResponse({'message': '{} Entries were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)         
   
