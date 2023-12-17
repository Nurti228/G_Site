from django.db import models


class Books(models.Model):
    book_name = models.CharField(max_length=50)
    book_descr = models.TextField()
    book_image = models.ImageField(upload_to='')
    book_price = models.CharField(max_length=50, null=True)
    book_author = models.CharField(max_length=50, null=True)
    book_created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.book_name
