# Generated by Django 3.1.3 on 2021-02-19 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=50)),
                ('date_created', models.DateTimeField()),
                ('complete', models.BooleanField(default=False)),
            ],
        ),
    ]
