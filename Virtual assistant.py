import wx
import wikipedia
import wolframalpha
#for speech
import os
import sys
import pyttsx3
import speech_recognition as sr
import pyaudio
engine = pyttsx3.init()



class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None,
            pos=wx.DefaultPosition, size=wx.Size(450, 100),
            style=wx.MINIMIZE_BOX | wx.SYSTEM_MENU | wx.CAPTION |
             wx.CLOSE_BOX | wx.CLIP_CHILDREN,
            title="PyDa")
        panel = wx.Panel(self)
        my_sizer = wx.BoxSizer(wx.VERTICAL)
        lbl = wx.StaticText(panel,
        label="Hello manu how can i help you")
        my_sizer.Add(lbl, 0, wx.ALL, 5)
        self.txt = wx.TextCtrl(panel, style=wx.TE_PROCESS_ENTER,size=(400,30))
        self.txt.SetFocus()
        self.txt.Bind(wx.EVT_TEXT_ENTER, self.OnEnter)
        my_sizer.Add(self.txt, 0, wx.ALL, 5)
        panel.SetSizer(my_sizer)
        self.Show()

    def OnEnter(self, event):
        input = self.txt.GetValue()
        answer = input.lower()
        if input == ' ':
            r = sr.Recognizer()
            with sr.Microphone() as source:
                audio = r.listen(source)
            try:
                self.txt.setValue(r.recognize_google(audio))
            except sr.UnknownValueError:
                print("google speech recognnition coud not understand audio")
            except sr.requesterror as e:
                print("coould not request result from google, {}".format(e))
        try:
            #wolframalpha
            app_id = "enter api key"
            client = wolframalpha.Client(app_id)
            res = client.query(input)
            answer = next(res.results).text
            print (answer)
        except:
            #wikipedia
            answer = (wikipedia.summary(input))
            print (answer)
        engine.say(answer)
        engine.runAndWait()
if __name__ == "__main__":
    app = wx.App(True)
    frame = MyFrame()
    app.MainLoop()
