from django.db import models
from wagtail.snippets.models import register_snippet
from wagtail.core.fields import StreamField
from wagtail.admin.edit_handlers import StreamFieldPanel, FieldPanel
from wagtail.core import blocks


class WordTranslationBlock(blocks.StreamBlock):
    translations = blocks.StructBlock([
        ('word', blocks.CharBlock(max_length=255, required=True)),
        ('en', blocks.CharBlock(max_length=255)),
        ('sp', blocks.CharBlock(max_length=255)),
        ('fr', blocks.CharBlock(max_length=255))
    ])

@register_snippet
class Translation(models.Model):
    page = models.CharField(max_length=255, blank=False)
    body = StreamField(WordTranslationBlock())

    panels = [
        FieldPanel('page'),
        StreamFieldPanel('body'),
    ]

    def __str__(self):
        return self.page
