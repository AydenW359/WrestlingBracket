import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import pandas as pd

class RosterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Roster Manager")

        # Notebook for tabs
        self.notebook = ttk.Notebook(root)
        self.notebook.pack(expand=1, fill="both")

        # Tabs
        self.upload_tab = ttk.Frame(self.notebook)
        self.format_tab = ttk.Frame(self.notebook)

        self.notebook.add(self.upload_tab, text="Upload")
        self.notebook.add(self.format_tab, text="Format")

        # Initialize DataFrame
        self.data = pd.DataFrame(columns=["Name", "Weight Class", "Record"])

        # Build UI
        self.create_upload_tab()
        self.create_format_tab()

    def create_upload_tab(self):
        # File upload
        upload_label = tk.Label(self.upload_tab, text="Upload CSV File:")
        upload_label.pack(pady=5)

        upload_button = ttk.Button(self.upload_tab, text="Browse", command=self.upload_csv)
        upload_button.pack(pady=5)

        # Editable table
        self.tree = ttk.Treeview(self.upload_tab, columns=("Name", "Weight Class", "Record"), show="headings")
        for col in self.tree["columns"]:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=100)
        self.tree.pack(expand=1, fill="both", pady=10)

        # Manual input
        input_frame = ttk.Frame(self.upload_tab)
        input_frame.pack(pady=5)

        self.name_var = tk.StringVar()
        self.weight_var = tk.StringVar()
        self.record_var = tk.StringVar()

        tk.Entry(input_frame, textvariable=self.name_var, width=15).grid(row=0, column=0, padx=5)
        tk.Entry(input_frame, textvariable=self.weight_var, width=15).grid(row=0, column=1, padx=5)
        tk.Entry(input_frame, textvariable=self.record_var, width=15).grid(row=0, column=2, padx=5)
        ttk.Button(input_frame, text="Add Entry", command=self.add_entry).grid(row=0, column=3, padx=5)

    def upload_csv(self):
        file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
        if file_path:
            try:
                self.data = pd.read_csv(file_path)
                self.update_tree()
            except Exception as e:
                messagebox.showerror("Error", f"Failed to load file: {e}")

    def update_tree(self):
        # Clear existing data
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Insert new data
        for _, row in self.data.iterrows():
            self.tree.insert("", "end", values=row.tolist())

    def add_entry(self):
        new_row = [self.name_var.get(), self.weight_var.get(), self.record_var.get()]
        self.data.loc[len(self.data)] = new_row
        self.update_tree()

    def create_format_tab(self):
        format_label = tk.Label(self.format_tab, text="Format Data by Weight Class:")
        format_label.pack(pady=5)

        format_button = ttk.Button(self.format_tab, text="Generate Brackets", command=self.generate_brackets)
        format_button.pack(pady=5)

    def generate_brackets(self):
        grouped = self.data.groupby("Weight Class")
        result = ""
        for weight, group in grouped:
            result += f"Weight Class: {weight}\n"
            result += group.to_string(index=False)
            result += "\n\n"

        # Display result
        result_window = tk.Toplevel(self.root)
        result_window.title("Brackets")
        tk.Text(result_window, wrap="word").insert("1.0", result).pack(expand=1, fill="both")


if __name__ == "__main__":
    root = tk.Tk()
    app = RosterApp(root)
    root.mainloop()
