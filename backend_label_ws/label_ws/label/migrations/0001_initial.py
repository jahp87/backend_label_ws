# Generated by Django 4.2.5 on 2023-09-07 13:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BaseLabel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('label_assignment', models.BooleanField(default=True)),
                ('label_exclusivity', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name_plural': 'Base attributes',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='LabelTypes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='AttributeLabel',
            fields=[
                ('baselabel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='label.baselabel')),
                ('attribute_name', models.CharField(max_length=150, verbose_name='attributes name')),
            ],
            options={
                'verbose_name_plural': 'attributes',
                'ordering': ['attribute_name'],
            },
            bases=('label.baselabel',),
        ),
        migrations.CreateModel(
            name='MultiLabel',
            fields=[
                ('baselabel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='label.baselabel')),
            ],
            options={
                'verbose_name_plural': 'multilabels',
                'ordering': ['name'],
            },
            bases=('label.baselabel',),
        ),
        migrations.CreateModel(
            name='SimpleLabel',
            fields=[
                ('baselabel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='label.baselabel')),
            ],
            options={
                'verbose_name_plural': 'Simple attributes',
                'ordering': ['name'],
            },
            bases=('label.baselabel',),
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('data_type', models.CharField(max_length=150)),
                ('annotation_type', models.CharField(max_length=150)),
                ('labels', models.ManyToManyField(blank=True, related_name='labels', to='label.baselabel')),
            ],
            options={
                'verbose_name_plural': 'Images',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Level',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level_name', models.CharField(max_length=150)),
                ('multillabel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='levels', to='label.multilabel')),
            ],
            options={
                'verbose_name_plural': 'levels',
                'ordering': ['level_name'],
            },
        ),
    ]
