# Generated by Django 4.1.2 on 2023-11-16 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ListModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('capital_name', models.CharField(max_length=255, verbose_name='Capital Name')),
                ('capital_qty', models.BigIntegerField(default=0, verbose_name='Capital Qty')),
                ('capital_cost', models.FloatField(default=0, verbose_name='Capital Cost')),
                ('creater', models.CharField(max_length=255, verbose_name='Who Created')),
                ('openid', models.CharField(max_length=255, verbose_name='Openid')),
                ('is_delete', models.BooleanField(default=False, verbose_name='Delete Label')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='Create Time')),
                ('update_time', models.DateTimeField(auto_now=True, null=True, verbose_name='Update Time')),
            ],
            options={
                'verbose_name': 'Capital',
                'verbose_name_plural': 'Capital',
                'db_table': 'capital',
                'ordering': ['-id'],
            },
        ),
    ]
