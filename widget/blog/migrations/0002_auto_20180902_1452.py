# Generated by Django 2.1.1 on 2018-09-02 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='when',
            field=models.DateField(),
        ),
    ]
