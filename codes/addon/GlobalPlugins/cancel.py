import globalPluginHandler
import ui
import addonHandler
addonHandler.initTranslation()
class GlobalPlugin(globalPluginHandler.GlobalPlugin):
	def script_sndkeycu(self,gesture):
		ui.message(_('undu'))
		gesture.send()
	__gestures = {
		"kb:Control+z": "sndkeycu",
	}