# Generated by Django 3.2.8 on 2024-10-07 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Home',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(blank=True, max_length=50, null=True)),
                ('about', models.TextField()),
                ('copyright', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
    ]