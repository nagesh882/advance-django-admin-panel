from django.shortcuts import render
from rest_framework import viewsets
from login.models import Register, Products
from rest_api.serializers import registerSerializer, productSerializer
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.filters import SearchFilter


# ModelViewSet is used for userViewSet and ProductViewSet
# GET, POST, PUT, PATHCH, DELETE, OPTION and HEAD request

class userViewSet(viewsets.ModelViewSet):
    queryset = Register.objects.all()
    serializer_class = registerSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [SearchFilter]
    search_fields = ['user_name']



class productViewSet(viewsets.ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = productSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [SearchFilter]
    search_fields = ['product_name']