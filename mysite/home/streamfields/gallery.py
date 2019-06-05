# GalleryId
# Title
# Description
# Image

from django.db import models
from wagtail.core.fields import StreamField
from wagtail.core.blocks import ListBlock, RichTextBlock, StructBlock, CharBlock
from wagtail.images.blocks import ImageChooserBlock


class GalleryItem(StructBlock):
    title = CharBlock(required=False)
    description = RichTextBlock()
    image = ImageChooserBlock()

class GalleryBlock(StructBlock):
    item = ListBlock(GalleryItem())

    class Meta:
        template = 'home/blocks/gallery_block.html'
