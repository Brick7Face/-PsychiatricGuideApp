# Generated by Django 2.1.5 on 2019-02-13 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0006_auto_20190213_1643'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='step',
            name='treatment',
        ),
        migrations.AddField(
            model_name='treatment',
            name='steps',
            field=models.ManyToManyField(to='application.Step'),
        ),
    ]