import pyttsx3
from tkinter import *

root_window = Tk()
root_window.geometry("540x450")

speech_voice = pyttsx3.init()
rate = speech_voice.getProperty('rate')
speech_voice.setProperty('rate',50)

#first window function start
def on_entry(event):
    speech_voice.say("balakirthika")
    speech_voice.runAndWait()

def on_entry_2(event):
    speech_voice.say("hemasutha")
    speech_voice.runAndWait()

def on_entry_3(event):
    speech_voice.say( "Hari")
    speech_voice.runAndWait()

def on_entry_4(event):
    speech_voice.say("rubika")
    speech_voice.runAndWait()

def on_entry_5(event):
    speech_voice.say("ajay kumar")
    speech_voice.runAndWait()

def intro(event):
    speech_voice.say("Welcome to BLIND PEOPLES LEARNING APPLICATION")
    speech_voice.runAndWait()
#first window function end








# question function start.
def question_1(question,answer_1,answer_2,answer_3):
    qus = question
    ans_1 = answer_1
    ans_2 = answer_2
    ans_3 = answer_3
     #python question window
    qws_window = Toplevel(root_window) #second window object is created.
    qws_window.title("Learning question Window") 
    qws_window.geometry("900x500")
    

    #python_qus_frame = Frame(qws_window,highlightbackground='red',highlightthickness=2)
    #python_qus_frame.pack()
    
    def answer_checking():
        #speech_voice.say("write answer Good")
        #speech_voice.runAndWait()
        qws_window.destroy()
    
    def wrong_answer():
        #speech_voice.say("wrong answer")
        #speech_voice.runAndWait()
        qws_window.destroy()
    #answer1 read
    def on_entry(event):
        pass
        #speech_voice.say(ans_1)
        #speech_voice.runAndWait()

    #answer 2 read
    def on_entry_2(event):
        pass
        #speech_voice.say(ans_2)
        #speech_voice.runAndWait()

    #answer3 read
    def on_entry_3(event):
        pass
        #speech_voice.say(ans_3)
        #speech_voice.runAndWait()
    
    #question read
    def question_read_1(event):
        pass
        #speech_voice.say(qus)# question read
        #speech_voice.runAndWait() 
        
    
    q_1 = Label(qws_window, text=qus,font=('serif',15,'bold'),padx=60,pady=20)
    q_1.pack(pady=10)
    #q_1.bind("<Enter>",question_read_1)

    t_b = Button(qws_window, text=ans_1,font=('serif',15,'bold'),padx=180,pady=10, command=wrong_answer)
    t_b.pack(pady=10)
    #t_b.bind("<Enter>",on_entry)

    t_b_2 = Button(qws_window, text=ans_2,font=('serif',15,'bold'),padx=180,pady=10,command=answer_checking)
    t_b_2.pack(pady=10)
    #t_b_2.bind("<Enter>",on_entry_2)

    t_b_3 = Button(qws_window, text=ans_3,font=('serif',15,'bold'),padx=180,pady=10, command=wrong_answer)
    t_b_3.pack(pady=10)
    #t_b_3.bind("<Enter>",on_entry_3)
   
