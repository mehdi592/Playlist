
import datetime
from django.db import migrations, models
import music_nation.models


class Migration(migrations.Migration):

    dependencies = [
        ('music_nation', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='album_logo',
            field=models.FileField(upload_to=music_nation.models.user_directory_path),
        ),
        migrations.AlterField(
            model_name='album',
            name='uploaded_on',
            field=models.DateField(default=datetime.datetime(2018, 10, 4, 14, 28, 46, 653211)),
        ),
        migrations.AlterField(
            model_name='song',
            name='song_file',
            field=models.FileField(upload_to=music_nation.models.user_directory_path),
        ),
    ]
