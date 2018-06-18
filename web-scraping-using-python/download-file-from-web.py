# download from internet
# run pip install requests

import requests

# file exists
res = requests.get('http://automatetheboringstuff.com/files/rj.txt')

print(res.status_code)

print(len(res.text))

print(res.text[:500])

res.raise_for_status() # for downloading


# file not exists
badRes = requests.get('http://automatetheboringstuff.com/files/txtfksfsdkfksnfs')

#badRes.raise_for_status() # for downloading error

# write the file

playFile = open('demo.txt', 'wb')
for chunk in res.iter_content(100000):
    playFile.write(chunk)

playFile.close()