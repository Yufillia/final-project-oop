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