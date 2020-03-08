# Generated by Django 3.0.3 on 2020-02-28 05:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('netbankingapp', '0002_auto_20200228_0439'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='pin',
            field=models.CharField(blank=True, help_text='Required. 6 digits or 4 digit number', max_length=300, null=True),
        ),
        migrations.CreateModel(
            name='AllTransactions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('withdrawstatus', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('depositstatus', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('transferedMoney', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='account', to='netbankingapp.Account')),
                ('receiveracc', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='receiversacc', to='netbankingapp.Account')),
            ],
        ),
    ]
