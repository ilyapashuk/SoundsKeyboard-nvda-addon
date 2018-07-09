# Build customizations
# Change this file instead of sconstruct or manifest files, whenever possible.

# Full getext (please don't change)
_ = lambda x : x

# Add-on information variables
addon_info = {
# add-on Name
	"addon-name" : "SoundsKeyboard",
	# Add-on description
	# TRANSLATORS: Summary for this add-on to be shown on installation and add-on informaiton.
	"addon-summary" : _("sounds by keyboard events"),
	# Add-on description
	# Translators: Long description to be shown for this add-on on installation and add-on information
	"addon-description" : _("plays sounds by operations with clipboard and some other keyboard events"),
	# version
	"addon-version" : "2.4",
	# Author(s)
	"addon-author" : "ilyapashuk",
# URL for the add-on documentation support
"addon-url" : None
}


import os.path

# Define the python files that are the sources of your add-on.
# You can use glob expressions here, they will be expanded.
pythonSources = ['addon/GlobalPlugins/copy.py', 'addon/GlobalPlugins/cut.py', 'addon/GlobalPlugins/pas.py', 'addon/GlobalPlugins/cancel.py', 'addon/GlobalPlugins/selectall.py', 'addon/GlobalPlugins/prntscr.py']

# Files that contain strings for translation. Usually your python sources
i18nSources = pythonSources + ["buildVars.py"]

