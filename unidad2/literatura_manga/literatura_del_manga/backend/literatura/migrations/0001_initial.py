# Generated by Django 5.1.7 on 2025-03-31 23:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Manga',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genero', models.CharField(max_length=100)),
                ('autor', models.CharField(max_length=100)),
                ('volumenes', models.IntegerField()),
                ('tema_principal', models.CharField(max_length=255)),
            ],
        ),
    ]
