# Generated by Django 4.1.2 on 2023-04-26 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0010_review'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CardNo', models.IntegerField(max_length=16, null=True)),
                ('CardCvv', models.IntegerField(max_length=3, null=True)),
            ],
        ),
    ]
