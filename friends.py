from selenium import webdriver
import time
browser = webdriver.Chrome(executable_path='C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')
print("请你确保你的QQ已在电脑登录，当浏览器跳出快速登陆的时候选择你需要登录的QQ,每次只能爬取一个qq")
#inp = input("您的选择是：")
qq_id = input("输入你的qq账户：")
#qq_pass = input("输入你的qq密码：")
browser.get("https://qzone.qq.com/")
browser.maximize_window()
time.sleep(10)
browser.get("https://user.qzone.qq.com/"+str(qq_id)+"/profile/permit")
time.sleep(5)
browser.switch_to.frame("ttinfo")
browser.find_element_by_id('entry_desc').click()
time.sleep(2)
#如果你的好友超级多，不妨把这个值设置大一些
for i in range(20):
    browser.execute_script('document.getElementsByClassName("friends-detail friends-detail-visit qz-scrollbar")[0].scrollTop=10000')
    time.sleep(1)
for link in browser.find_elements_by_xpath("//*[@data-uin]"):
    print (link.get_attribute('data-uin'))
    with open(str(qq_id)+'.txt','a') as f:
        f.write(link.get_attribute('data-uin')+'\n')
        f.close()
print("okk")
