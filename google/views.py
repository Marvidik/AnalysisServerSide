from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import GoogleDataSerializer
from .models import GoogleData
from rest_framework import status

from datetime import date

# Create your views here.

@api_view(["POST"])
def post_new_analysis(request):
    if request.method == "POST":
        info = request.data
        serializer = GoogleDataSerializer(data=info)

        if serializer.is_valid():
            # Extract the 'today' field from the request data
            today = serializer.validated_data.get('today')

            # Check if data with the same date already exists
            if GoogleData.objects.filter(today=today).exists():
                return Response({'message': 'Data with the same date already exists.'}, status=status.HTTP_400_BAD_REQUEST)

            # Save the new data
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


# For Updating Data For Google
@api_view(["PUT"])
def update_todays_google(request):
    try:
        google_data_instance = GoogleData.objects.get(today=date.today())  # Provide any conditions to get the specific instance
    except GoogleData.DoesNotExist:
        return Response({'message': 'GoogleData not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == "PUT":
        info = request.data
        serializer = GoogleDataSerializer(google_data_instance, data=info)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)