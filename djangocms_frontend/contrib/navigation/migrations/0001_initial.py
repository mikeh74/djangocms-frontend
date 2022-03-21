# Generated by Django 3.2.12 on 2022-03-16 17:18

from django.db import migrations


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("djangocms_frontend", "0001_initial"),
        ("link", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="NavBrand",
            fields=[],
            options={
                "verbose_name": "Brand",
                "proxy": True,
                "indexes": [],
                "constraints": [],
            },
            bases=("djangocms_frontend.frontenduiitem",),
        ),
        migrations.CreateModel(
            name="NavContainer",
            fields=[],
            options={
                "verbose_name": "Navigation container",
                "proxy": True,
                "indexes": [],
                "constraints": [],
            },
            bases=("djangocms_frontend.frontenduiitem",),
        ),
        migrations.CreateModel(
            name="Navigation",
            fields=[],
            options={
                "verbose_name": "Navigation",
                "proxy": True,
                "indexes": [],
                "constraints": [],
            },
            bases=("djangocms_frontend.frontenduiitem",),
        ),
        migrations.CreateModel(
            name="NavLink",
            fields=[],
            options={
                "verbose_name": "Navigation Link",
                "proxy": True,
                "indexes": [],
                "constraints": [],
            },
            bases=("link.link",),
        ),
        migrations.CreateModel(
            name="PageTree",
            fields=[],
            options={
                "verbose_name": "Page tree",
                "proxy": True,
                "indexes": [],
                "constraints": [],
            },
            bases=("djangocms_frontend.frontenduiitem",),
        ),
    ]