from django.db import models


# Create your models here.
class Workout(models.Model):
    name = models.CharField(max_length=200)
    notes = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Exercise(models.Model):
    name = models.CharField(max_length=200)
    one_rep_max = models.PositiveIntegerField()
    workout = models.ForeignKey(
        Workout,
        related_name="exercises",
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.name


class Set(models.Model):
    reps = models.PositiveIntegerField()
    weight = models.PositiveIntegerField()
    exercise = models.ForeignKey(
        Exercise,
        related_name="sets",
        on_delete=models.CASCADE,
    )
