# Generated by Django 2.1.9 on 2019-06-10 01:42

from django.db import migrations
import home.streamfields.contact
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20190610_0127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contentpage',
            name='body',
            field=wagtail.core.fields.StreamField([('gallery', wagtail.core.blocks.StructBlock([('item', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(required=False)), ('description', wagtail.core.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock())])))], icon='placeholder')), ('contact_form', home.streamfields.contact.ContactForm(icon='placeholder'))], blank=True),
        ),
    ]