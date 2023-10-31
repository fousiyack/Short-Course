from django.db import models


class ShortCourse(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=20,default='Enable' ,choices=[("Enable", "Enable"), ("Disable", "Disable")])
    image = models.ImageField(upload_to="short_courses/", blank=True, null=True)
    amounts = models.ManyToManyField("Amount")

    def __str__(self):
        return self.title

class Amount(models.Model):
    value = models.DecimalField(max_digits=10, decimal_places=2)
    text = models.TextField()

    def __str__(self):
        return str(self.value)
