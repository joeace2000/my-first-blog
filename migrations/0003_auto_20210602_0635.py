# Generated by Django 2.2.23 on 2021-06-02 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_priority'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='priority',
            field=models.PositiveIntegerField(),
        ),
    ]
