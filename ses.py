import playsound
import  speech_recognition as sr
from gtts import gTTS
import random
import webbrowser                                                                    
import datetime                                   
import webbrowser                                
import os.path
import pyautogui 
import webbrowser
import time
import pyaudio
from random import choice
import colorama
from colorama import Fore, Back, Style 
from dist import Arduino
import os
from pymata4 import pymata4
#GEREKLİ KÜTÜPHANELER


print (Fore.RED)
print('────────██████████████████████───────')
print('──────██████████████████████████──────')
print('────██████████████████████████████────')
print('────████████████████████████████████──')
print('──████████▒▒▒▒██████████████████████──')
print('──██████▒▒▒▒▒▒▒▒██▒▒▒▒▒▒▒▒██████████──')
print('──██████▒▒▒▒██▒▒▒▒▒▒▒▒██▒▒▒▒██████████')
print('██████▒▒▒▒▒▒██▒▒▒▒▒▒▒▒██▒▒▒▒████▒▒████')
print('██████▒▒▒▒▒▒██▒▒▒▒▒▒▒▒██▒▒▒▒██▒▒▒▒████')
print('██████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██████')
print('██████▒▒░░░░▒▒██▒▒▒▒██▒▒░░░░▒▒████████')
print('████████░░░░▒▒▒▒████▒▒▒▒░░░░██████████')
print('████████████▒▒▒▒▒▒▒▒▒▒▒▒██████████████')
print('──██──████████████▒▒▒▒██████████──██──')
print('────────────────██▒▒▒▒██──────██──────')

def konuş(yazı: object) -> object:
    tts = gTTS(text = yazı, lang= "tr")
    dosya_ismi = "ses"+ str(random.randint(0,1000000000000000000000)) + ".mp3"
    tts.save(dosya_ismi)
    playsound.playsound(dosya_ismi)  
    os.remove(dosya_ismi)
    
  
konuş('Merhaba efendim,nasıl yardımcı olabilirim')
    

def sesi_kaydet():
    r = sr.Recognizer()
    with sr.Microphone() as kaynak:
        r.energy_threshold = 1000
        print('Dinleniyor...')
       
        ses = r.listen(kaynak)
        
        söylenen_cümle = ""

        try:
            print('Tanımlanıyor...')
            söylenen_cümle = r.recognize_google(ses, language="Tr-tr")
            print(f'Söylenen komut: {söylenen_cümle}\n')

        except Exception:
            print("söylediğiniz cümleyi anlayamadım")
        
        except sr.RequestError:
            konuş('Sistemin çalışmıyor')

    return söylenen_cümle


