# Generated by Django 4.2.7 on 2023-11-30 22:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0021_remove_bill_discount'),
    ]

    operations = [
        migrations.AddField(
            model_name='bill',
            name='discount',
            field=models.PositiveBigIntegerField(default=100),
        ),
    ]