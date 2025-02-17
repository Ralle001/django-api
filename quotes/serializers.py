from rest_framework import serializers
from .models import Quote

class QuoteSerializer(serializers.ModelSerializer):
    """
    Serializer for the Quote model.
    
    Converts Quote instances to JSON format and vice versa.
    
    Meta:
        model (Quote): The model to be serialized.
        fields (list): The fields to be included in the serialized output.
    """
    class Meta:
        model = Quote
        fields = ['id', 'text', 'author', 'created_at']
