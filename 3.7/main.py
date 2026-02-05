import tkinter as tk
import ui      
import logic   

def main():
    
    root = tk.Tk() 
    app = ui.MainWindow(root, logic.process_text) 
    root.mainloop()

if __name__ == "__main__":
    main()
