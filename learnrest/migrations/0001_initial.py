# Generated by Django 2.2.14 on 2020-09-11 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Signup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=8)),
                ('phone', models.CharField(max_length=10)),
                ('address', models.CharField(max_length=50)),
            ],
        ),
    ]
