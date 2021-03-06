# Generated by Django 3.1.2 on 2021-01-07 11:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userfood',
            name='order_date',
        ),
        migrations.RemoveField(
            model_name='userfood',
            name='order_received',
        ),
        migrations.RemoveField(
            model_name='userfood',
            name='recipe',
        ),
        migrations.AlterField(
            model_name='userfood',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='UserOrders',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('order_send', models.DateTimeField(blank=True)),
                ('order_start', models.DateTimeField(blank=True)),
                ('order_finish', models.DateTimeField(blank=True)),
                ('recipe', models.ManyToManyField(blank=True, to='main.Recipes')),
            ],
        ),
        migrations.CreateModel(
            name='CookFood',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='orders.userorders')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='userfood',
            name='order',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='orders.userorders'),
        ),
    ]
