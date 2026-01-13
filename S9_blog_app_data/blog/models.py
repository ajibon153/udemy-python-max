from django.db import models
from django.core.validators import MinLengthValidator
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.


class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(null=False, blank=False, unique=True)

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.full_name()


class Tag(models.Model):
    name = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=200)
    excerpt = models.CharField(max_length=200)
    image = models.CharField(max_length=100)
    date = models.DateField(auto_now=True)
    slug = models.SlugField(default="", blank=True,
                            null=False, db_index=True)
    content = models.TextField(
        validators=[MinLengthValidator(10)], default="", blank=True)
    # id feleted author will set to null, not delete the post
    author = models.ForeignKey(
        Author, on_delete=models.SET_NULL, null=True)
    tag = models.ManyToManyField(Tag)

    def get_absolute_url(self):
        return reverse("posts-page", args=[self.slug])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)  # call the real save() method

    def __str__(self):
        return self.title
