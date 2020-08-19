from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
from rest_framework.decorators import api_view

from restapp.models import Feedback
from restapp.serializers import FeedbackSerializer

####################   Feedback       
      
@api_view(['GET', 'POST', 'DELETE'])
def feedback_list(request):
    # GET list of Feedback, POST a new Feedback, DELETE all Feedback
    if request.method == 'GET':
        feedbacks = Feedback.objects.all()      
        feedback_serializer = FeedbackSerializer(feedbacks, many=True)
        return JsonResponse(feedback_serializer.data, safe=False)
        # 'safe=False' for objects serialization
 
    elif request.method == 'POST':
        feedback_data = JSONParser().parse(request)
        feedback_serializer = FeedbackSerializer(data=feedback_data)
        if feedback_serializer.is_valid():
            feedback_serializer.save()
            return JsonResponse(feedback_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(feedback_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = Feedback.objects.all().delete()
        return JsonResponse({'message': '{} Feedbacks were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)         
        
        
@api_view(['GET', 'PUT', 'DELETE'])
def feedback_detail(request, pk):
    # find feedback by pk (id)
    try: 
        feedback = Feedback.objects.get(pk=pk) 
    except Feedback.DoesNotExist: 
        return JsonResponse({'message': 'The feedback not available'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        feedback_serializer = FeedbackSerializer(feedback) 
        return JsonResponse(feedback_serializer.data) 
 
    elif request.method == 'PUT': 
        feedback_data = JSONParser().parse(request) 
        feedback_serializer = FeedbackSerializer(service, data=feedback_data) 
        if feedback_serializer.is_valid(): 
            feedback_serializer.save() 
            return JsonResponse(feedback_serializer.data) 
        return JsonResponse(feedback_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        feedback.delete() 
        return JsonResponse({'message': 'The feedback was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT) 
        
@api_view(['GET'])
def job_feedback(request, pk):
    feedback = Feedback.objects.all()
    feedback = feedback.filter(job_id__exact=int(pk))
    if request.method == 'GET': 
        feedback_serializer = FeedbackSerializer(feedback, many=True)
        return JsonResponse(feedback_serializer.data, safe=False) 

@api_view(['GET'])
def expert_feedback(request, pk):
    feedbacks = Feedback.objects.all()
    feedbacks = feedbacks.filter(expert_id__exact=int(pk))
    rating = 0 
    count = 0 
    for f in feedbacks:
        f_rating = feedbacks['rating']
        count = count + 1
        rating = rating + f_rating

    avg_rating = rating / count 

    if request.method == 'GET': 
        return JsonResponse({'avg_rating': avg_rating}, status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def expert_feedback_rating(request, pk):
    feedbacks = Feedback.objects.all()
    feedback = feedbacks.filter(expert_id__exact=int(pk))
    if request.method == 'GET': 
        feedback_serializer = FeedbackSerializer(feedback, many=True)
        return JsonResponse(feedback_serializer.data, safe=False) 


@api_view(['GET'])
def customer_feedback(request, pk):
    feedbacks = Feedback.objects.all()
    feedback = feedbacks.filter(_id__exact=int(pk))
    if request.method == 'GET': 
        feedback_serializer = FeedbackSerializer(feedback, many=True)
        return JsonResponse(feedback_serializer.data, safe=False) 
