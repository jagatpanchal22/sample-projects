from rest_framework.response import Response
from rest_framework.views import APIView
from . import serializers
from .models import Company, Order
from django.http import Http404
from rest_framework import status
from rest_framework.authentication import (
    SessionAuthentication,
    TokenAuthentication,
)
from rest_framework.permissions import IsAuthenticated


class CompanyList(APIView):
    """
    List all company, or create a new company.
    """

    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        companies = Company.objects.all()
        serializer = serializers.CompanySerializer(companies, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = serializers.CompanySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CompanyDetail(APIView):
    """
    Retrieve, update or delete a company instance.
    """

    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return Company.objects.get(pk=pk)
        except Company.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        company = self.get_object(pk)
        serializer = serializers.CompanySerializer(company)
        return Response(serializer.data)

    def put(self, request, pk):
        company = self.get_object(pk)
        serializer = serializers.CompanySerializer(company, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        company = self.get_object(pk)
        company.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class OrderList(APIView):
    """
    List all Orders, or create a new order by company.
    """

    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, company_id):
        orders = Order.objects.filter(by_company_id__exact=company_id)
        serializer = serializers.OrderSerializer(orders, many=True)
        return Response(serializer.data)

    def post(self, request, company_id):
        serializer = serializers.OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OrderDetail(APIView):
    """
    Retrieve, update or delete a company instance.
    """

    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_object(self, company_id, pk):
        try:
            return Order.objects.get(by_company_id__exact=company_id, pk=pk)
        except Order.DoesNotExist:
            raise Http404

    def get(self, request, company_id, pk):
        order = self.get_object(company_id, pk)
        serializer = serializers.OrderSerializer(order)
        return Response(serializer.data)

    def put(self, request, company_id, pk):
        order = self.get_object(company_id, pk)
        serializer = serializers.OrderSerializer(order, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, company_id, pk):
        order = self.get_object(company_id, pk)
        order.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
