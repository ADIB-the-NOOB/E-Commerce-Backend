# Generated by Django 4.1.2 on 2022-10-26 15:20

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='id',
            field=models.UUIDField(default=uuid.UUID('139048e6-2339-4cf3-9312-4d57669d8142'), editable=False, primary_key=True, serialize=False),
        ),
    ]
