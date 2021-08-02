
radhika = "radhikagarg1601"
anshul = "anshul.d.sharma.7"
utkarsh = "utkarsh.parkhi.1"
rishi = "rishi.ranjan.54966"
ritvik = "ritvik.jain.52206"


sqlRest = "UPDATE users SET Name='NULL', City='NULL', Work='NULL', Scrapped='0';"
sqlcTable = "CREATE TABLE users (username varchar(255), Name varchar(255), City varchar(255), Work varchar(255), Scrapped int);"
sqliTable = "INSERT INTO users (username, Scrapped) VALUES ('radhikagarg1601', 0), ('ritvik.jain.52206', 0), ('rishi.ranjan.54966', 0), ('utkarsh.parkhi.1', 0), ('anshul.d.sharma.7', 0);"

sqlSelect1 = "SELECT * FROM users WHERE username = '"

userPath = '//*[@id="m_login_email"]'
passPath = '//*[@id="m_login_password"]'
loginButton = '//*[@id="login_password_step_element"]/button'
englishPath = '//*[@id="locale-selector"]/div/div[1]/div[3]/span/a'
loginNotNow = '//*[@id="root"]/div[1]/div/div[2]/div[3]/div[1]/div/div/a'
namePath = '//*[@id="MChromeHeader"]/div/div[3]/a'
cityPath = '//*[@id="living"]//h4'
workList = '//*[@id="work"]/div/*'
likePath = '//div[div[div[text()="Likes"]]]/div[3]/a'
likesCount = '//*[@id="timelineBody"]/div/div/div/*[div]'
itemsPath = '//*[@id="timelineBody"]/div/div/div/div/*'
item2Path = '//*[@id="timelineBody"]/div/div/div/div/div/*'

header1 = '//*[@id="timelineBody"]/div/div/div/div['
header2 = ']//header//div[text()]'
headerPage1 = '//*[@id="timelineBody"]/div/div/div/div['
keyText1 = '//*[@id="timelineBody"]/div/div/div/div/div['
keyText2 = ']//div[@class="content"]/div[1]'
keyImage1 = '//*[@id="timelineBody"]/div/div/div/div/div/div['
