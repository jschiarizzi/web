# Generated by Django 2.1.1 on 2018-09-17 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0107_auto_20180912_1703'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraction',
            name='action',
            field=models.CharField(choices=[('Login', 'Login'), ('Logout', 'Logout'), ('added_slack_integration', 'Added Slack Integration'), ('removed_slack_integration', 'Removed Slack Integration'), ('updated_avatar', 'Updated Avatar'), ('account_disconnected', 'Account Disconnected')], max_length=50),
        ),
    ]
