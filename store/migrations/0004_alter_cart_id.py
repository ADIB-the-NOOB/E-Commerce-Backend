# Generated by Django 4.1.2 on 2022-10-26 16:13

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_alter_cart_id_alter_cartitem_cart_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='id',
            field=models.UUIDField(default=uuid.UUID('2de5b916-2638-4b19-947b-b38ac27c7dc3'), editable=False, primary_key=True, serialize=False),
        ),
    ]
