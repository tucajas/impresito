# Generated by Django 3.1.1 on 2020-10-28 16:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('impresito_api', '0003_auto_20201028_1643'),
    ]

    operations = [
        migrations.CreateModel(
            name='Membership',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_joined', models.DateField()),
                ('invite_reason', models.CharField(max_length=64)),
                ('materiaprima', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='impresito_api.materiaprima')),
                ('proveedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='impresito_api.proveedor')),
            ],
        ),
    ]
