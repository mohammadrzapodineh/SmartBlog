# Generated by Django 4.0.4 on 2022-05-22 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0002_alter_post_status_alter_post_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(blank=True, editable=False, max_length=250, unique_for_date='publish'),
        ),
    ]
