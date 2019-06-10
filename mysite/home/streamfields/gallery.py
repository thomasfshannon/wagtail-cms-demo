# GalleryId
# Title
# Description
# Image

from django.db import models
from wagtail.core.fields import StreamField
from wagtail.core.blocks import ListBlock, RichTextBlock, StructBlock, CharBlock
from wagtail.images.blocks import ImageChooserBlock

# creates a gallery item w/ title description and image upload
class GalleryItem(StructBlock):
    title = CharBlock(required=False)
    description = RichTextBlock()
    image = ImageChooserBlock()

# Creates a gallery w/ list og gallery items
class GalleryBlock(StructBlock):
    item = ListBlock(GalleryItem())
    
    # declare name of template in meta in which content is invoked
    class Meta:
        template = 'home/blocks/gallery_block.html'
