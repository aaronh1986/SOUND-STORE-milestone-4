# Generated by Django 3.2.7 on 2021-10-20 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blogpost',
            options={'ordering': ('-created_on',)},
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='author',
            field=models.CharField(max_length=250),
        ),
    ]
