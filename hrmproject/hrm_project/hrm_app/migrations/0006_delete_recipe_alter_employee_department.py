# Generated by Django 5.0.4 on 2024-05-10 20:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hrm_app', '0005_department_alter_employee_department'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Recipe',
        ),
        migrations.AlterField(
            model_name='employee',
            name='department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hrm_app.department'),
        ),
    ]
