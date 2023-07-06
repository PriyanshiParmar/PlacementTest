from PIL import Image
from django.shortcuts import render
from matplotlib import image
import requests
from selenium import webdriver
from time import sleep
from pywebcopy import save_webpage

# from urlbox import UrlboxClient
# from django.core.files.base import ContentFile
# from django_screenshots import Builder
import pyautogui

# Create your views here.
def index(request):
  url = 'https://reqres.in/api/users'
  response = requests.get(url, headers={'Content-Type':      
    'application/json'})
  users = response.json().get('data')
  print(users)
  return render(request, "index.html", {'users': users})

def view_user(request, id):
  url = 'https://reqres.in/api/users/'+ id
  response = requests.get(url, headers={'Content-Type':      
    'application/json'})
  user = response.json().get('data')
  print(user)
  return render(request, "profile.html", {'user': user})

def takeScreenshot(request):
  
  url = request.post['url']
  print(url)
  download_folder = 'C:/Users/Priyanshi/Downloads/'
  kwargs = {'bypass_robots': True, 'project_name': 'recognisable-name'}
  save_webpage(url, download_folder, **kwargs)
  # driver = webdriver.Chrome()
  # driver.get(url)
  # # sleep(1)
  # print('Hello')
  # # print(request.post['url'])
  # print('Hello')
  # driver.save_screenshot("screenshot.png")
  # image = Image.open("screenshot.png")
  # image.show()
  # driver.quit()
  # print("end...")
#   if request.method == 'POST':
 
#     user_url = request.POST['url']
#     urlbox_client = UrlboxClient()
#     response = urlbox_client.get({"url": user_url})
#     myfile = ContentFile(response.content)
#     # response = HttpResponse(content_type='image/png')
#     image.save(response, 'png')
#     response['Content-Disposition'] = 'attachment; filename={0}'.format("Export.png")
#     print(myfile)
#     return response
  
#    b = Builder(request.post['url']) 
#    b.capture() 
#    print(b.image_url)
    # myScreenshot = pyautogui.screenshot()
    # print(myScreenshot)
    # myScreenshot.save(r'C:\Users\Priyanshi\Downloads\file.png')