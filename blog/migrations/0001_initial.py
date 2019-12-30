# Generated by Django 2.2.9 on 2019-12-29 22:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='', verbose_name='images/')),
                ('title', models.CharField(max_length=100)),
                ('pub_date', models.DateField(auto_now=True)),
                ('body', models.TextField()),
            ],
        ),
    ]
