import tkinter as tk
from tkinter import colorchooser, filedialog, messagebox
from PIL import ImageGrab

class PaintApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Paint App")
        self.root.geometry("1100x600")

        # Variables (Encapsulation)
        self.stroke_size = tk.IntVar(value=1)
        self.stroke_color = tk.StringVar(value="black")
        self.prev_color = tk.StringVar(value="white")
        self.prev_color2 = tk.StringVar(value="white")
        self.text_value = tk.StringVar()
        self.prev_point = [0, 0]

        self.setup_ui()

    def setup_ui(self):
        frame1 = tk.Frame(self.root, height=100, width=1100)
        frame1.grid(row=0, column=0, sticky=tk.NW)

        # Tools
        tools_frame = tk.Frame(frame1, relief=tk.SUNKEN, borderwidth=3)
        tools_frame.grid(row=0, column=0)
        tk.Button(tools_frame, text="Pencil", width=10, command=self.use_pencil).grid(row=0, column=0)
        tk.Button(tools_frame, text="Eraser", width=10, command=self.use_eraser).grid(row=1, column=0)

        # Size
        size_frame = tk.Frame(frame1, relief=tk.SUNKEN, borderwidth=3)
        size_frame.grid(row=0, column=1)
        tk.OptionMenu(size_frame, self.stroke_size, *[1, 2, 3, 4, 5, 10]).grid(row=0, column=0)

        # Colors
        color_frame = tk.Frame(frame1, relief=tk.SUNKEN, borderwidth=3)
        color_frame.grid(row=0, column=2)
        tk.Button(color_frame, text="Select Color", command=self.select_color).grid(row=0, column=0)

        # Save/Clear
        save_frame = tk.Frame(frame1, relief=tk.SUNKEN, borderwidth=3)
        save_frame.grid(row=0, column=3)
        tk.Button(save_frame, text="Save", command=self.save_image).grid(row=0, column=0)
        tk.Button(save_frame, text="Clear", command=self.clear_canvas).grid(row=1, column=0)

        # Text Entry
        text_frame = tk.Frame(frame1, relief=tk.SUNKEN, borderwidth=3)
        text_frame.grid(row=0, column=4)
        tk.Entry(text_frame, textvariable=self.text_value).grid(row=0, column=0)

        # Canvas
        self.canvas = tk.Canvas(self.root, bg="white", height=500, width=1100)
        self.canvas.grid(row=1, column=0)
        self.canvas.bind("<B1-Motion>", self.paint)
        self.canvas.bind("<ButtonRelease-1>", self.reset_paint)
        self.canvas.bind("<Button-2>", self.write_text)

    def use_pencil(self):
        self.stroke_color.set("black")
        self.canvas.config(cursor="arrow")

    def use_eraser(self):
        self.stroke_color.set("white")
        self.canvas.config(cursor="dotbox")

    def select_color(self):
        color = colorchooser.askcolor(title="Select Color")[1]
        if color:
            self.prev_color2.set(self.prev_color.get())
            self.prev_color.set(color)
            self.stroke_color.set(color)

    def paint(self, event):
        x, y = event.x, event.y
        if self.prev_point != [0, 0]:
            self.canvas.create_line(self.prev_point[0], self.prev_point[1], x, y,
                                    fill=self.stroke_color.get(), width=self.stroke_size.get())
        self.prev_point = [x, y]

    def reset_paint(self, event):
        self.prev_point = [0, 0]

    def write_text(self, event):
        self.canvas.create_text(event.x, event.y, text=self.text_value.get(), fill=self.stroke_color.get())

    def save_image(self):
        file = filedialog.asksaveasfilename(defaultextension=".jpg")
        if file:
            x = self.root.winfo_rootx()
            y = self.root.winfo_rooty() + 100
            x1 = x + self.canvas.winfo_width()
            y1 = y + self.canvas.winfo_height()
            ImageGrab.grab().crop((x, y, x1, y1)).save(file)
            messagebox.showinfo("Saved", f"Image saved to {file}")

    def clear_canvas(self):
        self.canvas.delete("all")
    
    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    root = tk.Tk()
    app = PaintApp(root)
    app.run()