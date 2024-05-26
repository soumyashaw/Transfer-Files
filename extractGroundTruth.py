import os

def filter_files_in_directory(output_file, new_output_file):
    # Get the list of all files in the current directory
    files_in_directory = set(os.listdir('/home/soumyas_kvmohan/ASVspoof2021/LA/ASVspoof2019_LA_eval/flac/'))
    #print(files_in_directory[0])

    try:
        # Open the output.txt file for reading
        with open(output_file, 'r') as infile:
            # Open the new output file for writing
            with open(new_output_file, 'w') as outfile:
                # Iterate through each line in the output.txt file
                for line in infile:
                    # Extract the filename from the line (assuming it's the first part of the line)
                    filename = str(line.strip().split()[1]) + '.flac'
                    # Check if the file is present in the current directory
                    if filename in files_in_directory:
                        # Write the full line to the new output file
                        outfile.write(line)
        print(f"Filtered lines written to {new_output_file}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Define the paths to the input and output files
output_file = '/home/soumyas_kvmohan/ASVspoof2021/LA/full_ASVspoof2019.LA.cm.eval.trl.txt'  # Path to the generated output.txt file
new_output_file = 'ASVspoof2019.LA.cm.eval.trl.txt'  # Path to the new output file

# Call the function to filter files and write to the new output file
filter_files_in_directory(output_file, new_output_file)

