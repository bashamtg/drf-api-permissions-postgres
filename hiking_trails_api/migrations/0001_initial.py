# Generated by Django 4.0.4 on 2022-05-31 19:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='HikingTrails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trail_name', models.CharField(max_length=64)),
                ('description', models.TextField()),
                ('google_maps_directions', models.URLField(max_length=600)),
                ('all_trails_link', models.URLField(max_length=600)),
                ('lat', models.CharField(max_length=100)),
                ('lon', models.CharField(max_length=100)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
