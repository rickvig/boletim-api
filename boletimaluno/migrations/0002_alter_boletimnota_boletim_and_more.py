# Generated by Django 4.0.4 on 2022-11-09 13:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('boletimaluno', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boletimnota',
            name='boletim',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='boletimaluno.boletim'),
        ),
        migrations.AlterField(
            model_name='boletimnota',
            name='disciplina',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='boletimaluno.disciplina'),
        ),
    ]
