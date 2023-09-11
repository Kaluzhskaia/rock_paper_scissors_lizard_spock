# Generated by Django 4.1.3 on 2023-09-11 11:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('player1_name', models.CharField(max_length=30)),
                ('player2_name', models.CharField(max_length=30)),
                ('player1_score', models.PositiveIntegerField(default=0)),
                ('player2_score', models.PositiveIntegerField(default=0)),
                ('with_computer', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Move',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('player1_choice', models.CharField(choices=[('Rock', 'Rock'), ('Paper', 'Paper'), ('Scissors', 'Scissors'), ('Lizard', 'Lizard'), ('Spock', 'Spock')], max_length=8)),
                ('player2_choice', models.CharField(choices=[('Rock', 'Rock'), ('Paper', 'Paper'), ('Scissors', 'Scissors'), ('Lizard', 'Lizard'), ('Spock', 'Spock')], max_length=8)),
                ('winner', models.CharField(max_length=30)),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gameplay.game')),
            ],
        ),
    ]