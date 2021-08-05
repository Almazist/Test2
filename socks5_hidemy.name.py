
import os
import sys
import time
import traceback
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

my_getdir = os.path.dirname(os.path.abspath(__file__))
print(my_getdir)

print()

try:
    proxy = []

    options = Options()
    # options.add_argument("--headless") # скрытый режим
    # options.add_argument("window-size=10,5")

    options.binary_location = "D:\\Program Files\\GoogleChromePortable\\App\\Chrome-bin\\chrome.exe"
    browser = webdriver.Chrome(options=options, executable_path=my_getdir+r'\\chromedriver.exe')

    # browser.minimize_window()
    #browser = webdriver.PhantomJS(r'D:\Program Files\phantomjs-2.1.1-windows\bin\phantomjs.exe')
    browser.get('https://hidemy.name/ru/proxy-list/')
    #browser.set_window_position(345, 0)
    i = 0
    while True:
        element = browser.find_elements_by_class_name("inner")
        if len(element) > 0:
            browser.find_element_by_xpath("//span[text()='Socks 5']").click()
            actions = ActionChains(browser)
            actions.send_keys(Keys.PAGE_DOWN)
            actions.perform()
            actions = ActionChains(browser)
            actions.send_keys(Keys.UP)
            actions.perform()
            browser.find_element_by_xpath('//button[@class="btn_1 blue_btn"]').click()

            element = browser.find_element_by_xpath('//tbody').text

            i = 0
            while True:
                i += 1
                print('Page '+str(i))
                l = []
                l = element.split("\n\r")
                with open(my_getdir+"\\element.txt", "w", encoding="utf-8") as file:
                    print(*l, file=file)

                with open(my_getdir+"\\element.txt", 'r') as f:
                    l = f.read().splitlines()

                for s in l:
                    if s.find('.') > -1:
                        d = dict.fromkeys(s, 0)
                        for c in s:
                            d[c] += 1
                        if d['.'] > 2:
                            s = s.replace(' ', ':')
                            k = s.find(':')
                            k = s.find(':', k+1)
                            s = s[0:k]
                            print(s)
                            proxy.append(s)

                element = browser.find_elements_by_xpath('//li[@class="next_array"]')
                if len(element) > 0:
                    element[0].click()
                    element = browser.find_element_by_xpath('//tbody').text
                else:
                    break
                time.sleep(5)
            break
        else:
            i += 1
            if i > 10:
                break
            print()
            print("timeout")
            time.sleep(5)
            print('Обновляем страницу')
            browser.refresh()

            #screenshot = browser.save_screenshot(my_getdir+"\\my_screenshot.png")

    print()

except:
    print(traceback.format_exc())
finally:
    browser.quit()


print()
p = []
if os.path.isfile(my_getdir+"\\proxy.txt"):
    with open(my_getdir+"\\proxy.txt", 'r') as f:
        p = f.read().splitlines()


i = 0
for s in proxy:
    if s not in p:
        p.append(s)
        i += 1

with open(my_getdir+"\\proxy.txt", "w") as f:
    for s in p:
        f.write(str(s) + '\n')

print("Added: "+str(i))
print("OK")
time.sleep(5)
