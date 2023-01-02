import turtle
import random
import time
import os 
import tkinter as tk
 
# Αρχικές Τιμές παραμέτρων εμφάνισης 
 
n = 50              # πλήθος στοιχειων
maxint = 500        # ευρος τιμών δειγματος [1, maxint] 
DELAY = 0.00        # καθυστέρηση στο σχεδιασμό γραφικών
SPEED = 1           # ταχυτητα σχεδίασης
COLOR0 = "lightcyan"# Χρώμα αταξινόμητων στοιχειων
COLOR1 = "tomato"   # χρώμα στοιχειου προς ταξινόμηση
COLOR2 = "yellow"   # χρώμα στοιχειων που μετακινούνται δεξιά
COLOR3 = "turquoise"# χρώμα ταξινομηξμένων
TXTCOLOR = "white"   # χρώμα γραμμάτων και περιγράμματος
LINECOLOR = "blue"  # χρώμα  περιγράμματος
BGCOLOR = "black"   # χρώμα backgound
SCREENX = 1225      # πλάτος οθόνης 
SCREENY = 600       # μήκος οθόνης 
global v            # καθολική μεταβλητή για τη λίστα V 

# αρχικοποίηση λίστας n- στοιχείων
def randomizelist(n): 
    L = [0] * n   
    for i in range(n): 
        L[i] = random.randint(1,maxint)
    return L

# ανοίγει το αρχείο config.txt για επεξεργασία 
def open_file():
  filepath = "config.txt"
  if os.path.isfile('config.txt'):
     with open(filepath, "r") as input_file:
        text = input_file.read()
        global txt_edit
        txt_edit.insert(tk.END, text)
     window.title(f"Config Editor Application - {filepath}")


# αποθηκεύει το αρχείο config.txt
def save_file():
  
  filepath = "config.txt"
  if os.path.isfile('config.txt'):
    with open(filepath, "w") as output_file:
           
        text = txt_edit.get(1.0, tk.END)
        output_file.write(text)
        output_file.close()
        tk.messagebox.showinfo(title="saving...", message="config file was saved...")
    window.title(f"Config Editor Application - {filepath}")

# ενημερώνει τις global μεταβλητές εμφάνισης από το αρχείο config.txt      
def initfromtxt( ):
    global n,maxint,DELAY,SPEED
    global COLOR0,COLOR1,COLOR2
    global COLOR3,TXTCOLOR,BGCOLOR,SCREENX,SCREENY
    global txt_edit
    if os.path.isfile('config.txt'):
      with open("config.txt" , mode="r") as my_file:
         for line in my_file:
            if line!='\n' and line[0]!="#": 
                x=line.split()
                x1=x[0]
                x2=x[2]
                if x1 == 'n' : n= int(x2)
                if x1 == 'maxint' : maxint= int(x2)
                if x1 == 'DELAY' : DELAY= float(x2)
                if x1 == 'SPEED' : SPEED= int(x2)
                if x1 == 'COLOR0': COLOR0= x2
                if x1 == 'COLOR1': COLOR1= x2
                if x1 == 'COLOR2': COLOR2= x2
                if x1 == 'COLOR3': COLOR3= x2
                if x1 == 'TXTCOLOR' :TXTCOLOR= x2
                if x1 == 'BGCOLOR' : BGCOLOR= x2
                if x1 == 'SCREENX' : SCREENX= int(x2)
                if x1 == 'SCREENY' : SCREENY= int(x2)

                   
      my_file.close()

# ορίζει ένα παράθυρο του tkinter που θα χρησιμοποιήσουμε ως  μικρό επεξεργαστή κειμένου
# ανοίγει το αρχείο config.txt και το βάζει  για επεξεργασία στο παράθυρο tkinter
# --- με αυτό τον τρόπο μπορούμε να αλλάξουμε τις τιμές των παραμέτρων σχεδίασης ----
# εμφανίζει επίσης τα πλήκτρα save και exit για αποθήκευση και κλείσιμο του παραθύρου
    
def Configuration():
    global window, v
    window = tk.Tk()
    window.title("Config Editor Application")
    window.rowconfigure(0, minsize=200, weight=1)
    window.columnconfigure(1, minsize=200, weight=1)
    window.option_add('*Font', 'arial 14')
    window.focus_set()
    window.wm_attributes('-topmost', 1)   # το παράθυρο γίνετε ενεργό (ontop)
    global txt_edit
    txt_edit = tk.Text(window)
    open_file()
    fr_buttons = tk.Frame(window, relief=tk.RAISED, bd=2)
    btn_save = tk.Button(fr_buttons, text="  Save ", command=save_file)
    exit_button = tk.Button(fr_buttons, text="  Exit ", command=window.destroy)
    
    btn_save.grid(row=1, column=0, sticky="ew", pady=10,padx=10 )
    exit_button.grid(row=2, column=0, sticky="ew", pady=5,padx=10)

    
    fr_buttons.grid(row=0, column=1, sticky="ns")
    txt_edit.grid(row=0, column=0, sticky="nsew")

    window.mainloop()
    #Οι μεταβλητές εμφάνισης παιρνουν τιμές από το αρχείο 
    initfromtxt()
    # Δημιουργία Λίστας
    v=randomizelist(n)
 

