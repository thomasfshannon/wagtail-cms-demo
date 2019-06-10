from wagtail.core.blocks import StreamBlock, CharBlock
from .gallery import GalleryBlock
from .contact import ContactForm
from wagtail.core.fields import StreamField

# create a stream block which contains a list of global site blocks
class CommonBlock(StreamBlock):
    gallery = GalleryBlock(icon='placeholder')
    contact_form = ContactForm(icon='placeholder')
    