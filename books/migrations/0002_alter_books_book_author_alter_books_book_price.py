# Generated by Django 5.0 on 2023-12-17 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='book_author',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='books',
            name='book_price',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
