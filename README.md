Sounds Keyboard Nvda Addon
Plays sounds by operations with clipboard (Copping, cutting and pasting)
Also has a sound for printscreen key.
Also can say information about this events as in FakeClipBoardAnouncement
Sounds Files are placed:
in installed version:
%AppData%\nvda\addons\SoundsKeyboard\globalPlugins
where %AppData% is a foldir AppData\roaming in current user directory
in portable version:
nvda\UserConfig\Addons\SoundsKeyboard\GlobalPlugins
where nvda is a directory with files of portable copy of nvda.
note: playing and saing functions works only if in sounds catalog there are their config files (play.set for sound playing and talk.set for saying)
to disable one of this functions you must remove their config file.
to enable it, create it again.
files can be empty.

Warning! This addon is not compatible with fakeClipboardAnouncement addon.

Sound for ctrl+z and ctrl+a combinations is not found yet, but code to saying messages about them are builtin to the addon.
It's not depends of play.set and talk.set config files.
