# Generated by Django 3.1.3 on 2020-12-16 16:29

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Posts', '0007_remove_post_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='resumo',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True),
        ),
    ]
