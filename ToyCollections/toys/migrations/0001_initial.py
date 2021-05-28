# Generated by Django 3.2.3 on 2021-05-24 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Toy",
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
                ("created", models.DateTimeField(auto_now_add=True)),
                ("name", models.CharField(default="", max_length=150)),
                (
                    "description",
                    models.CharField(blank=True, default="", max_length=250),
                ),
                (
                    "toy_category",
                    models.CharField(blank=True, default="", max_length=250),
                ),
                ("release_date", models.DateTimeField()),
                ("was_include_in_home", models.BooleanField(default=False)),
            ],
            options={
                "ordering": ("name",),
            },
        ),
    ]