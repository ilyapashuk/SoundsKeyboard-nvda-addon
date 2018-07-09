import globalPluginHandler
import os.path
import winsound
import api
import inputCore
import scriptHandler
import os
import addonHandler
import ui
moduleDir = os.path.dirname(__file__)
sndp = os.path.join(moduleDir, 'copy.wav')
playset = os.path.join(moduleDir, 'play.set')
talkset = os.path.join(moduleDir, 'talk.set')
addonHandler.initTranslation()
class GlobalPlugin(globalPluginHandler.GlobalPlugin):
	def script_sndkey(self,gesture):
		if os.path.isfile(playset):
			winsound.PlaySound(sndp, winsound.SND_ASYNC)
		if os.path.isfile(talkset):
			ui.message(_('copy'))
		gesture.send()
		focus = api.getFocusObject()
		if not focus:
			return 
		if focus.windowClassName == 'ConsoleWindowClass':
			return
		globalMapScripts = []
		globalMaps = [inputCore.manager.userGestureMap, inputCore.manager.localeGestureMap]
		for globalMap in globalMaps:
			for identifier in gesture.identifiers:
				globalMapScripts.extend(globalMap.getScriptsForGesture(identifier))
		treeInterceptor = focus.treeInterceptor
		if treeInterceptor and treeInterceptor.isReady:
			func = scriptHandler._getObjScript(treeInterceptor, gesture, globalMapScripts)
			if func and (not treeInterceptor.passThrough or getattr(func,"ignoreTreeInterceptorPassThrough",False)):
				func(treeInterceptor)
				return

	__gestures = {
		"kb:Control+c": "sndkey",
	}