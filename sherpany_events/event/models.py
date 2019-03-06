from django.db import models
from django.utils import timezone


class Event(models.Model):
    user = models.ForeignKey('user.User', null=False, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now, null=False, db_index=True)
    title = models.CharField(max_length=25, editable=True, blank=False, null=False)
    description = models.TextField(max_length=500, editable=True, blank=False, null=False)
    participants = models.ManyToManyField('user.User', related_name='assisting_events')

    def __str__(self):
        return '#%s' % self.id

    class Meta:
        verbose_name = 'Event'
        verbose_name_plural = 'Events'
        ordering = ['-date']

