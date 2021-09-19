import sys

import tkinter as tk
import tkinter.ttk as ttk

from chart_rip import get_week
import view_support

# Execution starts here !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
def vp_start_gui():
    url = 'https://www.billboard.com/charts/hot-100' # this sample dos not support chart choosing, only Hot-100 is used
    d = get_week(url)   # get the chart

    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = Toplevel1 (top=root, dict=d) # creates the static components in the page
    view_support.init(top=root, gui=top, dict=d) # creates the dynamic components in the page
    root.mainloop()

w = None

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None

# Creates all the static elements in the window
class Toplevel1:
    def __init__(self, dict, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # Xcolor: 'gray85'
        _fgcolor = '#000000'  # Xcolor: 'black'
        _compcolor = '#d9d9d9' # Xcolor: 'gray85'
        _ana1color = '#d9d9d9' # Xcolor: 'gray85'
        _ana2color = '#ececec' # Closest Xcolor: 'gray92'
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("1563x722+0+0")
        top.minsize(148, 1)
        top.maxsize(1400, 1055)
        top.resizable(1, 1)
        top.title("Billboard Hot 100 Songs of the Week")
        top.configure(background="#d9d9d9")

        self.chartL = tk.Label(top) # chart label
        self.chartL.place(relx=0.023, rely=0.028, height=26, width=82)
        self.chartL.configure(background="#d9d9d9")
        self.chartL.configure(disabledforeground="#a3a3a3")
        self.chartL.configure(foreground="#000000")
        self.chartL.configure(text='''Chart:''')

        self.dateL = tk.Label(top)  # chart date label
        self.dateL.place(relx=0.385, rely=0.028, height=26, width=74)
        self.dateL.configure(background="#d9d9d9")
        self.dateL.configure(disabledforeground="#a3a3a3")
        self.dateL.configure(foreground="#000000")
        self.dateL.configure(text='''Date:''')

        self.TSeparator3 = ttk.Separator(top)
        self.TSeparator3.place(relx=0.0, rely=0.083, relwidth=1.017)
        self.TSeparator3.configure(takefocus="0")

        self.menubar = tk.Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)

        self.TSeparator4 = ttk.Separator(top)
        self.TSeparator4.place(relx=0.838, rely=0.083, relheight=0.928)
        self.TSeparator4.configure(orient="vertical")
        self.TSeparator4.configure(takefocus="0")    

        # refresh button, executes the refresh function in view_support.py
        self.refresh = tk.Button(top, command=view_support.refresh) 
        self.refresh.place(relx=0.874, rely=0.333, height=33, width=116)
        self.refresh.configure(activebackground="#ececec")
        self.refresh.configure(activeforeground="#000000")
        self.refresh.configure(background="#d9d9d9")
        self.refresh.configure(disabledforeground="#a3a3a3")
        self.refresh.configure(foreground="#000000")
        self.refresh.configure(highlightbackground="#d9d9d9")
        self.refresh.configure(highlightcolor="black")
        self.refresh.configure(pady="0")
        self.refresh.configure(text='''Refresh''')        

        ''' save to json button, executes the save_week function in view_support.py
        save_week's first parameter is the json, the second is the file name (here it is the chart's date)
        '''
        self.save = tk.Button(top, command=(lambda: view_support.save_week(dict, dict['date'] + ".json"))) 
        self.save.place(relx=0.874, rely=0.444, height=33, width=116)
        self.save.configure(activebackground="#ececec")
        self.save.configure(activeforeground="#000000")
        self.save.configure(background="#d9d9d9")
        self.save.configure(disabledforeground="#a3a3a3")
        self.save.configure(foreground="#000000")
        self.save.configure(highlightbackground="#d9d9d9")
        self.save.configure(highlightcolor="black")
        self.save.configure(pady="0")
        self.save.configure(text='''Save json''')

        self.Frame3 = tk.Frame(top)
        self.Frame3.place(relx=0.027, rely=0.111, relheight=0.838, relwidth=0.804)
        self.Frame3.configure(relief='groove')
        self.Frame3.configure(borderwidth="2")
        self.Frame3.configure(relief="groove")
        self.Frame3.configure(background="#d9d9d9")

        # arrow up/down images
        global up, down
        up =  tk.PhotoImage(file="sup.png")
        down = tk.PhotoImage(file="sdown.png")

        self.posBF = tk.Frame(self.Frame3)
        self.posBF.place(relx=0.005, rely=0.017, height=40, width=130) 
        
        self.posT = tk.Label(self.posBF)
        self.posT.place(relx=0.0, rely=0.017, height=40, width=45)
        self.posT.configure(text='''Position''')
        self.posBU = ttk.Button(self.posBF, command=(lambda: view_support.order('pos', False)))
        self.posBU.place(relx=0.4, rely=0.2, height=25, width=35)
        self.posBU.configure(image=up)
        self.posBD = ttk.Button(self.posBF, command=(lambda: view_support.order('pos', True)))
        self.posBD.place(relx=0.70, rely=0.2, height=25, width=35)
        self.posBD.configure(image=down)

        self.artistBF = tk.Frame(self.Frame3)
        self.artistBF.place(relx=0.150, rely=0.017, height=40, width=238)   
        
        self.artistT = tk.Label(self.artistBF)
        self.artistT.place(relx=0.2, rely=0.017, height=40, width=30)
        self.artistT.configure(text='''Artist''')
        self.artistBU = ttk.Button(self.artistBF, command=(lambda: view_support.order('artist', False)))
        self.artistBU.place(relx=0.4, rely=0.2, height=25, width=35)
        self.artistBU.configure(image=up)
        self.artistBD = ttk.Button(self.artistBF, command=(lambda: view_support.order('artist', True)))
        self.artistBD.place(relx=0.65, rely=0.2, height=25, width=35)
        self.artistBD.configure(image=down)

        self.titleBF = tk.Frame(self.Frame3)
        self.titleBF.place(relx=0.450, rely=0.017, height=40, width=168)   
        
        self.titleT = tk.Label(self.titleBF)
        self.titleT.place(relx=0.2, rely=0.017, height=40, width=30)
        self.titleT.configure(text='''Title''')
        self.titleBU = ttk.Button(self.titleBF, command=(lambda: view_support.order('title', False)))
        self.titleBU.place(relx=0.4, rely=0.2, height=25, width=35)
        self.titleBU.configure(image=up)
        self.titleBD = ttk.Button(self.titleBF, command=(lambda: view_support.order('title', True)))
        self.titleBD.place(relx=0.65, rely=0.2, height=25, width=35)
        self.titleBD.configure(image=down)


        peakL = tk.Label(self.Frame3)
        peakL.place(relx=0.650, rely=0.017, height=37, width=74)
        peakL.configure(background="#d9d9d9")
        peakL.configure(disabledforeground="#a3a3a3")
        peakL.configure(foreground="#000000")
        peakL.configure(text='''Peak''')

        weeksL = tk.Label(self.Frame3)
        weeksL.place(relx=0.720, rely=0.017, height=37, width=116)
        weeksL.configure(background="#d9d9d9")
        weeksL.configure(disabledforeground="#a3a3a3")
        weeksL.configure(foreground="#000000")
        weeksL.configure(text='''Weeks''')

        trendL = tk.Label(self.Frame3)
        trendL.place(relx=0.810, rely=0.017, height=37, width=75)
        trendL.configure(background="#d9d9d9")
        trendL.configure(disabledforeground="#a3a3a3")
        trendL.configure(foreground="#000000")
        trendL.configure(text='''Trend''')

        playL = tk.Label(self.Frame3)
        playL.place(relx=0.890, rely=0.017, height=37, width=75)
        playL.configure(background="#d9d9d9")
        playL.configure(disabledforeground="#a3a3a3")
        playL.configure(foreground="#000000")
        playL.configure(text='''Play''')

        self.TSeparator1 = ttk.Separator(self.Frame3)
        self.TSeparator1.place(relx=-0.002, rely=0.094, relwidth=1.015)
        self.TSeparator1.configure(cursor="fleur")

        self.Scrolledwindow1 = ScrolledWindow(self.Frame3)
        self.Scrolledwindow1.place(relx=0.0, rely=0.099, relheight=0.904, relwidth=0.992)
        self.Scrolledwindow1.configure(background="white")
        self.Scrolledwindow1.configure(borderwidth="2")
        self.Scrolledwindow1.configure(highlightbackground="wheat")
        self.Scrolledwindow1.configure(relief="groove")
        self.Scrolledwindow1.configure(selectbackground="#ddc8a1")
        self.color = self.Scrolledwindow1.cget("background")
        self.Scrolledwindow1_f = tk.Frame(self.Scrolledwindow1,
                            background=self.color)
        self.Scrolledwindow1.create_window(0, 0, anchor='nw',
                                           window=self.Scrolledwindow1_f)    


