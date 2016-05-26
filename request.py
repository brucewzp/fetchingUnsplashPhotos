import requests
import urllib2
import os

# unsplash apikey
payload = {'client_id': 'YOUR_UNSPLASH_KEY'}
r = requests.get('https://api.unsplash.com/photos', params = payload)
print("requests_url:" + r.url + "...")
print(r.status_code)
response = r.json()
for p in response:
    pic_url = p['urls']['raw']
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
