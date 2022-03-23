from django.db import models


class Members(models.Model):
    GENDER = (
        ('Male', 'Мужской'),
        ('Female', 'Женский')
    )

    name = models.CharField(verbose_name='Имя', max_length=50)
    surname = models.CharField(verbose_name='Фамилия', max_length=50)
    gender = models.CharField(verbose_name='Пол', max_length=10, default='Male', choices=GENDER)
    mail = models.CharField(max_length=50)
    avatar = models.ImageField(verbose_name='Аватар', upload_to='images/avatars/')

    def __str__(self):
        return f'{self.name} {self.surname}'
