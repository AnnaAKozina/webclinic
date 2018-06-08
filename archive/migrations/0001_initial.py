# Generated by Django 2.0.6 on 2018-06-08 15:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=150, verbose_name='Имя')),
                ('sname', models.CharField(max_length=250, verbose_name='Фамилия')),
                ('speciality', models.CharField(max_length=150, verbose_name='Специальность')),
            ],
        ),
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=250, verbose_name='Имя')),
                ('sname', models.CharField(max_length=250, verbose_name='Фамилия')),
                ('address', models.CharField(max_length=250, verbose_name='Адрес')),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Кличка')),
                ('species', models.CharField(max_length=50, verbose_name='Вид животного')),
                ('breed', models.CharField(max_length=150, verbose_name='Порода')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='archive.Owner')),
            ],
        ),
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=250)),
                ('rdate', models.DateTimeField()),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='archive.Doctor')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='archive.Patient')),
            ],
        ),
    ]