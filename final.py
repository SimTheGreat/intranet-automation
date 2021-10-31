#to do: work with crontab to finish this
import pandas



import time
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options  # for suppressing the browser
from twilio.rest import Client 
 
account_sid = 'ACcbb619690de6f58b2cb75fb54476a38a' 
auth_token = '7374fbd0dbaf5c8aeff09a802e13397c' 
client = Client(account_sid, auth_token) 
def runnin():
    df = pandas.read_csv('/Users/sim.singh/Desktop/coding/teams-bot/data_stuff/data.csv')
    option = webdriver.ChromeOptions()
    option.add_argument('headless')
    option.add_argument('log-level=2')
    driver = webdriver.Chrome("/Users/sim.singh/Desktop/coding/whatsapp/chromedriver",options=option)
    print("part1")

    driver.get("https://intranet.tam.ch/kue")

    username = "/html/body/div[5]/div/form[1]/div[1]/fieldset/input[3]"
    username_box = driver.find_element_by_xpath(username)
    #enters the contacts name
    username_box.send_keys("samriddhi.singh")


    password = "/html/body/div[5]/div/form[1]/div[1]/fieldset/input[4]"
    password_box = driver.find_element_by_xpath(password )
    #enters the contacts name
    password_box.send_keys("Simsalabim(10)")
    time.sleep(2)
    submit="/html/body/div[5]/div/form[1]/div[1]/button"
    sumbit_box = driver.find_element_by_xpath(submit )
    sumbit_box.click()

    driver.get("https://intranet.tam.ch/kue/gradebook")



    #to do scrape this now
    time.sleep(2)
    print("part2")
    for i in range(1,47,2):
        
        sub='//*[@id="gbl-grid"]/div[2]/table/tbody/tr['+str(i)+']/td[2]'
        sub_box = driver.find_element_by_xpath(sub)
        
        
        somethin='//*[@id="gbl-grid"]/div[2]/table/tbody/tr['+str(i)+']'
        somethin_box = driver.find_element_by_xpath(somethin)
        somethin_box.click()
        
        time.sleep(2)
        
        cell='//*[@id="gbl-grid"]/div[2]/table/tbody/tr['+str(i+1)+']/td[2]/div/div[2]'
        cell_box = driver.find_element_by_xpath(cell)

        

        if len(cell_box.text) != 0:

            cell_g='//*[@id="gbl-grid"]/div[2]/table/tbody/tr['+str(i+1)+']/td[2]/div/div[2]/table/tbody/tr/td[1]'
            
            try:
                cell_g_box = driver.find_element_by_xpath(cell_g)
                
                
                
                if cell_g_box.text in df.title.unique():  
                    
                    pass
                else:

                    message = client.messages.create(  
                                    messaging_service_sid='MGcdeb7a7758875b116e1c85f889ec6b22', 
                                    body=sub_box.text+" is online"+"\n"+cell_box.text,      
                                    to='+41786481417'
                                ) 
                    
                    df = df.append({'subject':sub_box.text, 'grade':cell_box.text,"title":cell_g_box.text}, ignore_index=True)
                
                
            except Exception as e:
                print("An exception occurred: ", e) 
                

    


    df.to_csv("/Users/sim.singh/Desktop/coding/teams-bot/data_stuff/data.csv", index=False)
