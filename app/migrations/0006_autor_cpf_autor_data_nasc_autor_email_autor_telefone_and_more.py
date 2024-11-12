# Generated by Django 5.1.3 on 2024-11-12 17:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_emprestimo'),
    ]

    operations = [
        migrations.AddField(
            model_name='autor',
            name='cpf',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='autor',
            name='data_nasc',
            field=models.DateField(default='2000-01-01'),
        ),
        migrations.AddField(
            model_name='autor',
            name='email',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='autor',
            name='telefone',
            field=models.ImageField(default=0, upload_to=''),
        ),
        migrations.AddField(
            model_name='editora',
            name='cnpj',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='editora',
            name='data_fundacao',
            field=models.DateField(default='2000-01-01'),
        ),
        migrations.AddField(
            model_name='editora',
            name='email',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='editora',
            name='razao_social',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='editora',
            name='telefone',
            field=models.ImageField(default=0, upload_to=''),
        ),
        migrations.AlterField(
            model_name='autor',
            name='cidade',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app.cidade'),
        ),
        migrations.AlterField(
            model_name='autor',
            name='nome',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='editora',
            name='cidade',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app.cidade'),
        ),
        migrations.AlterField(
            model_name='editora',
            name='nome',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='editora',
            name='site',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='cidade',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app.cidade'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='cpf',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='data_nasc',
            field=models.DateField(default='2000-01-01'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='email',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='nome',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='telefone',
            field=models.ImageField(default=0, upload_to=''),
        ),
    ]