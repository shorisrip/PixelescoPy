import random
import threading
import time
from picture import *
from db_operations import *
from gui_operations import GuiWindow


def worker(guiObj):

    ################# INPUT SECTION ################################################
    # Input file path, desired extensions and timer in seconds
    file_path = "/Users/kaermorhen/Desktop/tkinter_files/images/"
    file_extensions = ('.jpg', '.png')
    timer = 10
    ################################################################################


    # Fetch file list
    files_matched = list_all_pictures(file_path, file_extensions)
    files_not_viewed = files_matched

    # Choose one and change its status from  "not_viewed" to "viewed" in db
    while len(files_not_viewed) != 0:
        chosen = random.choice(files_matched)
        if is_not_viewed(chosen):
            pictureObj = Picture(chosen)
            # Display the chosen for <timer> seconds
            pictureObj.display(guiObj)
            time.sleep(timer)
            # Change the status of "chosen" to "viewed"
            mark_as_viewed(chosen)
        else :
            # skip to next
            pass
        # Remove chosen ones from variable to avoid reead from db
        files_not_viewed = list(set(files_not_viewed) - set([chosen]))
        if len(files_not_viewed) == 0:
            print("All images have been viewed, starting from the beginning once again")
            mark_all_as_not_viewed()
            files_not_viewed = files_matched


# Keep GUI on main thread and everything else on thread
guiObj = GuiWindow()
thread_list = []
thread = threading.Thread(target=worker, args=(guiObj,))
thread_list.append(thread)
thread.start()
guiObj.run_window_on_loop()