# Projecto to automate organiziation of different files according to their types

import os 
import shutil

# Define the directory to organize
DIRECTORY = "./Test Script"
OUTPUT_DIRECTORY = os.path.join(DIRECTORY, "Organized Files")

# Define file type categories
FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".pptx", ".xlsx"],
    "Audio": [".mp3", ".wav", ".aac"],
    "Videos": [".mp4", ".mov", ".avi", ".mkv"],
    "Archives": [".zip", ".rar", ".tar", ".gz"],
    "Scripts": [".py", ".sh", ".bat", ".js"]
}

# Function to Organize file
def organize_files(directory):
    if not os.path.exists(directory):   # Checking if directory exist or not
        print("Directory does not exist.")
        return
    
    # Create the output directory if it doesn't exist
    if not os.path.exists(OUTPUT_DIRECTORY):
        os.makedirs(OUTPUT_DIRECTORY)
    
    # Create folders for categories inside the output directory if not exist
    for category in FILE_TYPES.keys():
        category_path = os.path.join(OUTPUT_DIRECTORY, category)
        if not os.path.exists(category_path):
            os.makedirs(category_path)
    
    # Iterate through files and move them to respective folders
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path):
            for category, extensions in FILE_TYPES.items():
                if any(filename.lower().endswith(ext) for ext in extensions):
                    shutil.move(file_path, os.path.join(OUTPUT_DIRECTORY, category, filename))
                    print(f"Moved: {filename} -> {category}")
                    break

if __name__ == "__main__":
    organize_files(DIRECTORY)