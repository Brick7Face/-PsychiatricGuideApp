# Generated by Django 2.1.5 on 2019-02-17 06:53

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0008_auto_20190217_0639'),
    ]

    operations = [
        migrations.AddField(
            model_name='phq9',
            name='current_step',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='application.Patient'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='dob',
            field=models.DateField(default=datetime.date(1, 1, 1), help_text='Enter patient date of birth'),
        ),
    ]