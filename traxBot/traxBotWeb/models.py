from django.db import models

# Create your models here.
class Position(models.Model):
    xPos = models.FloatField()
    yPos = models.FloatField()
    def __str__(self):
        ret = "(%f, %f)" % (self.xPos, self.yPos)
        return(ret)
