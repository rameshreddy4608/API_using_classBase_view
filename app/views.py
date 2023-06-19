from django.shortcuts import render

# Create your views here.


# Create your views here.

from rest_framework.views import APIView
from app.models import *

from app.seralizer import *

from rest_framework.response import Response

class ProductCurd(APIView):
    def get(self,request):
        PQS=product.objects.all()
        PJD=productserilazer(PQS,many=True)
        return Response(PJD.data)