# Generated by Django 5.1.7 on 2025-03-26 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='age',
            field=models.IntegerField(blank=True, null=True, verbose_name='Age of the employee'),
        ),
    ]
