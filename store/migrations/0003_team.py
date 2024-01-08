# Generated by Django 5.0.1 on 2024-01-07 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_blog'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='имя')),
                ('function', models.CharField(max_length=100, verbose_name='должность')),
                ('image', models.ImageField(blank=True, null=True, upload_to='photo', verbose_name='фото')),
            ],
        ),
    ]
