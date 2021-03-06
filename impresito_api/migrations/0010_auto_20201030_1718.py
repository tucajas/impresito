# Generated by Django 3.1.1 on 2020-10-30 17:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('impresito_api', '0009_auto_20201030_1024'),
    ]

    operations = [
        migrations.AddField(
            model_name='materiaprima',
            name='ordenDeTrabajo',
            field=models.ForeignKey(default=10, on_delete=django.db.models.deletion.CASCADE, to='impresito_api.ordendetrabajo'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pedido',
            name='idcliente',
            field=models.ForeignKey(default=10, on_delete=django.db.models.deletion.CASCADE, to='impresito_api.cliente'),
            preserve_default=False,
        ),
    ]
