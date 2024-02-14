from rest_framework import serializers
from django.contrib.auth.models import User, Group

from .models import Menu, Booking,MenuItem

class MenuSerializer(serializers.ModelSerializer):
    class Meta():
        model = Menu
        fields = ['id','name','price','inventory']
        
class BookingSerializer(serializers.ModelSerializer):
    class Meta():
        model = Booking
        fields = '__all__'

class GroupNameField(serializers.RelatedField):
    def to_representation(self, value):
        # Return the group name
        return value.name

class UserSerializer(serializers.ModelSerializer):
    groups = GroupNameField(many=True, read_only=True)
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')

class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = ['id','name','price','inventory']