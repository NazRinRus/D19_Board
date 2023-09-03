# Generated by Django 4.2.4 on 2023-09-02 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('abs', '0006_alter_ads_text_ads'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ads',
            name='position',
            field=models.CharField(choices=[['TK', 'Tanks'], ['HL', 'Heals'], ['DD', 'Damage Dealers'], ['MH', 'Merchants'], ['GM', 'Guildmasters'], ['QG', 'Questgivers'], ['BS', 'Blacksmiths'], ['LW', 'Leatherworkers'], ['PO', 'Potions'], ['SM', 'Spell masters']], default='TK', max_length=2),
        ),
    ]
