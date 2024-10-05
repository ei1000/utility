import tkinter as tk
import customtkinter as ctk
import os




class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Script Runner")
        self.geometry("800x600")

        # Container to hold all frames
        container = ctk.CTkFrame(self)
        container.pack(fill="both", expand=True)

        self.frames = {}

        # Initialize the frames and store them in a dictionary
        for F in (MainMenu, Pdf2Markdown, ScriptTemplate):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        # Show the main menu initially
        self.show_frame(MainMenu)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

# Main Menu Frame
class MainMenu(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        
        label = ctk.CTkLabel(self, text="Main Menu", font=('Helvetica', 20))
        label.pack(pady=20)
        
        button1 = ctk.CTkButton(self, text="Run Script 1", 
                                command=lambda: controller.show_frame(Pdf2Markdown))
        button1.pack(pady=10)
        
        button2 = ctk.CTkButton(self, text="Run Script Template", 
                                command=lambda: controller.show_frame(ScriptTemplate))
        button2.pack(pady=10)
        
        quit_button = ctk.CTkButton(self, text="Quit", command=controller.quit)
        quit_button.pack(pady=10)

# Script 1 Frame
class Pdf2Markdown(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        # Script 1 UI
        script_label = ctk.CTkLabel(self, text="Script 1", font=('Helvetica', 20))
        script_label.pack(pady=10)
        
        arg_label = ctk.CTkLabel(self, text="Select input file: ")
        arg_label.pack(pady=10)

        # File 1 selection
        self.selected_input_file = ctk.CTkLabel(self, text='No file selected')
        self.selected_input_file.pack(pady=10)

        browse_button = ctk.CTkButton(self, text='Browse files', command=lambda: self.browse_files(self.selected_input_file))
        browse_button.pack(pady=10)

        # File 2 selection
        arg_label2 = ctk.CTkLabel(self, text="Select input folder: ")
        arg_label2.pack(pady=10)

        self.selected_input_file2 = ctk.CTkLabel(self, text='No folder selected')
        self.selected_input_file2.pack(pady=10)

        browse_button2 = ctk.CTkButton(self, text='Browse folders', command=lambda: self.browse_files(self.selected_input_file2, select_type='folder'))
        browse_button2.pack(pady=10)

        # Run script button
        run_button = ctk.CTkButton(self, text="Run Script 1", command=self.execute_script_1)
        run_button.pack(pady=10)

        # Back to main menu button
        back_button = ctk.CTkButton(self, text="Back to Main Menu", command=lambda: controller.show_frame(MainMenu))
        back_button.pack(side='bottom', pady=10, fill='x')

    def browse_files(self, input_file_label, select_type='file'):
        """Handles file/folder browsing and updates the label"""
        if select_type == 'file':
            filename = ctk.filedialog.askopenfilename(title='Select a File',
                                                  filetypes=(('PDF files', '*.pdf*'), ('all files', '*.*')))
        elif select_type == 'folder':
            filename = ctk.filedialog.askdirectory(title='Select a folder')

        if filename:
            input_file_label.configure(text=filename)
    
    def execute_script_1(self):
        """Executes the script with the selected file and folder"""
        file_path_1 = self.selected_input_file.cget("text") 
        file_path_2 = self.selected_input_file2.cget("text")
        
        if file_path_1 == 'No file selected' or file_path_2 == 'No folder selected':
            tk.messagebox.showwarning("Warning", "Please select both a file and a folder.")
        else:
            # Run the external script (replace this with your own script path)
            os.system(f"python pdf_2_markdown/pdf_2_markdown.py {file_path_1} {file_path_2}")
            tk.messagebox.showinfo("Pdf converted to markdown", f"File can be found in: {file_path_2}")

# Script Template Frame
class ScriptTemplate(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        label = ctk.CTkLabel(self, text="Script Template", font=('Helvetica', 20))
        label.pack(pady=20)

        browse_button = ctk.CTkButton(self, text="Browse Files", command=self.browse_files)
        browse_button.pack(pady=10)
        
        back_button = ctk.CTkButton(self, text="Back to Main Menu", 
                                    command=lambda: controller.show_frame(MainMenu))
        back_button.pack(pady=10)

    def browse_files(self):
        filename = tk.filedialog.askopenfilename(title="Select a File")
        if filename:
            tk.messagebox.showinfo("Selected File", f"File: {filename}")

if __name__ == "__main__":
    app = App()
    app.mainloop()
