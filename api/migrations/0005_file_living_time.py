# Generated by Django 3.0.3 on 2020-07-14 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20200714_1520'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='living_time',
            field=models.DateTimeField(null=True),
        ),
    ]
