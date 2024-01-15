import os
import librosa
import numpy as np
import soundfile as sf

def addWhiteNoise(audio, snr_dB):
    # Load the audio file
    signal, sr = librosa.load(audio, sr=None)

    # Calculate the power of the signal
    signal_power = np.sum(signal ** 2) / len(signal)

    # Calculate the noise power based on the desired SNR
    snr_linear = 10 ** (snr_dB / 10.0)
    noise_power = signal_power / snr_linear

    # Generate white Gaussian noise with the same length as the signal
    noise = np.random.normal(scale=np.sqrt(noise_power), size=len(signal))

    # Add the noise to the signal
    noisy_signal = signal + noise

    return noisy_signal, sr

parent_dir = "/hkfs/home/haicore/hgf_cispa/hgf_yie2732/sampledASVspoof2021/LA/ASVspoof2019_LA_eval/original/"
target_dir = "/hkfs/home/haicore/hgf_cispa/hgf_yie2732/sampledASVspoof2021/LA/ASVspoof2019_LA_eval/20dB/"
audioFiles = os.listdir(parent_dir)

ctr = 0

for audio in audioFiles:
    input_audio = parent_dir + str(audio)
    output_audio = target_dir + str(audio)
    desired_snr_dB = 20

    noisy_signal, sample_rate = addWhiteNoise(input_audio, desired_snr_dB)

    # Save the output with noise to a new file
    sf.write(output_audio, noisy_signal, sample_rate)
    ctr += 1
    print(ctr)

