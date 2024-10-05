import speech_recognition as sr
import webbrowser # For browsing
import pyttsx3 # To convert text to speech
import winsound # For beep
from gtts import gTTS
import time
import os
import keyboard
import cv2 # For camera
from AppOpener import open # To open App

def speak(text: str): 
    jarvis = pyttsx3.init()
    jarvis.say(text)
    jarvis.runAndWait()

def play_alarm (frequency = 400 ,duration = 400):
    winsound.Beep(frequency, duration)

def open_camera(quit_k = 'q'):
    # Open default camera
    cap = cv2.VideoCapture(0)

    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()

        # Display the resulting frame
        cv2.imshow('Camera', frame)

        # Exit loop if 'q' key is pressed
        if cv2.waitKey(1) & 0xFF == ord(quit_k):
            break

    # Release the camera and close OpenCV windows
    cap.release()
    cv2.destroyAllWindows()

def browsing(search: str):

    search = search.lower()

    if search == "open google" :
        webbrowser.open("https://www.google.com/")
    elif "open facebook" in search :
        webbrowser.open("https://www.facebook.com/")
    elif search == "open flipkart" :
        webbrowser.open("https://www.flipkart.com/")
    elif search == "open youtube":
        webbrowser.open("https://www.youtube.com/")
    elif search == "open chatgpt" or search == "open chat gpt" :
        webbrowser.open("https://chatgpt.com/")
    elif "open instagram" in search :
        webbrowser.open("https://www.instagram.com/")
    elif "open linkedin" in search :
        webbrowser.open("https://in.linkedin.com/")
    elif "open maps" in search or "open google maps" in search:
        webbrowser.open("https://www.google.com/maps/")
    elif search == "open amazon":
        webbrowser.open("https://www.amazon.in/")
    elif "open camera" in search :
        open_camera()
    elif search == "open whatsapp":
        open("whatsapp")
    elif search == "open chrome":
        open("google chrome")
    elif search == "open microsoft edge":
        open("microsoft edge")
    elif search == "open telegram":
        open("telegram desktop")    

    elif search.startswith("open youtube ") and (("play" in search) or ("open" in search)) and not ("search" in search): #or "open" in search):
        if "mrbeast" in search or "mr beast" in search :
           webbrowser.open('https://www.youtube.com/@mrbeast') 
        elif "beastboyshub" in search or "beast boy" in search or "beast boy shub" in search or "shub" in search:
           webbrowser.open('https://www.youtube.com/@yesmartypie') 
        elif "carryminati" in search or "carry minati" in search :
           webbrowser.open('https://www.youtube.com/@carryminati') 
        elif "yessmartypie" in search or "yes smartypie" in search or "yes smarty pie" in search :
           webbrowser.open('https://www.youtube.com/@yesmartypie') 
        elif "ezio18rip" in search or "ezio 18 rip" in search :
           webbrowser.open('https://www.youtube.com/@ezio18rip')
        elif "live insaan" in search :
           webbrowser.open('https://www.youtube.com/@liveinsaan')
        elif "triggered insaan" in search :
           webbrowser.open('https://www.youtube.com/@triggeredinsaan') 
        elif "sambutcha" in search :
           webbrowser.open('https://www.youtube.com/@sambutcha')
        else:
            inpt = search.split(" ")[4:]
            channel = ''.join([str(wd) for wd in inpt])
            webbrowser.open(f"https://www.youtube.com/@{channel}")

    elif search.startswith("open youtube ") and "search" in search:

        if "search for" in search:
            inpt_2 = search.split(" ")[5:]
            yt_search = '%20'.join([str(wd2) for wd2 in inpt_2])
            webbrowser.open(f"https://www.youtube.com/results?search_query={yt_search}")
        else:
            inpt_2 = search.split(" ")[4:]
            yt_search = '%20'.join([str(wd2) for wd2 in inpt_2])
            webbrowser.open(f"https://www.youtube.com/results?search_query={yt_search}")

    elif search.startswith("open amazon") and "search" in search:

        if "search for" in search:
            inpt_3 = search.split(" ")[5:]
            az_search = '%20'.join([str(wd3) for wd3 in inpt_3])
            webbrowser.open(f"https://www.amazon.in/s?k={az_search}&ref=nb_sb_noss")
        else:
            inpt_3 = search.split(" ")[4:]
            az_search = '%20'.join([str(wd3) for wd3 in inpt_3])
            webbrowser.open(f"https://www.amazon.in/s?k={az_search}&ref=nb_sb_noss")

    elif search.startswith("open google") and ("search" in search):

        if "search for" in search:
            inpt_4 = search.split(" ")[5:]
            gl_search = '+'.join([str(wd4) for wd4 in inpt_4])
            webbrowser.open(f"https://www.google.co.in/search?q={gl_search}&sca_esv=03201d68773a4f6e&sca_upv=1&sxsrf=ADLYWIIvy5nbMLBEThV7ZfWoep6KWpMwqw%3A1723468294962&source=hp&ei=Bgq6Zu7kOPG8vr0PkLiB0Ao&iflsig=AL9hbdgAAAAAZroYFnj8pf42rIdAQx6f7axWMMRUn56E&ved=0ahUKEwju_4Dcw--HAxVxnq8BHRBcAKoQ4dUDCBg&uact=5&oq=hello+why+hello+8+-&gs_lp=Egdnd3Mtd2l6IhNoZWxsbyB3aHkgaGVsbG8gOCAtMgYQABgWGB4yCxAAGIAEGIYDGIoFMgsQABiABBiGAxiKBTIIEAAYgAQYogRIm3pQthVYh3BwAXgAkAEAmAHnB6AB7HKqAQg0LTEuNi4xMrgBA8gBAPgBAZgCFKAChXWoAgrCAgcQIxgnGOoCwgIHEC4YJxjqAsICChAjGIAEGCcYigXCAgsQABiABBiRAhiKBcICCxAAGIAEGLEDGIMBwgILEC4YgAQYsQMYgwHCAhQQLhiABBixAxjRAxiDARjHARiKBcICBRAuGIAEwgIIEAAYgAQYsQPCAg0QLhiABBixAxhDGIoFwgINEAAYgAQYsQMYQxiKBcICCBAuGIAEGLEDwgIKEAAYgAQYQxiKBcICChAuGIAEGEMYigXCAgUQABiABMICERAuGIAEGLEDGNEDGIMBGMcBwgIQEC4YgAQYsQMYQxjJAxiKBcICEBAuGIAEGNEDGEMYxwEYigXCAgsQABiABBiSAxiKBcICEBAuGIAEGLEDGEMYgwEYigXCAhAQABiABBixAxhDGMkDGIoFwgIKEC4YgAQYAhjLAcICChAAGIAEGAIYywHCAggQABgWGB4YD8ICDBAuGNEDGBYYxwEYHsICBRAhGKABwgIFECEYnwXCAgcQABiABBgNmAMakgcKMS40LTUuMy4xMaAH5KcB&sclient=gws-wiz")
        else:
            inpt_4 = search.split(" ")[4:]
            gl_search = '+'.join([str(wd4) for wd4 in inpt_4])
            webbrowser.open(f"https://www.google.co.in/search?q={gl_search}&sca_esv=03201d68773a4f6e&sca_upv=1&sxsrf=ADLYWIIvy5nbMLBEThV7ZfWoep6KWpMwqw%3A1723468294962&source=hp&ei=Bgq6Zu7kOPG8vr0PkLiB0Ao&iflsig=AL9hbdgAAAAAZroYFnj8pf42rIdAQx6f7axWMMRUn56E&ved=0ahUKEwju_4Dcw--HAxVxnq8BHRBcAKoQ4dUDCBg&uact=5&oq=hello+why+hello+8+-&gs_lp=Egdnd3Mtd2l6IhNoZWxsbyB3aHkgaGVsbG8gOCAtMgYQABgWGB4yCxAAGIAEGIYDGIoFMgsQABiABBiGAxiKBTIIEAAYgAQYogRIm3pQthVYh3BwAXgAkAEAmAHnB6AB7HKqAQg0LTEuNi4xMrgBA8gBAPgBAZgCFKAChXWoAgrCAgcQIxgnGOoCwgIHEC4YJxjqAsICChAjGIAEGCcYigXCAgsQABiABBiRAhiKBcICCxAAGIAEGLEDGIMBwgILEC4YgAQYsQMYgwHCAhQQLhiABBixAxjRAxiDARjHARiKBcICBRAuGIAEwgIIEAAYgAQYsQPCAg0QLhiABBixAxhDGIoFwgINEAAYgAQYsQMYQxiKBcICCBAuGIAEGLEDwgIKEAAYgAQYQxiKBcICChAuGIAEGEMYigXCAgUQABiABMICERAuGIAEGLEDGNEDGIMBGMcBwgIQEC4YgAQYsQMYQxjJAxiKBcICEBAuGIAEGNEDGEMYxwEYigXCAgsQABiABBiSAxiKBcICEBAuGIAEGLEDGEMYgwEYigXCAhAQABiABBixAxhDGMkDGIoFwgIKEC4YgAQYAhjLAcICChAAGIAEGAIYywHCAggQABgWGB4YD8ICDBAuGNEDGBYYxwEYHsICBRAhGKABwgIFECEYnwXCAgcQABiABBgNmAMakgcKMS40LTUuMy4xMaAH5KcB&sclient=gws-wiz")

    elif search.startswith("search"):

        if "search for" in search:
            inpt_4 = search.split(" ")[2:]
            gl_search = '+'.join([str(wd4) for wd4 in inpt_4])
            webbrowser.open(f"https://www.google.co.in/search?q={gl_search}&sca_esv=03201d68773a4f6e&sca_upv=1&sxsrf=ADLYWIIvy5nbMLBEThV7ZfWoep6KWpMwqw%3A1723468294962&source=hp&ei=Bgq6Zu7kOPG8vr0PkLiB0Ao&iflsig=AL9hbdgAAAAAZroYFnj8pf42rIdAQx6f7axWMMRUn56E&ved=0ahUKEwju_4Dcw--HAxVxnq8BHRBcAKoQ4dUDCBg&uact=5&oq=hello+why+hello+8+-&gs_lp=Egdnd3Mtd2l6IhNoZWxsbyB3aHkgaGVsbG8gOCAtMgYQABgWGB4yCxAAGIAEGIYDGIoFMgsQABiABBiGAxiKBTIIEAAYgAQYogRIm3pQthVYh3BwAXgAkAEAmAHnB6AB7HKqAQg0LTEuNi4xMrgBA8gBAPgBAZgCFKAChXWoAgrCAgcQIxgnGOoCwgIHEC4YJxjqAsICChAjGIAEGCcYigXCAgsQABiABBiRAhiKBcICCxAAGIAEGLEDGIMBwgILEC4YgAQYsQMYgwHCAhQQLhiABBixAxjRAxiDARjHARiKBcICBRAuGIAEwgIIEAAYgAQYsQPCAg0QLhiABBixAxhDGIoFwgINEAAYgAQYsQMYQxiKBcICCBAuGIAEGLEDwgIKEAAYgAQYQxiKBcICChAuGIAEGEMYigXCAgUQABiABMICERAuGIAEGLEDGNEDGIMBGMcBwgIQEC4YgAQYsQMYQxjJAxiKBcICEBAuGIAEGNEDGEMYxwEYigXCAgsQABiABBiSAxiKBcICEBAuGIAEGLEDGEMYgwEYigXCAhAQABiABBixAxhDGMkDGIoFwgIKEC4YgAQYAhjLAcICChAAGIAEGAIYywHCAggQABgWGB4YD8ICDBAuGNEDGBYYxwEYHsICBRAhGKABwgIFECEYnwXCAgcQABiABBgNmAMakgcKMS40LTUuMy4xMaAH5KcB&sclient=gws-wiz")
        else:
            inpt_4 = search.split(" ")[1:]
            gl_search = '+'.join([str(wd4) for wd4 in inpt_4])
            webbrowser.open(f"https://www.google.co.in/search?q={gl_search}&sca_esv=03201d68773a4f6e&sca_upv=1&sxsrf=ADLYWIIvy5nbMLBEThV7ZfWoep6KWpMwqw%3A1723468294962&source=hp&ei=Bgq6Zu7kOPG8vr0PkLiB0Ao&iflsig=AL9hbdgAAAAAZroYFnj8pf42rIdAQx6f7axWMMRUn56E&ved=0ahUKEwju_4Dcw--HAxVxnq8BHRBcAKoQ4dUDCBg&uact=5&oq=hello+why+hello+8+-&gs_lp=Egdnd3Mtd2l6IhNoZWxsbyB3aHkgaGVsbG8gOCAtMgYQABgWGB4yCxAAGIAEGIYDGIoFMgsQABiABBiGAxiKBTIIEAAYgAQYogRIm3pQthVYh3BwAXgAkAEAmAHnB6AB7HKqAQg0LTEuNi4xMrgBA8gBAPgBAZgCFKAChXWoAgrCAgcQIxgnGOoCwgIHEC4YJxjqAsICChAjGIAEGCcYigXCAgsQABiABBiRAhiKBcICCxAAGIAEGLEDGIMBwgILEC4YgAQYsQMYgwHCAhQQLhiABBixAxjRAxiDARjHARiKBcICBRAuGIAEwgIIEAAYgAQYsQPCAg0QLhiABBixAxhDGIoFwgINEAAYgAQYsQMYQxiKBcICCBAuGIAEGLEDwgIKEAAYgAQYQxiKBcICChAuGIAEGEMYigXCAgUQABiABMICERAuGIAEGLEDGNEDGIMBGMcBwgIQEC4YgAQYsQMYQxjJAxiKBcICEBAuGIAEGNEDGEMYxwEYigXCAgsQABiABBiSAxiKBcICEBAuGIAEGLEDGEMYgwEYigXCAhAQABiABBixAxhDGMkDGIoFwgIKEC4YgAQYAhjLAcICChAAGIAEGAIYywHCAggQABgWGB4YD8ICDBAuGNEDGBYYxwEYHsICBRAhGKABwgIFECEYnwXCAgcQABiABBgNmAMakgcKMS40LTUuMy4xMaAH5KcB&sclient=gws-wiz")

    elif (search.startswith("open flipkart") or search.startswith("open flipcart")) and ("search" in search):

        if "search for" in search:
            inpt_5 = search.split(" ")[5:]
            fl_search = '%20'.join([str(wd5) for wd5 in inpt_5])
            webbrowser.open(f"https://www.flipkart.com/search?q={fl_search}&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off")
        else:
            inpt_5 = search.split(" ")[4:]
            fl_search = '%20'.join([str(wd5) for wd5 in inpt_5])
            webbrowser.open(f"https://www.flipkart.com/search?q={fl_search}&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off")


    elif search.startswith("open"):
        site = search.split(" ")[1]
        webbrowser.open(f"www.{site}.com")

    # elif search.startswith("play"):
    #     song = search.split(" ")[1]
    #     link = Music.songs[song]
    #     webbrowser.open(link)

    else:    
        print()    
        print("Not Available")
        speak("Sorry, the task is out of my range.")


