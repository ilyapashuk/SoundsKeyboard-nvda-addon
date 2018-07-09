# -*- coding: UTF-8 -*-
import globalPluginHandler
import os.path
import winsound
import ui
import addonHandler
moduleDir = os.path.dirname(__file__)
sndp = os.path.join(moduleDir, 'cut.wav')
playset = os.path.join(moduleDir, 'play.set')
talkset = os.path.join(moduleDir, 'talk.set')
addonHandler.initTranslation()
class GlobalPlugin(globalPluginHandler.GlobalPlugin):
	def script_sndkeycu(self,gesture):
		if os.path.isfile(playset):
			winsound.PlaySound(sndp, winsound.SND_ASYNC)
		if os.path.isfile(talkset):
			ui.message(_('cut'))
		gesture.send()
	__gestures = {
		"kb:Control+x": "sndkeycu",
	}