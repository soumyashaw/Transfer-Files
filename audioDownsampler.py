import os
from pydub import AudioSegment

def downsample_audio_files(directory, output_directory, target_sample_rate):
    itr = 0
    # Iterate over all files in the directory
    for filename in os.listdir(directory):
        itr += 1
        if filename.endswith(".wav") or filename.endswith(".flac"):
            # Load the audio file
            audio = AudioSegment.from_file(os.path.join(directory, filename))

            # Downsample the audio
            audio = audio.set_frame_rate(target_sample_rate)

            # Save the downsampled audio to the output directory
            output_filename = os.path.join(output_directory, filename)
            audio.export(output_filename, format="flac")
            print("Downsampled audio file " + str(itr) + " of " + str(len(os.listdir(directory))))

# Example usage
directory = "/hkfs/home/haicore/hgf_cispa/hgf_yie2732/sampledASVspoof2021/LA/ASVspoof2019_LA_eval/flac/"
output_directory = "/hkfs/home/haicore/hgf_cispa/hgf_yie2732/sampledASVspoof2021/LA/ASVspoof2019_LA_eval/downsampledFLAC"
target_sample_rate = 3400

itr = 0

downsample_audio_files(directory, output_directory, target_sample_rate)
