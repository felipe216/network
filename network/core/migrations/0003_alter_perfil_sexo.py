# Generated by Django 5.1.3 on 2024-11-21 00:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_remove_perfil_idade_perfil_data_nascimento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfil',
            name='sexo',
            field=models.CharField(choices=[('M', 'Masculino'), ('F', 'Feminino')], max_length=1, null=True),
        ),
    ]
