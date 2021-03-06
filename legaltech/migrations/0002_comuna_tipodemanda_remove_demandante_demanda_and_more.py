# Generated by Django 4.0.4 on 2022-04-17 19:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('legaltech', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comuna',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Tipodemanda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=25)),
            ],
        ),
        migrations.RemoveField(
            model_name='demandante',
            name='demanda',
        ),
        migrations.RenameField(
            model_name='demanda',
            old_name='caso',
            new_name='id_caso',
        ),
        migrations.RemoveField(
            model_name='caso',
            name='author',
        ),
        migrations.AddField(
            model_name='demanda',
            name='apellido1',
            field=models.CharField(blank=True, default='', max_length=25, null=True),
        ),
        migrations.AddField(
            model_name='demanda',
            name='apellido2',
            field=models.CharField(blank=True, default='', max_length=25, null=True),
        ),
        migrations.AddField(
            model_name='demanda',
            name='dv1',
            field=models.CharField(blank=True, default='', max_length=2, null=True),
        ),
        migrations.AddField(
            model_name='demanda',
            name='dv2',
            field=models.CharField(blank=True, default='', max_length=2, null=True),
        ),
        migrations.AddField(
            model_name='demanda',
            name='nombre1',
            field=models.CharField(blank=True, default='', max_length=25, null=True),
        ),
        migrations.AddField(
            model_name='demanda',
            name='nombre2',
            field=models.CharField(blank=True, default='', max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='demanda',
            name='rut1',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='demanda',
            name='rut2',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='demanda',
            name='telefono1',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='demanda',
            name='telefono2',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.DeleteModel(
            name='Demandado',
        ),
        migrations.DeleteModel(
            name='Demandante',
        ),
        migrations.AddField(
            model_name='demanda',
            name='comuna1',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comuna1', to='legaltech.comuna'),
        ),
        migrations.AddField(
            model_name='demanda',
            name='comuna2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comuna2', to='legaltech.comuna'),
        ),
        migrations.AlterField(
            model_name='demanda',
            name='tipodemanda',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='legaltech.tipodemanda'),
        ),
    ]
