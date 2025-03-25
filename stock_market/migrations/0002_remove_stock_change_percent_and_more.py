# Generated by Django 5.1.7 on 2025-03-24 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock_market', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stock',
            name='change_percent',
        ),
        migrations.RemoveField(
            model_name='stock',
            name='current_price',
        ),
        migrations.RemoveField(
            model_name='stock',
            name='dividend_yield',
        ),
        migrations.RemoveField(
            model_name='stock',
            name='last_updated',
        ),
        migrations.RemoveField(
            model_name='stock',
            name='market_cap',
        ),
        migrations.RemoveField(
            model_name='stock',
            name='pe_ratio',
        ),
        migrations.RemoveField(
            model_name='stock',
            name='volume',
        ),
        migrations.AddField(
            model_name='stock',
            name='graph_path',
            field=models.ImageField(blank=True, max_length=255, null=True, upload_to='stock_graphs/'),
        ),
        migrations.AddField(
            model_name='stock',
            name='last_price',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='stock',
            name='predicted_1y',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='stock',
            name='predicted_2y',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='stock',
            name='predicted_3y',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='stock',
            name='predicted_4y',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='stock',
            name='predicted_5y',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='stock',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='stock',
            name='symbol',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
