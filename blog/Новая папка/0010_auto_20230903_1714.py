from django.db import migrations, models
import datetime

def convert_time_to_timestamp(apps, schema_editor):
    UserInfo = apps.get_model('ваше_приложение', 'UserInfo')
    for user in UserInfo.objects.all():
        user.data = datetime.datetime.combine(datetime.date.today(), user.data)
        user.save()

class Migration(migrations.Migration):

    dependencies = [

    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='data_new',
            field=models.DateTimeField(default=datetime.datetime.now),
            preserve_default=False,
        ),
        migrations.RunPython(convert_time_to_timestamp),
        migrations.RemoveField(
            model_name='userinfo',
            name='data',
        ),
        migrations.RenameField(
            model_name='userinfo',
            old_name='data_new',
            new_name='data',
        ),
    ]
