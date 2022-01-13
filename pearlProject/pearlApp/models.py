from django.db import models

# Create your models here.

from django.db import models

class Pearls(models.Model):
    title = models.CharField(max_length=20)
    list = models.TextField()
    pub_date = models.DateTimeField()
    

    def __str__(self) -> str:
        return f"{self.podcast_name}: {self.title}"

