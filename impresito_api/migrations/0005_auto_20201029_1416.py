# Generated by Django 3.1.1 on 2020-10-29 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('impresito_api', '0004_membership'),
    ]

    operations = [
        migrations.RenameField(
            model_name='membership',
            old_name='date_joined',
            new_name='fecha',
        ),
        migrations.RemoveField(
            model_name='membership',
            name='invite_reason',
        ),
        migrations.AddField(
            model_name='materiaprima',
            name='members',
            field=models.ManyToManyField(through='impresito_api.Membership', to='impresito_api.Proveedor'),
        ),
    ]
