from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200, default='N/A')
    year = models.IntegerField(default=0000)
    edition = models.CharField(max_length=50, null=True, blank=True)
    author = models.CharField(max_length=100 , default='N/A')
    course_code = models.CharField(max_length=20, default='N/A')  
    condition = models.CharField(max_length=50, default='good')   
    availability_status = models.BooleanField(default=True)       

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'books'
        ordering = ['-year']
        verbose_name = 'Book'
        verbose_name_plural = 'Books'
