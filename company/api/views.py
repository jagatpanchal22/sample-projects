from rest_framework.response import Response
from rest_framework.views import APIView
from . import serializers
from .models import Company, Order
from django.http import Http404
from rest_framework import status


class Companies(APIView):

    def get(self, request):
        Companies = Company.objects.all()
        serializer = serializers.CompanySerializer(Companies, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = serializers.CompanySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CompanyDetail(APIView):

    def get(self, request, company_id):
        try:
            company = Company.objects.get(pk=company_id)
        except Company.DoesNotExist:
            raise Http404
        serializer = serializers.CompanySerializer(company)
        return Response(serializer.data)

    def delete(self, request, company_id):
        try:
            company = Company.objects.get(pk=company_id)
        except Company.DoesNotExist:
            raise Http404
        company.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class Orders(APIView):

    def get(self, request, company_id):
        orders = Order.objects.filter(by_company_id__exact=company_id)
        serializer = serializers.OrderSerializer(orders, many=True)
        return Response(serializer.data)

    def post(self, request, company_id):
        try:
            Company.objects.get(pk=company_id)
        except Company.DoesNotExist:
            raise Http404

        serializer = serializers.OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(by_company_id__exact=company_id)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OrderDetail(APIView):

    def get(self, request, company_id, order_id):
        try:
            order = Order.objects.get(by_company_id__exact=company_id, pk=order_id)
        except Order.DoesNotExist:
            raise Http404
        serializer = serializers.OrderSerializer(order)
        return Response(serializer.data)

    def delete(self, request, company_id, order_id):
        try:
            recipe = Order.objects.get(by_company_id__exact=company_id, pk=order_id)
        except Order.DoesNotExist:
            raise Http404
        recipe.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
