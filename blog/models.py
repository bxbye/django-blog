from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='blog/', default='blog/django.png')
    # You can add more fields like author, tags, etc.

    def __str__(self) -> str:
        return self.title +'-'+ str(self.date_posted.year)

    