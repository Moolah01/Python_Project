# Generated by Django 5.1.2 on 2024-11-23 06:53

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Class Name')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Class Description')),
                ('max_students', models.PositiveIntegerField(default=30, verbose_name='Maximum Students')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('students', models.ManyToManyField(blank=True, related_name='enrolled_classes', to=settings.AUTH_USER_MODEL, verbose_name='Students')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='classes', to=settings.AUTH_USER_MODEL, verbose_name='Teacher')),
            ],
            options={
                'verbose_name': 'Class',
                'verbose_name_plural': 'Classes',
            },
        ),
    ]