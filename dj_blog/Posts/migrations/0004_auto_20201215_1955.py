# Generated by Django 3.1.4 on 2020-12-15 22:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Posts', '0003_post_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(upload_to='img'),
        ),
    ]
