from django.shortcuts import render
# from backend.models import Bucket
from backend import models
from rest_framework.response import Response
from rest_framework import status

from django.contrib.auth.models import User, Group
from rest_framework import serializers
from rest_framework import generics
# from rest_framework import viewsets
from rest_framework import permissions

# Views & Serializers
class BucketSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Bucket
        # fields = ['url', 'username', 'email', 'groups']
        fields = '__all__'

class BucketViewSet(generics.ListAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = models.Bucket.objects.all()
    serializer_class = BucketSerializer



class todolistSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Todolist
        fields = '__all__'

class Getbybucketid(generics.ListAPIView):

    def list(self, request):
        try:
            bucket_id = self.request.GET.get('id')
            queryset = models.Todolist.objects.filter(bucket__id=bucket_id)
            serializer_class = todolistSerializer(queryset,many=True)
            return Response(serializer_class.data, status=status.HTTP_200_OK)

        except:
            return Response("Not able to get the details",
                            status=status.HTTP_400_BAD_REQUEST)

class CreateTask(generics.ListCreateAPIView):
    def post(self, request):
        try:
            bucketid = self.request.query_params.get('bucketid')
            text =self.request.query_params.get('text')
            new_task = models.Todolist.objects.create(bucket_id=bucketid,text=text)
            serializer_class = todolistSerializer(new_task)
            return Response(serializer_class.data, status=status.HTTP_200_OK)

        except:
            return Response("Not able to get the details",
                            status=status.HTTP_400_BAD_REQUEST)


class UpdateTask(generics.UpdateAPIView):
    def put(self, request):
        try:
            import pdb;pdb.set_trace()
            taskid = self.request.query_params.get('id')
            data=dict()
            
            data['text'] = self.request.query_params.get('text')
            data['completed'] = self.request.query_params.get('completed')
            taskobj = models.Todolist.objects.get(id=taskid)
            data['bucket'] = taskobj.bucket.id
            # new_task = models.Todolist.objects.update(id=taskid,text=text, completed=completed)
            serializer_class = todolistSerializer(taskobj, data)
            serializer_class.is_valid(raise_exception=True)
            self.perform_update(serializer_class)
            return Response(serializer_class.data, status=status.HTTP_200_OK)

        except:
            return Response("Not able to get the details",
                            status=status.HTTP_400_BAD_REQUEST)

class CreateBucket(generics.ListCreateAPIView):
    def post(self, request):
        try:
            bucketname = self.request.query_params.get('bucket_name')
            new_bucket = models.Bucket.objects.create(bucket_name=bucketname)
            serializer_class = BucketSerializer(new_bucket)
            return Response(serializer_class.data, status=status.HTTP_200_OK)

        except:
            return Response("Not able to get the details",
                            status=status.HTTP_400_BAD_REQUEST)