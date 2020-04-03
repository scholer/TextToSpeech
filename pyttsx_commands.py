# Copyright 2019, Rasmus Sorensen <rasmusscholer@gmail.com>
"""

## Using pyttsx3:

Usage:
```
import pyttsx3
engine = pyttsx3.init()
engine.say("I will speak this text")
engine.runAndWait()
```

Documentation, pyttsx3:

*



## Package names:

Too bad that Package Control doesn't support having a "display name".
You can theoretically name your package anything, but the docs has the following recommendations:

* Use CamelCase or underscore_notation. Other Python packages in ST3 will be able to more easily interact with it.
    Additionally, the search indexer will properly split words, making search results more accurate.
    Obviously this does not matter if your package name is a single word or contains no Python.
* Check hard-coded references. The package name is (effectively) used as the package folder name.
    Any file path references in a theme or Python code must use this package folder name.
    Be sure your local package folder name matches. See the .no-sublime-package file discussed in step 5
    if you need to ensure files are always unpacked into a folder.

Name candidates:

* TTS-Text-to-speech - my favorite, but doesn't conform to the "CamelCase or underscore_notation" recommendation.
* TTS_Text_to_speech - conforms to "CamelCase or underscore_notation" recommendation, but looks ugly.
* TTSTextToSpeech - conforms to "CamelCase or underscore_notation" recommendation, but looks ugly.
* TextToSpeechTTS -
* TextToSpeech


# .sublime-commands:

```json
    // pyttsx3 commands
    {
        "caption": "TTS: Speak Text (pyttsx3)",
        "command": "tts_speak_selected_text_async",
        "args": {}
     },
    {
        "caption": "TTS: Stop Speaking (pyttsx3)",
        "command": "tts_stop_speaking",
        "args": {}
     },
    {
        "caption": "TTS: Reset Engine (pyttsx3)",
        "command": "tts_reset_engine",
        "args": {}
     }
```


"""

import sublime
import sublime_plugin

import os
import subprocess
import sys
import tempfile
import shlex
import time

abort_requested = False

try:
    import pyttsx3
except ImportError:
    # print("pyttsx3 not natively available; trying to monkey-patch system using ./lib folder.")
    # sys.path.append(os.path.join(os.path.dirname(__file__), 'lib'))
    # sys.path.append(os.path.join(os.path.dirname(__file__), 'lib', "pythonwin"))
    # sys.path.append(os.path.join(os.path.dirname(__file__), 'lib', "pypiwin32_system32"))
    # sys.path.append(os.path.join(os.path.dirname(__file__), 'lib', "win32"))
    # sys.path.append(os.path.join(os.path.dirname(__file__), 'lib', "win32", "lib"))
    # sys.path.append(os.path.join(os.path.dirname(__file__), 'lib', "win32com"))
    # sys.path.append(os.path.join(os.path.dirname(__file__), 'lib', "win32comext"))
    # from .lib import pyttsx3
    # print("pyttsx3:", pyttsx3)

    print("pyttsx3 not availalbe; using alternative TTS method.")
    pyttsx3 = None
    # Fall back to using system calls:
    if sys.platform == 'win32':
        # Use PowerShell:
        def speak(text):
            # TODO, OBS: Using window.run_command("exec", kwargs) may be better!
            file = tempfile.NamedTemporaryFile(mode='w', delete=False)
            file.write(text)
            file.close()
            # powershell -Command "Add-Type -AssemblyName System.speech; $s = New-Object -TypeName System.Speech.Synthesis.SpeechSynthesizer; $s.Speak('Hello world!')"
            cmd_args = [
                'powershell', '-NonInteractive', '-Command',
                ('Add-Type -AssemblyName System.speech; '
                 '$content = [IO.File]::ReadAllText("{filename}"); '
                 '$s = New-Object -TypeName System.Speech.Synthesis.SpeechSynthesizer; '
                 '$s.Speak($content); '
                 ).format(filename=file.name)
            ]
            output = subprocess.check_output(cmd_args, stderr=subprocess.STDOUT, shell=True)
            print("TTS process output:", output)
    elif sys.platform == 'darwin':
        def speak(text):
            cmd_args = ['say', text]
            output = subprocess.check_output(cmd_args, stderr=subprocess.STDOUT, shell=True)
    else:
        def speak(text):
            cmd_args = ['espeak', text]
            output = subprocess.check_output(cmd_args, stderr=subprocess.STDOUT, shell=True)

# Use a single, global TTS engine:
# Actually, it appears pyttsx3.init() already implements an engine cache.
engine = None


