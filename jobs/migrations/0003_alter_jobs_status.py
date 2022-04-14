# Generated by Django 4.0.3 on 2022-04-08 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0002_jobs'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobs',
            name='status',
            field=models.CharField(choices=[('C', 'Em criação'), ('AA', 'Aguardando aprovação'), ('F', 'Finalizado')], default='C', max_length=2),
        ),
    ]
