# Generated by Django 5.0.6 on 2024-06-03 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Functions', '0002_teammember_image_alter_portflolio_projecrs_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='portflolio_projecrs',
            name='projects_type',
            field=models.CharField(blank=True, choices=[('Web', 'Website'), ('app', 'Mobile App'), ('card', 'Card')], max_length=50, null=True),
        ),
    ]
