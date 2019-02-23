# Generated by Django 2.1.7 on 2019-02-23 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Annotations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('src', models.CharField(max_length=300)),
                ('text', models.CharField(max_length=300)),
                ('shape_type', models.CharField(max_length=300)),
                ('x', models.DecimalField(decimal_places=10, max_digits=20)),
                ('y', models.DecimalField(decimal_places=10, max_digits=20)),
                ('width', models.DecimalField(decimal_places=10, max_digits=20)),
                ('height', models.DecimalField(decimal_places=10, max_digits=20)),
            ],
            options={
                'verbose_name': 'Annotation',
                'verbose_name_plural': 'Annotations',
            },
        ),
    ]
