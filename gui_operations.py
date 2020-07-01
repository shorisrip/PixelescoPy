from tkinter import *
from PIL import ImageTk, Image
# pip install Pillow


class GuiWindow():
    def __init__(self):
        self.root = Tk()
        self.screen_width = self.root.winfo_screenwidth()
        self.screen_height = self.root.winfo_screenheight()
        self.image_label = None
        self.image = None

    def run_window_on_loop(self):
        button_exit = Button(self.root, text="Exit Program", command=self.root.quit)
        button_exit.grid(row=1, column=1)
        self.root.mainloop()

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

