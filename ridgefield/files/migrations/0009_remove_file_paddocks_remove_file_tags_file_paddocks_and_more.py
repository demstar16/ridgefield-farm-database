# Generated by Django 4.1.1 on 2022-09-30 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('files', '0008_alter_pastfile_fileref'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='file',
            name='paddocks',
        ),
        migrations.RemoveField(
            model_name='file',
            name='tags',
        ),
        migrations.AddField(
            model_name='file',
            name='paddocks',
            field=models.ManyToManyField(blank=True, related_name='paddocks', to='files.paddock'),
        ),
        migrations.AddField(
            model_name='file',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='tags', to='files.tag'),
        ),
    ]