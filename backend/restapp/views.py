from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
from rest_framework.decorators import api_view
 
from restapp.models import Customer
from restapp.serializers import CustomerSerializer
from restapp.models import Expert
from restapp.serializers import ExpertSerializer

####################   Customer

@api_view(['GET', 'POST', 'DELETE'])
def customer_list(request):
    # GET list of customers, POST a new customer, DELETE all customer
    if request.method == 'GET':
        customers = Customer.objects.all()
        
        name = request.GET.get('name', None)
        if name is not None:
            customers = customers.filter(name__icontains=name)
        
        customer_serializer = CustomerSerializer(customers, many=True)
        return JsonResponse(customer_serializer.data, safe=False)
        # 'safe=False' for objects serialization
 
    elif request.method == 'POST':
        customer_data = JSONParser().parse(request)
        customer_serializer = CustomerSerializer(data=customer_data)
        if customer_serializer.is_valid():
            customer_serializer.save()
            return JsonResponse(customer_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(customer_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = Customer.objects.all().delete()
        return JsonResponse({'message': '{} Customer were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)       
       
@api_view(['GET', 'PUT', 'DELETE'])
def customer_detail(request, pk):
    # find customer by pk (id)
    try: 
        customer = Customer.objects.get(pk=pk) 
    except Customer.DoesNotExist: 
        return JsonResponse({'message': 'The customer does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        customer_serializer = CustomerSerializer(customer) 
        return JsonResponse(customer_serializer.data) 
 
    elif request.method == 'PUT': 
        customer_data = JSONParser().parse(request) 
        customer_serializer = CustomerSerializer(customer, data=customer_data) 
        if customer_serializer.is_valid(): 
            customer_serializer.save() 
            return JsonResponse(customer_serializer.data) 
        return JsonResponse(customer_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        customer.delete() 
        return JsonResponse({'message': 'Customer was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)


####################   Expert            
@api_view(['GET', 'POST', 'DELETE'])
def expert_list(request):
    # GET list of experts, POST a new expert, DELETE all experts
    if request.method == 'GET':
        experts = Expert.objects.all()
        
        name = request.GET.get('name', None)
        if name is not None:
            experts = experts.filter(name__icontains=name)
        
        expertSerializer = ExpertSerializer(experts, many=True)
        return JsonResponse(expertSerializer.data, safe=False)
        # 'safe=False' for objects serialization
 
    elif request.method == 'POST':
        expert_data = JSONParser().parse(request)
        expertSerializer = ExpertSerializer(data=expert_data)
        if expertSerializer.is_valid():
            expertSerializer.save()
            return JsonResponse(expertSerializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(expertSerializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = Expert.objects.all().delete()
        return JsonResponse({'message': '{} Expert were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)       
       
@api_view(['GET', 'PUT', 'DELETE'])
def expert_detail(request, pk):
    # find Expert by pk (id)
    try: 
        expert = Expert.objects.get(pk=pk) 
    except Expert.DoesNotExist: 
        return JsonResponse({'message': 'The Expert does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        expertSerializer = ExpertSerializer(expert) 
        return JsonResponse(expertSerializer.data) 
 
    elif request.method == 'PUT': 
        expert_data = JSONParser().parse(request) 
        expertSerializer = ExpertSerializer(expert, data=expert_data) 
        if expertSerializer.is_valid(): 
            expertSerializer.save() 
            return JsonResponse(expertSerializer.data) 
        return JsonResponse(expertSerializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        expert.delete() 
        return JsonResponse({'message': 'Expert was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
