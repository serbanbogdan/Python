import requests
import re
import ctypes
import pathlib
from PIL import Image, ImageDraw, ImageFont
from user_input import statie, wallpaper_png

site1 = requests.get('http://www.meteoromania.ro/')
site2 = requests.get('https://bleacherreport.com/nba')
site3 = requests.get('https://www.cursbnr.ro/')

text1 = site1.text
text2 = site2.text
text3 = site3.text

# ANM
info_html = re.findall('<li id="' + statie + '"[\s\S]*?</li>', text1)[0]
info_text_temp = re.findall('>([\S\s]*?)<',info_html)

# BR
info_text2_temp = re.findall('"(•[\s\S]*?)"',text2)[0]
info_text2_temp = info_text2_temp.replace('\\n','\n')

# CursBNR
info_text3_temp = re.findall('(?<=class="value".).*(?=<)',text3)

info_text_list = [i for i in info_text_temp if i!='']
info_text = (info_text_list[0] + '\nmeteoromania.ro' + '\n\n• ' +
    # ANM
    info_text_list[1] + '\n• ' +
    info_text_list[2] + info_text_list[3] + '\n• ' +
    info_text_list[4] + info_text_list[5] + '\n• ' +
    info_text_list[6] + info_text_list[7] + '\n• ' +
    info_text_list[8] + info_text_list[9] + '\n• ' +
    info_text_list[10] + info_text_list[11] +
    '\n\n\n\n\n' +
    #Curs Valutara
    'CURS VALUTAR\ncursbnr.ro\n\ncurs:\n• ' +
    info_text3_temp[0] + '\n• ' + info_text3_temp[1] + '\n• ' +
    info_text3_temp[6] + '\n\nrobor:\n• ' +
    info_text3_temp[3] + '\n• ' + info_text3_temp[4] + '\n• ' +
    info_text3_temp[5] +
    '\n\n\n\n\n' +
    # Bleacher Report
    'Around the Association'.upper() + '\nbleacher report\n\n' +
    info_text2_temp
    )

info_text = re.sub('&#186;', '°',info_text)

wallpaper = Image.open(wallpaper_png).convert('RGBA')
scrie = ImageDraw.Draw(wallpaper,'RGBA')
font = ImageFont.truetype("arial.ttf", 14)
scrie.multiline_text((1600,350), info_text, fill=(201,204,210, 255), font=font)
wallpaper.save('pngs\\wallpaper_to_set.png')

folder_path = str(pathlib.Path(__file__).parent.absolute())
folder_path = folder_path + "\pngs\wallpaper_to_set.png"

ctypes.windll.user32.SystemParametersInfoW(20, 0, folder_path , 3)

print(info_text)