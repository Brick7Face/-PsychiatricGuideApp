# Generated by Django 2.1.5 on 2019-02-17 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0009_auto_20190217_0653'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='phq9',
            name='current_step',
        ),
        migrations.AddField(
            model_name='phq9',
            name='change_treatment',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='phq9',
            name='diagnosis',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='phq9',
            name='severity_score',
            field=models.IntegerField(default=5),
        ),
        migrations.AddField(
            model_name='phq9',
            name='suicide_risk',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='phq9',
            name='question_1',
            field=models.IntegerField(default=5),
        ),
        migrations.AlterField(
            model_name='phq9',
            name='question_10',
            field=models.IntegerField(default=5),
        ),
        migrations.AlterField(
            model_name='phq9',
            name='question_2',
            field=models.IntegerField(default=5),
        ),
        migrations.AlterField(
            model_name='phq9',
            name='question_3',
            field=models.IntegerField(default=5),
        ),
        migrations.AlterField(
            model_name='phq9',
            name='question_4',
            field=models.IntegerField(default=5),
        ),
        migrations.AlterField(
            model_name='phq9',
            name='question_5',
            field=models.IntegerField(default=5),
        ),
        migrations.AlterField(
            model_name='phq9',
            name='question_6',
            field=models.IntegerField(default=5),
        ),
        migrations.AlterField(
            model_name='phq9',
            name='question_7',
            field=models.IntegerField(default=5),
        ),
        migrations.AlterField(
            model_name='phq9',
            name='question_8',
            field=models.IntegerField(default=5),
        ),
        migrations.AlterField(
            model_name='phq9',
            name='question_9',
            field=models.IntegerField(default=5),
        ),
    ]
