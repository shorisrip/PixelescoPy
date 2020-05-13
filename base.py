import random
from picture import *
from db_operations import *

################# INPUT SECTION ################################################
# Input file path, desired extensions and timer in seconds
file_path = "/Users/kaermorhen/Desktop/"
file_extensions = ('.jpg', '.png')
timer = 1
################################################################################


# files_matched = list_all_pictures(file_path, file_extensions)
# populate_db_with_paths(files_matched)


files_matched = list_all_pictures(file_path, file_extensions)
files_not_viewed = files_matched

# Choose one and change its status from  "not_viewed" to "viewed" in db
while len(files_matched) != 0:
    chosen = random.choice(files_matched)
    if is_not_viewed(chosen):
        pictureObj = Picture(chosen)
        # Display the chosen for <timer> seconds
        pictureObj.display(timer)
        # Change the status of "chosen" to "viewed"
        mark_as_viewed(chosen)
    else :
        # skip to next
        pass
    # Remove chosen ones from variable to avoid reead from db
    files_not_viewed = list(set(files_not_viewed) - set([chosen]))
