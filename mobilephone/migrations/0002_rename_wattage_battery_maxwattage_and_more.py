# Generated by Django 4.0.3 on 2022-03-22 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mobilephone', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='battery',
            old_name='wattage',
            new_name='maxWattage',
        ),
        migrations.AddField(
            model_name='battery',
            name='providedWattage',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.RemoveField(
            model_name='battery',
            name='technologies',
        ),
        migrations.AddField(
            model_name='battery',
            name='technologies',
            field=models.ManyToManyField(to='mobilephone.batterytech'),
        ),
    ]
