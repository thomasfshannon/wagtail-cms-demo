from django.db import models
from wagtail.core.models import Page
from wagtail.admin.edit_handlers import StreamFieldPanel
from wagtail.core.fields import StreamField
from .streamfields.common import CommonBlock
class HomePage(Page):
    pass

# creates a content page w/ general stream block
class ContentPage(Page):
    body = StreamField(CommonBlock, blank=True)

    content_panels = Page.content_panels + [
        StreamFieldPanel('body'),
    ]