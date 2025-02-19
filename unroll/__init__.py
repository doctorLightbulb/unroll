"""Unroll
=======

Unroll is a Python module to ease transcription of piano rolls to sheet music.
It transcribes either a MIDI file or a video of a piano roll. It finds
the notes, the tempo, roughly separates the hands, and writes the result
in a Lilypond file. In particular

You can use it like this: ::

    # TO TRANSCRIBE FROM A VIDEO

    from unroll import video2scan, rollscan2keystrikes
    focus = lambda im : im[[156],58:478]
    scan = video2scan(videofile = "limehouse_nights.mp4", focus = focus)
    keystrikes = rollscan2keystrikes(scan)
    keystrikes = ks.transposed(26)
    keystrikes.transcribe('score.ly', quarter_durations = [2,10,0.02])

    # TO TRANSCRIBE FROM A MIDI FILE

    from unroll import midi2keystrikes
    keystrikes = midi2keystrikes('tiger_rag.mid')
    ks.transcribe('score.ly', quarter_durations = [50,100,0.02])


Then you must edit ``score.ly`` to correct the mistakes and when you are done you compile it with
::

    lilypond score.ly

"""

__all__ = [
    "KeyStrikes",
    "midi2keystrikes",
    "video2rollscan",
    "rollscan2keystrikes",
]

from .KeyStrikes import KeyStrikes
from .MIDI import midi2keystrikes
from .video import rollscan2keystrikes, video2rollscan
