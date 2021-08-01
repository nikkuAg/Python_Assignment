import mysql.connector
import time
from selenium import webdriver
from getpass import getpass
from selenium.webdriver.common.by import By
from webdriver_manager import driver

# Making connection to mysql
mydb = mysql.connector.connect(
    host="localhost",
    user="divyansh",
    password="divyansh",
    database="python_Assignment"
)


def resetDatabase():
    mycursor = mydb.cursor()
    sql = "UPDATE users SET Name='NULL', City='NULL', Work='NULL', Scrapped='0';"
    mycursor.execute(sql)
    mydb.commit()


def decorator(func):
    def checkUsername(username):
        mycursor = mydb.cursor()
        # Checking if the table exists in database
        sql = "SHOW TABLES;"
        mycursor.execute(sql)
        global exit
        exit = 0
        result = mycursor.fetchall()
        for row in result:
            if 'users' in row:
                exit = 1
                break
        if exit == 0:
            # Creating the table if not present in database
            sql = "CREATE TABLE users (username varchar(255), Name varchar(255), City varchar(255), Work varchar(255), Scrapped int);"
            mycursor.execute(sql)
            mydb.commit()
            sql = "INSERT INTO users (username, Scrapped) VALUES ('radhikagarg1601', 0), ('ritvik.jain.52206', 0), ('rishi.ranjan.54966', 0), ('utkarsh.parkhi.1', 0), ('anshul.d.sharma.7', 0);"
            mycursor.execute(sql)
            mydb.commit()
            exit = 1
        if exit == 1:
            # Checking if username exists in database
            sql = "SELECT * FROM users WHERE username = '" + str(username) + "'"
            mycursor.execute(sql)
            result = mycursor.fetchall()
            if(result != []):
                return func(username)
            else:
                raise Exception("This username does not exist.")
    return checkUsername


class Person:
    def __init__(self, n, c="Roorkee", w=[]):
        self.name = n
        self.city = c
        self.work = w

    def show(self):
        print("My name is {} and my current city is {}.".format(self.name, self.city))


Flogin = 0


@decorator
def scrap(username):
    global Flogin
    if (Flogin == 0):
        facebookLogin(Lusername, Lpassword)
        Flogin = 1
    time.sleep(2)
    mycursor = mydb.cursor()
    sql = "SELECT * FROM users WHERE username='" + username + "';"
    mycursor.execute(sql)
    result = mycursor.fetchone()
    if result[4] == 0:
        URL = "https://m.facebook.com/{}".format(username) + "/about"
        driver.get(URL)
        time.sleep(2)
        # Scrapping Name
        name = driver.find_element(By.XPATH, '//*[@id="MChromeHeader"]/div/div[3]/a').text
        # Scrapping City
        city = driver.find_element(By.XPATH, '//*[@id="living"]//h4').text
        workCount = len(driver.find_elements(By.XPATH, '//*[@id="work"]/div/*'))
        work = []
        x = 1
        # Scrapping Work
        while(x <= workCount):
            work.append(driver.find_element(By.XPATH, '//*[@id="work"]/div/div[' + str(x) + ']//span').text)
            x += 1
        dataWork = str(work).replace('[', '').replace("'", "").replace(']', '')
        getFullPage()
        driver.find_element(By.XPATH, '//div[div[div[text()="Likes"]]]/div[3]/a').click()
        time.sleep(2)
        likePage = len(driver.find_elements(By.XPATH, '//*[@id="timelineBody"]/div/div/div/*[div]'))
        x = 2
        favourites = {}
        # Scrapping Favourites
        while(x <= likePage):
            header = str(driver.find_element(By.XPATH, '//*[@id="timelineBody"]/div/div/div/div[' + str(x) + ']//header//div[text()]').text)
            driver.find_element(By.XPATH, '//*[@id="timelineBody"]/div/div/div/div[' + str(x) + ']//header//a').click()
            time.sleep(2)
            y = 1
            key = []
            if(header != 'SPORTS TEAMS' and header != 'SPORTSPEOPLE'):
                totalItems = len(driver.find_elements(By.XPATH, '//*[@id="timelineBody"]/div/div/div/div/*'))
                while y <= totalItems:
                    key.append(driver.find_element(By.XPATH, '//*[@id="timelineBody"]/div/div/div/div/div[' + str(y) + ']//div[@class="content"]/div[1]').text)
                    y += 1
            else:
                totalItems = len(driver.find_elements(By.XPATH, '//*[@id="timelineBody"]/div/div/div/div/div/*'))
                while y <= totalItems:
                    key.append(driver.find_element(By.XPATH, '//*[@id="timelineBody"]/div/div/div/div/div/div[' + str(y) + ']//span').text)
                    y += 1
            favourites.update({header: key})
            driver.back()
            x += 1
        print("List of favourities of " + str(name) + " are:")
        print()
        for z in favourites:
            print(z + " :  " + str(favourites[z]))
            print()
        mycursor = mydb.cursor()
        sql = "UPDATE users SET Name='" + name + "', City='" + city + "', Work='" + dataWork + "', Scrapped='1' WHERE username='" + username + "';"
        mycursor.execute(sql)
        mydb.commit()

        return "Scrapped"
    else:
        sql = "SELECT * FROM users WHERE username='" + username + "';"
        mycursor.execute(sql)
        result = mycursor.fetchone()
        name = result[1]
        city = result[2]
        workStr = str(result[3])
        work = workStr.split(",")
        myobj = Person(name, city, work)
        myobj.show()

        return "Show function"


def getFullPage():
    SCROLL_PAUSE_TIME = 7
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(SCROLL_PAUSE_TIME)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height
    time.sleep(2)


def facebookLogin(username, password):
    driver.get("https://m.facebook.com/login/?next&ref=dbl&fl&refid=8")
    element = driver.find_element(By.XPATH, '//*[@id="locale-selector"]/div/div[1]/div[3]/span/a')
    element.click()
    time.sleep(2)
    userInput = driver.find_element(By.XPATH, '//*[@id="m_login_email"]')
    userInput.send_keys(username)
    passInput = driver.find_element(By.XPATH, '//*[@id="m_login_password"]')
    passInput.send_keys(password)
    signButton = driver.find_element(By.XPATH, '//*[@id="login_password_step_element"]/button')
    signButton.click()
    time.sleep(4)
    if driver.current_url == "https://m.facebook.com/login/?next&ref=dbl&fl&refid=8":
        raise Exception("Incorrect Login Credentials")
    elif driver.current_url == "https://m.facebook.com/login/save-device/?login_source=login#_=_":
        driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/div/div[2]/div[3]/div[1]/div/div/a').click()


Lusername = input("Enter your facebook username: ")
Lpassword = getpass("Enter your password: ")


time.sleep(1)


driver = webdriver.Chrome(executable_path="/usr/bin/chromedriver")
time.sleep(2)
driver.maximize_window()
time.sleep(1)
