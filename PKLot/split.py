# generate 3 folders for train, validation and test
# each folder contains 2 subfolders for images and labels

# from folder PUCPR UFPR04 UFPR05 get all images and labels
# split them into train, validation and test
# split ratio: 0.8, 0.1, 0.1

import os
import shutil
import random

# Define the paths
source_folders = ['./PUCPR', './UFPR04', './UFPR05']
target_base_folder = './dataset'
subfolders = ['images', 'labels']
split_ratios = [0.8, 0.1, 0.1]

# Create train, validation, and test folders
for split in ['train', 'validation', 'test']:
    split_folder = os.path.join(target_base_folder, split)
    os.makedirs(split_folder, exist_ok=True)
    
    # Create subfolders for images and labels
    for subfolder in subfolders:
        os.makedirs(os.path.join(split_folder, subfolder), exist_ok=True)

# Copy images and labels to the appropriate split folders
for source_folder in source_folders:
    for subfolder in subfolders:
        source_path = os.path.join(source_folder, subfolder)
        all_files = os.listdir(source_path)
        
        # Shuffle the files randomly
        random.shuffle(all_files)
        
        # Calculate the split indices
        total_files = len(all_files)
        train_split = int(split_ratios[0] * total_files)
        validation_split = train_split + int(split_ratios[1] * total_files)
        
        # Copy files to the appropriate split folders
        for i, file in enumerate(all_files):
            if i < train_split:
                split = 'train'
            elif i < validation_split:
                split = 'validation'
            else:
                split = 'test'
            
            target_folder = os.path.join(target_base_folder, split, subfolder)
            shutil.copy(os.path.join(source_path, file), target_folder)

print("Data split and folders created successfully.")

