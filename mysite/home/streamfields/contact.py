from wagtail.core.blocks import StaticBlock


class ContactForm(StaticBlock):
    class Meta:
        template = 'home/blocks/contact_us_block.html'
