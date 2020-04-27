import random
from picture import *
from db_operations import *

################# INPUT SECTION ################################################
# Input file path, desired extensions and timer in seconds
file_path = "/Users/kaermorhen/Desktop/"
file_extensions = ('.jpg', '.png')
timer = 1
################################################################################


# If no files in db
if is_table_empty():
    # Store all possible files with status "not_viewed"
    files_matched = list_all_pictures(file_path, file_extensions)
    populate_db_with_paths(files_matched)
    files_not_viewed = files_matched
else:
    files_not_viewed = list_not_viewed()



# Choose one and change its status from  "not_viewed" to "viewed" in db
while len(files_not_viewed) != 0:
    chosen = random.choice(files_not_viewed)
    pictureObj = Picture(chosen)
    # Display the chosen for <timer> seconds
    pictureObj.display(timer)
    # Remove this line when Display method is implmented
    print("Chosen:" , chosen)
    # Change the status of "chosen" to "viewed"
    mark_as_viewed(chosen)
    # Remove these 2 lines when transfer method is implemented
    files_not_viewed = list(set(files_not_viewed) - set([chosen]))
    print("Array:", files_not_viewed)

# Find an ORM
# Define schema
# Define logic to move image back to dekha hoy ni after some days