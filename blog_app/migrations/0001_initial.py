# Generated by Django 4.0 on 2021-12-19 18:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TypeDeCulture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_culture', models.CharField(blank=True, max_length=200, null=True)),
                ('description', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CultureAfrica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, null=True, unique=True, verbose_name='Titre')),
                ('content', models.TextField(blank=True, null=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('created_on', models.DateField(auto_now_add=True)),
                ('commentary', models.TextField(blank=True, null=True, verbose_name='Votre Commentaire')),
                ('type_culture', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog_app.typedeculture')),
            ],
        ),
    ]