import discord
from discord.ext import commands
import datetime
from urllib import parse, request
import re
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, wait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
import subprocess
import os
import zipfile
import time
import pandas as pd

executable_path = "/webdrivers"
os.environ["webdriver.chrome.driver"] = executable_path
chrome_options = Options()
chrome_options.add_extension(
'C:\\Users\\tebit\\Desktop\\bot_ts3_v1.1\\extensions\\uBlock-Origin_v1.35.2.crx')
chrome_options.add_extension(
'C:\\Users\\tebit\\Desktop\\bot_ts3_v1.1\\extensions\\Audio_Only_Youtube_0_9_0_0.crx')
chrome_options.add_extension(
'C:\\Users\\tebit\\Desktop\\bot_ts3_v1.1\\extensions\\YouTube_NonStop_0_9_0_0.crx')
driver_path = 'C:\\Users\\tebit\\Desktop\\bot_ts3_v1.1\\chromedriver.exe'
driver = webdriver.Chrome(original_window)            


bot1 = commands.Bot(command_prefix='!', description="This is the hekoer bot")

@bot1.command()
async def ping(ctx):
    ctx.send('pong')

@bot1.command()
async def info(ctx):
    embed = discord.Embed(title=f"{ctx.guild.name}", description="Lorem Ipsum asdasd", timestamp=datetime.datetime.utcnow(), color=discord.Color.blue())
    embed.add_field(name="Server created at", value=f"{ctx.guild.created_at}")
    embed.add_field(name="Server Owner", value=f"{ctx.guild.owner}")
    embed.add_field(name="Server Region", value=f"{ctx.guild.region}")
    embed.add_field(name="Server ID", value=f"{ctx.guild.id}")
    # embed.set_thumbnail(url=f"{ctx.guild.icon}")
    embed.set_thumbnail(url="https://pluralsight.imgix.net/paths/python-7be70baaac.png")
    await ctx.send(embed=embed)

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

bot1.run('ODc1NTQ1NzQ4NTI2MjE1MjU4.YRXFhQ.va6j_UEfcGAqPEiEPonYP781OTQ')