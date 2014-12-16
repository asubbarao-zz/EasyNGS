#NAME OF THE FILE: EasyNGS_with_UI_v1.py
#DATE CREATED: 12/03/2014
#AUTHOR(s): Kiranmayee Dhavala

"""This module, when run, gives a widget which can be used as a GUI. It consists
of Class with attributes and Methods which perform important
functions that open, read and store required data from the file uploaded through
GUI. It requires the following modules:wx, numpy, pandas.

The initialization of class, consist of attributes for design of widget. This followed
by few more methods for details to be displayed on the widgets. The three main methods,
OnButtonDesign, OnButtonSam, OnButtonMpileup are used to open three unique data files 
and extract and store the desired elements. """

import wx
import numpy as np
import pandas as pands        
import classes_easyngs as cl


ID_DESIGN     = 1  # 
ID_SAM        = 2
ID_MPILEUP    = 3
ID_OUTPUT     = 4


class ListBox(wx.Frame):
    
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title, size=(500, 450))

        panel = wx.Panel(self, -1)
        hbox = wx.BoxSizer(wx.HORIZONTAL)

        self.listbox = wx.ListBox(panel, -1)
        hbox.Add(self.listbox, 1, wx.EXPAND | wx.ALL, 20)

        btnPanel = wx.Panel(panel, -1)
        vbox = wx.BoxSizer(wx.VERTICAL)
        bDesign = wx.Button(btnPanel, ID_DESIGN, 'Design File', size=(90, 30))
        bSam = wx.Button(btnPanel, ID_SAM, 'SAM File', size=(90, 30))
        bMpileup = wx.Button(btnPanel, ID_MPILEUP, 'Mpileup File', size=(90, 30))
        bOutput = wx.Button(btnPanel, ID_OUTPUT, 'Output File', size=(90, 30))

        self.Bind(wx.EVT_BUTTON, self.OnButtonDesign, id=ID_DESIGN)
        self.Bind(wx.EVT_BUTTON, self.OnButtonSam, id=ID_SAM)
        self.Bind(wx.EVT_BUTTON, self.OnButtonMpileup, id=ID_MPILEUP)

        vbox.Add((-1, 50))
        vbox.Add(bDesign)
        vbox.Add(bSam, 0, wx.TOP, 5)
        vbox.Add(bMpileup, 0, wx.TOP, 5)
        vbox.Add(bOutput, 0, wx.TOP, 5)

        btnPanel.SetSizer(vbox)
        hbox.Add(btnPanel, 0.6, wx.EXPAND | wx.RIGHT, 20)
        panel.SetSizer(hbox)

        self.Centre()
        self.Show(True)
        
        self.statusbar = self.CreateStatusBar()
        self.statusbar.SetStatusText("Welcome")
        
        self.design = cl.design_np()
        self.sam = cl.sam_np()
        self.mpileup = cl.mpile_up()
                   
    def DialogBox(self):
        wx.FutureCall(5000, self.ShowMessage)

        self.SetSize((300, 200))
        self.SetTitle('Message box')
        self.Centre()
        self.Show(True)

    def ShowMessage(self, message, title):
        self.message = message
        self.title = title
        wx.MessageBox(self.message,self.title, wx.OK | wx.ICON_INFORMATION)


    def OpenFileCsv(self, fname):
        try: 
            csvdata = pands.read_csv(fname, sep = ",")
            self.statusbar.SetStatusText("Completed Reading File")
            return csvdata
        except IOError:
            err_msg = "File %s does not exist"%fname
            self.ShowMessage(err_msg, "Error")
            return pands.Dataframe()
            
            
    def LoadArray(self,csvdata):            
            self.statusbar.SetStatusText("Reading File")
            arraydata = np.asarray(csvdata.values, dtype = 'a1000')
            self.statusbar.SetStatusText("Completed Reading File")
            return arraydata    
        
        
    def OnButtonDesign(self, event):
        filename_csv = wx.GetTextFromUser('Enter Design File', 'Design File')
        self.statusbar.SetStatusText("Processing")
        if filename_csv != '':
            self.listbox.Append("Design File:" + filename_csv)
            retData      = self.OpenFileCsv(filename_csv)
            if retData.empty:
                return None
            self.design.populate_design_np(retData)
            self.ShowMessage("Done!!", "Success")
              
                
    #On pressing SAM button
    def OnButtonSam(self, event):
        filename_csv = wx.GetTextFromUser('Enter SAM File', 'SAM File')
        self.statusbar.SetStatusText("Processing")
        if filename_csv != '':
            self.listbox.Append("Sam File:" + filename_csv)
            retData      = self.OpenFileCsv(filename_csv)
            if retData.empty:
                return None
            self.sam.populate_sam_np(retData)
            self.ShowMessage("Done!!", "Success")
        
                    
            
    def OnButtonMpileup(self, event):
        filename_csv = wx.GetTextFromUser('Enter Mpileup File', 'Mpileup File')
        self.statusbar.SetStatusText("Processing")
        if filename_csv != '':
            self.listbox.Append("MPileup File:" + filename_csv)
            retData      = self.OpenFileCsv(filename_csv)
            if retData.empty:
                return None
            self.mpileup.populate_mpile_up(retData) 
            self.ShowMessage("Done!!", "Success")
    
        