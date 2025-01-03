# Generated by Django 4.2.7 on 2024-11-29 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasker', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=50, verbose_name='Username'),
        ),
    ]
