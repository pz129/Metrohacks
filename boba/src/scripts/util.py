import numpy as np
from matplotlib import pyplot as plt
from matplotlib.colors import LogNorm
import wave
import sys
import os
import os.path

import IPython.display as ipd

PI = np.pi

def find_peaks(x, thresh = 0.2) :
    ''' finds peaks in 1D vector.
    x: input vector
    thresh: relative threshold value. Discard peak whose value is
    lower than (thresh * max_peak_value).
    '''

    x0 = x[:-2]   # x
    x1 = x[1:-1]  # x shifted by 1
    x2 = x[2:]    # x shifted by 2

    peak_bools = np.logical_and(x0 < x1, x1 > x2) # where x1 is higher than surroundings
    values = x1[peak_bools]                       # list of all peak values

    # find a threshold relative to the highest peak
    th = np.max(values) * thresh
    
    # filter out values that are below th
    peak_bools = np.logical_and(peak_bools, x1 > th)

    peaks = np.nonzero( peak_bools )[0] + 1       # get indexes of peaks, shift by 1
    return peaks


def load_wav(filepath, t_start = 0, t_end = sys.maxint):
    """
    Load a wave file from filepath. Wave file must be 22050Hz and 16bit and must be either
    mono or stereo. Returns a numpy floating-point array with a range of [-1, 1]
    """
    
    wf = wave.open(filepath)
    num_channels, sampwidth, sr, end, comptype, compname = wf.getparams()
    
    # for now, we will only accept 16 bit files at 22k
    assert(sampwidth == 2)
    assert(sr == 22050)

    # start frame, end frame, and duration in frames
    f_start = int(t_start * sr)
    f_end = min(int(t_end * sr), end)
    frames = f_end - f_start

    wf.setpos(f_start)
    raw_bytes = wf.readframes(frames)

    # convert raw data to numpy array, assuming int16 arrangement
    samples = np.fromstring(raw_bytes, dtype = np.int16)

    # convert from integer type to floating point, and scale to [-1, 1]
    samples = samples.astype(np.float)
    samples *= (1 / 32768.0)

    if num_channels == 1:
        return samples

    elif num_channels == 2:
        return 0.5 * (samples[0::2] + samples[1::2])

    else:
        raise('Can only handle mono or stereo wave files')

def bin_to_freq(val, sr, win_size):
    return val * sr * 1./win_size

def freq_to_pitch(fq):
    return np.log2(fq/440.)*12+69

def pitch_to_spn(p):
    note = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
    mod = p % 12
    octive = p / 12 - 1
    if octive < 0:
        octive = 0
    # print octive
    spn = note[mod] + str(octive)
    # print spn
    return spn

def zpad(data, new_length):
    return np.concatenate((data, np.zeros(new_length - len(data))))
