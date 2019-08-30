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
spvoice = win32com.client.Dispatch('SAPI.SPVoice')


def reinitialize_voice():
    global spvoice
    # del spvoice
    spvoice = win32com.client.Dispatch('SAPI.SPVoice')
    return spvoice


def speak(sentence):
    return spvoice.Speak(sentence.encode('utf-8'), 19)  # returns immediately.


def pause():
    return spvoice.Pause()  # returns immediately.


def resume():
    return spvoice.Resume()  # returns immediately.


def skip(num_skip=1):
    return spvoice.Skip("Sentence", num_skip)  # returns immediately.


def skip_all():
    return skip(num_skip=1000)


def speak_and_wait_until_done(sentence):
    return spvoice.WaitUntilDone(sentence.encode('utf-8'), 19)  # blocks until done.


def test_speak_1():
    return speak("This is sentence number one. Sentence number one is really long and difficult to read.")


def test_speak_2():
    speak("This is sentence number one. Sentence number one is really long and difficult to read.")  # This is skipped.
    speak("This is sentence number two. This is sentence number three.")  # This is also skipped.
    return speak("This is sentence number four. ")  # Only says this.


