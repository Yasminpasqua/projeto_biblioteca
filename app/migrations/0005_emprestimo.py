# Generated by Django 5.1.2 on 2024-11-05 19:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_usuario_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Emprestimo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dataemprestimo', models.DateField()),
                ('datadevolucao', models.DateField()),
                ('livro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.livro', verbose_name='Livro')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.usuario', verbose_name='Usuario')),
            ],
        ),
    ]