while True:
    yazı = sesi_kaydet()
    
    if "nasılsın" in yazı:
        konuş("iyiyim siz nasılsınız")

    elif 'Google aç' in yazı:
            konuş("Google'ı açıyorum efendim.")
            webbrowser.open('https://google.com')
            
    elif 'YouTube aç' in yazı :
            konuş("Youtube'u açıyorum efendim.")
            webbrowser.open('https://www.youtube.com/')
                       
    elif 'saat kaç' in yazı :
            strtime = datetime.datetime.now().strftime('%H:%M:%S')
            konuş(f'efendim saat {strtime}')
                      
    elif 'bilgisayar bakımı aç' in yazı :
            konuş('bilgisayar bakımı açıyorum efendim')
            os.startfile("C:\BilgisayarBakım\Bilgisayar Bakım.exe")
    
    elif "Tarayıcıyı kapat" in yazı:
      konuş('tarayıcıyı kapatıyorum efendim')
      os.system("TASKKILL /F /IM msedge.exe")
      os.system("taskkill /f /im opera.exe")
      os.system("taskkill /f /im chrome.exe")
               
    elif "çal" in yazı:
        
        kelimeler = yazı.split(" ")

        url = "https://www.youtube.com/results?search_query="

        for kelime in kelimeler:
          url = url + kelime + "+"
          
        konuş('İstediğiniz şeyi çalıyorum efendim')
        webbrowser.open_new_tab(url)
        time.sleep(12.5)
        pyautogui.click(934, 315 , clicks=2)
                  
    elif "ara" in yazı:
        konuş('İstediğiniz şeyi arıyorum efendim')
        kelimeler = yazı.split(" ")
        url = "https://www.google.com/search?q="
        for kelime in kelimeler:
          url = url + kelime + "+"
        webbrowser.open_new_tab(url)
            
    elif "kaç" in yazı:
    
        kelimeler = yazı.split(" ")
        url = "https://www.google.com/search?q="
        for kelime in kelimeler:
          url = url + kelime + "+"
        webbrowser.open_new_tab(url)
    
    elif "seni oluşturan kim" in yazı:
         konuş('Beni oluşturup geliştiren kişinin ismi Emre Özcandır') 
    
    elif "Bilgisayarı kapat" in yazı:
      konuş('bilgisayarınız 5 saniye içinde kapanacaktır efendim')
      os.system("shutdown /s /t 5")   
     
    elif "not et" in yazı:
     r = sr.Recognizer()
     with sr.Microphone() as source:
       print("Şimdi söyleyiniz.")
       r.pause_threshold = 2
       audio = r.listen(source)
      
     try:
       dosya = open("a.txt","w",encoding="utf-8")
       yazı = r.recognize_google(audio, language="Tr-tr")
       print(yazı,file=dosya)
       dosya.close()
       konuş('not ettim efendim')
       
     except sr.UnknownValueError:
       print("Anlayamadım efendim. ")
          
    elif 'tamamdır' in yazı:
            konuş('tamam efendim.Görüşürüz')
            quit()    
    elif 'Fıkra anlat' in yazı:
        fıkralar = ["Delikanlı çalıştığı şirketin mektuplarını postalayacaktı. Postacı mektuplardan birisini tartıp; 'Bu çok ağır!' dedi. 'Biraz daha pul yapıştırmamız lazım.'Delikanlı:Abi!' dedi. 'O zaman daha ağır olmaz mı?'",
                    "Temel aldığı bir daktiloyu bozuk diye geri götürdü. Satıcı;- Neresi bozuk, dün aldığında sağlamdı.Temel:İki tane 'a' yok, saat yazamıyorum.",
                    "Adam, papağanını gümrükten kolay geçirebilmek için bir kutuya koymuş, üstüne de 'kırılacak eşya' diye yazmıştı.Gümrük memuru yazıyı okuyunca, kutuyu şöyle bir silkelemeye başladı. Aynı anda içeriden papağanın bağırdığı duyuldu.'Şangur şungur.. Şangur şungur..'",
                    "Platonik aşk yaşayan adamın birinin hayalleri gerçek olur; en çok sevdiği yıldız ile karşı karşıyadır, fırsat bu fırsat derken yıldız bayana sorar: –Saçınızdan bir tutam bana verirseniz size 100 dolar veririm! Yıldız: –Hımmm 500 dolar verirsen bütün peruk senin olsun.",
                    "Bir deli hastenisnde herkes zıplıyor, Temel yerinden kımıldamıyormuş  Biz patlamış mısırız, ben tavanın altına yapışmışım.",
                    "Küçük çocuk okulun ilk günü sonunda eve döner. Annesi sorar;  Bugün okulda ne öğrendiniz? Çocuk cevaplar; Yeterli değil, yarın tekrar gitmem gerek",
                    "Karınca Ve Fil bir gün bir karınca bir file aşık olmuş. Annesi bu durumu onaylamamış  Karınca Bana değil karnımdakine acı, demiş.",
                    "Bektaşi'ye sormuşlar. Dünya öküzün boynuzlarının üstünde duruyormuş, ne diyorsun bu işe? Valla onu bilmem ama buna inanan öküzlerin olduğunu biliyorum, demiş.",
                    "Temel'in eldivenle yazı yazdığını görenler sormuş Niye eldivenli yazıyorsun zor olmuyor mu?  Zorluğuna zor ama el yazımın tanınmasını istemeyrum.",
                    "Bir toplantıda, bir genç, Mehmet Akif'i küçük düşürmek ister: - Afedersiniz, siz veteriner misiniz? Mehmet Akif hiç istifini bozmadan şöyle yanıtlamış:- Evet, bir yeriniz mi ağrıyordu?",
                    
                
                ]
        secimfık=choice(fıkralar)
        konuş(secimfık)

    elif 'led kapat' in yazı:
        konuş("ledi kapatıyorum")
        Arduino.led_islemleri(0)

    elif 'led yak' in yazı:
        konuş("ledi yakıyorum")
        Arduino.led_islemleri(1)
        
    
