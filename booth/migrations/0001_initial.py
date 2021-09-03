# Generated by Django 3.2.6 on 2021-09-03 08:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='boothTags',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booth_tag', models.CharField(max_length=10, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='boothPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('intro', models.CharField(max_length=30)),
                ('pub_time', models.DateTimeField(auto_now_add=True)),
                ('body', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('booth_like', models.ManyToManyField(blank=True, related_name='booth_like', to=settings.AUTH_USER_MODEL)),
                ('hashtag_set', models.ManyToManyField(blank=True, to='booth.boothTags')),
            ],
        ),
        migrations.CreateModel(
            name='boothComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_contents', models.TextField()),
                ('comment_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('comment_writer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('post', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='booth.boothpost')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
    ]
