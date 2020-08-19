from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
from rest_framework.decorators import api_view

from restapp.models import MyService
from restapp.serializers import MyServiceSerializer
from restapp.models import SubService
from restapp.serializers import SubServiceSerializer

####################   Service       
      
@api_view(['GET', 'POST', 'DELETE'])
def service_list(request):
    # GET list of services, POST a new service, DELETE all service
    if request.method == 'GET':
        services = MyService.objects.all()
        
        name = request.GET.get('name', None)
        if name is not None:
            services = services.filter(title__icontains=name)
        
        services_serializer = MyServiceSerializer(services, many=True)
        return JsonResponse(services_serializer.data, safe=False)
        # 'safe=False' for objects serialization
 
    elif request.method == 'POST':
        service_data = JSONParser().parse(request)
        service_serializer = MyServiceSerializer(data=service_data)
        if service_serializer.is_valid():
            service_serializer.save()
            return JsonResponse(service_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(service_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = MyService.objects.all().delete()
        return JsonResponse({'message': '{} Services were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)         
        
        
@api_view(['GET', 'PUT', 'DELETE'])
def service_detail(request, pk):
    # find service by pk (id)
    try: 
        service = MyService.objects.get(pk=pk) 
    except MyService.DoesNotExist: 
        return JsonResponse({'message': 'The service does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        service_serializer = MyServiceSerializer(service) 
        return JsonResponse(service_serializer.data) 
 
    elif request.method == 'PUT': 
        service_data = JSONParser().parse(request) 
        service_serializer = MyServiceSerializer(service, data=service_data) 
        if service_serializer.is_valid(): 
            service_serializer.save() 
            return JsonResponse(service_serializer.data) 
        return JsonResponse(service_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        service.delete() 
        return JsonResponse({'message': 'Service was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT) 
        
@api_view(['GET'])
def service_list_published(request):
    # GET all published services
    services = MyService.objects.filter(is_available=True)
        
    if request.method == 'GET': 
        service_serializer = MyServiceSerializer(services, many=True)
        return JsonResponse(service_serializer.data, safe=False)           

@api_view(['GET'])
def service_subservices(request, pk):
    # GET all published services
    subservices = SubService.objects.filter(pk=pk)
        
    if request.method == 'GET': 
        subservice_serializer = SubServiceSerializer(subservices, many=True)
        return JsonResponse(subservice_serializer.data, safe=False)           

        
####################   SubService       
      
@api_view(['GET', 'POST', 'DELETE'])
def subservice_list(request):
    # GET list of services, POST a new service, DELETE all service
    if request.method == 'GET':
        sub_services = SubService.objects.all()
        
        name = request.GET.get('name', None)
        if name is not None:
            sub_services = sub_services.filter(title__icontains=name)
        
        subservices_serializer = SubServiceSerializer(sub_services, many=True)
        return JsonResponse(subservices_serializer.data, safe=False)
        # 'safe=False' for objects serialization
 
    elif request.method == 'POST':
        subservice_data = JSONParser().parse(request)
        subservice_serializer = SubServiceSerializer(data=subservice_data)
        if subservice_serializer.is_valid():
            subservice_serializer.save()
            return JsonResponse(subservice_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(subservice_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = SubService.objects.all().delete()
        return JsonResponse({'message': '{} Subservices were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)         
        
        
@api_view(['GET', 'PUT', 'DELETE'])
def subservice_detail(request, pk):
    # find subservice by pk (id)
    try: 
        subservice = SubService.objects.get(pk=pk) 
    except SubService.DoesNotExist: 
        return JsonResponse({'message': 'The subservice does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        subservice_serializer = SubServiceSerializer(subservice) 
        return JsonResponse(subservice_serializer.data) 
 
    elif request.method == 'PUT': 
        subservice_data = JSONParser().parse(request) 
        subservice_serializer = SubServiceSerializer(subservice, data=subservice_data) 
        if subservice_serializer.is_valid(): 
            subservice_serializer.save() 
            return JsonResponse(subservice_serializer.data) 
        return JsonResponse(subservice_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        subservice.delete() 
        return JsonResponse({'message': 'Subservice was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT) 
        
@api_view(['GET'])
def subservice_list_published(request):
    # GET all published services
    subservices = SubService.objects.filter(is_available=True)
        
    if request.method == 'GET': 
        subservice_serializer = SubServiceSerializer(services, many=True)
        return JsonResponse(subservice_serializer.data, safe=False)           