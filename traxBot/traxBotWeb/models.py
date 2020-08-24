from django.db import models

# Create your models here.
class Position(models.Model):
    xPos = models.FloatField()
    yPos = models.FloatField()
    zPos = models.FloatField()
    def __str__(self):
        ret = "(%f, %f, %f)" % (self.xPos, self.yPos, self.zPos)
        return(ret)
    def toString(self):
        ret = "(%f, %f, %f)" % (self.xPos, self.yPos, self.zPos)
        return(ret)

