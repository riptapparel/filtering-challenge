# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('shipping_method', models.CharField(max_length=100, choices=[(b'FCM', b'First Class Mail'), (b'PRI', b'Priority Mail')])),
                ('date_completed', models.DateTimeField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('product', models.CharField(max_length=100, choices=[(b'XS', b'Extra Small Tee'), (b'S', b'Small Tee'), (b'M', b'Medium Tee'), (b'L', b'Large Tee'), (b'XL', b'Extra Large Tee'), (b'2XL', b'Double Extra Large Tee')])),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('order', models.ForeignKey(related_name=b'items', to='orders.Order')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
