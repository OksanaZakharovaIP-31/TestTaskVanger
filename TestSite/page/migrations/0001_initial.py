# Generated by Django 4.1 on 2023-11-16 13:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import filer.fields.image


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.FILER_IMAGE_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('order_field', models.PositiveIntegerField(default=0)),
                ('photo', filer.fields.image.FilerImageField(on_delete=django.db.models.deletion.PROTECT, related_name='photo_slider', to=settings.FILER_IMAGE_MODEL)),
            ],
            options={
                'ordering': ['order_field'],
            },
        ),
    ]
