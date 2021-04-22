
# Kütüpaneler
import random
import numpy
from selenium import webdriver                                    #pip install selenium
import time                                                       #pip install times
from selenium.webdriver.support.ui import WebDriverWait           #pip install selenium-elements
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from apscheduler.schedulers.background import BackgroundScheduler  #pip install APScheduler
program = BackgroundScheduler()
program.start()



class InstagramBot:
    def __init__(self,username,password,person):

        self.username = username
        self.password = password
        self.person = person
        self.Get_url = 'https://www.instagram.com/'
        self.driver = webdriver.Chrome("./chromedriver.exe") #cgromedriver indirmek için (https://chromedriver.chromium.org/downloads)
        self.logindon = False

        self.followersCount = 0
        self.followingCount = 0

        self.followedList = []
        self.doNotFollowList = []
        self.whitelist = []


        self.webDriverWait = WebDriverWait      # webDriverZaman önce belirli bir koşulun oluşmasını beklemek için tanımladığınız bir koddur.
        self.ec = EC
        self.by = By
        self.FilesDosya()
        self.Selenim()

    def Selenim(self):
        if not self.logindon:
            self.Login( )
            self.UserBilgiToplama( )
        print(".................")
        AnAsAyfA = int(input("[1] Takipçileri Takip Et\n[2] Takip Edildi Takibi Bırak\n[3] Tümünü Takibi Bırak \n[4] hızlı Tümünü Takibi Bırak \n[5] fotagraf beğenmek için\n[6] Sizi takip etmeyen kişiler\n[7] Instagram bot takipci atma \nSeçim:\t"))
        if AnAsAyfA ==1:
            self.FollowFollowers( )
        elif AnAsAyfA ==2:
            self.UnfollowFollowed( )
        elif AnAsAyfA == 3:
            self.UnfollowAll( )
        elif AnAsAyfA == 5:
            self.like_posts()
        elif AnAsAyfA == 6:
            self.Falow()
        elif AnAsAyfA == 7:
            self.bot_falow()
        elif AnAsAyfA == "q":
            self.driver.quit()
            return

    def NumBerConveRter(self , text):
        # Instagram'ın kısaltmasını bir sayıya dönüştürür
        if "k" in text:
            return int((float(text.replace("k" , ""))) * 1000)
        elif "m" in text:
            return int((float(text.replace("m" , ""))) * 1000000)
        else:
            return int(text)


    def Zaman(self , min , max):
        time.sleep(random.choice(numpy.arange(min , max , 0.1)))
    def Link(self , user):
        # Instagram sayfasına gider
        self.driver.get("{}{}/".format(self.Get_url , user))
        time.sleep(5)


    def FilesDosya(self):
        # Mevcut d  eğilse kullanıcı için dosya oluşturur
        temp = open("[Followed][{}]".format(self.username) , "a+")
        temp.close()
        temp = open("[DoNotFollow][{}]".format(self.username) , "a+")
        temp.close()

        #Sizi takip etmeynler
        temp = open("[follwlist][{}]".format(self.username),"a+")
        temp.close()

        #Bot kullanıçılar
        temp = open("[User_Bot]","a+")
        temp.close()
        temp = open("[PassWord_Bot]","a+")
        temp.close()
    def ReadDosya(self):
        # Daha önce yazılan  kullanıcı adlarını dosyadan alır
        self.Zaman(1 , 1.5)
        self.foLLowedList = []
        self.dontFollowList = []
        self.follwwwLList = []

        #Bot
        self.UserBotList = []
        self.PassWordBotList = []

        with open("[Followed][{}]".format(self.username) , "r+") as liste:
            listes = liste.readlines( )# readlines * liste halinde yazdırır
            for readLines in listes:
                self.foLLowedList.append(readLines.strip( )) # append * Listeye ekleme
        with open("[DoNotFollow][{}]".format(self.username) , "r+") as liste:
            listes = liste.readlines( )
            for readLines in listes:
                self.dontFollowList.append(readLines.strip( )) # strip (boşluk kaldır karakteri gelen varsayılan) kaldırır
        with open("[follwlist][{}]".format(self.username) , "r+") as liste:
            listes = liste.readlines( )
            for readLines in listes:
                self.follwwwLList.append(readLines.strip( )) # strip (boşluk kaldır karakteri gelen varsayılan) kaldırır

        #bot
        with open("[User_Bot] ","r+") as liste:
            listes = liste.readlines( )
            for readLines in listes:
                self.UserBotList.append(
                    readLines.strip( ))  # strip (boşluk kaldır karakteri gelen varsayılan) kaldırır
        with open("[PassWord_Bot]" , "r+") as liste:
            listes = liste.readlines( )
            for readLines in listes:
                self.PassWordBotList.append(
                    readLines.strip( ))  # strip (boşluk kaldır karakteri gelen varsayılan) kaldırır

    def TakipListesi(self , name):
        # Tkaip edilen kullanıcıların adını dosya ekler
        with open("[Followed][{}]".format(self.username) , "a+") as liste:
            temp = name.strip( ) + "\n"
            liste.write(temp)
        with open("[DoNotFollow][{}]".format(self.username) , "a+") as liste:
            temp = name.strip( ) + "\n"
            liste.write(temp)

    def dontFollowLisT(self , name):
        #  DoNotFollow dosyasına bir kullanıcı ekler
        with open("[DoNotFollow][{}]".format(self.username) , "a+") as liste:
            temp = name.strip( ) + "\n"
            liste.write(temp)
        self.ReadDosya( )

    def FoLLowedList(self , name):
        #  Takip edilen kullanıcı adını dosyadan kaldırır
        with open("[Followed][{}]".format(self.username) , "r") as liste:
            listes = liste.readlines( )
        with open("[Followed][{}]".format(self.username) , "w") as liste:
            for line in listes:
                if line.strip( ) != name:
                    liste.write(line)

    def  DontfoLLowLisT(self, name):
        #  follwlist dosyasına bir kullanıcı ekler
        with open("[follwlist][{}]".format(self.username) , "a+") as liste:
            temp = name.strip( ) + "\n"
            liste.write(temp)
        self.ReadDosya()


    def DontfoLLowList(self , name):
        #  Takip edilen kullanıcı adını dosyadan kaldırır
        with open("[Followed][{}]".format(self.username) , "r") as liste:
            listes = liste.readlines( )
        with open("[Followed][{}]".format(self.username) , "w") as liste:
            for line in listes:
                if line.strip( ) != name:
                    liste.write(line)

    def Login(self):
        self.driver.get(self.Get_url)
        self.webDriverWait(self.driver , 10).until(self.ec.presence_of_element_located((self.by.NAME , 'username')))
        self.webDriverWait(self.driver , 10).until(self.ec.presence_of_element_located((self.by.NAME , 'password')))
        self.webDriverWait(self.driver , 10).until(self.ec.element_to_be_clickable(
            (self.by.XPATH , "/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]")))
        self.driver.find_element_by_name('username').send_keys(self.username)
        self.driver.find_element_by_name('password').send_keys(self.password)
        self.driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]").click( )
        self.logindon = True
        time.sleep(5)
        if self.driver.current_url == "https://www.instagram.com/accounts/onetap/?next=%2F":
            print("Başarılı bir şekilde giriş yaptınız.")
            print(self.password)
            print(self.person)

        elif self.driver.current_url == "https://www.instagram.com/":
            print("\tGiriş yapamadınız \n Username konturel ediniz. \n Password konturol ediniz.")
            self.driver.close( )

    def UnfollowUser(self , user):
        # Takip edilen kşileri aracılığıyla takip etmeyi bırakır.
        self.Link(user)
        UserName = self.driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/header/section/div[1]") # Kullanıcı adını alır
        button = UserName.find_elements_by_xpath(".//button")
        if (button and button[0].text != "Takip Et"):
            if (len(button) > 2):
                button[1].click()
            else:
                button[0].click()
            time.sleep(3)
            self.driver.find_element_by_xpath("/html/body/div[5]/div/div/div/div[3]/button[1]").click()
    def followUser(self , user):
        # Takip edilen kşileri aracılığıyla takip etmeyi bırakır.
        self.Link(user)
        UserName = self.driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/header/section/div[1]") # Kullanıcı adını alır
        button = UserName.find_elements_by_xpath(".//button")
        if (button and button[0].text != "Çıkar"):
            if (len(button) > 2):
                button[1].click()
            else:
                button[0].click()
            time.sleep(3)
            self.driver.find_element_by_xpath("/html/body/div[5]/div/div/div/div[3]/button[1]").click()

    def UnfollowFollowed(self):
        self.ReadDosya( )
        userting = len(self.followedList)
        miktar = int(input("Kaç tanesinin takibi bırakılacağı? (takip etti {})\t".format(userting)))
        while miktar > userting:
            miktar = int(input("Kaç tanesini takip etmekten vazgeçmeli? (takip etti {})\t".format(userting)))

        for i in range(miktar):
            user = self.followedList[i]
            self.Zaman(10 , 15)
            self.UnfollowUser(user)
            self.FoLLowedList(user)
            print("[{}] {} takibi bırakıldı {}".format(i + 1 , self.username , user))
        self.ReadDosya( )



    def UserBilgiToplama(self):
        # Takipçi  miktarını  alır
        self.Link(self.username)
        # Takipçi sayısını alır
        temp = self.driver.find_element_by_xpath(
            "//*[@id='react-root']/section/main/div/header/section/ul/li[2]/a/span").text
        self.followersCount = self.NumBerConveRter(temp)
        # Takip edenlerin miktarını alır
        temp = self.driver.find_element_by_xpath(
            "//*[@id='react-root']/section/main/div/header/section/ul/li[3]/a/span").text
        self.followingCount = self.NumBerConveRter(temp)

    def FollowFollowers(self):
        # seçtiğiniz kullanıcın takipçilerini takip eder.
        self.ReadDosya( )
        self.Link(self.person)
        print(self.person)
        temp = self.driver.find_element_by_xpath(
            "//*[@id='react-root']/section/main/div/header/section/ul/li[2]/a/span").text
        numoffollowers = self.NumBerConveRter(temp)

        miktar = int(input("Kaç kişiyi takip edecek? (Daha az {})\t".format(temp)))
        while miktar > numoffollowers:
            miktar = int(input("Kaç kişiyi takip edecek? (Daha az {})\t".format(temp)))

        self.driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/header/section/ul/li[2]/a").click( )
        i , k = 1 , 1
        while (k <= miktar):
            self.Zaman(1 , 1.5)
            Userlister = self.driver.find_element_by_xpath("/html/body/div[5]/div/div/div[2]/ul/div/li[{}]".format(i))
            button = Userlister.find_elements_by_xpath(".//Button")
            userting = Userlister.find_element_by_css_selector(".FPmhX.notranslate._0imsa").text
            if (button) and (button[0].text == "Takip Et") and (userting not in self.doNotFollowList):
                self.Zaman(10 , 15)
                button[0].click( )
                self.TakipListesi(userting)  # dosyaya  kullanıcı adını yazar
                self.dontFollowLisT(userting)
                print("[{}] {} takip etti {}".format(k , self.username , userting))
                k += 1
            self.Zaman(1 , 1.5)
            print("Kullanıcıları çekiyor")
            self.driver.execute_script("arguments[0].scrollIntoView()" , Userlister)
            i += 1

    def UnfollowAll(self):
        self.UserBilgiToplama( )
        miktar = int(input("Kaç tanesini takip etmekten vazgeçebilirim? (Takip etme {})\t".format(self.followingCount)))
        while miktar > self.followingCount:
            miktar = int(input("Kaç tanesini takip etmekten vazgeçebilirim? (Takip etme {})\t".format(self.followingCount)))
        self.driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/header/section/ul/li[3]/a").click( )
        i , k = 1 , 1
        while (k <= miktar):
            self.Zaman(1 , 1.5)
            currentUser = self.driver.find_element_by_xpath("/html/body/div[5]/div/div/div[2]/ul/div/li[{}]".format(i))
            button = currentUser.find_elements_by_xpath(".//button")
            name = currentUser.find_element_by_css_selector(".FPmhX.notranslate._0imsa").text
            if (button) and (button[0].text == "Takiptesin") and (name not in self.whitelist):
                self.Zaman(20,25)
                button[0].click( )
                if name in self.followedList:
                    self.FoLLowedList(name)
                if name not in self.dontFollowList:
                    self.dontFollowLisT(name)
                self.Zaman(1 , 2)
                self.driver.find_element_by_xpath("/html/body/div[6]/div/div/div/div[3]/button[1]").click( )
                print("[{}] {} takibi bırakıldı {}".format(k , self.username , name))
                k += 1
            self.Zaman(1 , 1.5)
            self.driver.execute_script("arguments[0].scrollIntoView();" , currentUser)
            i += 1

    def Falow(self):
        self.ReadDosya( )
        self.UserBilgiToplama()
        print("Bu işlem biraz uzun sürebilir:")
        print("Takip etiğniz kullanıçı sayısı'{}':".format(self.followingCount))
        miktar = int(self.followingCount)
        self.driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/header/section/ul/li[3]/a").click()
        i , k = 1 , 1
        while (k <= miktar):
            self.Zaman(1 , 1.5)
            currentUser = self.driver.find_element_by_xpath("/html/body/div[5]/div/div/div[2]/ul/div/li[{}]".format(i))
            button = currentUser.find_elements_by_xpath(".//button")
            name = currentUser.find_element_by_css_selector(".FPmhX.notranslate._0imsa").text
            if (button) and (button[0].text == "Takiptesin") and (name not in self.whitelist):
                self.Zaman(15,25)
                if name not in self.follwwwLList:
                    self.DontfoLLowLisT(name)
                self.Zaman(1 , 2)
                print("Bu işlem biraz uzun süreçktir lütfen bekleyin")
                k += 1
            self.Zaman(1 , 1.5)
            print("Kullanıcıları çekiyor")
            self.driver.execute_script("arguments[0].scrollIntoView();" , currentUser)
            i += 1
        self.driver.refresh()
        self.Zaman(2 , 1.5)
        miktAr = int(self.followersCount)
        print("Takip etiğniz kullanıçı sayısı'{}':".format(self.followersCount))
        self.driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/header/section/ul/li[2]/a").click( )
        i , k = 1 , 1
        while (k <= miktAr):
            self.Zaman(1 , 1.5)
            currentUser = self.driver.find_element_by_xpath("/html/body/div[5]/div/div/div[2]/ul/div/li[{}]".format(i))
            button = currentUser.find_elements_by_xpath(".//button")
            name = currentUser.find_element_by_css_selector(".FPmhX.notranslate._0imsa").text
            if (button) and (button[0].text == "Çıkar") and (name not in self.whitelist):
                self.Zaman(15, 25)
                if name not in self.follwwwLList:
                    self.DontfoLLowLisT(name)
                print("Bu işlem biraz uzun süreçktir lütfen bekleyin")
                k += 1
            print("Kullanıcıları çekiyor")
            self.Zaman(1, 1.5)
            self.driver.execute_script("arguments[0].scrollIntoView()" , currentUser)
            i += 1


        self.those_dont_follow()
        print("sizi takip etmeyen kişi sayısı'{}'".format(len(self.list2)))
        miktar = len(self.list2)
        for i in range(miktar):
             user = self.list2[i]
             self.Zaman(10 , 15)
             self.UnfollowUser(user)
             self.DontfoLLowList(user)
             print("[{}] {} Takibi bırakıldı {}".format(i + 1 , self.username , user))
        self.ReadDosya( )
        print(self.list2)

    def those_dont_follow(self):
        self.list1 = self.follwwwLList
        self.list2 = []

        for i in self.list1:
            if i not in self.list2:
                self.list2.append(i)


    def bot_falow(self):
        print("user ve password dosyalarına kullanıcıları eklemeyi unutmayın!")
        self.ReadDosya( )
        userting = len(self.UserBotList)
        User = input("Takip edileçek kullanıcı adı:\t")
        miktar = int(input("Kaç tanesini takip edeceksin? (Bot sayısı {})\t".format(userting)))
        while miktar > userting:
            miktar = int(input("Kaç tanesini takip edeceksin?  (Bot sayısı  {})\t".format(userting)))

        for i in range(miktar):
            user = self.UserBotList[i]
            password = self.PassWordBotList[i]
            time.sleep(5)
            self.driver.find_element_by_xpath("//*[@id='react-root']/section/nav/div[2]/div/div/div[3]/div/div[5]/span/img").click( )
            time.sleep(4)
            self.driver.find_element_by_xpath(
                "//*[@id='react-root']/section/nav/div[2]/div/div/div[3]/div/div[5]/div[2]/div[2]/div[2]/div[2]").click( )

            time.sleep(5)
            self.driver.find_element_by_name("username").send_keys(user)
            self.Zaman(1 , 2)
            self.driver.find_element_by_name("password").send_keys(password)
            self.Zaman(1 , 2)
            self.driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]").click( )
            print("Logged In: {}".format(self.username))
            time.sleep(5)
            self.followUser(User)
            time.sleep(5)

        self.ReadDosya()

    def like_posts(self):
        print("fotoğraf begendirmek için Takip etmeniz gerekiyor.")
        user = input("Kullanıcı adı giriniz:\t")
        self.driver.get("https://www.instagram.com/{}".format(user))
        time.sleep(3)
        amount = int(input("Bir deger girniz:"))
        if amount == 0 :
            self.driver.quit()

        elif amount > 1:
            self.driver.find_element_by_class_name('v1Nh3').click( )

            i = 1
            while i <= amount:
                time.sleep(5)
                self.driver.find_element_by_class_name('fr66n').click( )
                self.driver.find_element_by_class_name('coreSpriteRightPaginationArrow').click( )
                i += 1



i = InstagramBot("velden_4646","3456A24eB94","furkand46")


