from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
import datetime
from django.utils import timezone

# Create your models here.

class Blogger(models.Model):
    """Model representing a blogger"""
    first_name = models.CharField(max_length=100, help_text="The blogger's first name.")
    last_name = models.CharField(max_length=100, help_text="The blogger's last name.")
    bio = models.CharField(max_length=500, help_text="A short biography of the user.")

    class Meta:
        ordering = ['last_name']

    def __str__(self):
        return f"{self.id} Blogger: {self.first_name} {self.last_name}"

class Post(models.Model):
    """Model representing a blog post."""
    # one to many
    title = models.CharField(max_length=100, help_text="Enter a title for your blog post.")
    slug = models.SlugField(max_length=200, unique=True)
    sub_title = models.CharField(max_length=100, blank=True, help_text="Enter a sub-title for your blog post.")
    content = models.TextField(max_length=2000, help_text="Enter the content of your blog post here.", unique=True)
    created_at = models.DateTimeField(auto_now_add=True, help_text="The time at which your post was created.")
    updated_at = models.DateTimeField(auto_now_add=True, help_text="The last time your blog post was updated.")
    blogger = models.ForeignKey(Blogger, on_delete=models.RESTRICT, default=1)
    likes = models.IntegerField(default=0)

    class Meta:
        ordering = ['updated_at']

    def __str__(self):
        """Return a string for the Post object"""
        return self.title

    def get_absolute_url(self):
        """Returns a URL to access the detail record for this particular post."""
        return reverse("blog:post_detail", args=[str(self.slug)])

class Comment(models.Model):
    """Model representing a blog post comment."""
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100, null=True)
    body = models.TextField(max_length=1000, help_text="Enter the content of your comment here.")
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_at']

    def __str__(self):
        return f"Comment i.d. ({self.id}) -  {self.post.title} - User {self.name}"