# Generated by Django 5.1.6 on 2025-02-20 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='complaint',
            name='token',
            field=models.CharField(blank=True, editable=False, max_length=6, null=True, unique=True),
        ),
    ]
