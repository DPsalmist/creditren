# Generated by Django 3.1.7 on 2021-03-17 16:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('loan', '0003_auto_20210316_1008'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='Group 1', max_length=20)),
                ('member', models.ForeignKey(null='blank', on_delete=django.db.models.deletion.CASCADE, related_name='group_member', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Lender',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateTimeField(auto_now_add=True)),
                ('end_date', models.DateTimeField()),
                ('frequency', models.IntegerField(blank=True, default=0)),
                ('status', models.CharField(choices=[('complete', 'Complete'), ('incomplete', 'Incomplete')], default='incomplete', max_length=30)),
                ('loan_type', models.CharField(choices=[('23', '6 Months'), ('48', '12 Months'), ('60', '15 Months'), ('96', '24 Months')], max_length=30)),
                ('loan_amount', models.FloatField()),
                ('description', models.TextField()),
                ('group', models.ForeignKey(null='blank', on_delete=django.db.models.deletion.CASCADE, related_name='batches', to='loan.group')),
                ('owner', models.ForeignKey(null='blank', on_delete=django.db.models.deletion.CASCADE, related_name='loan_owners', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-start_date',),
            },
        ),
        migrations.DeleteModel(
            name='Loan',
        ),
    ]