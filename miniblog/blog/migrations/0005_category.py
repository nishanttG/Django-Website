# Generated by Django 4.1.7 on 2024-10-08 04:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20241007_2229'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
    ]
