# Generated by Django 5.1.6 on 2025-02-20 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_complaint_token'),
    ]

    operations = [
        migrations.AddField(
            model_name='complaint',
            name='department',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
