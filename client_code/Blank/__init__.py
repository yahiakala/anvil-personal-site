from ._anvil_designer import BlankTemplate
from anvil import *
from anvil_extras import routing

from ..Home import Home
from ..ServiceMVP import ServiceMVP
from ..ServiceConsulting import ServiceConsulting


@routing.template(path="", priority=0, condition=None)
class Blank(BlankTemplate):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)

        # Any code you write here will run before the form opens.
