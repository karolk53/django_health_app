# Generated by Django 4.1.7 on 2023-03-16 10:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('boolpresures', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bloodpressureparameters',
            name='pulse',
            field=models.IntegerField(default=60),
        ),
        migrations.AddField(
            model_name='bloodpressureparameters',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='bloodpressureparameters',
            name='examination_date',
            field=models.DateTimeField(),
        ),
    ]