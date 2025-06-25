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