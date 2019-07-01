#Author Ian Wright
#thewian27@gmail.com

import os
import requests as r
from bs4 import BeautifulSoup as bs
import getpass
import time
import sys
import clipboard.clipboard as clip

def download_media(link, title, media_type):
	
	__data__ = r.get(link, timeout=60)

	file_formats = ['jpg','mp4']
	username = getpass.getuser()
	path = f'/home/{username}/Downloads/InstagramSaver'

	if os.path.exists(f'/{path}') == False:
		os.system(f'mkdir /{path}')

	if media_type == "image":
		print(link)
		with open(f'{path}/{title}.{file_formats[0]}', 'wb') as p:
			print(f'Downloading {media_type}....')
			p.write(__data__.content)
		print(f'[ * ] "{title}.{file_formats[0]}" has been saved to "{path}"')
	else:
		with open(f'{path}/"{title}.{file_formats[1]}"', 'wb') as v:
			print(f'Downloading {media_type}....')
			v.write(__data__.content)
		print(f'[ * ] "{title}.{file_formats[0]}" has been saved to "{path}"')

	clip.copy('')
	main("downloaded")


def get_html(response):
	page = bs(response, 'html5lib')
	try:
		video_link = page.find("meta", {"property":"og:video"})
		video_title = page.find("meta", {"property":"og:title"})
		vid_name = video_title['content']

		video_name = vid_name[vid_name.find(':')+3:-1]
		video_url = video_link['content']

		download_media(video_url, video_name, "video")

	except Exception as e:
		image_link = page.find("meta", {"property":"og:image"})
		image_title = page.find("meta", {"property":"og:title"})
		img_name = image_title['content']

		image_name = img_name[img_name.find(':')+3:-1]
		image_url = image_link['content']

		download_media(image_url, image_name, "image")
			
def get_url(url):
	headers = {'Referer':'https://www.instagram.com/','User-Agent':'Mozilla/5.0 (X11; Ubuntu;Gecko/20100101 Firefox/64.0'}
	http = r.get(url, headers=headers,timeout=60)
	
	if http.ok == True:
		get_html(http.text)

def draw_screen():
	os.system('clear')
	print('='*40)
	print('|'+' '*38+'|')
	print('\t[ * ]Instagram Saver\n\tAuthor: Ian Wright')
	print('\n[ * ] Copy any instagram post link...')

def main(response):
	draw_screen()
	detectedLink = False
	while not detectedLink:
		clipboardContent = clip.paste()
		if "instagram.com/p/" in clipboardContent:
			detectedLink = True
			post_link = clipboardContent
			print(f'[ * ] LINK received =>[{post_link}]\n [ * ] Downloading...')
			clipboardContent = ""
			break
		else:
			detectedLink = False
	get_url(post_link)

main("downloaded")

		
