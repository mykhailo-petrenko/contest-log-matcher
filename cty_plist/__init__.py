from os import path
from pyhamtools import LookupLib

# @TODO: try https://github.com/0x9900/DXEntity/blob/main/DXEntity/_dxentity.py instead and see the loading and query speed

country_prefix_list = path.join(path.dirname(__file__), "cty.plist")

lookup_lib = LookupLib(lookuptype="countryfile", filename=country_prefix_list)
