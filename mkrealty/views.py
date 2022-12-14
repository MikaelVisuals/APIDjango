from django_filters import rest_framework as filters
from .models import Realty
from .serializers import RealtySerializer
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework.permissions import IsAuthenticated


class MKRealtyFilter(filters.FilterSet):
    class Meta:
        model = Realty
        fields = {
            'type': ['icontains'],
            'location': ['icontains']
        }


class MKRealtyListView(generics.ListAPIView):
    filterset_class =MKRealtyFilter
    permission_classes = (IsAuthenticated,)
    queryset = Realty.objects.all()
    serializer_class = RealtySerializer\


    def get(self, request, format=None):
        realty = self.get_queryset().filter(status='Available')
        filter_backends = self.filter_queryset(realty)
        serializer = RealtySerializer(filter_backends, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = RealtySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class MKRealyDetail(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    def get_object(self, id):
        try:
            return Realty.objects.get(pk=id)
        except Realty.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, id, format=None):
        realty = self.get_object(id)
        serializer = RealtySerializer(realty)
        print(serializer)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        realty = self.get_object(id)
        serializer = RealtySerializer(realty, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, id, format=None):
        realty = self.get_object(id)
        realty.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
