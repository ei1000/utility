import customtkinter as ctk
import tkinter as tk
import os

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

        #Output label
        self.output_label = ctk.CTkLabel(self, text='')
        self.output_label.pack(pady=50)

        # Back to main menu button
        back_button = ctk.CTkButton(self, text="Back to Main Menu", command=lambda: controller.show_frame('MainMenu'))
        back_button.pack(side='bottom', pady=20, fill='x')

    def browse_files(self, input_file_label, select_type='file'):
        
        #If we want to find a file then it needs to be a pdf. Else if it is a folder just select a folder
        if select_type == 'file':
            filename = ctk.filedialog.askopenfilename(title='Select a File',
                                                  filetypes=(('PDF files', '*.pdf*'), ('all files', '*.*')))
        elif select_type == 'folder':
            filename = ctk.filedialog.askdirectory(title='Select a folder')

        #If a file was chosen, here is the path
        if filename:
            input_file_label.configure(text=filename)
    
    #Executing the script
    def execute_script_1(self):
        #The paths
        file_path_1 = self.selected_input_file.cget("text") 
        file_path_2 = self.selected_input_file2.cget("text")
        
        #A check incase only one is selected
        if file_path_1 == 'No file selected' or file_path_2 == 'No folder selected':
            tk.messagebox.showwarning("Warning", "Please select both a file and a folder.")
        
        #Run the script in the terminal and then give a pop-up for the user
        #Not decided if I want to keep using terminal here or just import the function instead.
        else:
            os.system(f"python pdf_2_markdown/pdf_2_markdown.py {file_path_1} {file_path_2}")
            self.output_label.configure(text=f"Pdf converted to markdown!\n\nFile can be found in: {file_path_2}", height=40, width=40)