
TextToSpeech:
===============

Text-to-speech (TTS) plugin for Sublime Text.

Use your system-provided speech synthesis platform to speak text from within Sublime Text.

On Windows, the "SAPI" speech engine/platform is used for TTS.

macOS and Linux is not currently supported, but the idea is to support both:

* On macOS, the "NSSS" speech engine/platform could used for TSS.
	Alternatively, we could call `say` from a subprocess
	(this can also easily be implemented manually using e.g. the build system.

On Linux, the "espeak" speech library (`libespeak.so`) could be used for TSS.




## Installation:

To install TextToSpeech, I recommend using the Sublime Text _Package Manager_:

1. Open Sublime Text.
2. Press `Ctrl+Shift+P` (or `Cmd+Shift+P`) to bring up the command pallet.
3. Start typing "package control: install package", and select the option from the list.
	* If you do not see this or any `Package Control:` entries, the package control plugin
		is likely not installed. Please refer to https://packagecontrol.io for help on setting
		up the "Package Control" package manager for Sublime Text.
4. Start typing "TextToSpeech" when the next window pops up, and select the entry from the list.
5. Close and restart Sublime Text.
6. Test that it works, as outlined under "Usage" below.


## Usage:

To speak text from Sublime Text:

1. Open a file and select some text.
2. Press `Ctrl+Shift+P` to bring up the command pallet.
3. Type **`TTS: Speak`** and select the entry from the list.
4. You should now hear the selected text being spoken.
	If no text was selected, the complete file will be used.
5. You can additionally use
	* **`TTS: Pause`** to pause the speech synthesis,
	* **`TTS: Resume`** to resume,
	* **`TTS: Skip`** to skip to the next sentence, and
	* **`TTS: Skip all`** to skip all remaining text and stop text-to-speech synthesis.
6. If something goes wrong and the TTS engine starts misbehaving, you can use
	`TTS: Reinitialize` to reset the TTS engine.


## Settings:

To adjust your TextToSpeech settings, go to "Preferences" -> "Package Settings"
-> TextToSpeech -> TextToSpeech Settings. You should then see a split window with two
tabs. The tab on the left is the default settings; the tab on the right is your 
user-specified settings. Copy the settings you want to change from the default settings
on the left to the user-settings on the right. Do not modify the default settings,
they will be overwritten whenever the plugin is updated!

The currently-available settings are:

* `"debug_print"` (default: false) - set this to `true` to have the plugin write a bunch of debugging output to the console.
* `"replace_trivial_eol_newline"` (default: true) - 
* `"tts_rate"`: (default: 0) - increase this to increase the rate/speed of the TTS synthesis.
* `"tts_volume"`: (default: 100) - decrease this to decrease the TTS volume.
* `"tts_voice"`: (default: null, meaning use default voice) - the voice to use, e.g. "Microsoft David", or "Microsoft Zira". This depends on which voices you have available on your system!


## Configuring Sublime Text TextToSpeech keyboard shortcuts:

It is quite easy to set up Sublime Text so you can control TextToSpeech
using your keyboard, you just have to configure your "Key Bindings".

To configure your Sublime Text "Key Bindings", go `Preferences -> Key Bindings`.
In the panel to the left (with a tab name ending with "--- User"), add the key bindings
you would like to use to control TextToSpeech.
For instance, add the following:

```json
	// TextToSpeech keyboard shortcuts:
	{ "keys": ["ctrl+t", "ctrl+t"], "command": "tts_speak" },
	{ "keys": ["ctrl+t", "ctrl+p"], "command": "tts_pause" },
	{ "keys": ["ctrl+t", "ctrl+r"], "command": "tts_resume" },
	{ "keys": ["ctrl+t", "ctrl+s"], "command": "tts_skip" },
	{ "keys": ["ctrl+t", "ctrl+a"], "command": "tts_skip_all" },
```

If you have not previously added any custom keyboard shortcuts, your "--- User" `sublime-keymap`
file in the left panel should now look like this:

```json
[
	// TextToSpeech keyboard shortcuts:
	{ "keys": ["ctrl+t", "ctrl+t"], "command": "tts_speak" },
	{ "keys": ["ctrl+t", "ctrl+p"], "command": "tts_pause" },
	{ "keys": ["ctrl+t", "ctrl+r"], "command": "tts_resume" },
	{ "keys": ["ctrl+t", "ctrl+s"], "command": "tts_skip" },
	{ "keys": ["ctrl+t", "ctrl+a"], "command": "tts_skip_all" },
]
```

The keymaps defined above requires you to first press `ctrl+t`,
and then press `ctrl` plus one of `t`, `p`, `r`, `s`, or `a`.

This will allow you to control TTS playback by pressing **`ctrl+t`**,
followed by one of the following key presses
to start/pause/resume/skip/stop TTS playback:

* **`ctrl+t`** to start the speech synthesis,
* **`ctrl+p`** to pause,
* **`ctrl+r`** to resume,
* **`ctrl+s`** to skip to the next sentence,
* **`ctrl+a`** to skip all remaining text and stop text-to-speech synthesis.

So, in order to start tts, you would just press **`ctrl+t` *twice*** rapidly on your keyboard.