def print_engine_debug(engine):
    print("engine:", engine)
    print("engine._inLoop:", engine._inLoop)
    print("engine._driverLoop :", engine._driverLoop)

    print("engine.proxy:", engine.proxy)
    print("engine.proxy._busy:", engine.proxy._busy)
    print("engine.proxy._queue:", engine.proxy._queue)
    print("engine.proxy._iterator:", engine.proxy._iterator)

    print("engine.proxy._driver :", engine.proxy._driver)
    print("engine.proxy._driver._tts:", engine.proxy._driver._tts)
    print("engine.proxy._driver._looping:", engine.proxy._driver._looping)
    print("engine.proxy._driver._speaking:", engine.proxy._driver._speaking)
    print("engine.proxy._driver._stopping:", engine.proxy._driver._stopping)


# class TtsSpeakSelectedTextBlockingCommand(sublime_plugin.TextCommand):
#     """ Command to speak selected text using TTS (speech synthesis).
#
#     command string: tts_speak_selected_text_blocking
#
#     Callable with:
#         sublime.run_command("tts_speak_selected_text_blocking")
#     """
#     def run(self, edit):
#         print("TtsSpeakSelectedTextBlockingCommand.run() invoked with edit token:", edit)
#
#         global abort_requested
#         abort_requested = False
#
#         text = "\n\n".join(self.view.substr(region) for region in self.view.sel())
#         if not text:
#             text = self.view.substr(sublime.Region(0, self.view.size()))
#         if not text:
#             print("No text selected; no text in buffer.")
#             return
#
#         try:
#             import pyttsx3
#         except ImportError:
#             pyttsx3 = None
#
#         if pyttsx3:
#             global engine
#             if engine is None:
#                 print("Initializing TTS engine...")
#                 engine = pyttsx3.init()
#                 # SAPI.SPVoice.Speak(text, flag)
#                 #        https://docs.microsoft.com/en-us/previous-versions/windows/desktop/ms723609%28v%3dvs.85%29
#                 # flags: https://docs.microsoft.com/en-us/previous-versions/windows/desktop/ms720892%28v%3dvs.85%29
#                 # Default flag is 19 = 16 + 2 + 1 = SVSFIsNotXML + SVSFPurgeBeforeSpeak + SVSFlagsAsync
#                 try:
#                     print(" - OK, TTS driver:", engine.proxy._module.__name__, engine.proxy)
#                 except AttributeError:
#                     pass
#             engine.say(text)
#             engine.runAndWait()
#         else:
#             print("\nOBS: pyttsx3 not available; using system call instead (slower).")
#             speak(text)


class TtsSpeakSelectedTextAsyncCommand(sublime_plugin.WindowCommand):
    """ Command to speak selected text using TTS (speech synthesis).
    This should be a WindowCommand, since we don't need to make any edits.

    command string: tts_speak_selected_text_async

    Callable with:
        sublime.run_command("tts_speak_selected_text_async")
    """
    def run(self):

        # print("TtsSpeakSelectedTextAsyncCommand.run() invoked with edit token:", edit)
        print("TtsSpeakSelectedTextAsyncCommand.run() invoked.")

        global abort_requested
        abort_requested = False

        # view = self.view
        view = self.window.active_view()
        text = "\n\n".join(view.substr(region) for region in view.sel())
        if not text:
            text = view.substr(sublime.Region(0, view.size()))
        if not text:
            print("No text selected; no text in buffer.")
            return

        # sublime.run_command("tts_start_speaking", {"text": text})
        # sublime.set_timeout_async(lambda: sublime.run_command("tts_start_speaking", {"text": text}), 0)
        print("Running:")
        print("sublime.set_timeout_async(lambda: self.speak(text), 0)")
        sublime.set_timeout_async(lambda: self.speak(text), 0)

    def speak(self, text, split="\n\n"):
        print("TtsStartSpeakingCommand.run() invoked with text (%s chars):" % (len(text),), text)

        if not text:
            print("TtsStartSpeakingCommand: No text selected; no text in buffer.")
            return

        global abort_requested

        try:
            import pyttsx3
        except ImportError:
            print("Adding ad-hoc pyttsx3 path to sys.path...")
            sys.path.insert(0, r"C:\Users\au206270\Dev\sublime-text-dev\temp\pyttsx3\all")

        import pyttsx3
        global engine
        if engine is None:
            print("Initializing TTS engine...")
            try:
                engine = pyttsx3.init()
            except ReferenceError:
                # I don't actually think we'll be able to catch this.
                engine = pyttsx3.init()
            try:
                print(" - OK, TTS driver:", engine.proxy._module.__name__, engine.proxy)
            except AttributeError:
                pass
        else:
            print("Re-using existing TTS engine:", engine)
        print("Speaking using TTS engine", engine)

        # engine.say(text)
        # engine.runAndWait()  # Invoking this before anything makes it not work at all.
        # return

        if split:
            text_parts = text.split(split)
        else:
            text_parts = [text]

        # engine.runAndWait()  # Invoking this before anything makes it not work at all.
        print("--------- engine, BEFORE starting say() and runAndWait() ------")
        print_engine_debug(engine)

        for part in text_parts:
            if abort_requested:
                print("TTS abort_requested:", abort_requested)
                return
            if engine.proxy._driver._stopping:
                print("engine.proxy._driver._stopping is:", engine.proxy._driver._stopping)
                return
            if not part:
                continue
            print("Queuing up %s of %s chars:" % (len(part), len(text)))
            engine.say(part)
            # Hmm, this only actually says the last thing that was added.
            print("Running engine.runAndWait(), queue is:", engine.proxy._queue)
            while engine.proxy._driver._speaking:
                if abort_requested:
                    return
                print("engine.proxy._driver._speaking is %s, sleeping 0.1 s ..." % (
                    engine.proxy._driver._speaking,))
                time.sleep(0.1)
            engine.runAndWait()
            print("Sleeping 0.5 s after runAndWait()...")
            time.sleep(0.5)
        # engine.runAndWait()


