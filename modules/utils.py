from Moduleloader import *
import Moduleloader
import Bot
import logging
import re
import threading
import time
from ts3.TS3Connection import TS3QueryException
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, wait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
import subprocess
import os

import pandas as pd
import discord
from discord.ext import commands
from urllib import parse, request
import re

__version__ = "0.4"
bot = None
logger = logging.getLogger("bot")


@Moduleloader.setup
def setup(ts3bot):
    global bot
    bot = ts3bot


executable_path = "/webdrivers"
os.environ["webdriver.chrome.driver"] = executable_path

chrome_options = Options()

chrome_options.add_extension(
    'C:\\Users\\tebit\\Desktop\\bot_ts3_v1.1\\extensions\\ezyZip.crx')
chrome_options.add_extension(
    'C:\\Users\\tebit\\Desktop\\bot_ts3_v1.1\\extensions\\Tampermonkey.crx')
chrome_options.add_extension(
    'C:\\Users\\tebit\\Desktop\\bot_ts3_v1.1\\extensions\\uBlock-Origin.crx')
chrome_options.add_extension(
    'C:\\Users\\tebit\\Desktop\\bot_ts3_v1.1\\extensions\\Audio_Only_Youtube_0_9_0_0.crx')
chrome_options.add_extension(
    'C:\\Users\\tebit\\Desktop\\bot_ts3_v1.1\\extensions\\YouTube-NonStop.crx')

driver_path = 'C:\\Users\\tebit\\Desktop\\bot_ts3_v1.1\\chromedriver.exe'
driver = webdriver.Chrome(executable_path=driver_path,
                          chrome_options=chrome_options)

original_window = driver.current_window_handle
# timer


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
            duracion = driver.find_element_by_css_selector(
                '#movie_player > div.ytp-chrome-bottom > div.ytp-chrome-controls > div.ytp-left-controls > div.ytp-time-display.notranslate > span:nth-child(2) > span.ytp-time-duration').get_attribute('textContent')
            duracion = re.sub(":", "", duracion)
            duracion = int(duracion)
            print(duracion)
            if duracion >= 750:
                webdriver.ActionChains(driver).key_down(
                    Keys.SHIFT).send_keys("N").perform()
                pass
        except Exception:
            print('fuk dady')
            pass


timer5 = timer5()
timer5.start()

print(original_window)

bot1 = commands.Bot(command_prefix='!', description="This is the hekoer bot")


@bot1.command()
async def ping(ctx):
    ctx.send('pong')


@bot1.command()
async def pds(ctx, message):
    driver.get('https://www.youtube.com/results?search_query=' + message)
    WebDriverWait(driver, 5)\
        .until(EC.element_to_be_clickable((By.XPATH,
                                           '//*[@id="thumbnail"]'.replace(' ', '.'))))\
        .click()
    cancion = WebDriverWait(driver, 5)\
        .until(EC.element_to_be_clickable((By.XPATH,
                                           '/html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[8]/div[2]/ytd-video-primary-info-renderer/div/h1/yt-formatted-string')))\
        .text
    await ctx.send("Reproduciendo " + cancion + 'usa !help para ver comandos')
    # Busqueda de cancion

bot1.login('ODc1NTQ1NzQ4NTI2MjE1MjU4.YRXFhQ.va6j_UEfcGAqPEiEPonYP781OTQ')


@command('hello',)
@group('Server Admin', 'Guest')
def hello(sender):
    Bot.send_msg_to_client(bot.ts3conn, sender, "Hello Admin!")


@command('help',)
@group('Server Admin', 'Guest')
def get_command_list(sender):
    Bot.send_msg_to_client(bot.ts3conn, sender,
                           "=============================================")
    Bot.send_msg_to_client(bot.ts3conn, sender, "!p = buscar cancion")
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
def musicplay(sender, msg,):
    song = msg.split()[1:]
    songg = " ".join(map(str, song))
    driver.get('https://www.youtube.com/results?search_query=' + songg)
    link = WebDriverWait(driver, 5)\
        .until(EC.visibility_of_element_located((By.XPATH,'//*[@id="video-title"]')))\
        .get_attribute('href')
    driver.implicitly_wait(5)
    driver.get(link) 
    cancion = WebDriverWait(driver, 15)\
        .until(EC.visibility_of_element_located((By.XPATH,
                                           '/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[8]/div[1]/div[2]/ytd-video-primary-info-renderer/div/h1/yt-formatted-string')))\
        .text
    Bot.send_msg_to_client(bot.ts3conn, sender,
                           "=============================================")
    Bot.send_msg_to_client(bot.ts3conn, sender, "Reproduciendo " + cancion)
    Bot.send_msg_to_client(bot.ts3conn, sender, "usa !help para ver comandos")
    Bot.send_msg_to_client(bot.ts3conn, sender,
                           "=============================================")
    # Busqueda de cancion


@command('pl')
@group('Server Admin', 'Guest')
def musicplay(sender, msg):
    song = msg.split()[1:]
    songg = "".join(map(str, song))
    songg = re.sub("\[URL]|\[/URL]", "", songg)
    try:
        cancion = WebDriverWait(driver, 5)\
            .until(EC.visibility_of_element_located((By.XPATH,
                                               '/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[8]/div[1]/div[2]/ytd-video-primary-info-renderer/div/h1/yt-formatted-string')))\
            .text
    except Exception:
        pass
    try:
        cancion = WebDriverWait(driver, 15)\
            .until(EC.visibility_of_element_located((By.XPATH,
                                               '/html/body/ytmusic-app/ytmusic-app-layout/ytmusic-player-bar/div[2]/div[2]/yt-formatted-string')))\
            .text
    except Exception:
        pass
    Bot.send_msg_to_client(bot.ts3conn, sender,
                           "=============================================")
    Bot.send_msg_to_client(bot.ts3conn, sender, "Reproduciendo " + cancion)
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
        info = driver.find_elements_by_xpath(
            "/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[8]/div[1]/div[2]/ytd-video-primary-info-renderer/div/h1/yt-formatted-string")[0].text
    except Exception:
        pass
    try:
        info = driver.find_elements_by_xpath(
            "/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/ytd-watch-metadata/div/div[1]/h1/yt-formatted-string")[0].text
    except Exception:
        pass
    try:
        info = driver.find_elements_by_xpath(
            "/html/body/ytmusic-app/ytmusic-app-layout/ytmusic-player-bar/div[2]/div[2]/yt-formatted-string")[0].text
    except Exception:
        pass
    Bot.send_msg_to_client(bot.ts3conn, sender,
                           "=============================================")
    Bot.send_msg_to_client(bot.ts3conn, sender, info)
    Bot.send_msg_to_client(bot.ts3conn, sender, urlcurrent)
    Bot.send_msg_to_client(bot.ts3conn, sender, "usa !help para ver comandos")
    Bot.send_msg_to_client(bot.ts3conn, sender,
                           "=============================================")

@command('purga')
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
