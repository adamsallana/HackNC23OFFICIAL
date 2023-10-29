import PriaidDiagnosisClient
import config
import sys
import json

import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import messagebox



class PriaidDiagnosisClientDemo:
    'Demo class to simulate how to use PriaidDiagnosisClient'


    def __init__(self):
        username = config.username
        password = config.password
        authUrl = config.priaid_authservice_url
        healthUrl = config.priaid_healthservice_url
        language = config.language
        self._printRawOutput = config.pritnRawOutput
        self.window = tk.Tk()
        super(PriaidDiagnosisClientDemo, self).__init__()
        self._diagnosisClient = PriaidDiagnosisClient.DiagnosisClient(username, password, authUrl, language, healthUrl)

        

    def simulate(self):
        # Load body locations
        
        
        selectedLocationID = self._loadBodyLocations()
        
        # Load body sublocations
        #selectedSublocationID = self._loadBodySublocations(selectedLocationID)

        self.window.mainloop() 


    def _loadBodyLocations(self):   # takes list of body locations from API
        bodyLocations = self._diagnosisClient.loadBodyLocations()
        
        if not bodyLocations:
            raise Exception("Empty body locations results")
         
        for bodyLocation in bodyLocations:
            print("{0} ({1})".format(bodyLocation["Name"], bodyLocation["ID"]))

        global selectedLocationID
        selectedLocationID = bodyLocations[0]  ## change to user input
        print("Sublocations for selected location {0}".format(selectedLocationID["Name"]))

        bodyLocationsList = []
        for location in bodyLocations:
            bodyLocationsList.append(location["Name"])

        # Calls method to create drop down menu
        self._tkBuildDropDown(bodyLocationsList, "Symptom Location")
        return selectedLocationID["ID"]

    def _loadBodySublocations(self, locId):  # arg is bodyLocation
        bodySublocations = self._diagnosisClient.loadBodySubLocations(locId)

        if not bodySublocations:
            raise Exception("Empty body sublocations results")
    
        for bodySublocation in bodySublocations:
            print("{0} ({1})".format(bodySublocation["Name"], bodySublocation["ID"]))

        global selectedSublocationID
        selectedLocationID = bodySublocations[0]
        print("Sublocations for selected location {0}".format(selectedSublocationID["Name"]))
        
        subLocationsList = []
        for location in subLocationsList:
            subLocationsList.append(location["Name"])

        ## Function call drop down menu
        self._tkBuildDropDown(subLocationsList, "Sublocation of symptom")
        print(selectedSublocationID)
        return selectedSublocationID["ID"]
        

    def _next(self):
        self.window.quit()
        print(selectedLocationID)

    def _tkBuildDropDown(self, value, title):

        #Window widgets
        self.window.geometry("400x350+400+50")
        self.window.title(title)

        #Assigns type and sets value
        tkSelectedTitle = tk.StringVar()
        tkSelectedTitle.set(title) 
       
        label = tk.Label(self.window, textvariable = tkSelectedTitle)
        label.pack()

        selectedLocationID = tk.StringVar()

        comboBox = ttk.Combobox(self.window, textvariable = selectedLocationID, values = value, width = 15)
        comboBox.pack(fill=tk.X, pady = 20)

        
        #bind the combobox!!
        comboBox.bind("<<ComboboxSelected>>", self._next())
        
        b1 = Button(self.window, text="OK", command=self._next)
        b1.pack()

        
        selectedLocationID = set(comboBox.get())

        

        #Window widgets
        

        #Assigns type and sets value
       

        #bind the combobox!!
       ## comboBox.bind("<<ComboboxSelected>>", self._pickBodyLocation)

        

    def _tkBuildDropDown2(self, value, title):

    #Window widgets
        self.window.geometry("400x350+400+50")
        self.window.title(title)

        #Assigns type and sets value
        tkSelectedTitle = tk.StringVar()
        tkSelectedTitle.set(title) 
    
        label = tk.Label(self.window, textvariable = tkSelectedTitle)
        label.pack()

        comboBox = ttk.Combobox(self.window, values = value, width = 15)
        comboBox.pack(pady = 40)

        
        #bind the combobox!!
        comboBox.bind("<<ComboboxSelected>>", self._next())

        #bind the combobox!!
        comboBox.bind("<<ComboboxSelected>>", self._pickBodyLocation)

        


        

diagnosisClientDemo = PriaidDiagnosisClientDemo()
diagnosisClientDemo.simulate()

