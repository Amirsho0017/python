# Generated by Django 5.0 on 2024-01-04 10:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0002_alter_user_options_alter_user_managers_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Permissions",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name="Role",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=200)),
                ("permissions", models.ManyToManyField(to="users.permissions")),
            ],
        ),
        migrations.AddField(
            model_name="user",
            name="role",
            field=models.ForeignKey(
                null=True, on_delete=django.db.models.deletion.SET_NULL, to="users.role"
            ),
        ),
    ]
