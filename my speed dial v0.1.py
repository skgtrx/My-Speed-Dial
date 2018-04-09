from tkinter import *
import webbrowser
def callback():
	webbrowser.open('http://google.com/search?q='+entry1.get())
	webbrowser.open('https://duckduckgo.com/?q='+entry1.get())
	webbrowser.open('http://bing.com/search?q='+entry1.get())
	webbrowser.open('http://search.yahoo.com/search?q='+entry1.get())
	webbrowser.open('https://youtube.com/results?search_query='+entry1.get())
	
# This above function is created for the button1. 

def get(event):
        webbrowser.open('http://google.com/search?q='+entry1.get())
        webbrowser.open('https://duckduckgo.com/?q='+entry1.get())
        webbrowser.open('http://bing.com/search?q='+entry1.get())
        webbrowser.open('http://search.yahoo.com/search?q='+entry1.get())
        webbrowser.open('https://youtube.com/results?search_query='+entry1.get())
        

# This above function is created for the event as for Return. It
# does't have any relation with the callback().

root=Tk()
root.title("My Speed Dial")
label1=Label(root,text='Query')
label1.grid(row=0,column=0)
entry1=Entry(root,width=50)
entry1.grid(row=0,column=1)
button1=Button(root,text='Search',width=10,command=callback)
button1.grid(row=0,column=2)
rbuttons=StringVar()
entry1.bind('<Return>',get)
# Here this bind attribute is for accessing this widget by another event like ENTER.
button2=Label(root,text='Google')
button2.grid(row=1,column=0,sticky=W)

button3=Label(root,text='DuckDuckGo     ')
button3.grid(row=1,column=1,sticky=W)

button4=Label(root,text='Bing')
button4.grid(row=1,column=1,sticky=W)

button5=Label(root,text='Yahoo')
button5.grid(row=1,column=2,sticky=W)

button6=Label(root,text='YouTube')
button6.grid(row=1,column=2,sticky=E)

entry1.focus()
root.attributes("-topmost",True)
# Here this attribute helps in keep our application at the top
# of the screen.

#root.minsize(550,100)
root.mainloop()


 
