# Generated by Django 4.2.6 on 2023-11-02 01:15

from django.db import migrations
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_homepage_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='information',
            field=wagtail.fields.RichTextField(blank=True),
        ),
    ]
