from django.db import models
from authentication.models import Student

class Message(models.Model):
    sender = models.CharField(max_length=200)
    receiver = models.CharField(max_length=200)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.sender} to {self.receiver} for {self.student.full_name}"
