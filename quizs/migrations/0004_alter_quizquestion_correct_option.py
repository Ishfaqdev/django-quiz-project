# Generated by Django 5.0.1 on 2024-01-27 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizs', '0003_alter_quizquestion_correct_option'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quizquestion',
            name='correct_option',
            field=models.CharField(max_length=1),
        ),
    ]
