# Generated by Django 3.2.20 on 2023-07-26 16:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_rename_step_instruction_steps'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Ingredient',
            new_name='Ingredients',
        ),
        migrations.RenameModel(
            old_name='Instruction',
            new_name='Instructions',
        ),
    ]