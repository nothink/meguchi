# Generated by Django 3.1.3 on 2020-11-23 10:40

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('key', models.CharField(blank=True, db_index=True, max_length=1024, primary_key=True, serialize=False, unique=True, validators=[django.core.validators.RegexValidator(message="This key isn't a vcard resource", regex='^vcard/')])),
                ('url', models.URLField(max_length=1024, validators=[django.core.validators.RegexValidator(message="This url isn't a url of vcard resources", regex='^http(s)?://(([0-9a-zA-Z]*.cloudfront.net)|(c.)?stat100.ameba.jp)/.*')])),
                ('fetched', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