# Δημιουργία οθόνης σχεδίασης turtle
# θα τη χρησιμοποιήσουμε για να σχεδιάζουμε τις μπάρες της ταξινόμησης
def setupscreen(x,y):
    screen = turtle.Screen()
    # να έχει πάντα focus - πρώτο πλάνο
    rootwindow = screen.getcanvas().winfo_toplevel()
    rootwindow.call('wm', 'attributes', '.', '-topmost', 1)

    screen.setup(x,y,startx=10,starty=10)
    screen.bgcolor(BGCOLOR)
    screen.tracer(0,0)
    screen.title('Insertion Sort Animation ΠΑΠΑΚΩΣΤΑΣ ΑΘΑΝΑΣΙΟΣ - ΚΟΡΟΓΙΑΝΝΟΣ ΙΩΑΝΝΗΣ - ΚΟΛΟΒΟΣ ΣΤΥΛΙΑΝΟΣ')
    turtle.hideturtle()
   
    return screen



# εκτυπώνει τα στοιχεια της λίστας v στο κάτω μέρος της οθόνης σχεδιασμού turtle
def writeList(v):
    x =  - int((screen.window_width()/2) -10)
    y =  - int((screen.window_height()/2)-10) 
    turtle.up()
    turtle.color(TXTCOLOR)
    style = ('Arial', 11 )
    turtle.goto(x, y)
    turtle.write(v, font=style,align='left')
    turtle.color(LINECOLOR)

# Σχεδιάζει μία μόνο μπάρα
# στο σημειο x,y
# μέ πλάτος w και ύψος h
# και χρώμα γεμίσματος color 
   
def draw_bar(x,y,w,h,color):
    turtle.speed(1)
    turtle.up()
    turtle.goto(x,y)
    turtle.seth(0)
    turtle.down()
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.fd(w)
    turtle.left(90)
    turtle.fd(h)
    turtle.left(90)
    turtle.fd(w)
    turtle.left(90)
    turtle.fd(h)
    turtle.left(90)
    turtle.end_fill()

    
