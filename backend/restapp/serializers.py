from rest_framework import serializers 
from restapp.models import Tutorial
from restapp.models import MyService
from restapp.models import SubService
from restapp.models import Customer
from restapp.models import Expert
from restapp.models import Expertise
from restapp.models import Job
from restapp.models import Payment
from restapp.models import Feedback
from restapp.models import City
from restapp.models import CityServiceSubservice

class TutorialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tutorial
        fields = ('id',
                  'title',
                  'description',
                  'publication',
                  'published')
                  
class MyServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyService
        fields = ('id',
                  'name',
                  'description', 
                  'is_available')    

class SubServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubService
        fields = ('id',
                  'name',
                  'details', 
                  'charges',
                  'is_available',
                  'service_id')                  
      
class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('id',
                  'name',
                  'phone', 
                  'email',
                  'password',
                  'address',
                  'city',
                  'pincode')                    

class ExpertSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expert
        fields = ('id',
                  'name',
                  'phone', 
                  'email',
                  'password',
                  'pincode', 
                  'rating')   

class ExpertiseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expertise
        fields = ('subservice_id',
                  'expert_id')                   


class ExpertSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expert
        fields = ('id',
                  'name',
                  'phone', 
                  'email',
                  'password',
                  'pincode', 
                  'rating') 

class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = ('id',
                  'cust_id',
                  'service_id',
                  'subservice_id', 
                  'expert_id',
                  'payment_id',
                  'address',
                  'city_id',
                  'start_date',
                  'start_time',
                  'end_date',
                  'end_time',
                  'job_status', 
                  'updated_by', 
                  'updated_by_type')                     

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ('id',
                  'pay_mode',
                  'job_id', 
                  'expert_id', 
                  'cust_id',
                  'charges',
                  'pay_status')  

class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = ('id',
                  'job_id',
                  'expert_id', 
                  'cust_id',
                  'desc', 
                  'rating') 

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ('id',
                  'name')                   


class CityServiceSubserviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = CityServiceSubservice
        fields = ('city_id',
                  'service_id', 
                  'subservice_id')                     