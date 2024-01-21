# Generated by Django 5.0.1 on 2024-01-20 23:06

import google.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('google', '0004_alter_googledata_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='googledata',
            old_name='date',
            new_name='today',
        ),
        migrations.AlterField(
            model_name='googledata',
            name='data',
            field=models.FileField(upload_to='', validators=[google.models.validate_csv_file]),
        ),
    ]
