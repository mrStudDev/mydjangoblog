# Generated by Django 3.1.4 on 2020-12-16 00:03

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Posts', '0004_auto_20201215_1955'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='conteudo',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True),
        ),
    ]
