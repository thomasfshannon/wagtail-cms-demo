from django.db import models
from wagtail.core.models import Page
from wagtail.admin.edit_handlers import StreamFieldPanel
from wagtail.core.fields import StreamField
from .streamfields.common import CommonBlock
from .snippets import Translation
class HomePage(Page):
    pass

# creates a content page w/ general stream block of reusable blocks
class ContentPage(Page):
    body = StreamField(CommonBlock, blank=True)
    
    # panels to show on the page
    content_panels = Page.content_panels + [
        StreamFieldPanel('body'),
    ]

class SinglePageApp(Page):
    translations = Translation.objects.all()