# Generated by Django 5.1.3 on 2024-11-27 10:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_likepost_alter_post_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ('-created_at', '-no_of_likes')},
        ),
    ]