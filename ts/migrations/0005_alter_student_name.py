# Generated by Django 5.0.3 on 2024-03-19 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ts', '0004_alter_student_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='name',
            field=models.CharField(max_length=255),
        ),
    ]
