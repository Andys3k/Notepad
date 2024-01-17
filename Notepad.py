import tkinter as tk
from tkinter import filedialog, colorchooser, simpledialog, ttk, messagebox

class NotepadApp:
    def __init__(self, root):
        # Initialize the main application window
        self.root = root
        self.root.title("Simple Notepad")

        # Configure a style for the resize grip
        style = ttk.Style()
        style.configure("Dark.TSizegrip", gripcolor="darkgrey")

        # PanedWindow for text editor and resize grip
        self.paned_window = ttk.PanedWindow(root, orient=tk.VERTICAL)
        self.paned_window.pack(expand=True, fill="both")

        # Text widget for editing
        self.text_widget = tk.Text(self.paned_window, wrap="word", width=50)
        self.paned_window.add(self.text_widget)

        # Resize grip with the "Dark.TSizegrip" style
        self.resize_grip = ttk.Sizegrip(self.root, style="Dark.TSizegrip")
        self.resize_grip.place(relx=1.0, rely=1.0, anchor="se")

        # Menu bar
        self.menu_bar = tk.Menu(root)
        self.root.config(menu=self.menu_bar)

        # File menu
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="New", command=self.new_file)
        self.file_menu.add_command(label="Open", command=self.open_file)
        self.file_menu.add_command(label="Save", command=self.save_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=self.root.destroy)

        # Settings menu
        self.settings_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Settings", menu=self.settings_menu)

        # Font Size submenu
        self.font_size_menu = tk.Menu(self.settings_menu, tearoff=0)
        self.settings_menu.add_cascade(label="Font Size", menu=self.font_size_menu)
        self.font_size_menu.add_command(label="Change Font Size", command=self.change_font_size)

        # Font Color submenu
        self.font_color_menu = tk.Menu(self.settings_menu, tearoff=0)
        self.settings_menu.add_cascade(label="Font Color", menu=self.font_color_menu)
        self.font_color_menu.add_command(label="Change Font Color", command=self.change_font_color)

        # Background Color submenu
        self.bg_color_menu = tk.Menu(self.settings_menu, tearoff=0)
        self.settings_menu.add_cascade(label="Background Color", menu=self.bg_color_menu)
        self.bg_color_menu.add_command(label="Change Background Color", command=self.change_bg_color)

        # Credits menu
        self.credits_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Credits", menu=self.credits_menu)
        self.credits_menu.add_command(label="Show Credits", command=self.show_credits)

        # Default font size
        self.default_font_size = 12

        # Initial font configuration
        self.text_widget.config(font=("TkDefaultFont", self.default_font_size))

    def new_file(self):
        # Clear the text widget
        self.text_widget.delete(1.0, tk.END)

    def open_file(self):
        # Ask user to select a file to open
        file_path = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])

        # If a file is selected, read its content and insert into text widget
        if file_path:
            with open(file_path, "r") as file:
                content = file.read()
                self.text_widget.delete(1.0, tk.END)
                self.text_widget.insert(tk.END, content)

    def save_file(self):
        # Ask user to select a file to save
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])

        # If a file is selected, write the content of the text widget to the file
        if file_path:
            with open(file_path, "w") as file:
                content = self.text_widget.get(1.0, tk.END)
                file.write(content)

    def change_font_size(self):
        # Ask user to enter a new font size
        new_size = simpledialog.askinteger("Change Font Size", "Enter new font size:", initialvalue=self.default_font_size)
        if new_size is not None:
            self.default_font_size = new_size
            self.text_widget.config(font=("TkDefaultFont", self.default_font_size))

    def change_font_color(self):
        # Ask user to select a new font color
        color = colorchooser.askcolor(initialcolor=self.text_widget.cget("fg"))[1]
        if color:
            self.text_widget.config(fg=color)

    def change_bg_color(self):
        # Ask user to select a new background color
        color = colorchooser.askcolor(initialcolor=self.text_widget.cget("bg"))[1]
        if color:
            self.text_widget.config(bg=color)

    def show_credits(self):
        # Show a messagebox with credits information
        credits_message = "Owner: ands3k (GitHub)\nCode: ChatGPT (AI)"
        messagebox.showinfo("Credits", credits_message)

if __name__ == "__main__":
    root = tk.Tk()
    app = NotepadApp(root)
    root.mainloop()
