# Generated by Django 2.1 on 2018-11-16 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_profile_orginization'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='orginization',
            field=models.CharField(blank=True, choices=[('Phi_Beta_Sigma', 'Phi Beta Sigma'), ('Zeta_Phi_Beta', 'Zeta Phi Beta')], max_length=128, null=True),
        ),
    ]