# Everything below is unimportant GUI stuff !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# The following code is added to facilitate the Scrolled widgets you specified.
class AutoScroll(object):
    '''Configure the scrollbars for a widget.'''
    def __init__(self, master):
        #  Rozen. Added the try-except clauses so that this class
        #  could be used for scrolled entry widget for which vertical
        #  scrolling is not supported. 5/7/14.
        try:
            vsb = ttk.Scrollbar(master, orient='vertical', command=self.yview)
        except:
            pass
        hsb = ttk.Scrollbar(master, orient='horizontal', command=self.xview)
        try:
            self.configure(yscrollcommand=self._autoscroll(vsb))
        except:
            pass
        self.configure(xscrollcommand=self._autoscroll(hsb))
        self.grid(column=0, row=0, sticky='nsew')
        try:
            vsb.grid(column=1, row=0, sticky='ns')
        except:
            pass
        hsb.grid(column=0, row=1, sticky='ew')
        master.grid_columnconfigure(0, weight=1)
        master.grid_rowconfigure(0, weight=1)

        # Copy geometry methods of master  (taken from ScrolledText.py)
        methods = tk.Pack.__dict__.keys() | tk.Grid.__dict__.keys() \
                | tk.Place.__dict__.keys()

        for meth in methods:
            if meth[0] != '_' and meth not in ('config', 'configure'):
                setattr(self, meth, getattr(master, meth))

    @staticmethod
    def _autoscroll(sbar):
        '''Hide and show scrollbar as needed.'''
        def wrapped(first, last):
            first, last = float(first), float(last)
            if first <= 0 and last >= 1:
                sbar.grid_remove()
            else:
                sbar.grid()
            sbar.set(first, last)
        return wrapped

    def __str__(self):
        return str(self.master)

