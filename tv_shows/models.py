from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Show(models.Model):
    TYPE_SHOW = (
        ('Comedy', 'Comedy'),
        ('Drama', 'Drama'),
        ('Kids', 'Kids'),
        ('Adult', 'Adult')
    )
    title = models.CharField(max_length=30, verbose_name='Write shows name')
    image = models.ImageField(upload_to='shows/', verbose_name='Add photos')
    description = models.TextField(verbose_name='Give shows description', blank=True)
    price = models.PositiveIntegerField(verbose_name='Write the price', validators=[MinValueValidator(15),
                                                                                    MaxValueValidator(5000)])
    genre = models.CharField(max_length=50, choices=TYPE_SHOW)
    author = models.CharField(max_length=50)
    trailer = models.URLField(verbose_name='Write the link to trailer')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
