import os.path
import time


class Picture:
    def __init__(self, path, timer):
        self.path = path
        self.timer = timer
        self.control_thread_obj = None
        self.display_thread_obj = None
        # self.flag = 0

    def set_display_thread_obj(self, thread_obj):
        self.display_thread_obj = thread_obj

    def set_control_thread_obj(self, thread_obj):
        self.control_thread_obj = thread_obj

    def display(self, guiObj):
        print("Thread 2 started")
        image_path = self.path
        guiObj.add_image(image_path)
        time.sleep(self.timer)
        print("Thread 2 end")
        print("Stop status set by Picture method")
        self.display_thread_obj._is_stopped = True


def list_all_pictures(file_path, file_extensions):
    files_matched = []
    for dirpath, dir_names, file_names in os.walk(file_path):
        for filename in [f for f in file_names if f.endswith(file_extensions)]:
            file_found = os.path.join(dirpath, filename)
            files_matched.append(file_found)
    return files_matched
