import random
from picture import *
from db_operations import *

# Input file path, desired extensions and timer in seconds
file_path = "/Users/kaermorhen/Desktop/"
file_extensions = ('.jpg', '.png')
timer = 1

# If no files in db
if is_table_empty():
    # Store all possible files in db table "not_viewed"
    files_matched = list_all_pictures(file_path, file_extensions)
    populate_db_with_paths(files_matched)
    files_not_viewed = files_matched
else:
    files_not_viewed = list_not_viewed()

# Store files_matched in db table "dekha_hoy_ni"
# todo

# Load files from db table "dekha_hoy_ni" in array
# todo
# Remove this line when the load method is implemented


# Choose one and move the entry from table "dekha_hoy_ni" to table "dekha_hoy_geche"
while len(files_not_viewed) != 0:
  chosen = random.choice(files_not_viewed)
  pictureObj = Picture(chosen)
  # Display the chosen for <timer> seconds
  pictureObj.display(timer)
  # Remove this line when Display method is implmented
  print("Chosen:" , chosen)
  # Add entry of chosen in table "dekha_hoy_geche", Remove entry of chosen in table "dekha_hoy_ni" and commit
  # todo
  # Remove these 2 lines when transfer method is implemented
  files_not_viewed = list(set(files_not_viewed) - set([chosen]))
  print("Array:", files_not_viewed)

# Find an ORM
# Define schema
# Define logic to move image back to dekha hoy ni after some days