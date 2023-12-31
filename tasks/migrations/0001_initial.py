# Generated by Django 4.2.4 on 2023-08-16 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True, verbose_name='Task name')),
                ('status', models.CharField(choices=[('u', 'Not Started yet'), ('o', 'Ongoing'), ('f', 'Finished')], default='u', max_length=1, verbose_name='Task status')),
            ],
        ),
    ]
