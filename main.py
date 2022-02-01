import PySide6

print(PySide6.__version__)

import sys
import time

import threading
import random
import sys
import os
from random import *
import datetime
import schedule

from playsound import playsound

from PySide6.QtQuick import QQuickWindow
from PySide6.QtGui import Qt
from PySide6.QtQml import QQmlApplicationEngine, QQmlComponent
from PySide6.QtCore import QUrl, Qt, Slot, Property
from PySide6.QtWidgets import (QWidget, QProgressBar, QFrame, QDialog, QVBoxLayout, QApplication, QLineEdit, QLabel, QPushButton, QGridLayout)
from __feature__ import snake_case



def colour(toColour):
       attack = False
       seed(int(float(datetime.datetime.now().microsecond)*25485039845))
       rando = randint(1, 100)
       if rando > 50:
               val = "38"
       else:
               val = "48"

       key=""
       exit = False
       #print("\n\n"+str(size.lines))
       p = ""
       pos = 1
       def calc_red():
            red = randint(1, 255)
            if red < 0:
                red = 0
            return red
       def calc_green():
            green = randint(1, 255)
            if green < 0:
                green = 0
            return green
       def calc_blue():
            blue = randint(1, 255)
            if blue < 0:
                blue = 0
            return blue

       p += "\\x1b["+val+";2;"+str(calc_blue())+";"+str(calc_green())+";"+str(calc_red())+"m"+toColour+" "
       #print(p+"\n")
       #time.sleep(0.01)
       pos = 0
       if not attack:
           p += " \\033[0m"
           p += "\033[0m"
       else:
           p += ""
       blank = ""
       pos = 0
       total = 0
       print(p)
       #print("\033["+str(line)+";0H\033[0m"+blank+"\033[0m")

       return p


