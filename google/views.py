from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import GoogleDataSerializer
from .models import GoogleData
from rest_framework import status

from datetime import date

# Create your views here.


@api_view(["GET"])
def getlatestgoogle(request):
    if request.method == 'GET':

        
        # Retrieve all GoogleData instances from the database
        google_data_objects = GoogleData.objects.filter(today=date.today())

        # Serialize the data using GoogleDataSerializer
        serializer = GoogleDataSerializer(google_data_objects, many=True)

        # Return the serialized data in the response
        return Response(serializer.data, status=status.HTTP_200_OK)
     


@api_view(["GET", "POST"])
def post_new_analysis(request):
    if request.method == "POST":
        info = request.data
        serializer = GoogleDataSerializer(data=info)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "GET":
        # Your logic for handling GET requests here
        return Response({'message': 'GET request handled successfully'}, status=status.HTTP_200_OK)


@api_view(["POST"])
def get_particular_google(request):
    today_value = request.data.get('today', None)

    if today_value is not None:
        reply = GoogleData.objects.filter(today=today_value)
        serializer = GoogleDataSerializer(reply, many=True)
        return Response(serializer.data)
    else:
        return Response({'error': 'Missing or invalid "today" value in the request data'}, status=400)