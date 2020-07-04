from tkinter import *
from PIL import ImageTk, Image


class GuiWindow():
    def __init__(self):
        self.picture_obj = None
        self.root = Tk()
        self.screen_width = self.root.winfo_screenwidth()
        self.screen_height = self.root.winfo_screenheight()
        self.image_label = None
        self.image = None
        self.folder_path = None
        self.timer = None

    def set_picture_obj(self, picture_obj):
        self.picture_obj = picture_obj

    def stop_thread(self):
        self.picture_obj.display_thread_obj._is_stopped = True
        print("Stop status set by GUI method")
        # self.picture_obj.flag = 1
        # print("flag is set to ", self.picture_obj.flag)
        print(">> button called")

    def exit_button(self):
        self.picture_obj.control_thread_obj._is_stopped = True
        self.picture_obj.display_thread_obj._is_stopped = True
        self.root.quit()

    def run_window_on_loop(self):
        button_exit = Button(self.root, text="Exit Program", command=self.exit_button)
        button_left = Button(self.root, text="<",)
        button_right = Button(self.root, text=">",
                              command=self.stop_thread)
        button_exit.grid(row=1, column=1, pady=5)
        button_left.grid(row=1, column=0, pady=5, columnspan=1)
        button_right.grid(row=1, column=2, pady=5, columnspan=1)
        self.root.mainloop()

    # def add_input_section(self):
    #     input_folder = Entry(self.root, width=100, text="Paste the folder path")
    #     input_folder.grid(row=0, column=0)
    #     input_timer = Entry(self.root, width=20, text="Enter timer in seconds")
    #     input_timer.grid(row=0, column=1)
    #     folder_path = None
    #     timer = None
    #     def entry_action(guiObj):
    #         guiObj.folder_path = input_folder.get()
    #         guiObj.timer = input_timer.get()
    #
    #     entry_Button = Button(self.root, text="Enter Your Stock Quote", command=lambda: entry_action(self))
    #     entry_Button.grid(row=0, column=2)
    #     return {"folder_path": folder_path, "timer": timer}

    def quit_window(self):
        self.root.quit()

    def resize(self, image_path):
        my_pic = Image.open(image_path)
        pic_height = my_pic.height
        pic_width = my_pic.width
        if my_pic.height > (self.screen_height - 100):
            new_height= self.screen_height - 100
            new_width = int(new_height / pic_height * pic_width)
            pic_height = new_height
            pic_width = new_width

        if pic_width > self.screen_width - 5:
            new_width = self.screen_height - 5
            new_height = int(new_width / pic_width * pic_height)
            pic_height = new_height
            pic_width = new_width

        resized_image = my_pic.resize((pic_width, pic_height), Image.ANTIALIAS)
        return resized_image

    def add_image(self, image_path):
        resized_img = self.resize(image_path)
        image_obj = ImageTk.PhotoImage(resized_img)
        image_label = Label(self.root, image=image_obj,
                            height=resized_img.height,
                            width=resized_img.width)
        self.image = image_obj # DO NOT REMOVE - Garbage collector error
        if self.image_label is not None:
            self.remove_image()
        image_label.grid(row=0, column=0, columnspan=3)
        self.image_label = image_label

    def remove_image(self):
        self.image_label.grid_forget()


