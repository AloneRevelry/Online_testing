# Generated by Django 2.2 on 2019-04-22 21:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('User', '0001_initial'),
        ('Student', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='files',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='User.Student', verbose_name='学号'),
        ),
    ]