#───────────────────────────────────────────────────────────────────────────────────────┐ 
# Σχεδιάζει όλες (n) μπάρες της λίστας στην οθόνη                                       │
# V : λίστα                                                                             │
# n πλήθος στοιχείων                                                                    │
# pos : η θέση του στοιχείου που πρέπει να μεταφερθει δεξιά                             │
# κ : η θέση του στοιχείου που θέλουμε να εντάξουμε στα ήδη ταξινομημένα                │
# mode : κάτάσταση σχεδίασης                                                            │
#       0.  Σχεδιάζει όλη την λίστα με το ίδιο χρώμα  (green)                           │
#       1.  Σχεδιάζει με διαφορετικό χρώμα (yellow)τη μπάρα που πρέπει να μετακινηθει   │
#           δεξιά. Επίσης σχεδιάζει με διαφορετικό χρώμα (green)τα ήδη ταξινομημένα     │
#           στοιχεια και με διαφορετικό χρώμα (grey) αταξινόμητα στοιχεία               │                    
#       2.  Σχεδιάζει με διαφορετικό χρώμα (tomato)τη θέση που εισάγεται                │
#           το προς ταξινόμηση στοιχείο                                                 │
#───────────────────────────────────────────────────────────────────────────────────────┘       
def draw_bars(v,n,pos=0,k=0,mode=0):
     

    x =  -(screen.window_width()//2 - 10)
    y =  -(screen.window_height()//2 -30)
    
    turtle.clear()
    w = screen.window_width()//(n+1)
    hy = (screen.window_height())/maxint
    
    for  i in range(n):
        h=int(v[i]*hy*0.9)  # Υψος στο 0.9 % της οθόνης
        
        if mode==0:    # οταν ολα θα έχουν ταξινομηθει
            draw_bar(x,y,w,h,COLOR3)    # χρώμα ταξινομημένων - πράσινο

            
        elif mode==1:  # κατά την μετακίνηση των στοιχειων                   
            if i==pos:
                draw_bar(x,y,w,h,COLOR2) # χρώμα στοιχειων που μετακινούνται δεξιά 
            elif i<k:
                draw_bar(x,y,w,h,COLOR3) # χρώμα ήδη ταξονομημένων - πράσινο
            else:
                draw_bar(x,y,w,h,COLOR0) # χρώμα αταξινόμητων - γκρί 
        elif mode==2:      #  οταν το στοιχείο πάει στη νέα θέση  
            if i==pos:
                draw_bar(x,y,w,h,COLOR1) # χρώμα νέας θέσης 
            elif i<k:
                draw_bar(x,y,w,h,COLOR3) # χρώμα ήδη ταξονομημένων - πράσινο
            else:
                draw_bar(x,y,w,h,COLOR0) # χρώμα αταξινόμητων - γκρί               
        x += w 
    writeList(v) # τύπωσε στο κάτω μέρος τη λίστα
    
   
    
           
#──────────────────────────────────────────────────────────────────┐    
# Τοποθετει ένα το στοιχειο κ στη σωστή θέση                       │ 
# ανάμεσα στα ήδη ταξινομημένα στοιχεία (0 έως κ-1)                │ 
# αφού προηγουμένως μετακινήσει κατά μία θέση δεξιά όσα στοιχεία   │ 
# ειναι μεγαλύτερα από το στοιχείο της θέσης κ.                    │ 
#──────────────────────────────────────────────────────────────────┘

def insert(v,k):
    x = v[k]
    draw_bars(v,n,k,k,2) # σχεδιάζει με διαφορετικό χρώμα την μπάρα του στοιχειου k - κόκκινο 
    time.sleep(DELAY)
    for i in range(k-1,-1,-1):
        if v[i] > x:        # μετακίνηση των στοιχείων που ειναι μεγαλύτερα από το x 
            v[i+1] = v[i]   # μία θέση δεξιά
            draw_bars(v,n,i+1,k,1) # σχεδιάζει το δαβδοδιάγραμμα - με κίτρινο στη θέση μετακίνησης
            time.sleep(DELAY)
        else:
            v[i+1] = x             # μεταφάρει το στοιχείο x στη νέα θέση 
            draw_bars(v,n,i+1,k,2) # σχεδιάζει με διαφορετικό χρώμα -κοκκινο- τη θέση τοποθέτησης 
            time.sleep(DELAY+0.01)
            break
    else :                   # αν πρέπει να εισαχθεί στην πρώτη θέση 
        v[0] = x             # δηλ. αν όλα τα στοιχεία είναι μεγαλύτερα απο το x   



   

#───────────────────────────────────────────────────────────────┐    
# Ταξινόμηση λίστας "με εισαγωγή"                               │
# καλει επαναλήπτικά την συνάρτηση insert                       │
# για όλα τα στοιχεία της λίστας εκτός από το πρώτο             │
#───────────────────────────────────────────────────────────────┘

# Ταξινόμηση με χρήση αναδρομής! 
# def insertion_sort(v,k):
#    if k == 1: return
#    insertion_sort(v,k-1)
#    insert(v,k-1)




# Ταξινόμηση χωρίς χρήση αναδρομής
# καλει τη συνάρτηση insert για κάθε στοιχείο της λίστας v
def insertion_sort1(v):
        for k in range(1,len(v)):
            insert(v,k)
        draw_bars(v,len(v))  #Εμφανίζει στο τέλος την ταξινομημένη τη λίστα  
    

# ή ίδια συνάρτηση χωρίς γραφικά
def insertion_sort2(v):
    for k in range(1,len(v)):
        x = v[k]
        for i in range(k-1,-1,-1):
            if v[i] > x:        # μετακίνηση των στοιχείων που ειναι μεγαλύτερα  
                v[i+1] = v[i]   # μία θέση δεξιά
            
            else:
                v[i+1] = x      # μεταφάρει το στοιχείο στη νέα θέση 
                break 
        else :                  # αν πρέπει να εισαχθεί στην πρώτη θέση
            v[0] = x




def sort_with_graph(v):
        global screen
        screen=setupscreen(SCREENX,SCREENY)  # δημιουργεί την οθόνη σχεδιασμού
        insertion_sort1(v)                   # ταξινομεί ολα τα στοιχεία της λίστας v   
        time.sleep(3)
        turtle.bye()     # κλεινει το παράθυρο σχεδιασμού       
        # ανανέωση περιβάλλοντος tutrle
        turtle.Turtle._screen = None  # force recreation of singleton Screen object
        turtle.TurtleScreen._RUNNING = True  # only set upon TurtleScreen() definition 

  

def menu():
 
    global v
    while True:
        print ('│────────────────────────────────────────────────┐')
        print ('│    0. Configuration                            │')
        print ('│    1. Randomize List                           │')
        print ('│    2. Sort with grafical demo                  │')
        print ('│    3. Sort whithout grafical demo              │')
        print ('│    4. Exit                                     │')
        print ('│────────────────────────────────────────────────┘')                                               
        x=input( ' Give your choice :')                       
        
        if x.isdigit():
            x=int(x)
        else:
            continue
        if x==0:
            Configuration()

        if x==1:
            v=randomizelist(n)

        if x==2:
            sort_with_graph(v)
                 
          
        if x==3:
            print('List Is: ',v)
            input('Press any key for begin sorting...')
            t1 = time.time()
            insertion_sort2(v)
            t2 = time.time()
            print('elapsed time={0:.10f}'.format(t2-t1))
            print ('Sorted List: ',v)
            print('\n')
           
        if x==4:
            print('Exit...')
            break

def main():
    global v
    initfromtxt()
    v=randomizelist(n)
    menu()

    
#------ ΑΡΧΗ ΠΡΟΓΡΑΜΜΑΤΟΣ -------
    
if __name__== "__main__" : main()
