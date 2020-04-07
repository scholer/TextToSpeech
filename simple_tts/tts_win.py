# Copyright 2019, Rasmus Sorensen <rasmusscholer@gmail.com>
"""

This is a simpler version that avoids all the complex stuff in pyttsx3,
and just uses the win32com api more directly.

Turns out, this is a lot more reliable than trying to work with the eventloop and callback
options in pyttsx3.


"""

# If `win32com.client` is not available, maybe consider using `comtypes`?
# But `python-win32` is available in Package Control dependencies, comtypes is not.

import win32com.client

# speech = win32com.client.Dispatch('System.Speech.Synthesis.SpeechSynthesizer')  # Doesn't work
spvoice = None  # Must initialize voice first.


def reinitialize_voice(rate=None, volume=None, voice=None):
    """ Re-initialize voice engine and reset rate, volume, and voice.
    Note that *pitch* is not a persistent setting, but rather an xml command
    that needs to be embedded in the byte-encoded input.
    """
    global spvoice
    # del spvoice
    spvoice = win32com.client.Dispatch('SAPI.SPVoice')
    if rate is not None:
        spvoice.rate = rate
    if volume is not None:
        spvoice.volume = volume
    if voice is not None:
        # Volume should be e.g. "Microsoft Sam", or "Microsoft David"
        spvoice.voice = voice
    return spvoice


def speak(sentence):
    if spvoice is None:
        reinitialize_voice()
    return spvoice.Speak(sentence.encode('utf-8'), 19)  # returns immediately.


def pause():
    if spvoice is None:
        reinitialize_voice()
    return spvoice.Pause()  # returns immediately.


def resume():
    if spvoice is None:
        reinitialize_voice()
    return spvoice.Resume()  # returns immediately.


def skip(num_skip=1):
    if spvoice is None:
        reinitialize_voice()
    return spvoice.Skip("Sentence", num_skip)  # returns immediately.


def skip_all():
    if spvoice is None:
        reinitialize_voice()
    return skip(num_skip=1000)


def speak_and_wait_until_done(sentence):
    if spvoice is None:
        reinitialize_voice()
    return spvoice.WaitUntilDone(sentence.encode('utf-8'), 19)  # blocks until done.


def test_speak_1():
    return speak("This is sentence number one. Sentence number one is really long and difficult to read.")


def test_speak_2():
    speak("This is sentence number one. Sentence number one is really long and difficult to read.")  # This is skipped.
    speak("This is sentence number two. This is sentence number three.")  # This is also skipped.
    return speak("This is sentence number four. ")  # Only says this.


