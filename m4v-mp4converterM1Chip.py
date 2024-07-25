import os
import subprocess
import tkinter as tk
from tkinter import filedialog

def convert_m4v_to_mp4(directory):
    # Check if the directory exists
    if not os.path.isdir(directory):
        print(f"Directory {directory} does not exist.")
        return

    # List all files in the directory
    files = os.listdir(directory)
    
    # Filter for .m4v files
    m4v_files = [f for f in files if f.endswith('.m4v')]
    
    # Convert each .m4v file to .mp4
    for m4v_file in m4v_files:
        mp4_file = os.path.splitext(m4v_file)[0] + '.mp4'
        m4v_path = os.path.join(directory, m4v_file)
        mp4_path = os.path.join(directory, mp4_file)
        
        # Call ffmpeg with VideoToolbox for hardware acceleration
        command = [
            'ffmpeg', '-i', m4v_path, 
            '-c:v', 'h264_videotoolbox', 
            '-c:a', 'copy', 
            mp4_path
        ]
        subprocess.run(command, check=True)
        
        print(f"Converted {m4v_file} to {mp4_file}")

def main():
    # Create a root window and hide it
    root = tk.Tk()
    root.withdraw()
    
    # Ask the user to select a directory
    directory = filedialog.askdirectory(title="Select Folder Containing .m4v Files")
    
    if directory:
        convert_m4v_to_mp4(directory)
    else:
        print("No directory selected.")

if __name__ == "__main__":
    main()