def Jarvis():
        while True:

            recognizer = sr.Recognizer()

            try:
                 
                 # Capture audio from the microphone
                with sr.Microphone() as source:
                    print("Listening...")
                    audio = recognizer.listen(source, timeout=20, phrase_time_limit=1.6)

                # Recognize speech using Google
                start = recognizer.recognize_google(audio)

                if ("quit" in start.lower() or "close" in start.lower()):
                    play_alarm(200, 200)
                    quit()

                # Listen for the wake word "Hey Jarvis"
                elif (start.lower() == "jarvis" or start.lower() == "hey jarvis"):

                    play_alarm()

                    speak("Hello! I am Jarvis, How Can I help You ?")

                    while True:
                        # Listen for command
                        with sr.Microphone() as source:
                            print(f"\nListening for command...")
                            audio_2 = recognizer.listen(source, timeout=30, phrase_time_limit=10) 

                        command = recognizer.recognize_google(audio_2)

                        if ("quit" in command.lower() or "close" in command.lower()):
                            play_alarm(200, 200)
                            quit()

                        print(f"Searching for - {command}")

                        browsing(command) # To search on internet

            except sr.WaitTimeoutError :
                print("Timeout Error")
            except sr.UnknownValueError:
                print("Voice is not audible")
            except Exception as e:
                print(f"Error: {e}")
            print()
            print()

#====================================================================================================

if __name__ == "__main__" :

    speak(f"  Initializing Jarvis...")
    Jarvis()
     
