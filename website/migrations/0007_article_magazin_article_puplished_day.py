# Generated by Django 5.1.3 on 2024-12-03 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0006_alter_article_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='magazin',
            field=models.CharField(blank=True, max_length=1500, null=True),
        ),
        migrations.AddField(
            model_name='article',
            name='puplished_day',
            field=models.DateField(blank=True, null=True),
        ),
    ]
