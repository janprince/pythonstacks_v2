# Generated by Django 4.1.4 on 2022-12-30 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_last_mod'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='meta_description',
            field=models.TextField(blank=True, max_length=200),
        ),
    ]