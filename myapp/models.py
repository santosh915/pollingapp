from django.db import models

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=300)

    def __str__(self):
        return self.question_text

g
class Choice(models.Model):
    question = models.ForeignKey(Question,on_delete = models.CASCADE,related_name = 'choices')
    options = models.CharField(max_length = 100 )
    vote = models.IntegerField(default = 0)



    def __str__(self):
        return self.options





