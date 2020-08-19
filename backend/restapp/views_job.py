from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
from rest_framework.decorators import api_view

from restapp.models import Job
from restapp.serializers import JobSerializer

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

####################   Jobs       
      
@api_view(['GET', 'POST', 'DELETE'])
def jobs_list(request):
    # GET list of Feedback, POST a new Feedback, DELETE all Feedback
    if request.method == 'GET':
        jobs = Job.objects.all()      
        jobs_serializer = JobSerializer(jobs, many=True)
        return JsonResponse(jobs_serializer.data, safe=False)
        # 'safe=False' for objects serialization
 
    elif request.method == 'POST':
        jobs_data = JSONParser().parse(request)
        jobs_serializer = JobSerializer(data=jobs_data)
        if jobs_serializer.is_valid():
            jobs_serializer.save()
            send_email(5)
            return JsonResponse(jobs_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(jobs_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = Job.objects.all().delete()
        return JsonResponse({'message': '{} Jobs were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)         
        
        
@api_view(['GET', 'PUT', 'DELETE'])
def jobs_detail(request, pk):
    # find feedback by pk (id)
    try: 
        job = Job.objects.get(pk=pk) 
    except Job.DoesNotExist: 
        return JsonResponse({'message': 'The job details not available'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        jobs_serializer = JobSerializer(job) 
        return JsonResponse(jobs_serializer.data) 
 
    elif request.method == 'PUT': 
        jobs_data = JSONParser().parse(request) 
        jobs_serializer = JobSerializer(job, data=jobs_data) 
        if jobs_serializer.is_valid(): 
            jobs_serializer.save() 
            return JsonResponse(jobs_serializer.data) 
        return JsonResponse(jobs_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        job.delete() 
        return JsonResponse({'message': 'The job was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT) 
        
@api_view(['GET'])
def jobs_feedback(request, pk):
    jobs = Job.objects.all()
    #TODO - apply filtering based on job id 
    job = jobs.filter(id__exact=int(pk))    
    if request.method == 'GET': 
        jobs_serializer = JobSerializer(jobs, many=True)
        return JsonResponse(jobs_serializer.data, safe=False) 

#http://localhost:8090/api/core/jobs/jobs_filters?start_date=2020-10-10&end_date=2020-12-12
@api_view(['GET'])
def job_filters(request):
    service_type = request.GET.get('service_type', None)
    service_status = request.GET.get('service_status', None)
    start_date = request.GET.get('start_date', None)
    end_date = request.GET.get('end_date', None)
    customer_id = request.GET.get('customer_id', None)
    expert_id = request.GET.get('expert_id', None)
    city_id = request.GET.get('city_id', None)

    jobs = Job.objects.all()

    if(service_type != None):
        jobs = jobs.filter(service_id__exact=int(service_type))    
    if(service_status != None):
        jobs = jobs.filter(job_status__exact=service_status)    
    if(start_date != None and end_date != None):
        jobs = jobs.filter(start_date__gte=start_date)    
        jobs = jobs.filter(end_date__lte=end_date)    
    if(customer_id != None):
        jobs = jobs.filter(cust_id__exact=int(customer_id))    
    if(expert_id != None):
        jobs = jobs.filter(expert_id__exact=int(expert_id))    
    if(city_id != None):
        jobs = jobs.filter(city_id__exact=int(city_id))       
        #jobs = jobs.filter(job_status__icontains='Active')    

    if request.method == 'GET': 
        jobs_serializer = JobSerializer(jobs, many=True)
        return JsonResponse(jobs_serializer.data, safe=False) 

def send_email(id):
    mail_content = "Your request with ID " + str(id) + " is registered!"
    #The mail addresses and password
    sender_address = 'ppawar@wilp.bits-pilani.ac.in'
    sender_pass = 'Rishi1234'
    receiver_address = 'pravin.pawar@pilani.bits-pilani.ac.in'

    #Setup the MIME
    message = MIMEMultipart()
    message['From'] = sender_address
    message['To'] = receiver_address
    message['Subject'] = 'A test mail sent by Python. It has an attachment.'   #The subject line
    message.attach(MIMEText(mail_content, 'plain'))
    
    #Create SMTP session for sending the mail
    session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
    session.starttls() #enable security
    session.login(sender_address, sender_pass) #login with mail_id and password
    text = message.as_string()
    session.sendmail(sender_address, receiver_address, text)
    session.quit()