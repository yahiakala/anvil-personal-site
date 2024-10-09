from ._anvil_designer import HomeTemplate
from anvil import *
from anvil_extras import routing
import anvil.js
from ..utils import is_mobile


@routing.route('', template='Blank')
class Home(HomeTemplate):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)
        # anvil.server.call('do_admin')
        # Any code you write here will run before the form opens.
        if is_mobile():
            self.lbl_dream.align = 'center'
            self.lbl_tagline.align = 'center'
            self.lbl_desc.align = 'center'
            self.btn_services.align = 'center'
            self.sp_hero_top.visible = False
            self.img_logo.height = 250
            self.img_logo.display_mode = 'shrink_to_fit'
            self.lbl_desc.visible = False
            

    def form_show(self, **event_args):
        self.lbl_dream.scroll_into_view()

    def btn_services_click(self, **event_args):
        """This method is called when the button is clicked"""
        self.cc_serv_mvp.scroll_into_view(smooth=True)

    def cc_serv_mvp_click(self, **event_args):
        routing.set_url_hash('mvp', load_from_cache=False)
        # anvil.js.window.location = 'mvp'

    def cc_serv_add_click(self, **event_args):
        routing.set_url_hash('consulting', load_from_cache=False)
        # anvil.js.window.location = 'consulting'
