# Generated by Django 2.0.1 on 2018-02-15 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='name',
            field=models.CharField(default=1, max_length=100, verbose_name='이름'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='issue',
            name='code_place',
            field=models.TextField(blank=True, null=True, verbose_name='코드 위치'),
        ),
    ]
