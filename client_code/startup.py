import anvil

from anvil_extras import routing
from .Blank import Blank

hash, pattern, dict = routing.get_url_components()

print(hash)
print(pattern)
routing.set_url_hash(hash)

routing.launch()