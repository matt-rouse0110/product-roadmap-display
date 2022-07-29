from functools import partial
from cmath import exp
from distutils import command
import sys
from ast import Global
from cgitb import text
from turtle import bgcolor, isvisible, width
from webbrowser import get
import ppt_objects
import tkinter as tk
from tkinter import Frame, Widget, ttk as ttk

print(str(True))
print(str(False))

def printChildren(object: Widget):
   children = object.winfo_children()
   for child in children:
      if child.winfo_ismapped():
         isVisible = "Is Visible"
      else:
         isVisible = "Is not Visible"
      widgetText = ';'
      if child.winfo_name() == 'quitButton':
         # print("Getting button text")
         # waiting = input("Ready to go?")
         widgetText = ';'+child.cget('text')
      grid_dets = child.grid_info()
      grid_dets['height'] = child.winfo_height()
      grid_dets['width'] = child.winfo_width()
      if not("in" in grid_dets):
         # print(str(child)  + ';' + str(child.winfo_width())+';',isVisible,widgetText)
         grid_dets['in'] = child.winfo_parent()
      grid_dets['name'] = child
      grid_dets_copy = {}
      for key in grid_dets:
         if key == 'height' or key == 'width' or key == 'in' or key == 'name':
            grid_dets_copy[key] = grid_dets[key]
      print(grid_dets_copy)
      printChildren(child)

class ScrollableFrame(ttk.Frame):
    def __init__(self, container, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        canvas = tk.Canvas(self)
        scrollbar = ttk.Scrollbar(self, orient="vertical", command=canvas.yview)
        self.scrollable_frame = ttk.Frame(canvas)

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )

        canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")

        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

