import os.path


class Picture:
    def __init__(self, path):
        self.path = path

    def display(self, guiObj):
        image_path = self.path
        guiObj.add_image(image_path)
        print("displayed")


def list_all_pictures(file_path, file_extensions):
    files_matched = []
    for dirpath, dir_names, file_names in os.walk(file_path):
        for filename in [f for f in file_names if f.endswith(file_extensions)]:
            file_found = os.path.join(dirpath, filename)
            files_matched.append(file_found)
    return files_matched
