from rest_framework import status
from rest_framework.response import Response 
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from .serializers import RegisterCustomUserSerializer
from .models import CustomUser
# Create your views here.

class CustomUserCreate(APIView):
    permissions_classes = [AllowAny]
    queryset = CustomUser.objects.all()

    def post(self, request):
        reg_serializer = RegisterCustomUserSerializer(data=request.data)
        if reg_serializer.is_valid():
            newuser = reg_serializer.save()
            if newuser:
                return Response(status=status.HTTP_202_CREATED)
        return Response(reg_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
