from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=65)
    email = models.EmailField()
    subject = models.CharField(max_length=35, null=True, blank=True)
    message = models.TextField(max_length=200)
    read = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if self.updated:
            self.read = True
        return super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} - {self.created}"