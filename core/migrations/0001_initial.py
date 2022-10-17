# Generated by Django 4.1.1 on 2022-10-03 09:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="User",
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
                ("added_at", models.DateTimeField(verbose_name="added_at")),
            ],
        ),
        migrations.CreateModel(
            name="Command",
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
                ("command_text", models.CharField(max_length=200)),
                ("added_at", models.DateTimeField(verbose_name="added_at")),
                (
                    "command",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="core.user"
                    ),
                ),
            ],
        ),
    ]