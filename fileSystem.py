import tkinter as tk
from tkinter import messagebox, simpledialog, ttk


# FILE SYSTEM CONFIG

TOTAL_BLOCKS = 64
BLOCK_SIZE = 4096  


class FileSystem:
    def __init__(self):
        self.free_blocks = [True] * TOTAL_BLOCKS
        self.files = {}  

    def allocate_blocks(self, file_size_blocks):
        """Allocate blocks: 1 index block + data blocks."""
        free_indices = [i for i, b in enumerate(self.free_blocks) if b]

        needed = file_size_blocks + 1  

        if len(free_indices) < needed:
            return None, None  

        index_block = free_indices[0]
        data_blocks = free_indices[1:needed]

        
        self.free_blocks[index_block] = False
        for blk in data_blocks:
            self.free_blocks[blk] = False

        return index_block, data_blocks

    def create_file(self, name, size_kb):
        if name in self.files:
            return "File already exists."

        required_blocks = -(-size_kb // (BLOCK_SIZE))  # ceiling division

        index_block, data_blocks = self.allocate_blocks(required_blocks)
        if index_block is None:
            return "Not enough disk space."

        self.files[name] = {
            "size_kb": size_kb,
            "index_block": index_block,
            "data_blocks": data_blocks,
            "content": ""
        }
        return "File created successfully."

    def delete_file(self, name):
        if name not in self.files:
            return "File not found."

        f = self.files[name]

        self.free_blocks[f["index_block"]] = True
        for blk in f["data_blocks"]:
            self.free_blocks[blk] = True

        del self.files[name]
        return "File deleted."

    def write_file(self, name, content):
        if name not in self.files:
            return "File doesn’t exist."
        self.files[name]["content"] = content
        return "Content written."

    def read_file(self, name):
        if name not in self.files:
            return "File missing."

        return self.files[name]["content"]

    def get_inode_table(self):
        table = []
        for name, info in self.files.items():
            table.append([
                name,
                f"{info['size_kb']} KB",
                info["index_block"],
                info["data_blocks"]
            ])
        return table


class FileSystemGUI:
    def __init__(self, root):
        self.fs = FileSystem()
        self.root = root
        root.title("Indexed File System Simulator")
        root.geometry("800x600")

        
        tk.Label(root, text="Indexed File System Simulator",
                 font=("Arial", 18, "bold")).pack(pady=10)

        
        frame = tk.Frame(root)
        frame.pack()

        
        tk.Button(frame, text="Create File", width=15, command=self.create_file).grid(row=0, column=0)
        tk.Button(frame, text="Delete File", width=15, command=self.delete_file).grid(row=0, column=1)
        tk.Button(frame, text="Write File", width=15, command=self.write_file).grid(row=0, column=2)
        tk.Button(frame, text="Read File", width=15, command=self.read_file).grid(row=0, column=3)

        tk.Button(frame, text="Show Inode Table", width=15, command=self.show_inode).grid(row=1, column=0)
        tk.Button(frame, text="Show Free Blocks", width=15, command=self.show_blocks).grid(row=1, column=1)

        
        self.output = tk.Text(root, height=18, width=95, font=("Consolas", 11))
        self.output.pack(pady=20)

    # ---------------- Actions -------------------

    def create_file(self):
        name = simpledialog.askstring("Create File", "Enter filename:")
        size = simpledialog.askinteger("Size", "Enter size in KB:")

        msg = self.fs.create_file(name, size)
        self.output.insert(tk.END, msg + "\n")

    def delete_file(self):
        name = simpledialog.askstring("Delete File", "Enter filename:")
        msg = self.fs.delete_file(name)
        self.output.insert(tk.END, msg + "\n")

    def write_file(self):
        name = simpledialog.askstring("Write", "Filename:")
        content = simpledialog.askstring("Content", "Enter file content:")
        msg = self.fs.write_file(name, content)
        self.output.insert(tk.END, msg + "\n")

    def read_file(self):
        name = simpledialog.askstring("Read", "Filename:")
        data = self.fs.read_file(name)
        self.output.insert(tk.END, f"Content: {data}\n")

    def show_inode(self):
        table = self.fs.get_inode_table()
        self.output.insert(tk.END, "\nINODE TABLE:\n")
        self.output.insert(tk.END, "-" * 70 + "\n")
        for row in table:
            self.output.insert(tk.END, f"Name: {row[0]}  | Size: {row[1]} | Index: {row[2]} | Blocks: {row[3]}\n")
        self.output.insert(tk.END, "-" * 70 + "\n")

    def show_blocks(self):
        self.output.insert(tk.END, "\nFREE BLOCKS STATUS:\n")
        for i in range(0, TOTAL_BLOCKS, 8):
            chunk = self.fs.free_blocks[i:i+8]
            text = " ".join(["F" if b else "A" for b in chunk])
            self.output.insert(tk.END, f"Blocks {i:02d}-{i+7:02d}:  {text}\n")


root = tk.Tk()
app = FileSystemGUI(root)
root.mainloop()
