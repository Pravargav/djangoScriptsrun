from django.db import models


class Question(models.Model):
    qn=models.CharField(max_length=217)
    soln=models.CharField(max_length=217)







