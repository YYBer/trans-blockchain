# Generated by Django 4.2.7 on 2023-12-15 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blockchainTestApp', '0002_alter_gamedata_blockchain_hash'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gamedata',
            name='blockchain_hash',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
    ]
