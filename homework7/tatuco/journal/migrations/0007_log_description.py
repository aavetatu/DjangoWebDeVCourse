# Generated by Django 4.2.1 on 2023-05-30 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0006_alter_log_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='log',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]