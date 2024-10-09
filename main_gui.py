import tkinter as tk
import customtkinter as ctk
import os
from pdf_2_markdown.pd2markdown_class import Pdf2Markdown
from algorithms.classes import RotateList

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("green")

#The main application class
class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        #Title to running program
        self.title("Utilities")

        #Set screen to be 70% of the users screen.
        screen_width = int(self.winfo_screenwidth() *0.7)
        screen_height = int(self.winfo_screenheight() *0.7)
        self.geometry(f"{screen_width}x{screen_height}")

        # Container to hold all frames
        container = ctk.CTkFrame(self)
        container.pack(fill="both", expand=True)

        #Add the script classes here in list below and it will generate dictionaries
        self.frame_classes= [MainMenu, Pdf2Markdown, RotateList] + [ScriptTemplate]
        self.frame_classes= {F.__name__: F for F in self.frame_classes}

        self.frames = {}
        # Initialize the frames and store them in a dictionary
        for frame_name, F in self.frame_classes.items():
            frame = F(container, self)
            self.frames[frame_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        #Center grid
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        
        #Show the main menu on startup
        self.show_frame('MainMenu')

        
    #Function to switch frame based on frame_name
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

# Main Menu Frame
class MainMenu(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        
        #Text and buttons for 
        label = ctk.CTkLabel(self, text="Main Menu", font=('Helvetica', 20))
        label.pack(pady=20, anchor='center')

        #Creating a button for every script
        for frame_name in list(controller.frame_classes.keys())[1:]:
            button = ctk.CTkButton(self, text=f'{frame_name}', 
                                    command=lambda frame_name=frame_name: controller.show_frame(frame_name))
            button.pack(pady=10, anchor='center')
        
        #Quit button
        quit_button = ctk.CTkButton(self, text="Quit", command=controller.quit, fg_color='#C3423F', hover_color='#8E2E2C')
        quit_button.place(relx=0.5, rely=1, anchor='s', y=-20)



# Script Template Frame for later expansion
class ScriptTemplate(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        #Top text
        label = ctk.CTkLabel(self, text="Script Template", font=('Helvetica', 20))
        label.pack(pady=20)
        
        #TODO logic goes here:


        # Run script button
        run_button = ctk.CTkButton(self, text="Run Script", command=self.execute_script)
        run_button.pack(pady=10)

        #Back button
        back_button = ctk.CTkButton(self, text="Back to Main Menu", 
                                    command=lambda: controller.show_frame('MainMenu'))
        back_button.pack(side='bottom', pady=20, fill='x')
    
    #Executing the script
    def execute_script(self):
        pass


#Make the program run when called. Start the loop.
if __name__ == "__main__":
    app = App()
    app.mainloop()
