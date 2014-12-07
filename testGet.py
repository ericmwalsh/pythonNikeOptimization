from datetime import datetime
import re
import requests
startTime = datetime.now()

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2107.3 Safari/537.36', 'Host': 'secure-store.nike.com', 'Connection': 'keep-alive', 'Referer': 'link', 'Accept-Encoding': 'gzip,deflate', 'Accept-Language': 'en-US,en;q=0.8'} 
cookie = {'RES_TRACKINGID': '849445096449926', 'RES_SESSIONID': '35166464048501571', 'AnalysisUserId': '128.999.77.22.1405689197999243', 'WRUID': '999997038.176257895', 'AKNIKE': 'aaaU7Y_RwjGvd9fnDJr9XSPidl715aSZs0uylTgXzcHxT2VFBj4hVOw', 'USID': '0EA26227358182A1AEACC9C39CABDEAF.sin-197-app-us-1', 'guidS': '030ca47a-4f90-4894-a8ad-70f7f4a96550', 'guidU': '5b2f32fc-91b7-4e8d-e2e1-1e733e171917', 'utag_main': '_st:1406883408970$ses_id:1406881306602%3Bexp-session', 'needlepin': 'N190d1405448840085428df001c216777a328777900add77900fd1001900000000000001177900b9e0000000009usrunning01177900bc72ea0000', '_unam': 'c0158ee-1474310f9da-28ebb10-1'}
payload = ### user selected
sesh = requests.Session()




linkOfShoe = "http://store.nike.com/us/en_us/pd/air-max-2015-running-shoe/pid-1546804/pgid-10097056" #user selected
sizeOfShoe = "7.5"  #user seleced 




r = sesh.get(linkOfShoe)
#print r.content

reg = re.compile('<input type="hidden" name="action" value="(.*)"/>[^.]*<input type="hidden" name="lang_locale" value="(.*)"/>[^.]*<input type="hidden" name="country" value="(.*)"/>[^.]*<input type="hidden" name="catalogId" value="(.*)"/>[^.]*<input type="hidden" name="productId" value="(.*)"/>[^.]*<input type="hidden" name="price" value="(.*)"/>[^.]*<input type="hidden" name="line1" value="(.*)"/>[^.]*<input type="hidden" name="line2" value="(.*)"/>[^$]*value="([0-9]{7}):' + sizeOfShoe + '"', re.MULTILINE)
matchObj = reg.search(r.text)

for group in matchObj.groups():
	print group


link = "https://secure-store.nike.com/us/services/jcartService?callback=nike_Cart_hanleJCartResponse&action=" + matchObj.group(1) + "&lang_locale=" + matchObj.group(2) + "&country=" + matchObj.group(3) + "&catalogId=" + matchObj.group(4) + "&productId=" + matchObj.group(5) + "&price=" + matchObj.group(6) + "&siteId=null&line1=" + matchObj.group(7) + "&line2=" + matchObj.group(8) + "&passcode=null&sizeType=null&skuAndSize=" + matchObj.group(9) + "%3A" + sizeOfShoe + "&qty=1&rt=json&view=3&skuId=" + matchObj.group(9) + "&displaySize=" + sizeOfShoe + "&_=1397536308748"

link =link.replace(' ','+').replace('&#x27;', '%27')
#print link

s = sesh.post("https://www.nike.com/profile/login?Content-Locale=en_US", params=payload)
print s.content

print " "

t = sesh.post(link, headers=headers, cookies=cookie)
print t.content

text_file1 = open("nikeresp.txt", "w")
text_file1.write(t.content.encode('utf-8'))
text_file1.close()

print(datetime.now()-startTime)