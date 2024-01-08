from django.db import models

class Project(models.Model):
    title = models.CharField(verbose_name='название', max_length=100)
    description = models.TextField(verbose_name='описание', blank=True)
    image = models.ImageField(verbose_name='изображение', blank=True, null=True, upload_to='images')
    place = models.CharField(verbose_name='место работы', max_length=100)

    def __str__(self) -> str:
        return f'{self.title} - {self.place}'
    
class Blog(models.Model):
    title = models.CharField(verbose_name='название', max_length=100)
    arcticle = models.TextField(verbose_name='статья')
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(verbose_name='изображение', blank=True, null=True, upload_to='images')

    def __str__(self) -> str:
        return f'{self.title} - {self.date.date().strftime("%d.%m.%Y")}'
    
class Team(models.Model):
    name = models.CharField(verbose_name='имя', max_length=100)
    function = models.CharField(verbose_name='должность', max_length=100)
    image = models.ImageField(verbose_name='фото', blank=True, null=True, upload_to='photo')

    def __str__(self) -> str:
        return f'{self.name}'
    

class Message(models.Model):
    first_name = models.CharField(verbose_name='имя', max_length=100)
    last_name = models.CharField(verbose_name='фамилия', max_length=100)
    email = models.EmailField(verbose_name='email', max_length=100)
    message = models.TextField(verbose_name='сообщение', max_length=500)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'{self.last_name} - {self.email}'
    

class Subscription(models.Model):
    email = models.EmailField(verbose_name='электронная почта', max_length=200)
    def __str__(self) -> str:
        return f'{self.email}'