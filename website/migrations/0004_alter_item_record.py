# Generated by Django 5.1.5 on 2025-04-01 08:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_item'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='record',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='website.record'),
        ),
    ]
