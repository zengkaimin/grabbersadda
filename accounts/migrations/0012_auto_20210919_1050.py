# Generated by Django 2.2.24 on 2021-09-19 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0011_webinfo_mail'),
    ]

    operations = [
        migrations.AddField(
            model_name='webinfo',
            name='featureimg',
            field=models.ImageField(default='site_images/feature.jpg', upload_to='site_images/'),
        ),
        migrations.AddField(
            model_name='webinfo',
            name='tagline',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]