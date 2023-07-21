from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)


    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'categories'
        ordering = ["id"]

    def __str__(self):
        return self.name
        

class Event(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    start_date = models.DateField()
    end_date = models.DateTimeField()
    location = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    is_free = models.BooleanField()

    class Meta:
        verbose_name = 'Event'
        verbose_name_plural = 'Events'
        ordering = ["id"]

    def __str__(self):
        return self.title