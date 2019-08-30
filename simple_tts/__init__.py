# Copyright 2019, Rasmus Sorensen <rasmusscholer@gmail.com>
"""

Text-to-speech methods:
-----------------------

## TTS, Windows:

* SAPI Windows API:
* System.Speech.Synthesis.SpeechSynthesizer.Speak API

* voice.exe
    * > "Voice.exe is a command line text to speech utility - just a thin wrapper around the builtin System.Speech.Synthesis."
    * https://www.elifulkerson.com/projects/commandline-text-to-speech.php

* PowerShell script.
    * `Add-Type -AssemblyName System.speech`
    * `$Speaker = New-Object -TypeName System.Speech.Synthesis.SpeechSynthesizer`
    * Methods:
        * `System.Speech.Synthesis.SpeechSynthesizer.Speak($speakString)`
        * `System.Speech.Synthesis.SpeechSynthesizer.SpeakAsync($speakString)`
        * `System.Speech.Synthesis.SpeechSynthesizer.SpeakSsmlAsync($speakString)`
        * `SpeakAsyncCancelAll()`.
        * `Rate`, `Volume`, `State`, `Voice`.
        * `SelectVoice()`.
    * Alternative, using ComObject:
        * `$s = New-Object -ComObject SAPI.SPVoice`
* About Speech Synthesis Markup Language (SSML):
    * https://www.w3.org/TR/speech-synthesis/



## TTS, macOS:

* `say` command line program.


## TTS, Linux




TTS python packages:
---------------------


SAPI via win32com.client:

* Example:
    ```
    import win32com.client as wincl
    wincl.Dispatch("SAPI.SpVoice").Speak("Hello World!")
    ```


pyttsx3: Text-to-speech x-platform

* > "pyttsx for python3 ( offline tts for python : works for both python2 and python3 )"
* > "pyttsx3 is a text-to-speech conversion library in Python. Unlike alternative libraries,
    it works offline, and is compatible with both Python 2 and 3."
* https://pypi.org/project/pyttsx3
* https://pyttsx3.readthedocs.io
* https://github.com/nateshmbhat/pyttsx3
    * 153 github stars; last commit May 2019.
* pyttsx - uses  SAPI5 on Windows XP, Windows Vista, and (untested) Windows 7:
* Installation: `pip install pyttsx3`
* Usage example:
    * `engine=pyttsx3.init(); engine.say('Good morning.'); engine.runAndWait()`
    * https://pyttsx3.readthedocs.io/en/latest/engine.html#examples
* Supported/included engines:
    * sapi5
    * nsss
    * espeak
* This is probably the way to go.

gTTS:

* > "Python library and CLI tool to interface with Google Translate's text-to-speech API."
* https://github.com/pndurette/gTTS
* https://gtts.readthedocs.io/en/latest/
* https://pypi.org/project/gTTS/


tts-watson:

* > "Text to speech using the IBM Watson API."
* Uses the IBM Watson web service for TTS generation.
* https://pypi.org/project/tts-watson/
* https://github.com/gfleetwood/tts-watson
* Requires `portaudio` - so macOS or Linux only.
* Also uses: `pyaudio` and `anyconfig`.

ibm-watson:

* This is the "official" python package for IBM Watson.
* https://cloud.ibm.com/apidocs/text-to-speech?code=python
* https://www.ibm.com/watson/services/text-to-speech/


voicerss-tts:

* > "Access the http://www.voicerss.org/api/ Text to Voice API."
    * Requires API key.
* Alternative implementation; official Python API bindings at http://www.voicerss.org/sdk/python.aspx.
* https://bitbucket.org/daycoder/voicerss_tts/src/master/
* https://pypi.org/project/voicerss-tts/

ttsbroker:

* https://pypi.org/project/ttsbroker/
* Engines:
    * Google Cloud TTS.
    * Amazon Polly (requires AWS API keys).
    * IBM Watson (requires Watson service credentials).
* https://github.com/alttch/ttsbroker


tts: (lol)
* https://pypi.org/project/tts/
    * 10 releases, all on the same day, July 14th 2017 (??).
* No website or github link.
* Contains 4 lines of code: A class that does
    `os.system("say "+self)`.
    And that is "release 1.1" - the 10th release.
    Earlier releases were not even functional, or just added setup.py metadata.
* Perhaps the poorest packages I've ever seen on PYPI.



From Journal week of 20190701:

- TTS in python?
    - https://pythonprogramminglanguage.com/text-to-speech/ - rather old article?
        - pyttsx - uses  SAPI5 on Windows XP, Windows Vista, and (untested) Windows 7:
            - `pip install pyttsx3`
            - `>>> engine=pyttsx3.init(); engine.say('Good morning.'); engine.runAndWait()`
            - https://pyttsx3.readthedocs.io/en/latest/
        - gTTS - Google’s Text-to-speech:
            - `pip install gTTS`
                - Requires: six, soupsieve, beautifulsoup4, bs4, click, chardet, idna, urllib3, requests, gtts-token.
            - `>>> gTTS(text='Good morning', lang='en').save(``"``goodmorning.mp3``"``)`
            - `gtts-cli.py` `"``Hello``"` `-l` `'``en``'` `-o hello.mp3`
        - Windows 10 built-in:
            - `conda install pypiwin32  # to install 'win32com'`
            - `>>> win32com.client.Dispatch("SAPI.SpVoice").Speak("Hello World")`
        - IBM Watson TTS:
            - `pip install tts-watson`
                - Requires: Flask, chardet, idna, certifi, urllib3, requests, Jinja2, pyaudio, anyconfig, bunch, pyyaml, Markupsafe, click.
            - `>>> tts_watson.TtsWatson.TtsWatson('watson_user', 'watson_password', 'en-US_AllisonVoice').play("Hello World")`
            - `tts-watson`  CLI
            - This appears to be python2 only??
                - Well, the pypi release is from 2016; Is python 2.7 (although that isn’t specified in the setup.py), only readme.
                - Latest github master is python3.
                - https://github.com/gfleetwood/tts-watson
            - Alternatively, use `ibm-watson`:
                - https://pypi.org/project/ibm-watson/
                - This is a general-purpose library for using all the IBM Watson APIs.
                - `ibm_watson.TextToSpeechV1(iam_apikey='{apikey}', url='{url}')`
        - Other projects:
            - ttsbroker
            -
    - Created conda env `tts-tests`:


## PowerShell examples and refs:

* https://www.powershellgallery.com/packages/Out-SpeechSynthesizer/1.0.0/Content/Out-SpeechSynthesizer.ps1
* https://gallery.technet.microsoft.com/scriptcenter/PowerShell-Tricks-Text-to-2992aa1b
* https://mcpmag.com/articles/2018/03/07/talking-through-powershell.aspx
* https://www.scriptinglibrary.com/languages/powershell/powershell-text-to-speech/
* https://www.pdq.com/blog/powershell-text-to-speech-examples/


## TTS CLI tools:


* voice.exe


* tts.js:
    * https://github.com/eheikes/tts/tree/master/packages/tts-cli
    * Uses Google Cloud or AWS for TTS synthesis.
* say.js
    * https://github.com/Marak/say.js/


## TTS, libraries:


* .NET:
    * https://docs.microsoft.com/en-us/dotnet/api/system.speech.synthesis.speechsynthesizer.speak?view=netframework-4.8
* Ansible:
    * https://docs.ansible.com/ansible/latest/modules/win_say_module.html


## TTS, refs:

* https://pythonprogramminglanguage.com/text-to-speech/
    Goes over the following:
    * pyttsx
    * gTTS
    * speech (iOS).
    * SAPI (Microsoft Windows 10) using wincom32.
    * tts-watson
*


"""

import sys

if sys.platform == "win32":
    from .tts_win import *
else:
    raise RuntimeError(
        "simple-tts currently only runs on Windows. We welcome contributions enabling TTS support on macOS and Linux. "
        "Please see README.md for alternative python packages that do support macOS and Linux."
    )
