# Generated by Django 3.2.18 on 2023-04-11 07:02
from django.db import migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('officehours_api', '0022_auto_20210428_1629'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='backend_metadata',
            field=jsonfield.fields.JSONField(blank=True, default=dict, null=True),
        ),
    ]
