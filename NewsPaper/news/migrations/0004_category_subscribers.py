# Generated by Django 4.1.5 on 2023-02-28 11:59

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('news', '0003_remove_category_subscribers_subscription'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='subscribers',
            field=models.ManyToManyField(related_name='categories', through='news.Subscription', to=settings.AUTH_USER_MODEL),
        ),
    ]