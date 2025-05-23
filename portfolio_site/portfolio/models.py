
from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def average_rating(self):
        ratings = self.rating_set.all()
        return round(sum(r.score for r in ratings) / ratings.count(), 2) if ratings else 0

class Rating(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    score = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    submitted_at = models.DateTimeField(auto_now_add=True)
