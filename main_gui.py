import tkinter as tk
from tkinter import messagebox, filedialog, ttk
import customtkinter as ctk
import os


def clear_window():
    """Helper function to clear all widgets in the window"""
    for widget in root.winfo_children():
        widget.destroy()

def show_main_menu():
    """Displays the main menu with script selection buttons"""
    clear_window()

    # Main menu buttons to select scripts
    menu_label = tk.Label(root, text="Select a Script to Run", font=('Helvetica', 20))
    menu_label.pack(pady=20)
    
    button_1 = ttk.Button(root, text="Run Script 1", command=run_script_1)
    button_1.pack(pady=10)
    
    button_2 = ttk.Button(root, text="Template for sript button", command=run_script_template)
    button_2.pack(pady=10)

    quit_button = ttk.Button(root, text="quit", command=lambda: root.destroy())
    quit_button.pack(side='bottom', pady=10, fill='x')


def run_script_template():
    """Replaces window content with Script 1 specific interface"""
    clear_window()

    # Script 1 UI
    script_label = tk.Label(root, text="Script 1", font=('Helvetica', 16))
    script_label.pack(pady=10)
    
    arg_label = tk.Label(root, text="Enter argument for script 1:")
    arg_label.pack(pady=10)
    
    arg_entry = ttk.Entry(root)
    arg_entry.pack(pady=10)
    
    def execute_script_1():
        argument1 = arg_entry.get()
        # Execute the script here (replace with actual call)
        # os.system(f"python script1.py {argument}")
        messagebox.showinfo("Script 1 Result", f"Running script 1 with argument: {argument1}")

    run_button = tk.Button(root, text="Run Script 1", command=execute_script_1)
    run_button.pack(pady=10)

    back_button = tk.Button(root, text="Back to Main Menu", command=show_main_menu)
    back_button.pack(side='bottom', pady=10, fill='x')

def run_script_1():
    """Replaces window content with Script 1 specific interface"""
    clear_window()

    # Script 1 UI
    script_label = tk.Label(root, text="Script 1", font=('Helvetica', 16))
    script_label.pack(pady=10)
    
    arg_label = tk.Label(root, text="Select input file: ")
    arg_label.pack(pady=10)

    #Function to find the file.
    def browse_files(input_file, select_type='file'):
        if select_type == 'file':
            filename = filedialog.askopenfilename(title='Select a File',
                                                filetypes=(('Text files', '*.pdf*'), ('all files', '*.*'))
                                                )
        
        elif select_type == 'folder':
            filename = filedialog.askdirectory(title='Select a folder')

        if filename:
            input_file.config(text=filename)
    
    #File 1
    selected_input_file = tk.Label(root, text='No file selected')
    selected_input_file.pack(pady=10)

    browse_button = ttk.Button(root, text='Browse files', command= lambda: browse_files(selected_input_file))
    browse_button.pack(pady=10)

    #File 2
    arg_label2 = tk.Label(root, text="Select input file: ")
    arg_label2.pack(pady=10)

    selected_input_file2 = tk.Label(root, text='No file selected')
    selected_input_file2.pack(pady=10)

    browse_button2 = ttk.Button(root, text='Browse folders', command= lambda: browse_files(selected_input_file2, select_type='folder'))
    browse_button2.pack(pady=10)
    
    
    #Now executing the script
    def execute_script_1():
        file_path_1 = selected_input_file.cget("text") 
        file_path_2 = selected_input_file2.cget("text")
        
        os.system(f"python pdf_2_markdown/pdf_2_markdown.py {file_path_1} {file_path_2}")
        messagebox.showinfo("Pdf converted to markdown", f"File can be found in: {file_path_2}")

    
    
    run_button = tk.Button(root, text="Run Script 1", command=execute_script_1)
    run_button.pack(pady=10)

    back_button = tk.Button(root, text="Back to Main Menu", command=show_main_menu)
    back_button.pack(side='bottom', pady=10, fill='x')

# Main window setup
root = tk.Tk()
root.geometry("800x800")
root.title("Script Runner")
style = ttk.Style()
style.theme_use('clam')

# Start by showing the main menu
show_main_menu()

# Start the Tkinter event loop
root.mainloop()
