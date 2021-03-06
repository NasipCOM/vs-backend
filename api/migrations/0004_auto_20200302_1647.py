# Generated by Django 3.0.2 on 2020-03-02 10:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_field_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fieldvalue',
            name='field',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='field_value', to='api.Field'),
        ),
        migrations.AlterField(
            model_name='fieldvalue',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='field_value', to='api.Product'),
        ),
    ]
