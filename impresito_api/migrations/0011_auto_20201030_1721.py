# Generated by Django 3.1.1 on 2020-10-30 17:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('impresito_api', '0010_auto_20201030_1718'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='venta',
            name='producto',
        ),
        migrations.AddField(
            model_name='producto',
            name='idventa',
            field=models.ForeignKey(default=10, on_delete=django.db.models.deletion.CASCADE, to='impresito_api.venta'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='venta',
            name='productox',
            field=models.CharField(default=0, max_length=100),
        ),
    ]