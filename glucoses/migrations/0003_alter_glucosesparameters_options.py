# Generated by Django 4.1.7 on 2023-03-16 10:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('glucoses', '0002_glucosesparameters_delete_bloodpressureparameters'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='glucosesparameters',
            options={'verbose_name': 'Glukoza', 'verbose_name_plural': 'Glukozy'},
        ),
    ]
