from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename  
window = Tk()
window.title("Text Editor")
window.geometry("600x500")
def open_file():
    path = askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if path:
        txt.delete(1.0, END)
        with open(path, "r")  as file:
            txt.insert(END, file.read())
        window.title(f"Text Editor - {path}")

def save_file():
    path= asksaveasfilename(defaultextension=".txt",
                            filetypes=[("Text Files", "*.txt"),("All Files","*.*")])
    if path:
        with open(path, "w")as f:
            f.write(txt.get(1.0,END))
            window.title(f"Text Editor - {path}")

txt = Text(window)
btn_frame= Frame(window)

Button(btn_frame, text='open', command=open_file).pack(fill="x")
Button(btn_frame, text="Save", command=save_file).pack(fill="x")

btn_frame.pack(side="left", fill="y")
txt.pack(side="right",expand=True, fill="both")
window.mainloop()