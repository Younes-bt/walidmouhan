# Generated by Django 5.1.3 on 2025-01-26 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0021_profile_email_profile_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='otp',
            field=models.CharField(blank=True, max_length=6, null=True),
        ),
    ]
