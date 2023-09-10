from django.db import models

# Create your models here.

class Animator(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Group(models.Model):
    name = models.CharField(max_length=50)
    animator = models.ForeignKey(Animator, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f'{self.name}: {self.animator}'


class Person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birthday = models.DateField()
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    chocolate_received = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        ordering = ('-chocolate_received','birthday__month', 'birthday__day')
        verbose_name_plural = 'People'