# Generated by Django 3.2.17 on 2024-03-03 06:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_category_comment_feature_image_product_productfeature'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='comment',
        ),
        migrations.AddField(
            model_name='comment',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.product'),
        ),
    ]