# Generated by Django 4.2.4 on 2023-08-27 09:42

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('abs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='text_post',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True),
        ),
    ]
