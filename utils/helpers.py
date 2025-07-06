from tkinter import ttk
from PIL import Image, ImageTk

def apply_styles(style):
    """Apply all style configurations"""
    for style_name, config in STYLE_CONFIG.items():
        style.configure(style_name, **config)

def resize_image(path, width, height):
    """Resize image while maintaining aspect ratio"""
    img = Image.open(path)
    img = img.resize((width, height), Image.LANCZOS)
    return ImageTk.PhotoImage(img)