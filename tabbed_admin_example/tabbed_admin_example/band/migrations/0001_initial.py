# Generated by Django 2.1 on 2019-10-21 00:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Band',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('bio', models.TextField(blank=True, null=True)),
                ('style', models.CharField(choices=[('rock', 'Rock'), ('metal', 'Metal'), ('funk', 'Funk'), ('jazz', 'Jazz')], max_length=100)),
                ('agent', models.CharField(blank=True, max_length=100, null=True)),
                ('phone', models.CharField(blank=True, max_length=100, null=True)),
                ('email', models.CharField(blank=True, max_length=100, null=True)),
                ('address', models.CharField(blank=True, max_length=100, null=True)),
                ('website', models.CharField(blank=True, max_length=100, null=True)),
                ('twitter', models.CharField(blank=True, max_length=100, null=True)),
                ('facebook', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Concert',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('band', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='band.Band')),
            ],
        ),
        migrations.CreateModel(
            name='Interview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('media_name', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('band', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='band.Band')),
            ],
        ),
        migrations.CreateModel(
            name='Musician',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('specialty', models.CharField(choices=[('vocal', 'Vocal'), ('guitar', 'Guitar'), ('bass', 'Bass'), ('drums', 'Drums')], max_length=100)),
                ('band', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='band.Band')),
            ],
        ),
        migrations.AddField(
            model_name='album',
            name='band',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='band.Band'),
        ),
    ]
