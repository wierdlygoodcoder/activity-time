# Generated by Django 3.2.16 on 2022-10-26 19:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200, unique=True)),
                ('last_name', models.CharField(max_length=200)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('booking_date', models.DateField()),
                ('booking_time', models.TimeField(max_length=30)),
                ('email', models.EmailField(max_length=100)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region='GB')),
                ('what_they_would_like_to_do', models.CharField(choices=[('buliding models', 'Buliding Models'), ('painting models', 'Painting Models'), ('playing wargames', 'Playing Wargames'), ('need specific pating addvice', 'Need Specific Painting Advice'), ('understanding how to play certain game', 'Understanding How To Play Certain Game'), ('advice on canvas poainting', 'Advice On Canvas Painting')], default='bulding models', max_length=50)),
                ('assigned_staff_member', models.CharField(choices=[('1', 'Gareth'), ('2', 'Emily'), ('3', 'Rodger'), ('4', 'Greg'), ('5', 'Alan'), ('6', 'Stevephen'), ('7', 'Patrick')], default='Greg', max_length=50)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users_ids', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
