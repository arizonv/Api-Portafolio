# Generated by Django 4.2.4 on 2023-09-10 14:39

import accounts.models
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import re


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Permiso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clase', models.CharField(choices=[('Permiso', 'Permiso'), ('Rol', 'Rol'), ('User', 'User'), ('Cliente', 'Cliente'), ('Reserva', 'Reserva'), ('Ticket', 'Ticket'), ('Boleta', 'Boleta'), ('TipoCancha', 'TipoCancha'), ('Cancha', 'Cancha'), ('Horario', 'Horario'), ('Agenda', 'Agenda')], max_length=15)),
                ('nombre', models.CharField(max_length=50)),
            ],
            options={
                'unique_together': {('clase', 'nombre')},
            },
        ),
        migrations.CreateModel(
            name='Rol',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(choices=[('admin', 'Administrador'), ('trabajador', 'Trabajador'), ('cliente', 'Cliente')], max_length=15, unique=True)),
                ('permisos', models.ManyToManyField(to='accounts.permiso')),
            ],
            options={
                'verbose_name_plural': 'roles',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('username', models.CharField(help_text='Un nombre corto que sera usado para identificarlo de forma unica en la plataforma.', max_length=30, unique=True, validators=[django.core.validators.RegexValidator(re.compile('^[\\w.@+-]+$'), 'ingrese un nombre de usuario valido Este valor debe contener solo letras, números excepto: @/./+/-/_.', 'invalid')], verbose_name='Usuario')),
                ('name', models.CharField(max_length=20, verbose_name='Nombre')),
                ('apellidos', models.CharField(max_length=30, verbose_name='Apellidos')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Email')),
                ('is_staff', models.BooleanField(default=False, verbose_name='Admin')),
                ('is_active', models.BooleanField(default=True, verbose_name='Ativo')),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='Data de Entrada')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('roles', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.rol')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'Usuario',
                'verbose_name_plural': 'Usuarios',
            },
            managers=[
                ('objects', accounts.models.CustomUserManager()),
            ],
        ),
    ]
