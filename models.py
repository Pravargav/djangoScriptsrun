from django.db import models


class Question1(models.Model):
    qn=models.CharField(max_length=217)
    soln=models.CharField(max_length=217)

class Question2(models.Model):
    qn=models.CharField(max_length=217)
    soln=models.CharField(max_length=217)

class Question3(models.Model):
    qn=models.CharField(max_length=217)
    soln=models.CharField(max_length=217)

class Question4(models.Model):
    qn=models.CharField(max_length=217)
    soln=models.CharField(max_length=217) 


class Rquestion1(models.Model):
    qn=models.CharField(max_length=217)

class Rquestion2(models.Model):
    qn=models.CharField(max_length=217)

class Rquestion3(models.Model):
    qn=models.CharField(max_length=217)

class Rquestion4(models.Model):
    qn=models.CharField(max_length=217)

class Option1(models.Model):
    question = models.ForeignKey(Rquestion1, on_delete=models.CASCADE)
    op = models.CharField(max_length=217)

class Option2(models.Model):
    question = models.ForeignKey(Rquestion2, on_delete=models.CASCADE)
    op = models.CharField(max_length=217)

class Option3(models.Model):
    question = models.ForeignKey(Rquestion3, on_delete=models.CASCADE)
    op = models.CharField(max_length=217)

class Option4(models.Model):
    question = models.ForeignKey(Rquestion4, on_delete=models.CASCADE)
    op = models.CharField(max_length=217)





