# Generated by Django 3.0.7 on 2020-07-14 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('officehours_api', '0017_profile_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='queue',
            name='bluejeans_allowed',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='queue',
            name='inperson_allowed',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='meeting',
            name='backend_type',
            field=models.CharField(choices=[('bluejeans', 'BlueJeans'), ('inperson', 'InPerson')], default='', max_length=20),
        ),
    ]
