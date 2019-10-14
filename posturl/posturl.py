import requests
post_url = "https://google.com"

headers = {
	'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
	'content-type':'application/json',
}

payload={}
cookie={}

r = requests.post(post_url,data=payload,cookies=cookie,headers=headers)
print(r.content)
