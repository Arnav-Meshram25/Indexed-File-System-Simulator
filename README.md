🟦 Indexed File System Simulator

A GUI-based simulation of Indexed File Allocation using Python and Tkinter.

🚀 How to Run the Project

Follow these simple steps to run the simulator.

1️⃣ Install Python

Check if Python is already installed:

python --version


If not installed, download from:
https://www.python.org/downloads/

2️⃣ Download or Clone the Repository
Option A — Download ZIP

Click Code → Download ZIP

Extract the ZIP

Option B — Clone using Git
git clone https://github.com/<your-username>/<your-repo>.git

3️⃣ Move into the Project Folder
cd <your-repo>

4️⃣ Install Tkinter if required

Most Windows/Mac systems already have Tkinter.

For Ubuntu/Linux:

sudo apt-get install python3-tk

5️⃣ Run the Program
python fileSystem.py


(or on some systems)

python3 fileSystem.py


A GUI window will open automatically.

📌 Project Overview

This project simulates an Indexed File Allocation File System, a classic OS concept used to understand how files are stored on disk using index blocks.

The simulator provides:

A visual and interactive interface

File creation

File deletion

File writing

File reading

Inode table display

Free block status view

🧠 Key OS Concepts Implemented
1️⃣ Indexed Allocation

Each file has:

1 index block

Several data blocks depending on file size

The index block contains pointers to all the allocated data blocks.

2️⃣ Disk Representation

Total Blocks → 64

Block Size → 4096 bytes (4 KB)

A simple free/allocated block bitmap is maintained

3️⃣ Inode Table

Stores:

File name

File size

Index block number

List of data blocks

4️⃣ Free Space Management

A boolean array tracks:

True → Free

False → Allocated
