from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from products.models import ProductViewHistory
from products.serializers import ProductViewHistorySerializer
from drf_yasg.utils import swagger_auto_schema

