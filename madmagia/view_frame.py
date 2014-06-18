import os
import sys
import subprocess

import sequence
import video_slice
from config import config


def main():
    if len(sys.argv) != 3:
        print >> sys.stderr, 'Args:'
        print >> sys.stderr, '    VIDEO_EP TIME'
        return sys.exit(1)
    try:
        epnum = sequence.epnum(sys.argv[1])
    except (ValueError, LookupError):
        raise ValueError('no such episode ' + sys.argv[1])
    imgf = video_slice.save_frame(sequence.parse_time(sys.argv[2]), epnum)
    if imgf is None:
        raise ValueError('Fail to extract frame')
    subprocess.Popen([config['display'], imgf])
