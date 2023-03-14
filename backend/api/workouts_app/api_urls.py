from django.urls import path, include
from .api_views import (
    WorkoutListApiView,
    WorkoutDetailApiView,
    ExerciseListApiView,
    ExerciseDetailApiView,
    SetListApiView,
    SetDetailApiView,
)

urlpatterns = [
    path("workouts/", WorkoutListApiView.as_view()),
    path("workouts/<int:workout_id>/", WorkoutDetailApiView.as_view()),
    path("workouts/exercises/", ExerciseListApiView.as_view()),
    path("workouts/exercises/<int:exercise_id>/", ExerciseDetailApiView.as_view()),
    path("workouts/exercises/sets/", SetListApiView.as_view()),
    path("workouts/exercises/sets/<int:set_id>/", SetDetailApiView.as_view()),
]
