# Generated by Django 4.0.5 on 2023-01-16 04:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('arquivo', '0002_documento_rename_tipodelancamento_tipodedocumento_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='documento',
            name='arquivo',
        ),
        migrations.DeleteModel(
            name='Arquivo',
        ),
    ]
