from django.db import models

import uuid

class File(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    file = models.FileField(upload_to='files/')
    category = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')
    number_of_pages = models.IntegerField()

    uploaded_at = models.DateTimeField(auto_now_add=True)
    uploaded_by = models.ForeignKey('Account.User', on_delete=models.CASCADE)

    
