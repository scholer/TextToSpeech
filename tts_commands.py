# Copyright 2019, Rasmus Sorensen <rasmusscholer@gmail.com>
"""

This module contains all TextToSpeech Sublime Text plugin commands.

"""


import sublime
import sublime_plugin
import sys
import re

if sys.platform == "win32":
    from .simple_tts import tts_win as tts
else:
    raise RuntimeError("TextToSpeech currently only supports Windows!")


SETTINGS_NAME = 'TextToSpeech.sublime-settings'
DEBUG_PRINT = False


def reinitialize_with_settings():
    settings = sublime.load_settings(SETTINGS_NAME)
    debug_print = settings.get("debug_print", DEBUG_PRINT)
    if debug_print:
        print("TTS settings:")
        print("rate:", settings.get("tts_rate"))
        print("volume:", settings.get("tts_volume"))
        print("voice:", settings.get("tts_voice"))
    return tts.reinitialize_voice(
        rate=settings.get("tts_rate"),
        volume=settings.get("tts_volume"),
        voice=settings.get("tts_voice"),
    )
reinitialize_with_settings()


class TtsSpeakCommand(sublime_plugin.WindowCommand):
    """ Command to speak selected text using TTS (speech synthesis).
    This should be a WindowCommand, since we don't need to make any edits.

    command string: tts_speak
    Callable with:
        sublime.run_command("tts_speak")
    """
    def run(self):
        # Get settings:
        settings = sublime.load_settings(SETTINGS_NAME)
        debug_print = settings.get("debug_print", DEBUG_PRINT)
        replace_trivial_eol_newline = settings.get("replace_trivial_eol_newline")
        regex_substitutions = settings.get("regex_substitutions")  # A list with <regex-pattern>, <substitute-text>
        if debug_print: 
            print("\nTTS Speak command invoked, settings are:")
            print("  debug_print: ", debug_print)
            print("  replace_trivial_eol_newline: ", replace_trivial_eol_newline)
            print("  regex_substitutions: ", "".join("\n    - %s" % (tup,) for tup in regex_substitutions) if regex_substitutions else regex_substitutions)

        # view = self.view  # for TextCommands, not WindowCommands
        view = self.window.active_view()
        text = "\n\n".join(view.substr(region) for region in view.sel())
        if not text:
            text = view.substr(sublime.Region(0, view.size()))
        if not text:
            print("No text selected; no text in buffer.")
            return
        if replace_trivial_eol_newline:
            trivial_eol_newline_regex = re.compile(r"\n(?=\w)")  # Newline not followed by another newline.
            text, counts = trivial_eol_newline_regex.subn(" ", text)  # Replace trivial newlines in text with a space.
            if debug_print:
                print("Substituted %s trivial end-of-line newlines a space." % (counts, ))
        if regex_substitutions:
            for pattern, repl in regex_substitutions:
                text, counts = re.subn(pattern, repl, text)
                if debug_print:
                    print("Substituted %s instances of pattern %r with string %r:" % (counts, pattern, repl))

        if debug_print:
            print("tts.speak(<%s chars>) ..." % (len(text),), end="")
        ret = tts.speak(text)
        if debug_print:
            print(ret)


class TtsPauseCommand(sublime_plugin.WindowCommand):
    """ Command to pause TTS speech. Can be resumed with TtsResumeCommand
    This should be a WindowCommand or ApplicationCommand, since we don't need to make any edits.

    command string: tts_pause
    Callable with:
        sublime.run_command("tts_pause")
    """
    def run(self):
        settings = sublime.load_settings(SETTINGS_NAME)
        debug_print = settings.get("debug_print", DEBUG_PRINT)
        if debug_print:
            print("tts.pause() ... ", end="")
        ret = tts.pause()
        if debug_print:
            print(ret)


class TtsResumeCommand(sublime_plugin.WindowCommand):
    """ Command to resume TTS speech synthesis.
    This should be a WindowCommand or ApplicationCommand, since we don't need to make any edits.

    command string: tts_resume
    Callable with:
        sublime.run_command("tts_resume")
    """
    def run(self):
        settings = sublime.load_settings(SETTINGS_NAME)
        debug_print = settings.get("debug_print", DEBUG_PRINT)
        if debug_print:
            print("tts.resume() ... ", end="")
        ret = tts.resume()
        if debug_print:
            print(ret)


class TtsSkipCommand(sublime_plugin.WindowCommand):
    """ Command to skip one or more sentences during TTS speech synthesis.

    command string: tts_skip
    Callable with:
        sublime.run_command("tts_skip")
    """
    def run(self, num_skip=1):
        settings = sublime.load_settings(SETTINGS_NAME)
        debug_print = settings.get("debug_print", DEBUG_PRINT)
        if debug_print:
            print("tts.skip(%s) ... " % (num_skip,), end="")
        ret = tts.skip(num_skip=num_skip)
        if debug_print:
            print(ret)


class TtsSkipAllCommand(sublime_plugin.WindowCommand):
    """ Command to skip all remaining sentences during TTS speech synthesis.

    command string: tts_skip_all
    Callable with:
        sublime.run_command("tts_skip_all")
    """
    def run(self):
        settings = sublime.load_settings(SETTINGS_NAME)
        debug_print = settings.get("debug_print", DEBUG_PRINT)
        if debug_print:
            print("tts.skip_all() ... ", end="")
        ret = tts.skip_all()
        if debug_print:
            print(ret)


class TtsReinitializeCommand(sublime_plugin.WindowCommand):
    """ Command to skip all remaining sentences during TTS speech synthesis.

    command string: tts_reinitialize
    Callable with:
        sublime.run_command("tts_reinitialize")
    """
    def run(self):
        settings = sublime.load_settings(SETTINGS_NAME)
        debug_print = settings.get("debug_print", DEBUG_PRINT)
        if debug_print:
            print("tts.reinitialize_voice() ... ", end="")
        ret = reinitialize_with_settings()
        if debug_print:
            print(ret)
