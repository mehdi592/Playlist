
import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('album_name', models.CharField(max_length=30)),
                ('uploaded_on', models.DateField(default=datetime.datetime(2018, 10, 4, 12, 35, 4, 306720))),
                ('album_logo', models.FileField(upload_to='')),
                ('album_genre', models.CharField(max_length=30)),
                ('album_artist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='albums', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('song_name', models.CharField(max_length=40)),
                ('song_file', models.FileField(upload_to='')),
                ('song_album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='songs', to='music_nation.Album')),
            ],
        ),
    ]
