# Generated by Django 5.0.6 on 2024-06-04 02:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Functions', '0003_portflolio_projecrs_projects_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='teammember',
            name='contact_no',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]
