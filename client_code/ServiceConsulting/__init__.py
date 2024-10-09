from ._anvil_designer import ServiceConsultingTemplate
from anvil import *
from anvil_extras import routing
from ..utils import is_mobile


@routing.route('consulting', template='Blank')
class ServiceConsulting(ServiceConsultingTemplate):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)

    def form_show(self, **event_args):
        self.lbl_dream.scroll_into_view()
        if is_mobile():
            self.img_logo.height = 250
            self.img_logo.display_mode = 'shrink_to_fit'
            self.lbl_desc.visible = False
            self.spacer_logo_top.visible = False