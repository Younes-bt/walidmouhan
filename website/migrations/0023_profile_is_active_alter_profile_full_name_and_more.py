# Generated by Django 5.1.3 on 2025-01-26 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0022_profile_otp'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='profile',
            name='full_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='rating',
            field=models.IntegerField(blank=True, default=5, null=True),
        ),
    ]
