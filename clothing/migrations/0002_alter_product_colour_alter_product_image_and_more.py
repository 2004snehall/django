# Generated by Django 5.1.6 on 2025-02-21 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clothing', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='colour',
            field=models.CharField(choices=[('Red', 'Red'), ('white', 'white'), ('pink', 'pink'), ('green', 'green'), ('black', 'black')], default='Red', max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(null=True, upload_to='product_img/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='size',
            field=models.CharField(choices=[('S', 'Small'), ('M', 'Medium'), ('L', 'Large'), ('XL', 'Extra large')], default='M', max_length=2, null=True),
        ),
    ]
