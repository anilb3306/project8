from django.urls import path
from app1.views import *
app_name="kumar"

urlpatterns=[
    path('app1/',app1,name='app1'),
]