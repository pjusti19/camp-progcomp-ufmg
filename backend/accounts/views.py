from rest_framework import serializers
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from accounts.services.auth_service import register_user, SignupError
from common.codeforces.client import CodeforcesAPIError
import logging

logger = logging.getLogger(__name__)

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
        register_user(**serializer.validated_data)
    except CodeforcesAPIError as e: 
        logger.error("%s", e)
        return Response({"detail": str(e)}, status=500)
    except SignupError as e: 
        logger.error("%s", e)
        return Response({"detail": str(e)}, status=400)
    
    return Response({}, status=201)
    
@api_view(["GET"])
@permission_classes([IsAuthenticated])
def show_profile(request):
    user = request.user
    return Response({
        "name": user.first_name, 
        "email": user.email,
        "codeforces_handle": user.codeforces_handle
    }, status=200)