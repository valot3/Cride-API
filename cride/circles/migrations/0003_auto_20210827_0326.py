# Generated by Django 3.1.1 on 2021-08-27 03:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('circles', '0002_auto_20210825_0530'),
    ]

    operations = [
        migrations.RenameField(
            model_name='membership',
            old_name='remaining_invitatio',
            new_name='remaining_invitations',
        ),
    ]
