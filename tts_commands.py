# Copyright 2019, Rasmus Sorensen <rasmusscholer@gmail.com>
"""

This module contains all TextToSpeech Sublime Text plugin commands.

"""


import sublime
import sublime_plugin
import sys

if sys.platform == "win32":
    from .simple_tts import tts_win as tts
else:
    raise RuntimeError("TextToSpeech currently only supports Windows..")

DEBUG_PRINT = False


class TtsSpeakCommand(sublime_plugin.WindowCommand):
    """ Command to speak selected text using TTS (speech synthesis).
    This should be a WindowCommand, since we don't need to make any edits.

    command string: tts_speak
    Callable with:
        sublime.run_command("tts_speak")
    """
    def run(self):
        # view = self.view
        view = self.window.active_view()
        text = "\n\n".join(view.substr(region) for region in view.sel())
        if not text:
            text = view.substr(sublime.Region(0, view.size()))
        if not text:
            print("No text selected; no text in buffer.")
            return
        if DEBUG_PRINT:
            print("tts.speak(<%s chars>) ..." % (len(text),), end="")
        ret = tts.speak(text)
        if DEBUG_PRINT:
            print(ret)


class TtsPauseCommand(sublime_plugin.WindowCommand):
    """ Command to pause TTS speech. Can be resumed with TtsResumeCommand
    This should be a WindowCommand or ApplicationCommand, since we don't need to make any edits.

    command string: tts_pause
    Callable with:
        sublime.run_command("tts_pause")
    """
    def run(self):
        if DEBUG_PRINT:
            print("tts.pause() ... ", end="")
        ret = tts.pause()
        if DEBUG_PRINT:
            print(ret)


class TtsResumeCommand(sublime_plugin.WindowCommand):
    """ Command to resume TTS speech synthesis.
    This should be a WindowCommand or ApplicationCommand, since we don't need to make any edits.

    command string: tts_resume
    Callable with:
        sublime.run_command("tts_resume")
    """
    def run(self):
        if DEBUG_PRINT:
            print("tts.resume() ... ", end="")
        ret = tts.resume()
        if DEBUG_PRINT:
            print(ret)


class TtsSkipCommand(sublime_plugin.WindowCommand):
    """ Command to skip one or more sentences during TTS speech synthesis.

    command string: tts_skip
    Callable with:
        sublime.run_command("tts_skip")
    """
    def run(self, num_skip=1):
        if DEBUG_PRINT:
            print("tts.skip(%s) ... " % (num_skip,), end="")
        ret = tts.skip(num_skip=num_skip)
        if DEBUG_PRINT:
            print(ret)


class TtsSkipAllCommand(sublime_plugin.WindowCommand):
    """ Command to skip all remaining sentences during TTS speech synthesis.

    command string: tts_skip_all
    Callable with:
        sublime.run_command("tts_skip_all")
    """
    def run(self):
        if DEBUG_PRINT:
            print("tts.skip_all() ... ", end="")
        ret = tts.skip_all()
        if DEBUG_PRINT:
            print(ret)


class TtsReinitializeCommand(sublime_plugin.WindowCommand):
    """ Command to skip all remaining sentences during TTS speech synthesis.

    command string: tts_reinitialize
    Callable with:
        sublime.run_command("tts_reinitialize")
    """
    def run(self):
        if DEBUG_PRINT:
            print("tts.reinitialize_voice() ... ", end="")
        ret = tts.reinitialize_voice()
        if DEBUG_PRINT:
            print(ret)
