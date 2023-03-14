from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Workout, Exercise, Set

from .serializers import WorkoutSerializer, ExerciseSerializer, SetSerializer


# Create your views here.
class WorkoutListApiView(APIView):
    def get(self, request):
        workouts = Workout.objects.all()
        serializer = WorkoutSerializer(workouts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        data = {
            "name": request.data.get("name"),
            "notes": request.data.get("notes"),
        }
        serializer = WorkoutSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class WorkoutDetailApiView(APIView):
    def get_object(self, workout_id):
        """
        Helper method to get the object with given todo_id
        """
        try:
            return Workout.objects.get(id=workout_id)
        except Workout.DoesNotExist:
            return None

    def get(self, request, workout_id):
        """
        Retrieves the Todo with given todo_id
        """
        workout = self.get_object(workout_id)
        if not workout:
            return Response(
                {"res": "Object with workout ID does not exist"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        serializer = WorkoutSerializer(workout)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, workout_id):
        """
        Updates the todo item with given todo_id if exists
        """
        workout = self.get_object(workout_id)
        if not workout:
            return Response(
                {"res": "Object with workout ID does not exist"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        data = {
            "name": request.data.get("name"),
            "notes": request.data.get("notes"),
        }
        serializer = WorkoutSerializer(instance=workout, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, workout_id):
        """
        Deletes the todo item with given todo_id if exists
        """
        workout = self.get_object(workout_id)
        if not workout:
            return Response(
                {"res": "Object with workout ID cannot be deleted"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        workout.delete()
        return Response(
            {"res": "Object successfully deleted!"},
            status=status.HTTP_200_OK,
        )


class ExerciseListApiView(APIView):
    def get(self, request):
        exercises = Exercise.objects.all()
        serializer = ExerciseSerializer(exercises, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        data = {
            "name": request.data.get("name"),
            "one_rep_max": request.data.get("one_rep_max"),
            "workout": request.data.get("workout"),
        }
        serializer = ExerciseSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ExerciseDetailApiView(APIView):
    def get_object(self, exercise_id):
        """
        Helper method to get the object with given todo_id
        """
        try:
            return Exercise.objects.get(id=exercise_id)
        except Exercise.DoesNotExist:
            return None

    def get(self, request, exercise_id):
        """
        Retrieves the Todo with given todo_id
        """
        exercise = self.get_object(exercise_id)
        if not exercise:
            return Response(
                {"res": "Object with exercise ID does not exist"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        serializer = ExerciseSerializer(exercise)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, exercise_id):
        """
        Updates the todo item with given todo_id if exists
        """
        exercise = self.get_object(exercise_id)
        if not exercise:
            return Response(
                {"res": "Object with exercise ID does not exist"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        data = {
            "name": request.data.get("name"),
            "notes": request.data.get("notes"),
        }
        serializer = ExerciseSerializer(instance=exercise, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, exercise_id):
        """
        Deletes the todo item with given todo_id if exists
        """
        exercise = self.get_object(exercise_id)
        if not exercise:
            return Response(
                {"res": "Object with exercise ID cannot be deleted"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        exercise.delete()
        return Response(
            {"res": "Object successfully deleted!"},
            status=status.HTTP_200_OK,
        )


class SetListApiView(APIView):
    def get(self, request):
        sets = Set.objects.all()
        serializer = SetSerializer(sets, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        data = {
            "reps": request.data.get("reps"),
            "weight": request.data.get("weight"),
            "exercise": request.data.get("exercise"),
        }
        serializer = SetSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SetDetailApiView(APIView):
    def get_object(self, set_id):
        """
        Helper method to get the object with given todo_id
        """
        try:
            return Set.objects.get(id=set_id)
        except Set.DoesNotExist:
            return None

    def get(self, request, set_id):
        """
        Retrieves the Todo with given todo_id
        """
        set = self.get_object(set_id)
        if not set:
            return Response(
                {"res": "Object with set ID does not exist"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        serializer = SetSerializer(set)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, set_id):
        """
        Updates the todo item with given todo_id if exists
        """
        set = self.get_object(set_id)
        if not set:
            return Response(
                {"res": "Object with set ID does not exist"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        data = {
            "reps": request.data.get("reps"),
            "weight": request.data.get("weight"),
            "exercise": request.data.get("exercise"),
        }
        serializer = SetSerializer(instance=set, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, set_id):
        """
        Deletes the todo item with given todo_id if exists
        """
        set = self.get_object(set_id)
        if not set:
            return Response(
                {"res": "Object with set ID cannot be deleted"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        set.delete()
        return Response(
            {"res": "Object successfully deleted!"},
            status=status.HTTP_200_OK,
        )
