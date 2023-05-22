import os
import random
import shutil

# 52 images for training
# 35 for testing
# 35 for val
training = 52
testing = 35
valing = 35

# /path/to/folder/A/
# /path/to/folder/B/

def distribution(num_images, dest_dir):
    # Path to the source directory
    source_dir = '/Users/hannaqasim/Desktop/Face Detection J/data/pictures' # change accordingly

    # Get a list of all the image files in the source directory
    image_files = [os.path.join(source_dir, f) for f in os.listdir(source_dir) if os.path.isfile(os.path.join(source_dir, f)) and f.endswith((".jpg", ".png", ".gif", ".jpeg"))]

    # Select num_images at random from the list of image files
    selected_images = random.sample(image_files, num_images)

    # Move the selected images to the destination directory
    for image in selected_images:
        shutil.move(image, dest_dir)

    return
    
# distributing
distribution(training, '/Users/hannaqasim/Desktop/Face Detection J/data/train/pictures') # change accordingly
distribution(testing, '/Users/hannaqasim/Desktop/Face Detection J/data/test/pictures') # change accordingly
distribution(valing, '/Users/hannaqasim/Desktop/Face Detection J/data/val/pictures') # change accordingly

# moves the respective json files to the label files
# credit: nicknochnack
for folder in ['train','test','val']:
    for file in os.listdir(os.path.join('data', folder, 'pictures')):
        
        filename = file.split('.')[0]+'.json'
        existing_filepath = os.path.join('data','labels', filename)
        if os.path.exists(existing_filepath): 
            new_filepath = os.path.join('data',folder,'labels',filename)
            os.replace(existing_filepath, new_filepath)