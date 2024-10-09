from ._anvil_designer import ServiceMVPTemplate
from anvil import *
from anvil_extras import routing
# import anvil.js
from ..utils import is_mobile


desc1 = """
- We'll get together for a 30 minute call to discuss your general requirements.
- If we’re a good fit, we’ll proceed with the next step!
"""

desc2 = """
- We’ll have a follow-up call to detail all of your requirements which include general functionality, features, user interaction, etc.
- We will ask specific questions which help clarify exactly what will go into your MVP.
- We’ll help narrow down your feature wish list into a realistic MVP. For example, creating a new ML model to detect cancer with 20 examples is... out of our wheelhouse.
"""

desc3 = """
- We'll put together a detailed document listing out every requirement.
- This document will go in our contract, so we ensure your app gets made the way you like it!
"""

desc4 = """
- We’ll first complete a rough mockup of your user interactions - logging in, clicking on menu items, and basic flows.
- We’ll then create a beautiful, high-fidelity design of the application.
- Everything from colours, fonts, and visual effects will be nailed down.
"""

desc5 = """
- This is where the magic happens!
- We’ll develop all of the functionality in the contract and share progress updates.
- During this stage, we’ll regularly solicit feedback on completed work to make sure it is up to snuff.
"""

desc6 = """
- The handoff is generally four steps: payment, hosting setup, training, and transfer of assets.
- We'll have a call to walk you through setting up your own web hosting. It's easy, we promise!
- During the call, we'll walk you through all of the code, database tables, and deployment options.
- For 30 days after the handoff, we provide support for bug fixes.
**Note**: hosting will cost approximately $55 USD per month.
"""


@routing.route('mvp', template='Blank')
class ServiceMVP(ServiceMVPTemplate):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)
        self.ic_1.description = desc1.lstrip()
        self.ic_2.description = desc2.lstrip()
        self.ic_3.description = desc3.lstrip()
        self.ic_4.description = desc4.lstrip()
        self.ic_5.description = desc5.lstrip()
        self.ic_6.description = desc6.lstrip()
        # dom_node = anvil.js.get_dom_node(self)
        # dom_node.addEventListener('click', self.hide_cp)
        
    def form_show(self, **event_args):
        self.lbl_dream.scroll_into_view()
        if is_mobile():
            self.img_logo.height = 250
            self.img_logo.display_mode = 'shrink_to_fit'
            self.lbl_desc.visible = False
            self.spacer_logo_top.visible = False

        # Any code you write here will run before the form opens.

    def icon_click(self, **event_args):
        self.cp_step_detail.visible = True
        self.lbl_step_desc_title.text = event_args['sender'].title
        # self.lbl_step_desc_desc.text = event_args['sender'].description
        self.rt_step_desc_desc.content = event_args['sender'].description
        self.cp_step_detail.scroll_into_view(smooth=True)

    def link_1_click(self, **event_args):
        """This method is called when the link is clicked"""
        pass
