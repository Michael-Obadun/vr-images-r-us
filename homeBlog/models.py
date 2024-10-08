from django.db import models
from django.contrib.auth.models import User

STATUS = ((0, "Draft"), (1, "Published"))

# Create your models here.

# i am also going to need 
    # featured_image = CloudinaryField('image', default='placeholder')
    # likes = models.ManyToManyField(User, related_name='hike_likes', blank=True)
class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    author = models.ForeignKey(
    User, on_delete=models.CASCADE, related_name="blog_posts"
)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)
   
    class Meta:
        ordering = ["-created_on"]
    def __str__(self):
        return f"{self.title} | written by {self.author}"       


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             related_name="comments")
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="commenter")
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)
    # approved model may have to be deleted

    class Meta:
        ordering = ["created_on"]
    def __str__(self):
        return f"{self.body} | written by {self.author}"

