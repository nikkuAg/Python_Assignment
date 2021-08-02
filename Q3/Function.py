from config import mydb
import constant
import time
from selenium import webdriver
from getpass import getpass
from selenium.webdriver.common.by import By
from webdriver_manager import driver



def resetDatabase():
    mycursor = mydb.cursor()
    mycursor.execute(constant.sqlRest)
    mydb.commit()


def decorator(func):
    def checkUsername(username):
        mycursor = mydb.cursor()
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
            mycursor.execute(constant.sqlcTable)
            mydb.commit()
            mycursor.execute(constant.sqliTable)
            mydb.commit()
            exit = 1
        if exit == 1:
            sql = constant.sqlSelect1 + username + "';"
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
    sql = constant.sqlSelect1 + username + "';"
    mycursor.execute(sql)
    result = mycursor.fetchone()
    if result[4] == 0:
        URL = "https://m.facebook.com/{}".format(username) + "/about"
        driver.get(URL)
        time.sleep(2)
        name = driver.find_element(By.XPATH, constant.namePath).text
        city = driver.find_element(By.XPATH, constant.cityPath).text
        workCount = len(driver.find_elements(By.XPATH, constant.workList))
        work = []
        x = 1
        while(x <= workCount):
            work.append(driver.find_element(By.XPATH, '//*[@id="work"]/div/div[' + str(x) + ']//span').text)
            x += 1
        dataWork = str(work).replace('[', '').replace("'", "").replace(']', '')
        getFullPage()
        driver.find_element(By.XPATH, constant.likePath).click()
        time.sleep(2)
        likePage = len(driver.find_elements(By.XPATH, constant.likesCount))
        x = 2
        favourites = {}
        while(x <= likePage):
            header = str(driver.find_element(By.XPATH, constant.header1 + str(x) + constant.header2).text)
            driver.find_element(By.XPATH, constant.headerPage1 + str(x) + ']//header//a').click()
            time.sleep(2)
            y = 1
            key = []
            if(header != 'SPORTS TEAMS' and header != 'SPORTSPEOPLE'):
                totalItems = len(driver.find_elements(By.XPATH, constant.itemsPath))
                while y <= totalItems:
                    key.append(driver.find_element(By.XPATH, constant.keyText1 + str(y) + constant.keyText2).text)
                    y += 1
            else:
                totalItems = len(driver.find_elements(By.XPATH, constant.item2Path))
                while y <= totalItems:
                    key.append(driver.find_element(By.XPATH, constant.keyImage1 + str(y) + ']//span').text)
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
        sql = constant.sqlSelect1 + username + "';"
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
    element = driver.find_element(By.XPATH, constant.englishPath)
    element.click()
    time.sleep(2)
    userInput = driver.find_element(By.XPATH, constant.userPath)
    userInput.send_keys(username)
    passInput = driver.find_element(By.XPATH, constant.passPath)
    passInput.send_keys(password)
    signButton = driver.find_element(By.XPATH, constant.loginButton)
    signButton.click()
    time.sleep(4)
    if driver.current_url == "https://m.facebook.com/login/?next&ref=dbl&fl&refid=8":
        raise Exception("Incorrect Login Credentials")
    elif driver.current_url == "https://m.facebook.com/login/save-device/?login_source=login#_=_":
        driver.find_element(By.XPATH, constant.loginNotNow).click()


Lusername = input("Enter your facebook username: ")
Lpassword = getpass("Enter your password: ")


time.sleep(1)


driver = webdriver.Chrome(executable_path="/usr/bin/chromedriver")
time.sleep(2)
driver.maximize_window()
time.sleep(1)
