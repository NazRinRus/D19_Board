# Generated by Django 4.2.4 on 2023-08-27 11:09

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('abs', '0004_alter_ads_text_ads'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ads',
            name='text_ads',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
