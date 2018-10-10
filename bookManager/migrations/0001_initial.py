# Generated by Django 2.2 on 2018-10-09 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_name', models.CharField(max_length=64)),
                ('book_author', models.CharField(max_length=64)),
                ('add_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
