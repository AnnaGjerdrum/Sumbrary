from django.db import models
from django.utils import timezone


class Summary(models.Model):
    summaryId = models.IntegerField()
    title = models.CharField(max_length=200)
    user = models.ForeignKey('auth.User')
    rating = models.IntegerField()
    numRates = models.IntegerField()
    filepath = models.TextField()
    subject = models.TextField()
    book = models.TextField()
    published_date = models.DateTimeField(
            default=timezone.now)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
