from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import CRUD
from .serializers import CRUDSerializer
from .models import Job

# Create your views here.


def profile(request):
    jobs = Job.objects
    return render(request, "jobs/home.html", {"jobs": jobs})


@api_view(["GET"])
def get_data(request, pk):
    try:
        data = CRUD.objects.get(pk=pk)
    except CRUD.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = CRUDSerializer(data)
    return Response(serializer.data)


@api_view(["POST"])
def create_data(request):
    serializer = CRUDSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["PUT"])
def update_data(request, pk):
    try:
        data = CRUD.objects.get(pk=pk)
    except CRUD.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = CRUDSerializer(data, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["DELETE"])
def delete_data(request, pk):
    try:
        data = CRUD.objects.get(pk=pk)
    except CRUD.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    data.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
