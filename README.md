
TextToSpeech:
===============

Text-to-speech (TTS) plugin for Sublime Text.

Use your system-provided speech synthesis platform to speak text from within Sublime Text.

On Windows, the "SAPI" speech engine/platform is used for TTS.

macOS and Linux is not currently supported, but the idea is to support both:

* On macOS, the "NSSS" speech engine/platform could used for TSS.
	Alternatively, we could call `say` from a subprocess
	(this can also easily be implemented manually using e.g. the build system.

On Linux, the "espeak" speech library (`libespeak.so`) is used for TSS.




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


## Configuring Sublime Text keyboard shortcuts:

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

The keymaps defined above requires you to press `ctrl+t`, followed by another keypress

You can now control TTS playback by pressing **`ctrl+t`,
followed by one of the following key presses
to start/pause/resume/skip/stop TTS playback:

* **`ctrl+t`** to start the speech synthesis,
* **`ctrl+p`** to pause,
* **`ctrl+r`** to resume,
* **`ctrl+s`** to skip to the next sentence,
* **`ctrl+a`** to skip all remaining text and stop text-to-speech synthesis.

You can now start tts by pressing **`ctrl+t` *twice*** rapidly on your keyboard.

