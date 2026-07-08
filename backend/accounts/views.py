from django.shortcuts import render
from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from services import signup_service
import requests

# Create your views here.
class RegisterSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=150)
    email = serializers.EmailField()
    password = serializers.CharField(min_length=8, write_only=True)
    codeforces_handle = serializers.CharField(max_length=100)
    
@api_view(["POST"])
def register(request):
    serializer = RegisterSerializer(data = request.data)
    serializer.is_valid(raise_exception=True)
    
    try:
        user = signup_service.register_user(**serializer.validated_data)
    except signup_service.SignupError as e: 
        return Response({"detail": str(e)}, status=400)
    
    return Response({"id": user.id, "email": user.email}, status=201)