import django_filters
from django.http import JsonResponse
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.views import APIView

from .models import Realty
from .serializers import RealtySerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework.permissions import IsAuthenticated


# @permission_classes([IsAuthenticated])
@api_view(['GET', 'POST'])
def listings(request, format=None):
    if request.method == 'GET':
        realty = Realty.objects.all()
        print(realty)
        serializer = RealtySerializer(realty, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = RealtySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def listing_detail(request, id, format=None):
    try:
        realty = Realty.objects.get(pk=id)
    except Realty.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = RealtySerializer(realty)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = RealtySerializer(realty, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
    elif request.method == 'DELETE':
        realty.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class MKRealtyListView(generics.ListAPIView):
    queryset = Realty.objects.all()
    serializer_class = RealtySerializer
    filter_fields = ('type', 'location')


