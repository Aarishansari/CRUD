from rest_framework import serializers
from .models import users


class usersSerializer(serializers.HyperlinkedModelSerializer):


     class Meta:
          model = users
          fields = ('User_id','Name','Age','Department','Subject')
