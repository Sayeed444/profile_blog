# Generated by Django 2.1 on 2019-04-15 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cityseapes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=121)),
                ('descriptinos', models.TextField(blank=True, null=True)),
                ('datetime', models.DateTimeField()),
                ('img', models.ImageField(upload_to='')),
            ],
            options={
                'ordering': ['-datetime'],
            },
        ),
        migrations.CreateModel(
            name='Nature',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=121)),
                ('descriptinos', models.TextField(blank=True, null=True)),
                ('datetime', models.DateTimeField()),
                ('img', models.ImageField(upload_to='')),
            ],
            options={
                'ordering': ['-datetime'],
            },
        ),
        migrations.CreateModel(
            name='Portraits',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=121)),
                ('descriptinos', models.TextField(blank=True, null=True)),
                ('datetime', models.DateTimeField()),
                ('img', models.ImageField(upload_to='')),
            ],
            options={
                'ordering': ['-datetime'],
            },
        ),
    ]
