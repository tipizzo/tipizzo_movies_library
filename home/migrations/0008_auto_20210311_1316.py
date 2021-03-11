# Generated by Django 3.1.7 on 2021-03-11 11:16

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_auto_20210310_1913'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='movie',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='movie',
            name='last_modified',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.RemoveField(
            model_name='movie',
            name='movie_category',
        ),
        migrations.AddField(
            model_name='movie',
            name='movie_category',
            field=models.ManyToManyField(related_name='movies', to='home.Category'),
        ),
    ]