class Application(ttk.Frame):
   def __init__(self, master=None):
      main_frame = ttk.Frame.__init__(self, master)
      
      main_canvas = tk.Canvas(main_frame, bg='purple')
      scroll=tk.Scrollbar(main_frame, orient=tk.VERTICAL,command=main_canvas.yview)

      self.second_frame = ttk.Frame(main_canvas)
      # main_canvas.bind("<Configure>",lambda e: main_canvas.configure(scrollregion=main_canvas.bbox("all")))
      # main_canvas.grid(sticky="news")
      # self.second_frame.bind("<Configure>", lambda e: self.second_frame.configure()
      # self.second_frame.grid(rowspan=50,columnspan=3,sticky="news")

      

      self.master.geometry("")
      print(self.winfo_screenheight())
      print(self.winfo_screenwidth())
      self.createWidgets()
      main_canvas.create_window(0,0,window=self.second_frame, anchor="nw")
      main_canvas.update_idletasks()
      bbox = main_canvas.bbox("all")
      main_canvas.configure(yscrollcommand=scroll.set,scrollregion=bbox)
      main_canvas.pack(side=tk.LEFT,fill=tk.BOTH,expand=True)
      scroll.pack(side=tk.RIGHT,fill=tk.Y)
      self.pack(fill=tk.BOTH,expand=True)
      self.main_canv = main_canvas
      self.resetScrollbar()
      self.submitCreated = False

      self.second_frame.bind("<Configure>", self.OnFrameConfigure)
      print(main_canvas.winfo_width())
      print(main_canvas.winfo_height())
      # self.main_canv.bind('<Configure>', self.FrameWidth)

   # def FrameWidth(self, event):
   #    canvas_width = event.width
   #    # print(canvas_width)
   #    # self.main_canv.config(self.main_canv, width = canvas_width)

   def OnFrameConfigure(self, event):
      self.main_canv.configure(width=event.width)
      if event.height <= self.winfo_screenheight()-20:
         self.main_canv.configure(height=event.height)
      self.main_canv.configure(scrollregion=self.main_canv.bbox("all"))

   def resetScrollbar(self):
      value = 1
      # self.master.geometry(str(self.master.winfo_width())+"x"+str(self.master.winfo_height()))
      # self.master.geometry("600x400")
      # self.winfo_toplevel().geometry("")
      # self.main_canv.bind("<Configure>",lambda e: self.main_canv.configure(scrollregion=self.main_canv.bbox("all")))
   def processLabel(self, rb_var: tk.IntVar, frame: ttk.Frame):
      """
      If it is a potential phase label, need to ask what the values are to look for - everything else will be excluded
      ***
      """
      print(rb_var)
      if rb_var.get() == 0:
         print("do stuff for storing content from tickets to display")
         children = frame.winfo_children()
         for child in children:
            if child.winfo_class() == 'Text':
               child.grid_remove()
            elif child.winfo_name() == "phaseTextEntry":
               child.grid_remove()
      elif rb_var.get() == 1:
         print("do stuff for sorting roadmap phases")
         children = frame.winfo_children()
         found = False
         for child in children:
            if child.winfo_class() == 'Text':
               child.grid()
               found = True
               print("re-enabled the text entry.")
               print(child.grid_info())
            elif child.winfo_name() == "phaseTextEntry":
               child.grid()
               print("re-enabled the text label.")
               print(child.grid_info())

         if(not(found)):
            frame.phaseLabel = ttk.Label(frame,text="Enter phases on new lines (in order)",name="phaseTextEntry")
            frame.phaseInput = tk.Text(frame,height=5, width=25)
            frame.phaseLabel.grid(row=3)
            frame.phaseInput.grid(row=3,column=1)
            self.master.geometry("")
         
      self.resetScrollbar()
      """ parent = frame.winfo_parent()
      while parent != '':
         print(parent)
         parent = parent.winfo_parent()
 """
   def createWidgets(self):
      self.createQuitButton()
      self.createInitialPrompts()
   def createInitialPrompts(self):
      topLevel = self.second_frame
      rowCnt = 2
      self.userLabel = ttk.Label(topLevel,text="Username")
      self.userInput = ttk.Entry(topLevel)
      self.userLabel.grid(row=rowCnt, column=1)
      self.userInput.grid(row=rowCnt, column=2)
      self.passwdLabel = ttk.Label(topLevel,text="Password")
      self.passwdInput = ttk.Entry(topLevel,show='*')
      rowCnt+=1
      self.passwdInput.grid(row=rowCnt, column=2)
      self.passwdLabel.grid(row=rowCnt, column=1,)
      rowCnt+=1
      self.choice = tk.IntVar()
      self.choice.set(-1)
      self.StdJiraChoice = ttk.Radiobutton(topLevel,variable=self.choice,text="Standard Jira Format",value=0,command=self.createStdJiraInputPrompts)
      self.StdJiraChoice.grid(row=rowCnt,column=1)
      rowCnt+=1
      self.CustJiraChoice = ttk.Radiobutton(topLevel,variable=self.choice,text="Custom Jira Query",value=1,command=self.createCustJiraInputPrompts)
      self.CustJiraChoice.grid(row=rowCnt,column=1)
      self.winfo_toplevel().update_idletasks()
      # printChildren(self)
   def createQuitButton(self):
      self.quitButton = ttk.Button(self.second_frame, text='Quit',
         command=self.quit,name="quitButton")
      self.quitButton.grid(row=0,column=0)
   def createStdJiraInputPrompts(self):
      # self.master.geometry("")
      children = self.winfo_children()
      stdFound = False
      for child in children:
         if child.winfo_name() == 'customFrame':
            children_widgets = self.CustFrame.winfo_children()
            for child_widget in children_widgets:
               child_widget.grid_remove()
            child.grid_remove()
         if child.winfo_name() == 'standardFrame':
            stdFound = True
            child.grid()

      if (not(stdFound) == True):
         topLevel = self.second_frame
         rowCnt = 6
         self.StdFrame = ttk.Frame(topLevel, name="standardFrame")
         self.StdFrame.grid(row=rowCnt,column=1,columnspan=2)
         self.projectTitleLabel = ttk.Label(self.StdFrame,text='Project')
         self.projectTitleLabel.grid(row=rowCnt,column=1)
         self.projectTitleInput = ttk.Entry(self.StdFrame)
         self.projectTitleInput.grid(row=rowCnt,column=2)
         rowCnt+=1
         self.labelsLabel = ttk.Label(self.StdFrame,text='Fields to include')
         self.labelsLabel.grid(row=rowCnt,column=1)
         self.labelsInput = tk.Listbox(self.StdFrame,selectmode=tk.MULTIPLE)
         self.labelsInput.insert(tk.END,"issueKey")
         self.labelsInput.insert(tk.END,"summary")
         self.labelsInput.insert(tk.END,"labels")
         self.labelsInput.insert(tk.END,"fixVersion")
         self.labelsInput.grid(row=rowCnt,column=2)
         self.labelsInput.bind('<<ListboxSelect>>', self.CreateSubmitButton)
      else:
         children_widgets = self.StdFrame.winfo_children()
         for child_widget in children_widgets:
            child_widget.grid()
   def createCustJiraInputPrompts(self):
      topLevel = self.second_frame
      # self.master.geometry("")
      children = self.winfo_children()
      custFound = False
      for child in children:
         if child.winfo_name() == 'standardFrame':
            children_widgets = self.StdFrame.winfo_children()
            for child_widget in children_widgets:
               child_widget.grid_remove()
            child.grid_remove()
         if child.winfo_name() == 'customFrame':
            custFound = True
            child.grid()
      if not(custFound) == True:
         rowCnt = 6
         self.CustFrame = ttk.Frame(topLevel, name='customFrame')
         self.CustFrame.grid(row=rowCnt,column=1,columnspan=2)
         self.JQLLabel = ttk.Label(self.CustFrame,text='JQL')
         self.JQLLabel.grid(row=rowCnt,column=1)
         self.JQLInput = ttk.Entry(self.CustFrame)
         self.JQLInput.grid(row=rowCnt,column=2)
         rowCnt+=1
         self.labelsLabel = ttk.Label(self.CustFrame,text='Fields to include')
         self.labelsLabel.grid(row=rowCnt,column=1)
         self.labelsInput = tk.Listbox(self.CustFrame,selectmode=tk.MULTIPLE)
         self.labelsInput.insert(tk.END,"issueKey")
         self.labelsInput.insert(tk.END,"summary")
         self.labelsInput.insert(tk.END,"labels")
         self.labelsInput.insert(tk.END,"fixVersion")
         self.labelsInput.grid(row=rowCnt,column=2)
         self.labelsInput.bind('<<ListboxSelect>>', self.CreateSubmitButton)
      else:
         children_widgets = self.CustFrame.winfo_children()
         for child_widget in children_widgets:
            child_widget.grid()
   def checkJQL(self,event):
      if self.JQLInput.get() != '':
         self.CreateSubmitButton(event=event)
   def CreateSubmitButton(self, event):
      # self.master.geometry("")
      topLevel = self.second_frame
      rowCnt = 8
      
      children = self.winfo_children()
      labelsFrameFound = False
      for child in children:
         if child.winfo_name() == 'labelsFrame':
            labelsFrameFound = True
      if not(labelsFrameFound):
         self.labelsMapFrame = ttk.Frame(topLevel,name="labelsFrame")
      else:
         frameChildren = self.labelsMapFrame.winfo_children()
         for childLabel in frameChildren:
            childLabel.grid_remove()
      """
      ***
      In here need to map out the selected fields over to the content of the roadmap item and the phases to be used (i.e. Now, Next, Future)

      Loop through each selected field and provide two options:
      1. Add as part of the roadmap item
      2. Contains a potential phase label
      """
      innerRowCnt = 1
      fieldSelection = self.labelsInput.curselection()
      for index in fieldSelection:
         if not(self.labelsMapFrame.winfo_ismapped()):
            self.labelsMapFrame.grid(row=rowCnt,columnspan=2)
         item = self.labelsInput.get(index)
         frame = ttk.Frame(self.labelsMapFrame, name=item+"LabelsFrame")
         frame.grid(row=innerRowCnt,columnspan=2)
         label = ttk.Label(frame,text=item)
         labelChoice = tk.IntVar()
         labelChoice.set(-1)
         detailChoice = ttk.Radiobutton(frame,variable=labelChoice,text=item + " as part of roadmap item details",value=0, command=partial(self.processLabel,labelChoice,frame))
         detailChoice.grid(row=1,column=1)
         label.grid(row=1)
         phaseChoice = ttk.Radiobutton(frame,variable=labelChoice,text=item + " as part of roadmap phase details",value=1, command=partial(self.processLabel,labelChoice,frame))
         phaseChoice.grid(row=2,column=1)
         innerRowCnt +=1

      if not(self.submitCreated):
         rowCnt +=1
         self.submitButton = ttk.Button(topLevel, text='Submit',
            command=self.storeData)
         self.submitButton.grid(row=rowCnt,column=1, columnspan=2)
         self.submitCreated = True
   def storeData(self):
      username = self.userInput.get()
      APIKey = self.passwdInput.get()
      project = self.projectTitleInput.get()
      fieldSelection = self.labelsInput.curselection()
      fields = ''
      for index in fieldSelection:
         item = self.labelsInput.get(index)
         if bool(fields):
            fields+= ','+item
         else:
            fields = item
      ppt_objects.executeRoadmapCreation(username, APIKey, project, fields)
      self.quit()

app = Application()
printChildren(app)
app.master.title('Roadmap Creation')
# app.master.geometry("400x400")
app.mainloop()


