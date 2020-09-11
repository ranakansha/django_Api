from rest_framework import serializers
from learnrest.models import Signup


class SignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Signup
        fields = ['id','name','password','phone','address']