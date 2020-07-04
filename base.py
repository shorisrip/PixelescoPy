import random
import threading
from picture import *
from db_operations import *
from gui_operations import GuiWindow


def worker(guiObj, thread_dict):

    ################# INPUT SECTION ################################################
    # Input file path, desired extensions and timer in seconds
    file_path = "/Users/kaermorhen/Desktop/tkinter_files/images/"
    file_extensions = ('.jpg', '.png')
    timer = 5
    ################################################################################

    # Fetch file list
    files_matched = list_all_pictures(file_path, file_extensions)
    files_not_viewed = files_matched
    print("Thread 1 started")
    # Choose one and change its status from  "not_viewed" to "viewed" in db
    while len(files_not_viewed) != 0:
        chosen = random.choice(files_not_viewed)
        if is_not_viewed(chosen):
            pictureObj = Picture(chosen, timer)
            pictureObj.set_control_thread_obj(thread_dict["control_thread"])
            # pictureObj.flag = 0
            guiObj.set_picture_obj(pictureObj)
            # yet another thread so that it can be terminated on will
            # Display the chosen for <timer> seconds
            # pictureObj.display(guiObj)
            thread_for_image_display = threading.Thread(target=pictureObj.display, args=(
            guiObj,))
            pictureObj.set_display_thread_obj(thread_for_image_display)
            # thread_list.append(thread_for_image_display)
            thread_dict["display_thread"] = thread_for_image_display
            start_time = time.time()
            thread_for_image_display.start()
            # thread_for_image_display._is_stopped = True

            # if pictureObj.flag == 0:
            #     print("flag is ", pictureObj.flag)
            while thread_for_image_display._is_stopped == False:
                if thread_for_image_display._is_stopped == True:
                    # thread_for_image_display.join()
                    print("Thread 2 joined thread 1")
                    break
            end_time = time.time()
            # Change the status of "chosen" to "viewed"
            mark_as_viewed(chosen)
            print("Back in Thread 1. Display time: {}".format(end_time - start_time))
        else :
            print("Skipping", chosen)
            # skip to next
            pass
        # Remove chosen ones from variable to avoid reead from db
        files_not_viewed = list(set(files_not_viewed) - set([chosen]))
        if len(files_not_viewed) == 0:
            mark_all_as_not_viewed()
            # files_not_viewed = files_matched
            guiObj.quit_window()
    print("All images have been viewed, starting from the beginning once again")
    guiObj.quit_window()


# Keep GUI on main thread and everything else on thread
guiObj = GuiWindow()
print("Main thread started")
thread_list = []
thread_dict = {}
thread_for_image_control = threading.Thread(target=worker, args=(guiObj,
                                                                 thread_dict))
thread_dict["control_thread"] = thread_for_image_control
thread_list.append(thread_for_image_control)
thread_for_image_control.start()
guiObj.run_window_on_loop()
# thread_for_image_control.join()
print("Thread 1 joined to Main thread ")
print("Main thread end")


