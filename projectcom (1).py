# Function for speech recognition

import speech_recognition as sr
import pyttsx

engine = pyttsx.init()
engine.setProperty('rate', 120)

def speak(text):
    engine.say(text)
    engine.runAndWait()

r = sr.Recognizer()

def listen():
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        speak("Speak Now")
        audio = r.listen(source)

        # Speech recognition using Google Speech Recognition

    try:
        return r.recognize_google(audio)
            # or: return recognizer.recognize_google(audio)
    except sr.UnknownValueError:
        speak("Could not understand audio")
    except sr.RequestError as e:
        print("Recog Error; {0}".format(e))

    return ""

#Read file
import pandas as pd
data=pd.read_csv('C:\Users\HP\Desktop\inventory.csv')

#data
# Asking Product and its parameters

item=" "
color=" "
size=" "
brand=" "
link=" "

def product():
    
#     def gen():
#         global gender
#         speak("Please select your gender, m for male , f for female?")
#         gender=listen().encode('ascii')
#         print gender
#         speak(("Your selected gender is",gender,"is that correct?"))
#         ans=listen()
#         if ans=="no":
#             gen()
#         else:
#             return
    
    speak("Welcome to Everyone Abled")
    def prod():
        ans=None
        global item
        speak("What are you planning to buy today?")
        item=listen().encode('ascii')
        
        if item!="shirt" and item!="shoes" and item!="pants":
         speak((item,"is not present in the inventory"))
         prod()
        else:
         print item
         speak(("Your selected item is",item,"is that correct?"))
         ans=listen()
        
        if ans=="no":
            prod()
        else:
            return
    
    def col():
        global color
        speak("What is your colour preference?")
        color=listen().encode('ascii')
        print color
        speak(("Your selected color is",color,"is that correct?"))
        ans=listen()
        if ans=="yes":
            return
        else:
            col()
    
    def siz():
        global size
        speak("What is your size preference?")
        size=listen().encode('ascii')
        print size
        speak(("Your selected size is",size,"is that correct?"))
        ans=listen()
        if ans=="yes":
            return
        else:
            siz()
        
    def bran():
        global brand
        speak("What is your brand preference?")
        brand=listen().encode('ascii')
        print brand
        speak(("Your selected brand is",brand,"is that correct?"))
        ans=listen()
        if ans=="yes":
            return
        else:
            bran()
   
#     gen()    
    prod()
    col() 
    siz()
    bran()
         
    print item,color,size,brand
    speak(("You are looking for a",item,"having color",color,"size",size,"and brand",brand))
    #speak(("Colour",color,"size",size,"brand",brand))
    speak("Do you confirm?")
    ans=listen()
    if ans=="no":
        product()
    elif  ans=="yes":
        speak("Wait while we check the availability of your desired item")
        

product()
        


# Matching Product with Inventory

def prod_match():
    matched_items={}
    cnt=1
    for index, row in data.iterrows():
        if  row['item'].lower()==item and row['size'].lower()==size and row['brand'].lower()==brand and row['colour'].lower()==color:
            matched_items[cnt]=row
            cnt=cnt+1
#         row['gender'].lower==gender and
        
    #if len(matched_items) >1 and len(matched_items) <3:
        #speak(("There are",len(matched_items)," items available matching your discription"))
        #for i in matched_items.keys():
            #speak(( i,"is priced at",matched_items[i]['Price']," rupees with an average rating of",matched_items[i]['Rating']))
            #speak("Please enter your desired preference")
            #pref=listen()
    
    global dataf
    dataf=pd.DataFrame(matched_items.values())
    print dataf
    speak(("There are",len(matched_items)," items available matching your discription"))
    
    def confirm():
            speak(("The best product is priced at",df1.iloc[0]['price']," rupees with an average rating of",df1.iloc[0]['rating']) )
            speak("Do you confirm?")
            ans=listen()
            if ans=="yes":
                global link
                link=df1.iloc[0]['link']
                print link
                speak("We will now shop for you on amazon.in with your login credentials")
            else:
                confirm()
    
    
    if len(matched_items) >1:
        
        speak("Which parameter do you want to sort on? , price or rating")
        pref=listen().encode('ascii')
        print pref
        if pref=="rating":
            df1=dataf.sort_values(['rating'],ascending=[False])

        elif pref=="price":
            df1=dataf.sort_values(['price'],ascending=[True])
            
        else:
            df1=dataf
            
        print df1
        
        confirm()
        
        
    elif len(matched_items)==1:
        
        confirm()
        
        
        
prod_match()      

# Step By Step (Crawl)

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
binary = FirefoxBinary("C:\\Users\\E062685\Documents\\software\\v45.1.0\\FirefoxPortableESR\\App\\Firefox\\firefox.exe")
driver = webdriver.Firefox(firefox_binary=binary)
driver.implicitly_wait(30)
driver.maximize_window()
# Opening Item purchased link
driver.get(link)
#clicking on buy now button
driver.find_element_by_xpath('//*[@id="buy-now-button"]').click()
#Putting Signin information
username = driver.find_element_by_xpath('//*[@id="ap_email"]')
password = driver.find_element_by_xpath('//*[@id="ap_password"]')
username.send_keys("9868248800")
password.send_keys("akashban")
driver.find_element_by_xpath('//*[@id="signInSubmit"]').click()
#driver.find_element_by_xpath('//*[@id="address-book-entry-0"]/div[2]/span/a').click()
driver.find_element_by_xpath('//*[@id="payment-change-link"]').click()

payment=driver.find_element_by_xpath('//*[@id="pm_0"]')
payment.click()
cv = driver.find_element_by_xpath('//*[@id="existingCvvNum"]')
speak("Please tell your cvv")
cvv=listen()
cv.send_keys(cvv)
cv.submit() 
# Place your order button
driver.find_element_by_xpath('//*[@id="order-summary-box"]/div[1]/div/div[1]/div/span/span/input').click()
# OTP and Submit

otp=driver.find_element_by_xpath('//*[@id="txtOtpPassword"]')
speak("Please tell your otp")
ot=listen() 
otp.send_keys(ot)
driver.find_element_by_xpath('//*[@id="cmdSubmit"]').click()



