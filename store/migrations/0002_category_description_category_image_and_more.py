# Generated by Django 4.1.5 on 2023-01-11 11:37

from django.db import migrations, models
import django.db.models.deletion
import store.models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='description',
            field=models.TextField(default=1, max_length=150),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=store.models.get_file_path),
        ),
        migrations.AddField(
            model_name='category',
            name='meta_description',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='category',
            name='meta_keywords',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='category',
            name='meta_title',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='category',
            name='name',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='category',
            name='status',
            field=models.BooleanField(default=False, help_text='0=default, 1=Hidden'),
        ),
        migrations.AddField(
            model_name='category',
            name='trending',
            field=models.BooleanField(default=1, help_text='0=default, 1=Trending'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='store.category'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.TextField(default=1, max_length=150),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='meta_description',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='meta_keywords',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='meta_title',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='name',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='original_price',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='product_image',
            field=models.ImageField(blank=True, null=True, upload_to=store.models.get_file_path),
        ),
        migrations.AddField(
            model_name='product',
            name='quantity',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='selling_price',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='small_description',
            field=models.TextField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='status',
            field=models.BooleanField(default=False, help_text='0=default, 1=Hidden'),
        ),
        migrations.AddField(
            model_name='product',
            name='trending',
            field=models.BooleanField(default=1, help_text='0=default, 1=Trending'),
            preserve_default=False,
        ),
    ]
