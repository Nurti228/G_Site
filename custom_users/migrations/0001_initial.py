# Generated by Django 3.2.5 on 2024-01-07 17:08

import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='auth.user')),
                ('phone_number', models.CharField(default=996, max_length=13, verbose_name='Укажите номер телефона')),
                ('date_of_birth', models.DateField(verbose_name='Дата рождения')),
                ('gender', models.CharField(choices=[(1, 'М'), (2, 'Ж')], max_length=10, verbose_name='Ваш пол')),
                ('source', models.TextField(verbose_name='Откуда вы узнали про нас')),
                ('country', models.CharField(max_length=20, verbose_name='Откуда вы?')),
                ('family', models.CharField(max_length=20, verbose_name='Семейное положение')),
                ('education', models.CharField(max_length=10, verbose_name='Уровень образования')),
                ('language', models.CharField(max_length=20, verbose_name='количество языков которыми владеете')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
