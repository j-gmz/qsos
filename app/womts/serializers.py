from .models import Womt
from rest_framework import serializers

class WomtSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Womt 
        fields = [
            "work_order_name",
            "created_date",
            "created_by",
            "status",
            "assigned_to",
        ]
    