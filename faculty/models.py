from django.db import models
from django.utils import timezone

class Student(models.Model):
    student_id = models.CharField(max_length=20, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    course = models.CharField(max_length=100)
    year = models.CharField(max_length=15)
    description = models.TextField()
    status = models.CharField(max_length=50)
    date_borrowed = models.CharField(max_length=30)  # Change to CharField

    def save(self, *args, **kwargs):
        if not self.pk:  # Only update date_borrowed if it's a new instance
            # Get the current date and time in the desired format
            formatted_date = timezone.now().strftime('%a, %d %b %Y')
            self.date_borrowed = formatted_date
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name_plural = "Students"
