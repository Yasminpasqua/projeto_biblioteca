# Generated by Django 5.1.3 on 2024-11-12 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_alter_leitor_cpf'),
    ]

    operations = [
        migrations.AlterField(
            model_name='autor',
            name='telefone',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='editora',
            name='telefone',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='telefone',
            field=models.CharField(default='', max_length=255),
        ),
    ]
