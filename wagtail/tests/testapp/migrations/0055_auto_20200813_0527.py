# Generated by Django 3.0.9 on 2020-08-12 20:27

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.tests.testapp.models


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0054_simpletask'),
    ]

    operations = [
        migrations.AlterField(
            model_name='streampage',
            name='body',
            field=wagtail.core.fields.StreamField([('text', wagtail.core.blocks.CharBlock()), ('rich_text', wagtail.core.blocks.RichTextBlock()), ('image', wagtail.tests.testapp.models.ExtendedImageChooserBlock()), ('product', wagtail.core.blocks.StructBlock([('name', wagtail.core.blocks.CharBlock()), ('price', wagtail.core.blocks.CharBlock())])), ('raw_html', wagtail.core.blocks.RawHTMLBlock()), ('books', wagtail.core.blocks.StreamBlock([('title', wagtail.core.blocks.CharBlock()), ('author', wagtail.core.blocks.CharBlock())]))]),
        ),
    ]
