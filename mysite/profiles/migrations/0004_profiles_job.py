# Generated by Django 2.1 on 2019-04-15 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_profiles_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='profiles',
            name='job',
            field=models.CharField(max_length=120, null=True),
        ),
    ]
