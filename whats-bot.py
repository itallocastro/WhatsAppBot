from selenium import webdriver
import time

class WhatsAppBot:
    def __init__(self):
        self.mensage = "Boa noite, você acabou de receber uma mensagem do bot automático do Itallo Patrick"
        self.person = ["Lucas Ufal"]
        options = webdriver.ChromeOptions()
        options.add_argument('lang=pt-br')
        self.driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')
    def sendMessage(self):
        # <span dir="auto" title="Momolada 🤩" class="_1wjpf _3NFp9 _3FXB1">Momolada <img crossorigin="anonymous" src="data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7" alt="🤩" draggable="false" class="b90 emoji wa _3FXB1" style="background-position: -60px -40px;"></span>
        # <div tabindex="-1" class="_1Plpp"><div tabindex="-1" class="_3F6QL _2WovP"><div class="_39LWd" style="visibility: visible;">Digite uma mensagem</div><div class="_2S1VP copyable-text selectable-text" contenteditable="true" data-tab="1" dir="ltr" spellcheck="true"></div></div></div>
        #<span data-icon="send" class=""><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="24" height="24"><path fill="currentColor" d="M1.101 21.757L23.8 12.028 1.101 2.3l.011 7.912 13.623 1.816-13.623 1.817-.011 7.912z"></path></svg></span>
        self.driver.get('https://web.whatsapp.com/')
        time.sleep(15)
        for person in self.person:
            person = self.driver.find_element_by_xpath(f"//span[@title='{person}']")
            time.sleep(3)
            person.click()
            time.sleep(2)
            chat_box = self.driver.find_elements_by_class_name("_1Plpp")            
            time.sleep(2)
            chat_box[0].send_keys(self.mensage)
            time.sleep(3)
            self.driver.find_element_by_xpath('//span[@data-icon="send"]').click()
            time.sleep(3)
bot = WhatsAppBot()
bot.sendMessage()