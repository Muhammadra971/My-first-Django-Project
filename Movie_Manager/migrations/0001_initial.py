# Generated by Django 5.1.3 on 2024-11-25 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Moviedata',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('year', models.IntegerField(null=True)),
                ('description', models.TextField()),
            ],
        ),
    ]
