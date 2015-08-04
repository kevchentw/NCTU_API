from django.db import models


class Mail(models.Model):
    name = models.CharField(max_length=50)
    date = models.DateField()
    mail_id = models.CharField(max_length=5)
    mail_type = models.CharField(max_length=50)
    dorm = models.CharField(max_length=50, default="")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

