# Generated by Django 2.1.2 on 2018-10-28 05:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('djadesh', '0012_auto_20181028_0531'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemimage',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='djadesh.Item'),
        ),
        migrations.AlterField(
            model_name='itemproperty',
            name='item',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='properties', to='djadesh.Item'),
        ),
    ]