from ._anvil_designer import ClickableCardTemplate
from anvil import *


class ClickableCard(ClickableCardTemplate):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value
        self.lbl_title.text = value
        
    @property
    def subtitle(self):
        return self._subtitle

    @subtitle.setter
    def subtitle(self, value):
        self._subtitle = value
        self.lbl_subtitle.text = value
        if self.lbl_subtitle.text and self.lbl_subtitle.text != '':
            self.lbl_subtitle.visible = True

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value
        self.lbl_desc.text = value
        
    @property
    def image(self):
        return self._img

    @image.setter
    def image(self, value):
        self._img = value
        self.img.source = value
    
    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, value):
        self._url = value
        self.link_card.url = value

    def link_card_click(self, **event_args):
        """This method is called when the link is clicked"""
        self.raise_event('click')
