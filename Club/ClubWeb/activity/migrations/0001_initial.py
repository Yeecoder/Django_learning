# Generated by Django 3.2 on 2021-06-08 15:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('signinaout', '0004_auto_20210529_2216'),
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('context', models.TextField()),
                ('publish_time', models.DateTimeField(auto_now_add=True)),
                ('change_time', models.DateTimeField(auto_now=True)),
                ('publisher', models.ForeignKey(default='bbb', on_delete=django.db.models.deletion.CASCADE, to='signinaout.user')),
            ],
        ),
    ]
