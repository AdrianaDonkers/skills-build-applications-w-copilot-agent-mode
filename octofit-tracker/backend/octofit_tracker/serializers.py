from rest_framework import serializers
from bson import ObjectId
from .models import User, Team, Activity, Leaderboard, Workout

class ObjectIdField(serializers.Field):
    def to_representation(self, value):
        return str(value)

    def to_internal_value(self, data):
        if not ObjectId.is_valid(data):
            raise serializers.ValidationError("Invalid ObjectId")
        return ObjectId(data)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class TeamSerializer(serializers.ModelSerializer):
    _id = ObjectIdField()

    class Meta:
        model = Team
        fields = ['_id', 'name', 'members']

class ActivitySerializer(serializers.ModelSerializer):
    _id = ObjectIdField()
    user = UserSerializer()  # Use nested serializer for the user field

    class Meta:
        model = Activity
        fields = ['_id', 'user', 'description']

class LeaderboardSerializer(serializers.ModelSerializer):
    _id = ObjectIdField()
    team = TeamSerializer()  # Use nested serializer for the team field

    class Meta:
        model = Leaderboard
        fields = ['_id', 'team', 'score']

class WorkoutSerializer(serializers.ModelSerializer):
    _id = ObjectIdField()
    user = UserSerializer()  # Use nested serializer for the user field

    class Meta:
        model = Workout
        fields = ['_id', 'user', 'duration']