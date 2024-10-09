from ._anvil_designer import IconCardTemplate
from anvil import *
import anvil.js


class IconCard(IconCardTemplate):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)
        dom_node = anvil.js.get_dom_node(self.link_card)
        dom_node.addEventListener('mouseover', self.mouseover_event)
        dom_node.addEventListener('mouseout', self.mouseoff_event)
        # Any code you write here will run before the form opens.

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value
        self.lbl_title.text = value

    @property
    def icon(self):
        return self._icon

    @icon.setter
    def icon(self, value):
        self._icon = value
        self.lbl_icon.icon = value

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value

    def link_card_click(self, **event_args):
        """This method is called when the link is clicked"""
        self.raise_event('click')

    def mouseover_event(self, sender, **event_args):
        self.lbl_title.bold = True
            
    def mouseoff_event(self, sender, **event_args):
        self.lbl_title.bold = False