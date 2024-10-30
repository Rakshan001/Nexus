# Generated by Django 5.1.2 on 2024-10-30 06:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alumni_details', '0003_alter_alumni_profile_picture'),
    ]

    operations = [
        migrations.CreateModel(
            name='CouncilMember',
            fields=[
                ('count_mem_id', models.AutoField(primary_key=True, serialize=False)),
                ('role', models.CharField(choices=[('President', 'President'), ('Vice President', 'Vice President'), ('Secretary', 'Secretary'), ('Joint Secretary', 'Joint Secretary')], max_length=20)),
                ('year', models.IntegerField()),
                ('alumni', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='council_members', to='alumni_details.alumni')),
            ],
            options={
                'indexes': [models.Index(fields=['role'], name='alumni_deta_role_36630f_idx'), models.Index(fields=['year'], name='alumni_deta_year_1d8f3f_idx')],
                'unique_together': {('alumni', 'role', 'year')},
            },
        ),
    ]