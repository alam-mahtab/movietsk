from django.db import models
from rest_framework import serializers
from .models import Movie

class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = "__all__"#('id','Name','Description','Date_Of_Joining')