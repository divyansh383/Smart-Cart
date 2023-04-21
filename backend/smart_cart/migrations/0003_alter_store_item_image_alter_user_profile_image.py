# Generated by Django 4.1.7 on 2023-04-21 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smart_cart', '0002_store_user_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='store',
            name='item_image',
            field=models.ImageField(blank=True, default='items/default_item.jpg', upload_to='items'),
        ),
        migrations.AlterField(
            model_name='user',
            name='profile_image',
            field=models.ImageField(blank=True, default='profiles/default_profile.jpg', upload_to='profiles'),
        ),
    ]
