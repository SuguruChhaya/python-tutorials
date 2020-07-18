# Making Icons, images, and exit buttons
# Icons have a .ico file extension (basically a png file)
# To import actual image files (png, jpg), you need to import a module called Pillow
from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Learn to Code!!')
root.iconbitmap('TrollFace..ico')

my_img = ImageTk.PhotoImage(Image.open("TrollFace..png"))
img_label = Label(image=my_img)

button_quit = Button(root, text="Exit Porgram", command=root.quit)
button_quit.pack()
img_label.pack()
root.mainloop()
