# Generated by Django 4.2.7 on 2023-11-30 21:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_rename_customer_id_order_customer_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='created_order',
            field=models.DateField(default=datetime.date.today),
        ),
    ]