from rest_framework.serializers import ModelSerializer
from ..models import Note


class NoteSerializer(ModelSerializer):
    class Meta:
        model = Note
        fields = '_all_'

from rest_framework import serializers
from ..models import Business  # Import your Business model here

class BusinessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Business
        fields = '__all__'
