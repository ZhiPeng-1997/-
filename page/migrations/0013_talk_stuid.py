# Generated by Django 2.1.2 on 2018-11-29 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0012_talk'),
    ]

    operations = [
        migrations.AddField(
            model_name='talk',
            name='stuID',
            field=models.CharField(default='null', max_length=13),
            preserve_default=False,
        ),
    ]