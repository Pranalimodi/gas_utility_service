# Generated by Django 5.1.2 on 2024-10-10 11:56

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("customer", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="servicerequest",
            old_name="description",
            new_name="details",
        ),
        migrations.RemoveField(
            model_name="servicerequest",
            name="email",
        ),
        migrations.RemoveField(
            model_name="servicerequest",
            name="name",
        ),
        migrations.AddField(
            model_name="servicerequest",
            name="customer_name",
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="servicerequest",
            name="request_type",
            field=models.CharField(default=23, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="servicerequest",
            name="updated_at",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name="servicerequest",
            name="service_type",
            field=models.CharField(
                choices=[
                    ("installation", "Installation"),
                    ("maintenance", "Maintenance"),
                    ("repair", "Repair"),
                ],
                max_length=50,
            ),
        ),
    ]
