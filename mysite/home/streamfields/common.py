from wagtail.core.blocks import StreamBlock
from .gallery import GalleryBlock
from wagtail.core.fields import StreamField

# create a stream block which contains a list of global site blocks
class CommonBlock(StreamBlock):
    gallery = GalleryBlock(icon="placeholder")