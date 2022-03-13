# Generated by Django 4.0.3 on 2022-03-08 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=25)),
                ('description', models.TextField()),
                ('recipe', models.TextField()),
                ('calories', models.IntegerField()),
                ('img', models.ImageField(upload_to='menu/images')),
            ],
        ),
    ]