# class TtsStartSpeakingCommand(sublime_plugin.ApplicationCommand):
#     """ Command to speak selected text using TTS (speech synthesis).
#
#     command string: tts_start_speaking
#
#     Callable with:
#         sublime.run_command("tts_start_speaking")
#     """
#     def run(self, text, split=None):
#         print("TtsStartSpeakingCommand.run() invoked with text:", text)
#
#         if not text:
#             print("TtsStartSpeakingCommand: No text selected; no text in buffer.")
#             return
#
#         import pyttsx3
#         global engine
#         if engine is None:
#             print("Initializing TTS engine...")
#             try:
#                 engine = pyttsx3.init()
#             except ReferenceError:
#                 engine = pyttsx3.init()
#             try:
#                 print(" - OK, TTS driver:", engine.proxy._module.__name__, engine.proxy)
#             except AttributeError:
#                 pass
#         else:
#             print("Re-using existing TTS engine:", engine)
#         print("Speaking using TTS engine", engine)
#         if split:
#             text_parts = text.split(split)
#         else:
#             text_parts = [text]
#         for part in text_parts:
#             if not part:
#                 continue
#             print("Queuing up %s of %s chars:" % (len(part), len(text)))
#             engine.say(part)
#         engine.runAndWait()


class TtsStopSpeakingCommand(sublime_plugin.ApplicationCommand):
    """ Command to speak selected text using TTS (speech synthesis).

    command string: tts_stop_speaking

    Callable with:
        sublime.run_command("tts_stop_speaking")
    """
    def run(self):

        global abort_requested
        abort_requested = True

        try:
            import pyttsx3
        except ImportError:
            pyttsx3 = None

        if pyttsx3:
            global engine
            if engine is None:
                print("No TTS engine initialized, aborting...")
                return
            print("Stopping TTS engine", engine)
            try:
                print(" - TTS driver:", engine.proxy._module.__name__, engine.proxy)
            except AttributeError:
                pass

            print(" --- BEFORE engine.stop() ----")
            print_engine_debug(engine)

            engine.stop()
            # TODO, OBS: It appears that engine.stop() is only effective the first time it is called.
            # Calling engine.stop() subsequently after starting again does not work.
            # Consider just destroying the object?
            # I think this might be because the SAPI5Driver is using `win32com.client.WithEvents`.
            # try:
            #     engine.endLoop()
            # except RuntimeError:
            #     print("engine.endLoop() - RuntimeError: run loop not started")

            print(" --- AFTER engine.stop() ----")
            print_engine_debug(engine)
            print("\n----------------      ---------------")

            # print("Deleting and stopping manually:")
            # engine.proxy._driver.stop()
            # del engine.proxy._queue[:]
        else:
            print("\nOBS: pyttsx3 not available; stopping alternate system-call TTS is not supported.")


class TtsResetEngineCommand(sublime_plugin.ApplicationCommand):
    """ Command to speak selected text using TTS (speech synthesis).

    command string: tts_reset_engine

    Callable with:
        sublime.run_command("tts_reset_engine")
    """
    def run(self):

        try:
            import pyttsx3
        except ImportError:
            pyttsx3 = None

        if pyttsx3:
            global engine
            if engine is None:
                print("No TTS engine initialized, aborting...")
                return
            print("TTS engine", engine)
            print(" - TTS driver:", engine.proxy._module.__name__, engine.proxy)
            print("Stopping TTS engine...", engine)
            engine.stop()
            print("Deleting TTS engine...")
            del engine.proxy._driver._advise
            del engine.proxy._driver
            del engine.proxy._engine
            del engine.proxy  # This should call DriverProxy._driver.destroy()
            del engine
            engine = None
            try:
                engine = pyttsx3.init()
            except ReferenceError:
                pass

            # I think pyttsx3 is using weakref, so the above may not even be enough.
        else:
            print("\nOBS: pyttsx3 not available; cannot reset TTS engine.")

