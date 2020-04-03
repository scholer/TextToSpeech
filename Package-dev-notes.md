
TODO:
-----

* TODO: Implement tts_preprocessing and add `"tts_preprocessing_pattern_files": [],` to default settings file.



How to create a Sublime Text package:
--------------------------------------

Writing the python code:

* Create a python file, `import sublime_plugin`, and create a new class that inherits from
    `sublime_plugin.TextCommand` or `sublime_plugin.WindowCommand`.
* Give the class a `.run()` method - this is the entry point through which the command is invoked.
* If your class is named `MyFancyFeatureCommand`, it can be invoked with `sublime.run_command("my_fancy_feature").
    (Sublime Text converts CamelCase to snake_case and removes trailing 'Command' postfix).
* Refer to https://www.sublimetext.com/docs/3/api_reference.html for details.


Add other packaging files:

* If your package/plugin depends on other python packages that does not come with python, you
    should add a `dependencies.json` file to the root directory of your package.


Refs, packaging:

* https://packagecontrol.io/docs/submitting_a_package
* https://packagecontrol.io/docs/dependencies
* https://github.com/wbond/package_control
* https://github.com/wbond/package_control/blob/master/example-dependencies.json



Installing dependencies:
-------------------------

***UPDATE: If you use the python-pywin32 dependency provided by package control,
then everything works out of the box. Just add the following to your `dependencies.json`:

```json
{
  "windows": {
    ">3000": [
      "python-pywin32"
    ]
  }
}
```

The `pywin32` dependency package can also be downloaded directly from
https://github.com/packagecontrol/sublime-pywin32.



Related Sublime Text packages:
-------------------------------

There does not appear to be any TTS-related packages on Package Control, as of this writing.

The only somewhat related package is "Speech", an abandoned speech recognition package.

Speech:

* https://packagecontrol.io/packages/Speech
* Speech recognition for Sublime Speech 2.
* Package source (Github) no longer available?
    * Probably moved to https://github.com/sashakmets/SublimeSpeech
* 146 downloads total.
* Uses the dragonfly library by Christo Butcher and pywin packages for Windows.
    * https://github.com/t4ngo/dragonfly
    * Which again usees Nuance's Dragon NaturallySpeaking, or Windows Speech Recognition.


Old notes, issues:
-------------------

Issue: pyttsx3 requires pywin32 on Windows, but the current version of pywin32
    only supports python 3.5+, not python 3.3.

* This is the case since at least version 222 (from Jan 2018).
* Version 214 (from 2010) was tagged as supporting Python 3.0-3.3, but this does not have any
    wheels or other files on pip.
* pypiwin32 version 219 *does* have a CPython 3.3 wheel!
* But the next version, pypiwin32 version 220, only has python 3.6.
* OBS: pipywin32 dist-package is published by the same people as pywin32,
    I think it initially included wheels, but now it is just an empty package,
    that installs pywin32 by including `install_requires='pywin32>=223'` in
    the `setup.py` of `pypiwin32`.
* The issue here is that pip tries to install the latest version of `pypiwin32`,
    and the latest version simply tries to install the latest version of `pywin32`,
    which doesn't support python 3.3.
* Instead, you just simply manually install the correct version of pywin32/pypiwin32.
* In conclusion, to install p `pywin32`, use:
    `pip install pypiwin32==219`
* Then you can install pyttsx3 using:
    `pip install pyttsx3`

