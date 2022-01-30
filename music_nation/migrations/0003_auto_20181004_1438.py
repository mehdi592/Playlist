

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music_nation', '0002_auto_20181004_1428'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='uploaded_on',
            field=models.DateField(default=datetime.datetime(2018, 10, 4, 14, 38, 27, 182802)),
        ),
    ]
