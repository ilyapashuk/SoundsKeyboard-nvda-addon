# -*- coding: UTF-8 -*-
import globalPluginHandler
import ui
import api
import inputCore
import scriptHandler
import addonHandler
addonHandler.initTranslation()
class GlobalPlugin(globalPluginHandler.GlobalPlugin):
	def script_sndkeycu(self,gesture):
		ui.message(_('SelectAll'))
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
		"kb:Control+a": "sndkeycu",
	}