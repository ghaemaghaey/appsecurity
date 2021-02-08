from rest_framework import generics
from .models import data
from .serializers import dataSerilizer
# Create your views here.
class status(generics.ListAPIView):
    queryset = data.objects.all()
    serializer_class = dataSerilizer