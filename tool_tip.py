
try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk
 
import time
    
class CreateToolTip(object):

    def __init__(self, widget, text='widget info'):
        self.widget = widget
        self.text = text
        self.widget.bind("<Enter>", self.enter)
        self.widget.bind("<Leave>", self.close)
        
    def enter(self, event=None):
        x = y = 0
        x, y, cx, cy = self.widget.bbox("insert")
        x += self.widget.winfo_rootx() + 20
        y += self.widget.winfo_rooty() + 38
        #================ creates a toplevel window===================#
        self.tw = tk.Toplevel(self.widget)
        #=================== Leaves only the label and removes the app window====================
        self.tw.wm_overrideredirect(True)
        self.tw.wm_geometry("+%d+%d" % (x, y))
#        time.sleep(.5)
        label = tk.Label(self.tw, text=self.text, justify='left',foreground="grey20",pady=1,
                             background='#f9fafc', relief="solid", borderwidth=1,highlightthickness=1,
                                 font=("Courier New ", "9", "normal"))
        label.pack(ipadx=2)
        
        
    def close(self, event=None):
        if self.tw:
            self.tw.destroy()
            
            
## testing ...
#if __name__ == '__main__':
#    root = tk.Tk()
#    btn1 = tk.Button(root, text="button 1")
#    btn1.pack(padx=10, pady=5)
#    button1_ttp = CreateToolTip(btn1, "mouse is over button 1")
#    btn2 = tk.Button(root, text="button 2")
#    btn2.pack(padx=10, pady=5)
#    button2_ttp = CreateToolTip(btn2, "mouse is over button 2")
#    root.mainloop()