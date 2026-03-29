from django.db import models


class Lead(models.Model):
    full_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)

    location = models.CharField(max_length=50)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} - {self.phone}"