#python question end....
# Given the write answer in -> 3 
def lesson_na_pass():
    question_1("Which type of programming language for python?","function oriented","all","object oriented")
    question_1("what is the Python First letter?","A","P","Z")
    question_1("which type of animal for python?","Lion","snake","Fish")
    question_1("who is created the python programming language","Balakrishnan","Guido van Rossum","Alexander")
    question_1("which year python program was created","1996","1991","2003")
    question_1("Zoho Corporation, is an Indian global technology company created year","2003","1996","2002")
    question_1("who is the Ceo of ZOHO corporation?","ratha","Sridhar Vembu","balakrishnan")
    question_1("first software company in India","Google","tata Consultancy Services","apple")
    question_1("Why is Python so demanded?","web app development","artificial intelligence and machine learning ","system software")
    question_1("what is the features of python programming language","learning is so hard","supports multiple programming paradigms","can not run quickly")
    
    #second off
    question_1("what is python.?","truck name","programming language","country name")
    question_1("Which animal is known as the Ship of the Desert?","lion","camel","cow")
    question_1(" How many days are there in a week?","3 day","7 days","10 day")
    question_1("How many hours are there in a day?","34 hour","24 houres","14 hour")
    question_1("How many letters are there in the English alphabet?","36 letters","26 letters","16 letters")
    question_1("Rainbow consist of how many colours?","6 colour","7 colours","8 colours")
    question_1(" How many minutes are there in an hour?","30 minutes","60 minutes","90 minutes")
    question_1("How many seconds are there in a minute?","30 seconds","60 seconds","90 seconds")
    question_1("How many seconds make one hour?","3500 seconds","3600 seconds","4600 seconds")
    question_1("Baby frog is known as ","frog","Tadpole","small frog")
    
    #thired off
    question_1("How many vowels are there in the English alphabet and name them?","4 vowels a e i o","5 vowels a e i o u","3 vowels a e i")
    question_1("Which animal is known as the king of the jungle?","tiger","lion","elephant")
    question_1("Name the National bird of India?","hen","Peacock","frog")
    question_1(" Name the National animal of India?","cow","Tiger","cat")
    question_1("Name the National fruit of India?","banana"," Mango ","graph")
    question_1("What is the National song of India?","jai hind","Vande Mataram","hindu stan")
    question_1("Name the National tree of India?","neem tree","Banyan tree","mango tree")
    question_1("Name the National river of India?","ratha","Ganga","krishna")
    question_1(" What is the capital of India?","madurai","New Delhi","chennai")
    
    #fourth off
    question_1("Name the biggest continent in the world?","india","Asia","russia")
    question_1("Which is the smallest month of the year?","may","February","june")
    question_1(" Which colour symbolises peace?","green","White","red")
    question_1("Name the largest mammal?","fish","Blue Whale","catefish")
    question_1("Who was the first Prime Minister of India?","ramasamy"," Pandit Jawaharlal Nehru","kannan kumar")
    question_1(" Who is the first woman prime minister of India?","ratha","Indira Gandhi","priya")
    question_1(" Name the densest jungle in the world?","the indian forest"," The Amazon rainforest","chiness forest")
    question_1("Anti-clockwise is it from left or right?","right","Left","no answer")
    question_1("Name the National Heritage Animal of India?","tiger","Elephant","king kong")


#first window codeing
en = Label(root_window, text="BLIND PEOPLES LEARNING APPLICATION",font=('serif', 15, 'bold'),padx=60,pady=20)
en.pack(pady=10)
en.bind("<Enter>",intro)

name_1 = Button(root_window, text="balakirthika",font=('serif', 20, 'bold'),padx=180,pady=10, command=lambda:lesson_na_pass())
name_1.pack(pady=5)
name_1.bind("<Enter>",on_entry)

name_2 = Button(root_window, text=" hemasutha ",font=('serif', 20, 'bold'),padx=180,pady=10, command=lambda:lesson_na_pass())
name_2.pack(pady=5)
name_2.bind("<Enter>",on_entry_2)

name_3 = Button(root_window, text="     hari     ",font=('serif', 20, 'bold'),padx=180,pady=10, command=lambda:lesson_na_pass())
name_3.pack(pady=5)
name_3.bind("<Enter>",on_entry_3)

name_4 = Button(root_window, text="    rubika   ",font=('serif', 20, 'bold'),padx=180,pady=10, command=lambda:lesson_na_pass())
name_4.pack(pady=5)
name_4.bind("<Enter>",on_entry_4)

name_5 = Button(root_window, text=" Ajaykumar ",font=('serif', 20, 'bold'),padx=180,pady=10, command=lambda:lesson_na_pass())
name_5.pack(pady=5)
name_5.bind("<Enter>",on_entry_5)

root_window.title("ULTRA COLLEGE OF ENGINEERING AND TECHNOLOGY")
root_window.resizable(False, False)
root_window.mainloop()

'''. 


 
'''

