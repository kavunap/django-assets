from django.db import models
# from author.models import Author

class Blog(models.Model):
    # author = models.ForeignKey(
    #     'Author',
    #     on_delete=models.CASCADE,
    # )
    title = models.CharField(max_length=255)
    content = models.TextField()

# class User

