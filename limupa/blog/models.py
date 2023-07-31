from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models


class Post(models.Model):
    user = models.ForeignKey('user.User', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='blog/images/', blank=True, null=True)
    categories = models.ManyToManyField('shop.ProductCategory', related_name='post')
    title = models.CharField(max_length=255)
    description = RichTextUploadingField()
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    user = models.ForeignKey('user.User', on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text
