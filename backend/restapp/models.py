from django.db import models

class Tutorial(models.Model):
    title = models.CharField(max_length=70, blank=False, default='')
    description = models.CharField(max_length=200,blank=False, default='')
    publication = models.CharField(max_length=70, blank=False, default='')
    published = models.BooleanField(default=False)
    
class MyService(models.Model):
    name = models.CharField(max_length=70, blank=False, default='')
    description = models.CharField(max_length=200,blank=False, default='')
    is_available = models.BooleanField(default=False)
    
class SubService(models.Model):
    name = models.CharField(max_length=70, blank=False, default='')
    details = models.CharField(max_length=200,blank=False, default='')
    charges = models.IntegerField(default=False)    
    is_available = models.BooleanField(default=False)
    service_id = models.IntegerField(default=-1)
    
class Customer(models.Model):
    name = models.CharField(max_length=70, blank=True, default='')
    phone = models.IntegerField( blank=True)
    email = models.CharField(max_length=200,blank=False, default='')
    password = models.CharField(max_length=200,blank=False, default='')
    address = models.CharField(max_length=200,blank=True, default='')
    city = models.CharField(max_length=200,blank=True, default='')
    pincode = models.IntegerField(blank=True)
    
class Expert(models.Model):
    name = models.CharField(max_length=70, blank=True, default='')
    phone = models.IntegerField(blank=True)
    email = models.CharField(max_length=200,blank=False, default='')
    password = models.CharField(max_length=200,blank=False, default='')
    address = models.CharField(max_length=200,blank=True, default='')
    city = models.CharField(max_length=200,blank=True, default='')
    pincode = models.IntegerField(blank=True)    
    rating = models.IntegerField(blank=True)    
    
class Expertise(models.Model):    
    subservice_id = models.IntegerField()
    expert_id = models.IntegerField()

class Job(models.Model):    
    cust_id = models.IntegerField()
    service_id = models.IntegerField(default=-1)
    subservice_id = models.IntegerField(default=-1)
    expert_id = models.IntegerField(default=-1)  
    payment_id = models.IntegerField(default=-1) 
    address = models.CharField(max_length=200,blank=True, default='')
    city_id = models.IntegerField(default=-1) 
    start_date = models.DateField()  
    start_time = models.TimeField()
    end_date = models.DateField(default='2020-12-31')
    end_time = models.TimeField(default='11:59:00')
    job_status = models.CharField(max_length=20,blank=False, default='') 
    updated_by = models.IntegerField(default=-1)
    updated_by_type = models.CharField(max_length=20,blank=False, default='') 

class Payment(models.Model):
    pay_mode = models.CharField(max_length=20,blank=False, default='') 
    job_id = models.IntegerField()
    cust_id = models.IntegerField(default=-1)
    expert_id = models.IntegerField(default=-1)
    charges = models.IntegerField()
    pay_status = models.CharField(max_length=20,blank=False, default='') 

class Feedback(models.Model):    
    job_id = models.IntegerField()
    cust_id = models.IntegerField(default=-1)
    expert_id = models.IntegerField(default=-1)
    desc = models.CharField(max_length=100,blank=False, default='') 
    rating = models.IntegerField()

class City(models.Model):
    name = models.CharField(max_length=20,blank=False, default='') 

class CityServiceSubservice(models.Model):
    city_id = models.IntegerField()
    service_id = models.IntegerField()
    subservice_id = models.IntegerField()
