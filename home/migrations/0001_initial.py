# Generated by Django 4.0.5 on 2022-06-29 11:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('title', models.CharField(max_length=50)),
                ('cat_id', models.AutoField(primary_key=True, serialize=False)),
                ('description', models.TextField(max_length=500)),
                ('add_date', models.DateField(auto_now_add=True, null=True)),
                ('image', models.ImageField(upload_to='category')),
                ('url', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('post_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=50)),
                ('content', models.TextField()),
                ('url', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='posts')),
                ('cat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.category')),
            ],
        ),
    ]