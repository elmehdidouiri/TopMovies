# Generated by Django 5.1.5 on 2025-01-19 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('director', models.CharField(max_length=255)),
                ('duration', models.IntegerField()),
                ('release_date', models.DateField()),
                ('rating', models.DecimalField(decimal_places=1, max_digits=3)),
            ],
        ),
    ]
