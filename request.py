import requests
import urllib2
import os

# unsplash apikey
page_num = 1
while True:
    payload = {'client_id': 'YOUR CLIENT_ID'
                ,'page':page_num}
    r = requests.get('https://api.unsplash.com/photos', params = payload)
    print("requests_url:" + r.url + "...")
    print(r.status_code)
    response = r.json()
    for p in response:
        pic_url = p['urls']['small']
        pic_id = p['id']
        print("downloading:"+pic_url+"...")
        # fetching picture
        imgData = urllib2.urlopen(pic_url).read()
        fileName = os.getcwd().replace("\\","/") + "/" + pic_id + ".jpg"
        print(fileName)
        # write to file
        if not os.path.exists(fileName):
            output = open(fileName,'wb+')
            output.write(imgData)
            output.close()
            print("Finished download " + pic_id)
        else:
            print("path not exists")
    page_num += 1
