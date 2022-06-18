# Generated by Django 4.0.5 on 2022-06-18 13:11

import django.contrib.auth.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=200)),
                ('Text', models.TextField(verbose_name='Any amount of text')),
                ('Created_date', models.DateTimeField(verbose_name='A date-time column')),
                ('Publish_date', models.DateTimeField(verbose_name='A date-time column')),
                ('Author', models.ForeignKey(on_delete=django.contrib.auth.models.User, to='blog.post')),
            ],
        ),
    ]