import pyttsx3
import speech_recognition as sr
import webbrowser
import pywhatkit
import wikipedia
import os
import pyautogui
import keyboard
import pyjokes
from PyDictionary import PyDictionary as Diction
import flask


Assistant = pyttsx3.init('sapi5')
voices = Assistant.getProperty('voices')
print(voices)
Assistant.setProperty('voices', voices[0].id)


def Speak(audio):
    print("   ")
    Assistant.say(audio)
    print(f": {audio}")
    Assistant.runAndWait()


def takecommand():
    command = sr.Recognizer()
    with sr.Microphone() as source:
        print("Eshitvomman...")
        command.pause_threshold = 1
        audio = command.listen(source)

        try:
            print("Bajarilmoqda...")
            query = command.recognize_google(audio, language='uz-UZ')
            print(f"Siz etdiz : {query}")

        except Exception as Error:
            return "none"

        return query.lower()


def TaskExe():

    def Music():
        Speak("Musiqa nomini ayting!")
        musicName = takecommand()

        if 'dj green' in musicName:
            os.startfile('C:\\musica\\dard_alam.mp3')

        elif 'avaz' in musicName or 'avval' in musicName:
            os.startfile('C:\\musica\\ISFANDI ft. AvaZ.mp3')

        elif 'sevimli video' in musicName or 'sevimli ashula' in musicName:
            os.startfile('C:\\Users\\user\\Desktop\\Sevimli\\video_2022-03-19_14-31-23.mp4')

        else:
            pywhatkit.playonyt(musicName)

        Speak("musiqa qoyildi Aziz mazza qiling!")

    def Whatsapp():
        Speak("foydalanuvchi nomini ayting menga!")
        name = takecommand()

        if 'Aziz' in name:
            Speak("Sms nomini ayting!")
            msg = takecommand()
            Speak("Vaqtni ayting Aziz!")
            Speak("Soat uslubida!")
            hour = int(takecommand())
            Speak("Vaqt minutda!")
            min = int(takecommand())
            pywhatkit.sendWhatmsg("+998998400597", msg, hour, min, 20)
            Speak("Ok Aziz , Yuborildi Whatsapp sms !")

        elif 'Aziza' in query:
            Speak("Sms nomini ayting!")
            msg = takecommand()
            Speak("Vaqtni ayting Aziz!")
            Speak("Soat uslubida!")
            hour = int(takecommand())
            Speak("Vaqt minutda!")
            min = int(takecommand())
            pywhatkit.sendWhatmsg("+998997212897", msg, hour, min, 20)
            Speak("Ok Aziz , Yuborildi Whatsapp sms !")

        else:
            Speak("Telefon nomerini ayting!")
            phone = int(takecommand())
            ph = '+998' + phone
            Speak("Sms nomini ayting!")
            msg = takecommand()
            Speak("Vaqtni ayting Aziz!")
            Speak("Soat uslubida!")
            hour = int(takecommand())
            Speak("Vaqt minutda!")
            min = int(takecommand())
            pywhatkit.sendWhatmsg(ph, msg, hour, min, 20)
            Speak("Ok Aziz , Yuborildi Whatsapp sms !")

    def OpenApps():
        Speak("Ok Aziz kutib turing!")

        if 'code' in query:
            os.startfile(
                "C:\\Users\\user\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")

        elif 'telegram' in query:
            os.startfile(
                "C:\\Users\\user\\AppData\\Roaming\\Telegram Desktop\\Telegram.exe")

        elif 'chrome' in query:
            os.startfile(
                "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")

        elif 'facebook' in query:
            webbrowser.open('https://www.facebook.com/')

        elif 'instagram' in query:
            webbrowser.open('https://www.instagram.com/')

        elif 'xarita' in query:
            webbrowser.open(
                'https://www.google.com/maps/@41.2778496,69.2289536,12z')

        elif 'yutub' in query:
            webbrowser.open('https://www.youtube.com')

        Speak("Sizning komandangiz tugadi Aziz!")

    def Dict():
        Speak("Aktivlashtirildi!")
        Speak("Bitta so'z ayting!")
        probl = takecommand()

        if 'meaning' in probl:
            probl = probl.replace("Bu nima", "")
            probl = probl.replace("ReAnny", "")
            probl = probl.replace("of")
            probl = probl.replace("ma'nosi", "")
            result = Diction.meaning(probl)
            Speak(f"Ma'nosi uchun {probl} {result}")

        elif 'synonym' in probl:
            probl = probl.replace("Bu nima", "")
            probl = probl.replace("ReAnny", "")
            probl = probl.replace("of")
            probl = probl.replace("sinonimi", "")
            result = Diction.synonym(probl)
            Speak(f"Sinonimi uchun {probl} {result}")

        elif 'antonym' in probl:
            probl = probl.replace("Bu nima", "")
            probl = probl.replace("ReAnny", "")
            probl = probl.replace("of")
            probl = probl.replace("antonimi", "")
            result = Diction.antonym(probl)
            Speak(f"Antonimi uchun {probl} {result}")

        Speak("lug'atdan chiqdi!")

    def CloseAPPS():
        Speak("Ok Aziz kutib turing!")

        if 'youtube' in query:
            os.system("TASKILL /F /im chrome.exe")

        elif 'chrome' in query:
            os.startfile("TASKILL /F /im chrome.exe")

        elif 'telegram' in query:
            os.startfile("TASKILL /C /im Telegram.exe")

        elif 'code' in query:
            os.system("TASKILL /F /im code.exe")

        elif 'instagram' in query:
            os.system("TASKILL /F /im chrome.exe")

        Speak("Sizning komandangiz tamomlandi")

    def YoutubeAuto():
        Speak("Sizning komandangiz nima ?")
        comm = takecommand()
        if 'pause' in comm:
            keyboard.press('Dj green Rasvo')

        elif 'restart' in comm:
            keyboard.press('0')

        elif 'mute' in comm:
            keyboard.press('m')

        elif 'skip' in comm:
            keyboard.press('l')

        elif 'back' in comm:
            keyboard.press('j')

        elif 'full screen' in comm:
            keyboard.press('f')

        elif 'film mode' in comm:
            keyboard.press('t')

        Speak("Bo'ldi Aziz")

    def ChromeAuto():
        Speak("Chrome Automation boshlandi!")

        command = takecommand()

        if 'close this tab' in command:
            keyboard.press_and_release('ctrl + w')

        elif 'open new tab' in command:
            keyboard.press_and_release('ctrl + t')

        elif 'open new window' in command:
            keyboard.press_and_release('ctrl + n')

        elif 'historiy' in command:
            keyboard.press_and_release('ctrl +h')

    while True:

        query = takecommand()

        if 'salom laylo' in query:
            Speak("Salam Azizbek, Men Laylo ismli qizaloqman ")
            Speak("Men Sizning yordamchingizman!")
            Speak("Qanday yordam kerak?")

        elif 'qalaysan' in query:
            Speak("Man yaxshiman Aziz")
            Speak("Nima gaaap")

        elif 'siz buzmoqchimisiz' in query:
            Speak("Ok Aziz, Biron narsa demoqchimisiz")
            break

        elif 'huu' in query:
            Speak("Axmoqmisiz Azizbek!")

        elif 'youtube search' in query:
            Speak("Ok Azizbek, Nima Haqida?")
            query = query.replace("ReAnny", "")
            query = query.replace("youtube search", "")
            web = 'https://www.youtube.com/results?search_query' + query
            webbrowser.open(web)
            Speak("Bo'ldi Aziz")

        elif 'izlash' in query:
            Speak("Nimani izlash kerak?")
            query = query.replace("ReAnny", "")
            query = query.replace("google searcher!", "")
            pywhatkit.search(query)
            Speak("Bo'ldi Aziz")

        elif 'website' in query:
            Speak("Ok Aziz, Izliman...")
            query = query.replace("ReAnny", "")
            query = query.replace("website", "")
            web1 = query.replace("Ochish", "")
            web2 = 'https://www.' + web1 + '.com'
            webbrowser.open(web2)
            Speak("Bajarildi!")

        elif 'launch' in query:
            Speak("Website nomini ayting menga!")
            name = takecommand()
            web = 'https://www.' + name + '.com'
            webbrowser.open(web)
            Speak("Bajarildi Azizbek!")

        elif 'musiqa' in query or 'aziza' in query:
            Music()

        elif 'wikipedia' in query:
            Speak("Izlanmoqda Wikipedia!")
            query = query.replace("ReAnny", "")
            query = query.replace("wikipedia", "")
            wiki = wikipedia.summary(query, 2)
            Speak(f"Wikipediaga ko'ra : {wiki}")

        elif 'whatsapp sms' in query:
            Whatsapp()

        elif 'screenshot' in query:
            aa = pyautogui.screenshot()
            aa.save('D:\\scrre')

        elif 'open facebook' in query:
            OpenApps()

        elif 'open instagram' in query:
            OpenApps()

        elif 'xaritani och' in query:
            OpenApps()

        elif 'code' in query:
            OpenApps()

        elif 'yutubni och' in query:
            OpenApps()

        elif 'open telegram' in query:
            OpenApps()

        elif 'open chrome' in query:
            OpenApps()

        elif 'close chrome' in query:
            CloseAPPS()

        elif 'close telegram' in query:
            CloseAPPS()

        elif 'close instagram' in query:
            CloseAPPS()

        elif 'close facebook' in query:
            CloseAPPS()

        elif 'restart' in query:
            keyboard.press('0')

        elif 'mute' in query:
            keyboard.press('m')

        elif 'skip' in query:
            keyboard.press('l')

        elif 'back' in query:
            keyboard.press('j')

        elif 'full screen' in query:
            keyboard.press('f')

        elif 'film mode' in query:
            keyboard.press('t')

        elif 'youtube tool' in query:
            YoutubeAuto()

        elif 'close this tab' in query:
            keyboard.press_and_release('ctrl + w')

        elif 'open new tab' in query:
            keyboard.press_and_release('ctrl + t')

        elif 'open new window' in query:
            keyboard.press_and_release('ctrl + n')

        elif 'historiy' in query:
            keyboard.press_and_release('ctrl +h')

        elif 'chrome automation' in query:
            ChromeAuto()

        elif 'joke' in query:
            get = pyjokes.get_joke()
            Speak(get)

        elif 'takrorla' in query:
            Speak("Gapiring Aziz")
            jj = takecommand()
            Speak(f"Sizning so'z : {jj}")

        elif 'mening joylashuvim' in query:
            Speak("Ok Azizbek")
            webbrowser.open(
                'https://www.google.com/maps/@41.2778496,69.2289536,12z')

        elif 'dictionary' in query:
            Dict()

        elif 'xayr' in query:
            Speak("Ok Azizbek, Sog' bo'ling!")
            break


TaskExe()
