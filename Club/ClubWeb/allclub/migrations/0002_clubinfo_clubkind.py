# Generated by Django 3.2 on 2021-05-08 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('allclub', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='clubinfo',
            name='clubkind',
            field=models.CharField(default='体育艺术类', max_length=255),
        ),
    ]
