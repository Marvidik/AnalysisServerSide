# Generated by Django 5.0.1 on 2024-01-20 10:55

import google.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('google', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='googledata',
            name='date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='googledata',
            name='data',
            field=models.FileField(upload_to='csv_files', validators=[google.models.validate_csv_file]),
        ),
    ]