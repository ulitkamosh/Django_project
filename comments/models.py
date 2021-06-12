from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User
from products.models import Product


class Comment(models.Model):
    class Meta:
        db_table = "comment"

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.content[0:100]

    def get_absolute_url(self):
        return reverse('add-comment', kwargs={'pk': self.pk})
