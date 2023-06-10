from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=128)
    icon_url = models.URLField(blank=True)

    def __str__(self) -> str:
        return f"{self.name}"

class Post(models.Model):
    title = models.CharField(max_length=128)
    content = models.TextField(blank=True, max_length=512)

    image1_url = models.URLField(blank=True, null=True)
    image2_url = models.URLField(blank=True, null=True)
    image3_url = models.URLField(blank=True, null=True)

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name="post"
    )

    def __str__(self):
        return f"Title: {self.title}, Description: {self.content}, Category: {self.category}"
