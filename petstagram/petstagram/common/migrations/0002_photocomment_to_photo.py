# Generated by Django 5.0.2 on 2024-03-12 13:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0001_initial'),
        ('photos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='photocomment',
            name='to_photo',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='photos.photo'),
            preserve_default=False,
        ),
    ]
