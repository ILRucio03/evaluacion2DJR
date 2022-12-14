# Generated by Django 4.1 on 2022-10-19 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='persona',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('fono', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='proyecto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fechainicio', models.DateField()),
                ('fechatermino', models.DateField()),
                ('nombre', models.CharField(max_length=50)),
                ('responsable', models.CharField(max_length=50)),
                ('prioridad', models.IntegerField()),
            ],
        ),
    ]
