import sys, json, threading
import webbrowser

from youtube_search import YoutubeSearch
from chart_rip import get_week

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

def on_btnExit():
    sys.exit()

def quit():
    sys.exit()

def refresh():
    '''
    Refreshes the window by rescrapping the chart
    '''
    clean_window()

    url = 'https://www.billboard.com/charts/hot-100' # only support for Hot-100
    d = get_week(url)
    display_header(d)
    display_list(d)

def save_week(data, filename):
    """Writes a json chart to a file.
     When adding support for multiple charts, 
     a file named with the chart's name must be
     create if it does not exist and the chart json
     saved in there.

    Args:
        data (json): the json to write to the file
        filename (string): the file name to write to
    """        
    with open(filename, 'w') as f:
        json.dump(data, f, sort_keys=False, indent=4, separators=(',', ': '))

w = 3
subFrames = []

def init(top, gui, dict, *args, **kwargs):
    '''
    Creates the dynamic components of the window.
    '''
    global w, top_level, root
    w = gui
    top_level = top
    root = top
    display_header(dict) # display the header (chart name and date)
    display_list(dict) # display the list of songs

def display_header(dict):
    '''
    Display the header (chart name and date)
    '''
    w.date = tk.Label(root)
    w.date.place(relx=0.422, rely=0.028, height=26, width=580)
    w.date.configure(background="#ffffff")
    w.date.configure(disabledforeground="#a3a3a3")
    w.date.configure(foreground="#000000")
    w.date.configure(text=dict['date'])

    w.chart = tk.Label(root)
    w.chart.place(relx=0.064, rely=0.028, height=26, width=442)
    w.chart.configure(background="#ffffff")
    w.chart.configure(disabledforeground="#a3a3a3")
    w.chart.configure(foreground="#000000")
    w.chart.configure(text=dict['code'])

def order(key, desc):
    '''
    Sorting function.
    key is the sortable attribute ('pos' (position), 'artist', and 'title'/
    desc: true if sort descending, false if sort ascending
    '''

    backC = '' # background color
    gray = '#d9d9d9'
    white = '#ffffff'

    global subFrames
    
    # sort the list of songs
    subFrames = sorted(subFrames, key=(lambda k: int(k[key]) if key == 'pos' else (k[key]).lower()), reverse=desc) 
    
    i = 0
    for fr in subFrames:
        
        # alternate background color between white and gray
        if i % 2 == 0:
            backC = white
        else:
            backC = gray

        fr['f'].configure(background=backC)
        fr['f'].grid(row=i) # change the song's positoin in the list

        # assign background color to list elements
        children = (fr['f']).winfo_children()
        for child in children:            
            if child.winfo_class() == 'Label':
                child.configure(background=backC)
        i += 1

def play_on_youtube(search):
    'Opens the first youtube video found when putting the search string as a youtube search'
    ythome = 'https://www.youtube.com'
    result = []    

    while not result: # module sometimes returns empty result for some reason
        result = YoutubeSearch(search, max_results=1).to_dict() # get the result of the search
    webbrowser.open_new_tab(ythome + result[0]['link']) # open in on youtube

