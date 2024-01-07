from django.db import models
from django.contrib.auth.models import User

MALE = 1
FEMALE = 2

GENDER_TYPE = (
    (MALE, "М"),
    (FEMALE, "Ж")
)


class CustomUser(User):
    phone_number = models.CharField(max_length=13, default=+996,
                                    verbose_name='Укажите номер телефона')
    date_of_birth = models.DateField(verbose_name='Дата рождения')
    gender = models.CharField(max_length=10, choices=GENDER_TYPE,
                              verbose_name="Ваш пол")
    source = models.TextField(verbose_name='Откуда вы узнали про нас')
    country = models.CharField(max_length=20, verbose_name='Откуда вы?')
    family = models.CharField(max_length=20, verbose_name='Семейное положение')
    education = models.CharField(max_length=10, verbose_name='Уровень образования')
    language = models.CharField(max_length=20, verbose_name='количество языков которыми владеете')


