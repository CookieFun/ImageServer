import re
from django.shortcuts import render
from rest_framework.views import APIView
from app.serializer import PhotoSerializer
from rest_framework.response import Response
from rest_framework import status
from app.models import MyPhoto
from django.http import Http404
from app.Gsearcher.gSearcher import Searcher
from django.shortcuts import render
from rest_framework.parsers import MultiPartParser, FormParser

# Create your views here.

def getsearch(url):
    myip="138.197.210.12:8000"
    # image_url = "http://"+myip+"/api"+url
    image_url = 'http://www.history.com/s3static/video-thumbnails/AETN-History_VMS/21/115/History_Engineering_the_Taj_Mahal_42712_reSF_HD_still_624x352.jpg'

    IS = Searcher(image_url)
    f = open('result.html', 'w', encoding='utf-8')
    f.write(IS.soup.prettify())
    bg=IS.getGuest()
    og=IS.getSearchList()
    ans={}
    ans['bg_title']=re.split(r':|,|-| ', bg[0][0])
    ans['bg_url']=bg[1]
    ans['os1_title']=re.split(r':|,|-| ', og[0][0][0])
    ans['os1_url']=og[0][1]
    ans['os2_title'] = re.split(r':|,|-| ', og[1][0][0])
    ans['os2_url'] = og[1][1]
    ans['os3_title'] = re.split(r':|,|-| ', og[2][0][0])
    ans['os3_url'] = og[2][1]
    f.close()
    return ans


class PhotoList(APIView):
    #parser_classes = (MultiPartParser, FormParser,)

    def get(self, request, format=None):
        photo = MyPhoto.objects.all()
        serializer = PhotoSerializer(photo, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        print(request.data)
        serializer = PhotoSerializer(data=request.data)
        print("!")
        if serializer.is_valid():
           serializer.save()
           img_url=serializer.data.get('image')
           print(img_url)
           ret_value=getsearch(img_url)
           # ret_value["ans"]=getsearch(img_url)
           print(ret_value)
           return Response(ret_value, status=status.HTTP_201_CREATED)
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