# Generated by Django 4.2.5 on 2023-09-29 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_recommender', '0002_respostausuario_delete_filme'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='respostausuario',
            name='id',
        ),
        migrations.AlterField(
            model_name='respostausuario',
            name='usuario',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
