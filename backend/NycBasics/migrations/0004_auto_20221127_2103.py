# Generated by Django 2.2 on 2022-11-28 02:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("NycBasics", "0003_user_token_timestamp"),
    ]

    operations = [
        migrations.AddField(
            model_name="rating_review",
            name="xyz",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="usermodel_username_set",
                to="NycBasics.User",
                to_field="username",
            ),
        ),
        migrations.AlterField(
            model_name="rating_review",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="usermodel_userid_set",
                to="NycBasics.User",
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="username",
            field=models.CharField(max_length=255, unique=True),
        ),
    ]