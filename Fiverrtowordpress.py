#Libraries
from tkinter import *
from selenium import webdriver
import webbrowser
import time
from selenium.webdriver.common.keys import Keys
import tkinter.font as font
import pickle



driver = webdriver.Chrome()


# Create root for our script
root=Tk()
root.title("Bot Fiverr to Wordpress")
root.geometry('400x300')
root.configure(background='#C000F9')



#create Entry to past link categorie fiverr when script start

enter_url_article=Label(text="Enter url of Categorie Fiverr : ", bg="#C000F9", fg="white")
enter_url_article.pack()
url_fiverr=Entry()
url_fiverr.pack()




#create Function and write all code inside it because we need it  
def my_machine():
        categorie_fiver = url_fiverr.get()
        affiliate_id=("https://track.fiverr.com/visit/?bta={your id}&brand=fiverrhybrid&landingPage=")

        html1 = """\
        <!-- wp:buttons {"align":"center"} -->
        <div class="wp-block-buttons aligncenter"><!-- wp:button {"borderRadius":2,"style":{"color":{"text":"#fffffa"}},"backgroundColor":"luminous-vivid-orange"} -->
        <div class="wp-block-button"><a class="wp-block-button__link has-luminous-vivid-orange-background-color has-text-color has-background" style="border-radius: 2px; color: #fffffa;" href="
        """
        html2 = """\
        "><strong>Check Service on Fiverr</strong></a></div>
        <!-- /wp:button --></div>
        <!-- /wp:buttons -->
        """
        code_img_part1 = '<img src="'
        code_img_part2 = '" alt="'
        code_img_part3 = '" />'


        # here we will browse categorie link
        driver.get(categorie_fiver)
        time.sleep(3)


        # here we will get description

        #we will use (try 7 except) to handle problems because sometimes fiverr uodate xpath
        try:
                title = driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div/div/div[2]/header/header/div[1]").text
                description = driver.find_element_by_name("description").get_attribute("content")
                print("title and description copied...")
        except:
                title = driver.find_element_by_class_name("title-wrapper").text
                description = driver.find_element_by_name("description").get_attribute("content")
                print("title and description copied...")
        time.sleep(3)

        # here we will get link of items (gigs) one by one
        try:
                item1 = driver.find_element_by_xpath(
                        "/html/body/div[2]/div[2]/div[2]/div/div/div[7]/div/div/div[1]/div/div/h3/a").get_attribute(
                        "href")

                print("item1 url copied...")

        except:
                pass
        time.sleep(3)
        try:
                item2 = driver.find_element_by_xpath(
                        "/html/body/div[2]/div[2]/div[2]/div/div/div[7]/div/div/div[2]/div/div/h3/a").get_attribute(
                        "href")
                print("item2 url copied...")


        except:
                pass
        time.sleep(3)
        try:
                item3 = driver.find_element_by_xpath(
                        "/html/body/div[2]/div[2]/div[2]/div/div/div[7]/div/div/div[3]/div/div/h3/a").get_attribute(
                        "href")
                print("item3 url copied...")

        except:
                pass
        time.sleep(3)
        try:
                item4 = driver.find_element_by_xpath(
                        "/html/body/div[2]/div[2]/div[2]/div/div/div[7]/div/div/div[4]/div/div/h3/a").get_attribute(
                        "href")
                print("item4 url copied...")

        except:
                pass
        time.sleep(3)
        try:
                item5 = driver.find_element_by_xpath(
                        "/html/body/div[2]/div[2]/div[2]/div/div/div[7]/div/div/div[5]/div/div/h3/a").get_attribute("href")
                print("item5 url copied...")

        except:
                pass
        time.sleep(3)
        try:
                item6 = driver.find_element_by_xpath(
                        "/html/body/div[2]/div[2]/div[2]/div/div/div[7]/div/div/div[6]/div/div/h3/a").get_attribute(
                        "href")
                print("item6 url copied...")

        except:
                pass
        time.sleep(3)
        try:
                item7 = driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div/div/div[7]/div/div/div[7]/div/div/h3/a").get_attribute(
                        "href")
                print("item7 url copied...")

        except:
                pass
        time.sleep(3)
        try:
                item8 = driver.find_element_by_xpath(
                        "/html/body/div[2]/div[2]/div[2]/div/div/div[7]/div/div/div[8]/div/div/h3/a").get_attribute(
                        "href")
                print("item8 url copied...")

        except:
                pass
        time.sleep(3)

        # here we will browser items one by one and copy title and description and image
        try:
                driver.get(item1)

                title1 = driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div/div[3]/div/div[1]/h1").text
                image1 = driver.find_element_by_xpath(
                        "/html/body/div[2]/div[2]/div[2]/div/div[3]/div/section/div[1]/div/div/div[1]/div/figure/img").get_attribute(
                        "src")
                description1 = driver.find_element_by_xpath(
                        "/html/body/div[2]/div[2]/div[2]/div/div[3]/div/div[3]/div/div[1]").text
                time.sleep(5)
        except:
                pass

        try:
                driver.get(item2)
                time.sleep(5)
                title2 = driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div/div[3]/div/div[1]/h1").text
                image2 = driver.find_element_by_xpath(
                        "/html/body/div[2]/div[2]/div[2]/div/div[3]/div/section/div[1]/div/div/div[1]/div/figure/img").get_attribute(
                        "src")
                description2 = driver.find_element_by_xpath(
                        "/html/body/div[2]/div[2]/div[2]/div/div[3]/div/div[3]/div/div[1]").text
                time.sleep(5)
        except:
                pass

        try:
                driver.get(item3)
                time.sleep(5)
                title3 = driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div/div[3]/div/div[1]/h1").text
                image3 = driver.find_element_by_xpath(
                        "/html/body/div[2]/div[2]/div[2]/div/div[3]/div/section/div[1]/div/div/div[1]/div/figure/img").get_attribute(
                        "src")
                description3 = driver.find_element_by_xpath(
                        "/html/body/div[2]/div[2]/div[2]/div/div[3]/div/div[3]/div/div[1]").text
                time.sleep(5)
        except:
                pass

        try:
                driver.get(item4)
                time.sleep(5)
                title4 = driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div/div[3]/div/div[1]/h1").text
                image4 = driver.find_element_by_xpath(
                        "/html/body/div[2]/div[2]/div[2]/div/div[3]/div/section/div[1]/div/div/div[1]/div/figure/img").get_attribute(
                        "src")
                description4 = driver.find_element_by_xpath(
                        "/html/body/div[2]/div[2]/div[2]/div/div[3]/div/div[3]/div/div[1]").text
                time.sleep(5)
        except:
                pass

        try:
                driver.get(item5)
                time.sleep(5)
                title5 = driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div/div[3]/div/div[1]/h1").text
                image5 = driver.find_element_by_xpath(
                        "/html/body/div[2]/div[2]/div[2]/div/div[3]/div/section/div[1]/div/div/div[1]/div/figure/img").get_attribute(
                        "src")
                description5 = driver.find_element_by_xpath(
                        "/html/body/div[2]/div[2]/div[2]/div/div[3]/div/div[3]/div/div[1]").text
                time.sleep(5)
        except:
                pass

        try:
                driver.get(item6)
                time.sleep(5)
                title6 = driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div/div[3]/div/div[1]/h1").text
                image6 = driver.find_element_by_xpath(
                        "/html/body/div[2]/div[2]/div[2]/div/div[3]/div/section/div[1]/div/div/div[1]/div/figure/img").get_attribute(
                        "src")
                description6 = driver.find_element_by_xpath(
                        "/html/body/div[2]/div[2]/div[2]/div/div[3]/div/div[3]/div/div[1]").text
                time.sleep(5)
        except:
                pass

        try:
                driver.get(item7)
                time.sleep(5)
                title7 = driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div/div[3]/div/div[1]/h1").text
                image7 = driver.find_element_by_xpath(
                        "/html/body/div[2]/div[2]/div[2]/div/div[3]/div/section/div[1]/div/div/div[1]/div/figure/img").get_attribute(
                        "src")
                description7 = driver.find_element_by_xpath(
                        "/html/body/div[2]/div[2]/div[2]/div/div[3]/div/div[3]/div/div[1]").text
                time.sleep(5)
        except:
                pass

        try:
                driver.get(item8)
                time.sleep(5)
                title8 = driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div/div[3]/div/div[1]/h1").text
                image8 = driver.find_element_by_xpath(
                        "/html/body/div[2]/div[2]/div[2]/div/div[3]/div/section/div[1]/div/div/div[1]/div/figure/img").get_attribute(
                        "src")
                description8 = driver.find_element_by_xpath(
                        "/html/body/div[2]/div[2]/div[2]/div/div[3]/div/div[3]/div/div[1]").text
                time.sleep(5)
        except:
                pass

        time.sleep(5)

        # we will try to login on wordpress

        try:
                driver.get("https://yoursite.com/wp-admin")
                time.sleep(5)
                yoursite_user= driver.find_element_by_id("user_login")
                yoursite_user.send_keys("your user or email on wordpress")
                yoursite_pass = driver.find_element_by_id("user_pass")
                yoursite_pass.send_keys("your modpass on wordpress")
                login = driver.find_element_by_id("wp-submit").click()
        except:
                pass
        time.sleep(5)
        driver.get("https://yoursite.com/wp-admin/post-new.php")

        post_title = driver.find_element_by_id("title").send_keys(title)

        time.sleep(5)
        click_on_text = driver.find_element_by_id("content-html").click()
        past_item1 = driver.find_element_by_id("content")
        past_item1.send_keys(Keys.ENTER)
        past_item1.send_keys(Keys.ENTER)
        past_item1.send_keys(description)
        past_item1.send_keys(Keys.ENTER)
        past_item1.send_keys(Keys.ENTER)
        past_item1.send_keys("#1-"+ str(title1))
        past_item1.send_keys(Keys.ENTER)
        past_item1.send_keys(Keys.ENTER)
        try:
                past_item1.send_keys(code_img_part1 + image1 + code_img_part2 + title + code_img_part3)
        except:
                pass
        past_item1.send_keys(Keys.ENTER)
        past_item1.send_keys(Keys.ENTER)
        past_item1.send_keys(description1)
        past_item1.send_keys(Keys.ENTER)
        past_item1.send_keys(html1 + affiliate_id + item1 + html2)
        print("we finish past the content item 1")
        past_item1.send_keys(Keys.ENTER)
        past_item1.send_keys(Keys.ENTER)
        past_item1.send_keys("#2-"+ str(title2))
        past_item1.send_keys(Keys.ENTER)
        past_item1.send_keys(Keys.ENTER)
        try:
            past_item1.send_keys(code_img_part1 + image2 + code_img_part2 + title + code_img_part3)
        except:
            pass
        past_item1.send_keys(Keys.ENTER)
        past_item1.send_keys(Keys.ENTER)
        past_item1.send_keys(description2)
        past_item1.send_keys(Keys.ENTER)
        past_item1.send_keys(html1 + affiliate_id + item2 + html2)
        print("we finish past the content item 2")
        past_item1.send_keys(Keys.ENTER)
        past_item1.send_keys(Keys.ENTER)
        past_item1.send_keys("#3-"+ str(title3))
        past_item1.send_keys(Keys.ENTER)
        past_item1.send_keys(Keys.ENTER)
        try:
            past_item1.send_keys(code_img_part1 + image3 + code_img_part2 + title + code_img_part3)
        except:
            pass
        past_item1.send_keys(Keys.ENTER)
        past_item1.send_keys(Keys.ENTER)
        past_item1.send_keys(description3)
        past_item1.send_keys(Keys.ENTER)
        past_item1.send_keys(html1 + affiliate_id + item3 + html2)
        print("we finish past the content item 3")
 
        past_item1.send_keys(Keys.ENTER)
        past_item1.send_keys(Keys.ENTER)
        past_item1.send_keys("#4-"+ str(title4))
        past_item1.send_keys(Keys.ENTER)
        past_item1.send_keys(Keys.ENTER)
        try:
            past_item1.send_keys(code_img_part1 + image4 + code_img_part2 + title + code_img_part3)
        except:
            pass
        past_item1.send_keys(Keys.ENTER)
        past_item1.send_keys(Keys.ENTER)
        past_item1.send_keys(description4)
        past_item1.send_keys(Keys.ENTER)
        past_item1.send_keys(html1 + affiliate_id + item4 + html2)
        print("we finish past the content item 4")
        past_item1.send_keys(Keys.ENTER)
        past_item1.send_keys(Keys.ENTER)
        past_item1.send_keys("#5-"+ str(title5))
        past_item1.send_keys(Keys.ENTER)
        past_item1.send_keys(Keys.ENTER)
        try:
            past_item1.send_keys(code_img_part1 + image5 + code_img_part2 + title + code_img_part3)
        except:
            pass
        past_item1.send_keys(Keys.ENTER)
        past_item1.send_keys(Keys.ENTER)
        past_item1.send_keys(description5)
        past_item1.send_keys(Keys.ENTER)
        past_item1.send_keys(html1 + affiliate_id + item5 + html2)
        print("we finish past the content item 5")
        past_item1.send_keys(Keys.ENTER)
        past_item1.send_keys(Keys.ENTER)
        past_item1.send_keys("#6-"+ str(title6))
        past_item1.send_keys(Keys.ENTER)
        past_item1.send_keys(Keys.ENTER)
        try:
            past_item1.send_keys(code_img_part1 + image6 + code_img_part2 + title + code_img_part3)
        except:
            pass
        past_item1.send_keys(Keys.ENTER)
        past_item1.send_keys(Keys.ENTER)
        past_item1.send_keys(description6)
        past_item1.send_keys(Keys.ENTER)
        past_item1.send_keys(html1 + affiliate_id + item6 + html2)
        print("we finish past the content item 6")
        past_item1.send_keys(Keys.ENTER)
        past_item1.send_keys(Keys.ENTER)
        past_item1.send_keys("#7-"+ str(title7))
        past_item1.send_keys(Keys.ENTER)
        past_item1.send_keys(Keys.ENTER)
        try:
            past_item1.send_keys(code_img_part1 + image7 + code_img_part2 + title + code_img_part3)
        except:
            pass
        past_item1.send_keys(Keys.ENTER)
        past_item1.send_keys(Keys.ENTER)
        past_item1.send_keys(description7)
        past_item1.send_keys(Keys.ENTER)
        past_item1.send_keys(html1 + affiliate_id + item7 + html2)
        print("we finish past the content item 7")
        past_item1.send_keys(Keys.ENTER)
        past_item1.send_keys(Keys.ENTER)
        past_item1.send_keys("#8-"+ str(title8))
        past_item1.send_keys(Keys.ENTER)
        past_item1.send_keys(Keys.ENTER)
        try:
            past_item1.send_keys(code_img_part1 + image8 + code_img_part2 + title + code_img_part3)
        except:
            pass
        past_item1.send_keys(Keys.ENTER)
        past_item1.send_keys(Keys.ENTER)
        past_item1.send_keys(description8)
        past_item1.send_keys(Keys.ENTER)
        past_item1.send_keys(html1 + affiliate_id + item8 + html2)
        print("we finish past the content item 8")










# this part is about copyright, you can put the link of Instagram or your website, I was put my Instagram

def callback(url):
    webbrowser.open_new(url)
myWidget = Label(root, text="Powered by @Zakaria_0.75")
myWidget.pack(side="bottom")
myWidget.bind("<Button-1>", lambda e: callback("https://www.instagram.com/zakaria_0.75/"))
#here we create font variable because we need it on button
myFont = font.Font(family='Helvetica', size=15, weight='bold')

#here we setup button (click button -> start bot)
button = Button(text = "Start",command=my_machine, bg="#00D7F9", fg="white", height=2, width=10)
button ['font'] = myFont
button.pack(pady=5)

root.mainloop()
#The end, See you in the next code
﻿