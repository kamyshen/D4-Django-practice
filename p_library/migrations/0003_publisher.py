# Generated by Django 2.2.6 on 2019-11-18 08:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('p_library', '0002_auto_20191114_1231'),
    ]

    operations = [
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('description', models.TextField()),
                ('country', models.CharField(max_length=2)),
                ('books', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='p_library.Book')),
            ],
        ),
    ]