def display_list(dict):
   '''
   Display the list
   '''
   inner_frame = w.Scrolledwindow1_f

   gray = '#d9d9d9'
   white = '#ffffff'
   photo_location = "yicon.png"
   
   # the youtube icon
   global _img0
   _img0 = tk.PhotoImage(file=photo_location)

   global subFrames
   subFrames = []
   i = 0

   for row in dict['chartRows']:
            
       # alternate background color between white and gray
        backC = ''
        if i % 2 == 0:
            backC = white
        else:
            backC = gray
        
        subFrames.append({'f': tk.Frame(inner_frame, width=1085, height=50), 'pos': row['tw'], 'artist': row['artist'], 'title':row['title']})
        subFrames[i]['f'].grid(row=i)        
        subFrames[i]['f'].configure(relief='groove')        
        subFrames[i]['f'].configure(borderwidth="2")        
        subFrames[i]['f'].configure(background=backC)        

        sep1 = ttk.Separator(subFrames[i]['f'])
        sep1.place(relx=0.122, rely=0.0, relheight=1.067)
        sep1.configure(orient="vertical")
        sep1.configure(takefocus="0")

        sep2 = ttk.Separator(subFrames[i]['f'])
        sep2.place(relx=0.416, rely=0.0, relheight=1.067)
        sep2.configure(orient="vertical")
        sep2.configure(takefocus="0")

        sep3 = ttk.Separator(subFrames[i]['f'])
        sep3.place(relx=0.660, rely=-0.222, relheight=1.289)
        sep3.configure(orient="vertical")
        sep3.configure(takefocus="0")

        sep4 = ttk.Separator(subFrames[i]['f'])
        sep4.place(relx=0.751, rely=0.0, relheight=1.067)
        sep4.configure(orient="vertical")
        sep4.configure(takefocus="0")

        sep5 = ttk.Separator(subFrames[i]['f'])
        sep5.place(relx=0.832, rely=-0.178, relheight=1.289)
        sep5.configure(orient="vertical")
        sep5.configure(takefocus="0")

        sep6 = ttk.Separator(subFrames[i]['f'])
        sep6.place(relx=0.895, rely=-0.178, relheight=1.289)
        sep6.configure(orient="vertical")
        sep6.configure(takefocus="0")        

        position = tk.Label(subFrames[i]['f'])
        position.place(relx=0.023, rely=0.222, height=26, width=50)
        position.configure(background=backC)
        position.configure(disabledforeground="#a3a3a3")
        position.configure(foreground="#000000")
        position.configure(text=row['tw'])

        artist = tk.Label(subFrames[i]['f'])
        artist.place(relx=0.124, rely=0.222, height=26, width=310)
        artist.configure(background=backC)
        artist.configure(disabledforeground="#a3a3a3")
        artist.configure(foreground="#000000")
        artist.configure(text=row['artist'])

        title = tk.Label(subFrames[i]['f'])
        title.place(relx=0.440, rely=0.222, height=26, width=220)
        title.configure(background=backC)
        title.configure(disabledforeground="#a3a3a3")
        title.configure(foreground="#000000")
        title.configure(text=row['title'])

        peak = tk.Label(subFrames[i]['f'])
        peak.place(relx=0.680, rely=0.222, height=26, width=50)
        peak.configure(background=backC)
        peak.configure(disabledforeground="#a3a3a3")
        peak.configure(foreground="#000000")
        peak.configure(text=row['peak'])

        weeks = tk.Label(subFrames[i]['f'])
        weeks.place(relx=0.763, rely=0.222, height=26, width=50)
        weeks.configure(background=backC)
        weeks.configure(disabledforeground="#a3a3a3")
        weeks.configure(foreground="#000000")
        weeks.configure(text=row['wc'])

        trend = tk.Label(subFrames[i]['f'])
        trend.place(relx=0.842, rely=0.222, height=26, width=50)
        trend.configure(background=backC)
        trend.configure(disabledforeground="#a3a3a3")
        trend.configure(foreground="#000000")
        trend.configure(text=row['trend'])

        search = row['artist'] + " " + row['title'] # use the artist and title to search on youtube        

        # youtube play button, use a Thread to keep the rest of the window responsive when pressing the button
        yPlay = ttk.Button(subFrames[i]['f'], command=(lambda search=search: threading.Thread(target=play_on_youtube, kwargs={'search': search}).start()))
        yPlay.place(relx=0.907, rely=0.01, height=40, width=100)
        yPlay.configure(takefocus="")
        yPlay.configure(image=_img0)
        
        i += 1
   # Magic which ties widget scrollbars to dimensions of the inner_frame.
   subFrames[0]['f'].wait_visibility()
   bbox = inner_frame.bbox()
   w.Scrolledwindow1.configure(scrollregion=bbox)   

# End of important stuff !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

def clean_window():
    global subFrames

    try:
        w.date.destroy()
        w.chart.destroy()
    except:
        pass

    for fr in subFrames:
        try:
            fr['f'].destroy()            
        except:
            pass

def destroy_window():
    # Function which closes the window.
    global top_level
    top_level.destroy()
    top_level = None

if __name__ == '__main__':
    import view
    view.vp_start_gui()