def _create_container(func):
    '''Creates a ttk Frame with a given master, and use this view frame to
    place the scrollbars and the widget.'''
    def wrapped(cls, master, **kw):
        container = ttk.Frame(master)
        container.bind('<Enter>', lambda e: _bound_to_mousewheel(e, container))
        container.bind('<Leave>', lambda e: _unbound_to_mousewheel(e, container))
        return func(cls, container, **kw)
    return wrapped

class ScrolledWindow(AutoScroll, tk.Canvas):
    '''A standard Tkinter Canvas widget with scrollbars that will
    automatically show/hide as needed.'''
    @_create_container
    def __init__(self, master, **kw):
        tk.Canvas.__init__(self, master, **kw)
        AutoScroll.__init__(self, master)

import platform
def _bound_to_mousewheel(event, widget):
    child = widget.winfo_children()[0]
    if platform.system() == 'Windows' or platform.system() == 'Darwin':
        child.bind_all('<MouseWheel>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Shift-MouseWheel>', lambda e: _on_shiftmouse(e, child))
    else:
        child.bind_all('<Button-4>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Button-5>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Shift-Button-4>', lambda e: _on_shiftmouse(e, child))
        child.bind_all('<Shift-Button-5>', lambda e: _on_shiftmouse(e, child))

def _unbound_to_mousewheel(event, widget):
    if platform.system() == 'Windows' or platform.system() == 'Darwin':
        widget.unbind_all('<MouseWheel>')
        widget.unbind_all('<Shift-MouseWheel>')
    else:
        widget.unbind_all('<Button-4>')
        widget.unbind_all('<Button-5>')
        widget.unbind_all('<Shift-Button-4>')
        widget.unbind_all('<Shift-Button-5>')

def _on_mousewheel(event, widget):
    if platform.system() == 'Windows':
        widget.yview_scroll(-1*int(event.delta/120),'units')
    elif platform.system() == 'Darwin':
        widget.yview_scroll(-1*int(event.delta),'units')
    else:
        if event.num == 4:
            widget.yview_scroll(-1, 'units')
        elif event.num == 5:
            widget.yview_scroll(1, 'units')

def _on_shiftmouse(event, widget):
    if platform.system() == 'Windows':
        widget.xview_scroll(-1*int(event.delta/120), 'units')
    elif platform.system() == 'Darwin':
        widget.xview_scroll(-1*int(event.delta), 'units')
    else:
        if event.num == 4:
            widget.xview_scroll(-1, 'units')
        elif event.num == 5:
            widget.xview_scroll(1, 'units')

if __name__ == '__main__':
    vp_start_gui()





