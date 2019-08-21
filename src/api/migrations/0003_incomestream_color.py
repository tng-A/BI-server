# Generated by Django 2.2.4 on 2019-08-21 19:08

from django.db import migrations, models
import src.api.helpers.colors


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20190820_1233'),
    ]

    operations = [
        migrations.AddField(
            model_name='incomestream',
            name='color',
            field=models.CharField(blank=True, default=src.api.helpers.colors.generate_random_color, help_text='Default color associated with this income stream.', max_length=255),
        ),
    ]
