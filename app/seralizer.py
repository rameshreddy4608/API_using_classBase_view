from rest_framework import serializers

from app.models import *

class productserilazer(serializers.ModelSerializer):
    class Meta:
        model=product
        fields='__all__'