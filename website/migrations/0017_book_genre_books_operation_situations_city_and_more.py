# Generated by Django 5.1.3 on 2025-01-24 16:01

import cloudinary.models
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0016_message_seen'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Book_genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='books_operation_situations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Profession',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Response_to_Book_requests',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='University',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=300)),
                ('pub_year', models.DateField(null=True)),
                ('pict', cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='image')),
                ('description', models.TextField(blank=True, max_length=1000, null=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='books_added', to=settings.AUTH_USER_MODEL)),
                ('genres', models.ManyToManyField(related_name='books', to='website.book_genre')),
            ],
        ),
        migrations.CreateModel(
            name='Book_operation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='operation', to='website.book')),
                ('borrwer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='book_in_borrowing_operation', to=settings.AUTH_USER_MODEL)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='books_in_operation', to=settings.AUTH_USER_MODEL)),
                ('situation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.books_operation_situations')),
                ('response', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.response_to_book_requests')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=50)),
                ('pict', cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='image')),
                ('rating', models.IntegerField(default=5)),
                ('books_actually_borrwed', models.ManyToManyField(related_name='borrwed_now', to='website.book')),
                ('books_added', models.ManyToManyField(related_name='added_by', to='website.book')),
                ('books_borrwed', models.ManyToManyField(related_name='borrwed_by', to='website.book')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.city')),
                ('profession', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.profession')),
                ('university', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.university')),
            ],
        ),
    ]
