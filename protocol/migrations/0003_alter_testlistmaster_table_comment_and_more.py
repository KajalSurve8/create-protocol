# Generated by Django 5.0.4 on 2024-04-10 23:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('protocol', '0002_testtable2'),
    ]

    operations = [
        migrations.AlterModelTableComment(
            name='testlistmaster',
            table_comment=None,
        ),
        migrations.AlterModelTable(
            name='testlistmaster',
            table='test_list_master',
        ),
    ]
