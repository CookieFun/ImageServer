from django.shortcuts import render
from rest_framework.views import APIView
from app.serializer import PhotoSerializer
from rest_framework.response import Response
from rest_framework import status
from app.models import MyPhoto
from django.http import Http404
from django.shortcuts import render
from rest_framework.parsers import MultiPartParser, FormParser

# Create your views here.
class PhotoList(APIView):
    #parser_classes = (MultiPartParser, FormParser,)

    def get(self, request, format=None):
        photo = MyPhoto.objects.all()
        serializer = PhotoSerializer(photo, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
       serializer = PhotoSerializer(data=request.data)
       print("!")
       if serializer.is_valid():
           serializer.save()
           return Response(serializer.data, status=status.HTTP_201_CREATED)
       return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PhotoDetail(APIView):

    def get_object(self, pk):
        try:
            return MyPhoto.objects.get(pk=pk)
        except MyPhoto.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        print("get")
        photo = self.get_object(pk)
        serializer = PhotoSerializer(photo)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        photo = self.get_object(pk)
        serializer = PhotoSerializer(photo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        photo = self.get_object(pk)
        photo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

def show_img(request, path):
    print(path)
    return render(request, 'show_img.html', {
        "img_url": path,
    })