class RocketWrite(QWidget):
    def calc_red(self):
        red = randint(1, 255)
        if red < 0:
            red = 0
        self.red = str(red)
        return red
    def calc_green(self):
        green = randint(1, 255)
        if green < 0:
            green = 0
        self.green = str(green)
        return green
    def calc_blue(self):
        blue = randint(1, 255)
        if blue < 0:
            blue = 0
        self.blue = str(blue)
        return blue

    def reconnect(self):
        creds = pika.PlainCredentials(sys.argv[2], sys.argv[3])

        self.connection = pika.BlockingConnection(pika.ConnectionParameters(sys.argv[1], 5672, '/', creds))
        self.channel = self.connection.channel()
        self.channel.exchange_declare(exchange='topicex', exchange_type='topic')

        result = self.channel.queue_declare('')

        queue_name = result.method.queue

        self.routing_key = 'trout'
        self.channel.basic_publish(exchange='topicex', routing_key=self.routing_key, body="bip")
        print("[x] Sent %r:%r" % (self.routing_key, "bip"))


    def emission(self, pos):
        self.calc_red()
        self.calc_green()
        self.calc_blue()
        message = "PACKAGE:"+self.red+":"+self.green+":"+self.blue+":"+str(pos+1)+":"+str(self.greeters[pos].text())
        #self.greeters[pos].text = self.greeters[pos].text
        self.greeters[pos].setStyleSheet("QLineEdit {color: rgb("+str(self.calc_red())+", "+str(self.calc_blue())+", "+str(self.calc_green())+");}")
        self.channel.basic_publish(exchange='topicex', routing_key="trout", body=message)
        print("[x] Sent %r:%r" %("trout", message) )



    def emissionNoColour(self, pos):
        message = "PACKAGE::::"+str(pos+1)+":"+str(self.greeters[pos].text())
        #self.greeters[pos].text() = self.greeters[pos].text()
        #self.greeters[pos].setStyleSheet("QLineEdit {color: rgb("+str(self.calc_red())+", "+str(self.calc_blue())+", "+str(self.calc_green())+");}")
        self.channel.basic_publish(exchange='topicex', routing_key="trout", body=message)
        print("[x] Sent %r:%r" %("trout", message) )

    def get_path(self):
        path = self.filePath.text() + self.greeters[1].text()
        print(path)
        self.folder_path = path

    def __init__(self):
        #t = threading.Thread(Heartbeat.__init__)
        #t.start()


        QWidget.__init__(self)
        self.hello =  [
                "hallo",
                "hi",
                "hola"
                ]

        self.buttons = []
        self.greeters = []
        self.senders = []
        self.tags = []
        self.resize(800, 150)
        self.layout = QGridLayout(self)
        self.layout.set_horizontal_spacing(0)
        self.layout.set_vertical_spacing(0)
        #self.setStyleSheet("QGridLayout {background-image: url('../art/pastel.png') 0 0 0 0 stretch stretch;color:green;}")
        #self.layout = QGridLayout(self)
        for i in range(6):

            self.set_window_title("Deer Spook 1.0")
            if i == 0:
                tag = QPushButton("Current System Time")
                tag.position = i
                tag.setStyleSheet("color:aqua;")
                self.layout.add_widget(tag, i, 0)
                self.tags.append(tag)
            if i == 1:
                tag = QPushButton("Folder for files")
                tag.position = i
                tag.setStyleSheet("color:aqua;")
                self.layout.add_widget(tag, i, 0)
                self.tags.append(tag)
                filePath = QLineEdit("/path/to/music/folder/")
                filePath.position = i
                filePath.set_max_length(60)
                self.filePath = filePath
                filePath.setStyleSheet("color:aqua;")
                self.layout.add_widget(filePath, i, 0)
            if i == 2:
                tag = QPushButton("Loop Starts")
                tag.position = i
                tag.setStyleSheet("color:aqua;")
                self.layout.add_widget(tag, i, 0)
                self.tags.append(tag)
            mess = QLineEdit("Messages!")
            mess.position = i
            mess.set_max_length(60)
            self.greeters.append(mess)
            mess.setStyleSheet("color:aqua;")
            self.layout.add_widget(mess, i, 1)
            if i == 1:
                mess.set_text("FILENAME.wav")
            if i == 2:
                mess.set_text("08:00")
            nameButton = QPushButton("boop")
            nameButton.setStyleSheet("color:aqua;")
            self.layout.add_widget(nameButton, i, 2)
            button = QPushButton(str(i))
            button.setStyleSheet("color:orange;")
            #self.position = i
            button.position = i
            self.layout.add_widget(button, i, 3)
            send = QPushButton("SEND")
            send.setStyleSheet("color:aqua;")
            send.position = i
            self.senders.append(send)
            self.layout.add_widget(send, i, 4)
            if i == 1:
                send.set_text("Set path")
                send.clicked.connect(self.get_path)
            #button.object_name = "butt"+str(i)
            self.buttons.append(button)
            self.setStyleSheet("background-color:#16394f;")
            self.nameDetail = QDialog()
            self.nameDetailLayout = QVBoxLayout(self.nameDetail)
            nameDetail = "Details"
            labelDetail = QPushButton(nameDetail)
            #labelDetail.clicked.connect(self.emission)
            self.nameDetailLayout.add_widget(labelDetail)

        self.established = False
    @Property(QWidget)
    def buttonList():
        return self.buttons
    @Property(QWidget)
    def conn():
        return self.connection
    @Slot()
    def name_detail(self):
        #code for showing a string in an array
        if not self.established:
            filename = '101/1.txt'
            out = []
            outString = ""
            count = 0
            with open(filename) as file:
                lines = file.readlines()
                for i in range(len(lines)):
                    outString += lines[i]
                count += 1
            #print(outString)
            l = QLabel(outString)

            self.nameDetail.layout().add_widget(l)
            l.show()
            self.established = True
        #self.nameDetail.setText(outString)
        self.nameDetail.resize(450, 500)
        self.nameDetail.setStyleSheet("background:black;font:Courier New;color:pink;")
        self.nameDetail.show()
    @Slot()
    def greet(self):
        butt = self.focus_widget()
        try:
            self.emission(butt.position)
            for b in self.greeters:
                #print(b.position)
                if b.position == butt.position + 1:
                    #print("Triggered")
                    b.setFocus()
                    b.set_text("")
        except Exception as e:
            print("Probably a closed pipe")
            self.reconnect()
            #this works!
            self.emission(butt.position)
            for b in self.greeters:
                #print(b.position)
                if b.position == butt.position + 1:
                    #print("Triggered")
                    b.setFocus()
                    b.set_text("")

        print("Butt  number"+str(butt.position))
        print(self.greeters[butt.position].text())
        print(butt.position)
    @Slot()
    def greetNoColour(self):
        butt = self.focus_widget()
        try:
            self.emissionNoColour(butt.position)

        except Exception as e:
            print("Probably a closed pipe")
            self.reconnect()
            #this works!
            self.emissionNoColour(butt.position)

        print("Butt  number"+str(butt.position))
        print(self.greeters[butt.position].text())
        print(butt.position)

    @Slot()
    def boop():
        print("boop")
        #self.message.text = random.choice(self.hello)

    def play_sound(self):
        playsound(self.folder_path)
    def main_loop(self):
        timeStart = self.greeters[2].text()
        schedule.every().day.at(timeStart).do(self.play_sound, "Starting sound loop")
        
        while True:
            #print(datetime.datetime.now().time())
            schedule.run_pending()
            self.greeters[0].set_text(str(datetime.datetime.now().time()))
            self.greeters[0].show()
            time.sleep(1)

if __name__ == "__main__":
    if len(sys.argv) !=  1:
        print("Usage is python main.py")
        sys.exit()


    #create the database Connection
    """conn = psycopg2.connect("dbname="+sys.argv[4]+" user="+sys.argv[5])
    cur = conn.cursor()

    cur.execute("SELECT * FROM threads")

    records = cur.fetchall()
    print(records)"""

    app = QApplication([])

    widget = RocketWrite()

    #This is because consuming messages is a blocking function
    t = threading.Thread(target=widget.main_loop)
    t.start()
    #tt = threading.Thread(target=input.channel.start_consuming)
    widget.show()


    #tt.start()
    #bip = threading.Thread(target=Heartbeat.__init__)
    #bip.start()
    app.exec()
    #This is because app.exec() was just wrapped in sys.exit()
    #and I need to do some closing
    #
    sys.exit()
