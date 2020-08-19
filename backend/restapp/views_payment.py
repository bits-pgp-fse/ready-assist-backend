from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
from rest_framework.decorators import api_view

from restapp.models import Payment
from restapp.serializers import PaymentSerializer

####################   Payment       
      
@api_view(['GET', 'POST', 'DELETE'])
def payments_list(request):
    # GET list of Payment, POST a new Payment, DELETE all Payment
    if request.method == 'GET':
        payments = Payment.objects.all()      
        payment_serializer = PaymentSerializer(payments, many=True)
        return JsonResponse(payment_serializer.data, safe=False)
        # 'safe=False' for objects serialization
 
    elif request.method == 'POST':
        payment_data = JSONParser().parse(request)
        payment_serializer = PaymentSerializer(data=payment_data)
        if payment_serializer.is_valid():
            payment_serializer.save()
            return JsonResponse(payment_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(payment_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = Payment.objects.all().delete()
        return JsonResponse({'message': '{} Payment details were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)         
        
        
@api_view(['GET', 'PUT', 'DELETE'])
def payments_detail(request, pk):
    # find feedback by pk (id)
    try: 
        payment = Payment.objects.get(pk=pk) 
    except Payment.DoesNotExist: 
        return JsonResponse({'message': 'The payments details not available'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        payment_serializer = PaymentSerializer(payment) 
        return JsonResponse(payment_serializer.data) 
 
    elif request.method == 'PUT': 
        payment_data = JSONParser().parse(request) 
        payment_serializer = PaymentSerializer(payment, data=payment_data) 
        if payment_serializer.is_valid(): 
            payment_serializer.save() 
            return JsonResponse(payment_serializer.data) 
        return JsonResponse(payment_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        payment.delete() 
        return JsonResponse({'message': 'The job was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT) 
        
@api_view(['GET'])
def job_payment(request, pk):
    payments = Payment.objects.all()
    payment = payments.filter(job_id__exact=int(pk))
    if request.method == 'GET': 
        payment_serializer = PaymentSerializer(payment, many=True)
        return JsonResponse(payment_serializer.data, safe=False)

@api_view(['GET'])
def expert_payment(request, pk):
    payments = Payment.objects.all()
    payment = payments.filter(expert_id__exact=int(pk))
    if request.method == 'GET': 
        payment_serializer = PaymentSerializer(payment, many=True)
        return JsonResponse(payment_serializer.data, safe=False)

@api_view(['GET'])
def mode_payment(request, pk):
    payments = Payment.objects.all()
    payment = payments.filter(pay_mode__icontains=pk)
    if request.method == 'GET': 
        payment_serializer = PaymentSerializer(payment, many=True)
        return JsonResponse(payment_serializer.data, safe=False)

@api_view(['GET'])
def status_payment(request, pk):
    payments = Payment.objects.all()
    payment = payments.filter(pay_status__icontains=pk)
    if request.method == 'GET': 
        payment_serializer = PaymentSerializer(payment, many=True)
        return JsonResponse(payment_serializer.data, safe=False)        
    