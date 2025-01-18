# Generated by Django 5.1.5 on 2025-01-17 21:54

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('actors', '0001_initial'),
        ('genres', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=500)),
                ('release_date', models.DateField(blank=True, null=True)),
                ('resume', models.CharField(blank=True, max_length=500, null=True)),
                ('actors', models.ManyToManyField(related_name='movies', to='actors.actor')),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='movies', to='genres.genre')),
            ],
        ),
    ]
