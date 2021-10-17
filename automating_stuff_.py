
import pandas
df = pandas.read_csv('/path/to/data.csv')


import time
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options  # for suppressing the browser
from twilio.rest import Client 
 
account_sid = '*************' #get from https://www.twilio.com/
auth_token = '************' #get from https://www.twilio.com/
client = Client(account_sid, auth_token) 

option = webdriver.ChromeOptions()
option.add_argument('headless')
option.add_argument('log-level=2')
driver = webdriver.Chrome("/path/to/chromdriver",options=option)

print("part1")

driver.get("https://intranet.tam.ch/")#after slash add your school's extension...example: kkn for kantonsschule küsnacht
#enters username
username = "/html/body/div[5]/div/form[1]/div[1]/fieldset/input[3]"
username_box = driver.find_element_by_xpath(username)
#enters the contacts name
username_box.send_keys("*")#replace asteric with your username

#enters password
password = "/html/body/div[5]/div/form[1]/div[1]/fieldset/input[4]"
password_box = driver.find_element_by_xpath(password )
password_box.send_keys("*")#replace asteric with your password

time.sleep(2)
#presses sumbmit button
submit="/html/body/div[5]/div/form[1]/div[1]/button"
sumbit_box = driver.find_element_by_xpath(submit )
sumbit_box.click()


#goes to the grade book
driver.get("https://intranet.tam.ch/kue/gradebook")




time.sleep(2)
print("part2")
for i in range(1,47,2):#website just built that way :/
    
    sub='//*[@id="gbl-grid"]/div[2]/table/tbody/tr['+str(i)+']/td[2]'
    sub_box = driver.find_element_by_xpath(sub)
    
    
    somethin='//*[@id="gbl-grid"]/div[2]/table/tbody/tr['+str(i)+']'
    somethin_box = driver.find_element_by_xpath(somethin)
    somethin_box.click()
    
    time.sleep(2)
    
    cell='//*[@id="gbl-grid"]/div[2]/table/tbody/tr['+str(i+1)+']/td[2]/div/div[2]'
    cell_box = driver.find_element_by_xpath(cell)

    

    if len(cell_box.text) != 0:


            
            
        if cell_box.text in df.grade:  
            pass
        else:

            
            #print("stuff",l,line)
            df = df.append({'subject':sub_box.text, 'grade':cell_box.text}, ignore_index=True)
            #sends message if new testscore is online
            message = client.messages.create(  
                                messaging_service_sid='MGcdeb7a7758875b116e1c85f889ec6b22', 
                                body=sub_box.text+" is online"+"\n"+cell_box.text,      
                                to='+41786481417'
                            ) 
   

print(df)
#updates csv file
df.to_csv("/Users/sim.singh/Desktop/coding/teams-bot/data_stuff/data.csv", index=False)
