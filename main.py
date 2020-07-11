from selenium import webdriver
from colorama import Fore, Back, Style
from colorama import init
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
#imports all necesary library

chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(options=chrome_options)
start_url = "https://covid19ph.com/"
driver.get(start_url)
driver.implicitly_wait(10)

init(autoreset=True)
print(Style.BRIGHT + Fore.GREEN + "CSP ERROR MIGHT APPEAR JUST IGNORORE")
loop = True

while loop == True:

    def latest():#get latest cases
        latest_xpath = driver.find_element_by_xpath('//*[@id="mainapp"]/div[2]/div[1]/div[2]/div/div/div[1]/div[2]/div/h3')
        latest_list = latest_xpath.text
        return latest_list 
        
    def recovered():# get recovered cases
        recovered_xpath = driver.find_element_by_xpath('//*[@id="mainapp"]/div[2]/div[1]/div[5]/div/div/div[1]/div[2]/div/h3')
        recovered_list =  recovered_xpath.text
        return recovered_list

    def deaths():# get all deaths
        deaths_xpath = driver.find_element_by_xpath('//*[@id="mainapp"]/div[2]/div[1]/div[4]/div/div/div[1]/div[2]/div/h3')
        deaths_list =  deaths_xpath.text
        return deaths_list 

    def active():# get all active cases
        active_xpath = driver.find_element_by_xpath('//*[@id="mainapp"]/div[2]/div[1]/div[3]/div/div/div[1]/div[2]/div/h3')
        active_list = active_xpath.text
        return active_list

    def seeall():# get all 
        latest() # run latest
        recovered()# run recovered
        deaths()# run Deaths
        print(Style.BRIGHT + Back.GREEN + "Recovered", recovered_list)# print recovered
        print(Style.BRIGHT + Back.YELLOW + "Cases", latest_list)# print latest cases
        print(Style.BRIGHT + Back.RED + "Deaths", deaths_list)# print latest death list 
        print(Style.BRIGHT + Back.YELLOW + "Active Cases", active_list)# print all active cases

    latest_list = latest() # latest list is inside of latest function
    recovered_list = recovered()# recovered list is inside of recoverd function
    deaths_list = deaths()# deaths list is inside of deaths function
    active_list = active()# active list is inside of active function
    for i in range (2):
        print("\n")

    user_input = input("use /help to see all of the commands: ")
    if user_input == "/help":
        print(Fore.CYAN + Style.BRIGHT + """
        /all = view all confirmed cases recoveries and deaths
        /deaths = view all confirmed deaths
        /recover = view all confirmed recoveries
        /cases = view all confirmed cases
        /active = view all active cases
        /quit = quit the aplication
        """)
        print(Back.MAGENTA + "I am planing to add support to firefox")

    if user_input == "/deaths":
        print(Style.BRIGHT + Back.RED + "Deaths", deaths_list)

    if user_input == "/recover":
        print(Style.BRIGHT + Back.GREEN + "Recovered", recovered_list)

    if user_input == "/cases":
        print(Style.BRIGHT + Back.YELLOW + "Cases", latest_list)

    if user_input == "/active":
        print(Style.BRIGHT + Back.YELLOW + "Active Cases", active_list)

    if user_input == "/all":
        seeall()
        
    if user_input == "/quit":
        driver.quit()
        loop = False
