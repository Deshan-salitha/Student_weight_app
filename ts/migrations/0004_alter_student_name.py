# Generated by Django 5.0.3 on 2024-03-19 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ts', '0003_alter_student_weight'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='name',
            field=models.CharField(max_length=250),
        ),
    ]