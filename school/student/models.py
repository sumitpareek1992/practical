from django.db import models
import random
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify

# Create your models here.
def random_string():
    return str(random.randint(1000, 9999))


class Score(models.Model):
    name = models.CharField(max_length=20)
    physics = models.FloatField()
    chemistry = models.FloatField()
    mathematics = models.FloatField()
    english = models.FloatField()
    computer = models.FloatField(default=1)
    parsent_no = models.CharField(max_length=5, default=random_string)
    previous_no = models.CharField(max_length=5, default="0")

    def __str__(self):
        return self.parsent_no


def pre_save_random_no(sender, instance, *args, **kwargs):
    q = Score.objects.all().last()
    if q:
        instance.previous_no = q
    else:
        instance.previous_no = ""
pre_save.connect(pre_save_random_no, sender=Score)
