from rest_framework import serializers
from .models import Workout, Exercise, Set


class WorkoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workout
        fields = [
            "name",
            "notes",
            "created",
            "updated",
            "id",
        ]


class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = [
            "name",
            "one_rep_max",
            "workout",
            "id",
        ]


class SetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Set
        fields = [
            "reps",
            "weight",
            "exercise",
            "id",
        ]
