
import requests

print(requests.__version__)
url = 'https://raw.githubusercontent.com/richeek05/Cmput404-Labs/main/find_version.py'
r = requests.get(url, allow_redirects=True)

open('Python Code', 'wb').write(r.content)

print('The file was saved successfully')


