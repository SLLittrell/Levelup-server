# Generated by Django 3.2 on 2021-05-05 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('levelupapi', '0003_auto_20210504_1641'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='skill_level',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
