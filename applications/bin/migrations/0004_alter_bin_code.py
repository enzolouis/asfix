# Generated by Django 5.0 on 2024-03-16 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bin', '0003_tag_bin_author_bin_created_at_bin_title_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bin',
            name='code',
            field=models.CharField(max_length=100),
        ),
    ]
