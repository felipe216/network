# Generated by Django 5.1.3 on 2024-11-21 00:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_perfil_sexo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfil',
            name='sexo',
            field=models.CharField(choices=[('M', 'Masculino'), ('F', 'Feminino'), ('O', 'Outro')], max_length=1, null=True),
        ),
    ]
