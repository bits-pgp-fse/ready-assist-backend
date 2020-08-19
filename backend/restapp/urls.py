from django.conf.urls import url 
from restapp import views 
from restapp import views_city
from restapp import views_services
from restapp import views_expertise 
from restapp import views_authentication 
from restapp import views_job
from restapp import views_feedback
from restapp import views_payment
 
urlpatterns = [ 
    #url(r'^api/tutorials/', views.tutorial_list),
    #url(r'^api/tutorials/(?P<pk>[0-9]+)$', views.tutorial_detail),
    #url(r'^api/tutorials/published$', views.tutorial_list_published),

    url(r'^api/core/cities$', views_city.city_list),
    url(r'^api/core/cities/services$', views_city.city_services_list),

    url(r'^api/authentication/registration$', views_authentication.register)  ,
    url(r'^api/authentication/login$', views_authentication.login)  ,
    url(r'^api/authentication/change_password$', views_authentication.change_password)  ,
    
    url(r'^api/core/services$', views_services.service_list)  ,
    url(r'^api/core/services/(?P<pk>[0-9]+)$', views_services.service_detail),
    url(r'^api/core/services/published$', views_services.service_list_published),
    url(r'^api/core/services/subservices/(?P<pk>[0-9]+)$', views_services.service_subservices),
    
    url(r'^api/core/subservices$', views_services.subservice_list)  ,
    url(r'^api/core/subservices/(?P<pk>[0-9]+)$', views_services.subservice_detail),
    url(r'^api/core/subservices/published$', views_services.subservice_list_published),
    
    url(r'^api/core/customers$', views.customer_list)  ,
    url(r'^api/core/customers/(?P<pk>[0-9]+)$', views.customer_detail),
    
    url(r'^api/core/experts$', views.expert_list)  ,
    url(r'^api/core/experts/(?P<pk>[0-9]+)$', views.expert_detail),
    url(r'^api/core/experts/expertise/(?P<pk>[0-9]+)$', views_expertise.expert_expertices),

    url(r'^api/core/expertise$', views_expertise.expertise_list)  ,
    url(r'^api/core/expertise/(?P<pk>[0-9]+)$', views_expertise.expertise_detail),

    url(r'^api/core/jobs$', views_job.jobs_list)  ,
    url(r'^api/core/jobs/(?P<pk>[0-9]+)$', views_job.jobs_detail),
    url(r'^api/core/jobs/jobs_filters$', views_job.job_filters),

    url(r'^api/core/payments$', views_payment.payments_list)  ,
    url(r'^api/core/payments/(?P<pk>[0-9]+)$', views_payment.payments_detail),
    url(r'^api/core/payments/job/(?P<pk>[0-9]+)$', views_payment.job_payment),
    url(r'^api/core/payments/mode/(?P<pk>.+)$', views_payment.mode_payment),
    url(r'^api/core/payments/status/(?P<pk>.+)$', views_payment.status_payment),

    url(r'^api/core/feedbacks$', views_feedback.feedback_list)  ,
    url(r'^api/core/feedbacks/(?P<pk>[0-9]+)$', views_feedback.feedback_detail),
    url(r'^api/core/feedbacks/job/(?P<pk>[0-9]+)$', views_feedback.job_feedback),
    url(r'^api/core/feedbacks/expert/(?P<pk>[0-9]+)$', views_feedback.expert_feedback),
    url(r'^api/core/feedbacks/expert_rating/(?P<pk>[0-9]+)$', views_feedback.expert_feedback_rating),
    url(r'^api/core/feedbacks/customer/(?P<pk>[0-9]+)$', views_feedback.customer_feedback)

]