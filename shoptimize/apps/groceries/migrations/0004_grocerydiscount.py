# Generated by Django 2.0 on 2018-01-27 21:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('groceries', '0003_grocerystore'),
    ]

    operations = [
        migrations.CreateModel(
            name='GroceryDiscount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price_before', models.DecimalField(decimal_places=2, max_digits=8)),
                ('price_after', models.DecimalField(decimal_places=2, max_digits=8)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='groceries.GroceryItem')),
                ('store', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='groceries.GroceryStore')),
            ],
        ),
    ]
