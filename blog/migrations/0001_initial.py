# Generated by Django 4.1.1 on 2023-07-05 20:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blogger',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(help_text="The blogger's first name.", max_length=100)),
                ('last_name', models.CharField(help_text="The blogger's last name.", max_length=100)),
                ('bio', models.CharField(help_text='A short biography of the user.', max_length=500)),
            ],
            options={
                'ordering': ['last_name'],
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Enter a title for your blog post.', max_length=100)),
                ('sub_title', models.CharField(blank=True, help_text='Enter a sub-title for your blog post.', max_length=100)),
                ('slug', models.SlugField(blank=True, help_text='Enter a URL friendly short label for your blog post.', max_length=100, unique=True)),
                ('content', models.TextField(help_text='Enter the content of your blog post here.', max_length=2000, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='The time at which your post was created.')),
                ('updated_at', models.DateTimeField(auto_now_add=True, help_text='The last time your blog post was updated.')),
                ('votes', models.IntegerField(default=0)),
                ('blogger', models.ForeignKey(default=1, on_delete=django.db.models.deletion.RESTRICT, to='blog.blogger')),
            ],
            options={
                'ordering': ['updated_at'],
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(help_text='Enter the content of your comment here.', max_length=1000)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('commenter', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='blog.blogger')),
                ('post', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, to='blog.post')),
            ],
            options={
                'ordering': ['created_at'],
            },
        ),
    ]
