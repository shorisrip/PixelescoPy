import random
from image import Picture
import os.path

# Input file path, desired extensions and timer in seconds
file_path = "/Users/kaermorhen/Desktop/"
file_extensions = ('.jpg', '.png')
timer = 1

# If no files in db
# Store all possible files in db table "dekha_hoy_ni"
# Fetch files and store in array
files_matched = []
for dirpath, dirnames, filenames in os.walk(file_path):
    for filename in [f for f in filenames if f.endswith(file_extensions)]:
        file_found = os.path.join(dirpath, filename)
        files_matched.append(file_found)
# Store files_matched in db table "dekha_hoy_ni"
# todo

# Load files from db table "dekha_hoy_ni" in array
# todo
# Remove this line when the load method is implemented
files_matched_copy = files_matched

# Choose one and move the entry from table "dekha_hoy_ni" to table "dekha_hoy_geche"
while len(files_matched_copy) != 0:
  chosen = random.choice(files_matched_copy)
  pictureObj = Picture(chosen)
  # Display the chosen for <timer> seconds
  pictureObj.display(timer)
  # Remove this line when Display method is implmented
  print("Chosen:" , chosen)
  # Add entry of chosen in table "dekha_hoy_geche", Remove entry of chosen in table "dekha_hoy_ni" and commit
  # todo
  # Remove these 2 lines when transfer method is implemented
  files_matched_copy = list(set(files_matched_copy) - set([chosen]))
  print("Array:" , files_matched_copy)

# Find an ORM
# Define schema
# Define logic to move image back to dekha hoy ni after some days