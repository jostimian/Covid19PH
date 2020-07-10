from selenium import webdriver
from colorama import Fore, Back, Style
from colorama import init
from selenium.webdriver.chrome.options import Options
init(autoreset=True)
chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(options=chrome_options)
start_url = "http://www.covid19.gov.ph/"
driver.get(start_url)
loop = True
print(Style.BRIGHT + Fore.GREEN + "CSP ERROR MIGHT APPEAR JUST IGNORORE")
while loop == True:
    def latest():
        latest_xpath = driver.find_element_by_xpath('//*[@id="post-17"]/div/div/div/div/section[1]/div/div/div[2]/div/div/div[3]/div/div/div[1]/span[2]')
        latest_list = latest_xpath.text
        return latest_list 
    def recovered():
        recovered_xpath = driver.find_element_by_xpath('//*[@id="post-17"]/div/div/div/div/section[1]/div/div/div[2]/div/div/div[4]/div/div/div[1]/span[2]')
        recovered_list =  recovered_xpath.text
        return recovered_list
    def deaths():
        deaths_xpath = driver.find_element_by_xpath('//*[@id="post-17"]/div/div/div/div/section[1]/div/div/div[2]/div/div/div[5]/div/div/div[1]/span[2]')
        deaths_list =  deaths_xpath.text
        return deaths_list 
    def active():
        active_xpath = driver.find_element_by_xpath('//*[@id="post-17"]/div/div/div/div/section[1]/div/div/div[2]/div/div/div[2]/div/div/div[1]/span[2]')
        active_list = active_xpath.text
        return active_list
    def seeall():
        latest()
        recovered()
        deaths()
        print(Style.BRIGHT + Back.GREEN + "Recovered", recovered_list)
        print(Style.BRIGHT + Back.YELLOW + "Cases", latest_list)
        print(Style.BRIGHT + Back.RED + "Deaths", deaths_list)
        print(Style.BRIGHT + Back.LIGHTRED_EX + "Active Cases", active_list)
    latest_list = latest()
    recovered_list = recovered()
    deaths_list = deaths()
    active_list = active()
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
        print(Back.MAGENTA + "We I mean I already change the database")
    if user_input == "/deaths":
        print(Style.BRIGHT + Back.RED + "Deaths", deaths_list)
    if user_input == "/recover":
        print(Style.BRIGHT + Back.GREEN + "Recovered", recovered_list)
    if user_input == "/cases":
        print(Style.BRIGHT + Back.YELLOW + "Cases", latest_list)
    if user_input == "/active":
        print(Style.BRIGHT + Back.LIGHTRED_EX + "Active Cases", active_list)
    if user_input == "/all":
        seeall()
    if user_input == "/quit":
        driver.quit()
        loop = False
