# Generated by Django 4.2.2 on 2023-09-18 19:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rental', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='rental',
            options={'permissions': (('can_rent', ' Can rent a book'),)},
        ),
    ]