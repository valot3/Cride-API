# Generated by Django 3.1.1 on 2021-09-10 15:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('circles', '0005_invitation'),
        ('rides', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ride',
            old_name='raiting',
            new_name='rating',
        ),
        migrations.AlterField(
            model_name='ride',
            name='offered_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='ride',
            name='offered_in',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='circles.circle'),
        ),
    ]
