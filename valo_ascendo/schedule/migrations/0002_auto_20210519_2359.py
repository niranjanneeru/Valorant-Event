# Generated by Django 3.1.11 on 2021-05-19 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='knockout',
            name='winner',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(1, 'TEAM 1'), ('TEAM 2', -1), ('NULL', 0)], null=True),
        ),
    ]
