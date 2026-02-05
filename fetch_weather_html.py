import requests
url='https://www.google.com/search?q=weather+patna'
headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"}
print('Requesting', url)
r=requests.get(url, headers=headers, timeout=10)
print('Status', r.status_code)
print('Len', len(r.text))
# save to file for inspection
open('weather_page.html','w', encoding='utf-8').write(r.text)
print('Saved weather_page.html')
print(r.text[:1000])
