import requests
link = "https://csf101-server-cap1.onrender.com/get/input/356"
request_file = requests.get(link)
with open('356.txt', 'wb') as file:
    file.write(request_file.content)
print('Downloaded: 356.txt')
