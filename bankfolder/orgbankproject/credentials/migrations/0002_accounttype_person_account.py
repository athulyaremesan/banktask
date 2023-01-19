# Generated by Django 4.1.5 on 2023-01-18 08:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('credentials', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AccountType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
            ],
        ),
        migrations.AddField(
            model_name='person',
            name='account',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='credentials.accounttype'),
        ),
    ]