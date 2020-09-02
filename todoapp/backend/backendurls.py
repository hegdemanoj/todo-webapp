from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url

from backend.views import BucketViewSet,CreateBucket,Getbybucketid,CreateTask,UpdateTask


urlpatterns = [
    path('buckets/', BucketViewSet.as_view()),
    path('newbucket/', CreateBucket.as_view()),
    
    # url(r"^buckets-test/$", BucketViewSet.as_view()),
    path('tasks/', Getbybucketid.as_view()),
    path('newtask/', CreateTask.as_view()),
    path('edittask/', UpdateTask.as_view()),
]