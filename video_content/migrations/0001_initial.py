# Generated by Django 2.2 on 2020-08-28 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Videos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('video', models.FileField(upload_to='videos/')),
            ],
            options={
                'verbose_name': 'video',
                'verbose_name_plural': 'videos',
            },
        ),
    ]
