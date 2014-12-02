from datetime import datetime
import re
import requests
startTime = datetime.now()
link = ('https://secure-store.nike.com/us/services/jcartService?callback=nike_Cart_hanleJCartResponse&action=addItem&lang_locale=en_US&country=US&catalogId=1&productId=1545104&price=120.0&siteId=null&line1=Nike+Free+4.0+Flyknit&line2=Women%27s+Running+Shoe&passcode=null&sizeType=null&skuAndSize=3894509%3A7&qty=1&rt=json&view=3&skuId=3894509&displaySize=7&_=1417400678233')
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2107.3 Safari/537.36', 'Host': 'secure-store.nike.com', 'Connection': 'keep-alive', 'Referer': 'link', 'Accept-Encoding': 'gzip,deflate', 'Accept-Language': 'en-US,en;q=0.8'} 
cookie = {'RES_TRACKINGID': '849445096449926', 'RES_SESSIONID': '905512340366840', 'AnalysisUserId': '128.999.77.22.1405689197999243', 'WRUID': '999997038.176257895', 'AKNIKE': 'aaaU7Y_RwjGvd9fnDJr9XSPidl715aSZs0uylTgXzcHxT2VFBj4hVOw', 'USID': '0EA26227358182A1AEACC9C39CABDEAF.sin-197-app-us-1', 'guidS': '030ca47a-4f90-4894-a8ad-70f7f4a96550', 'guidU': '5b2f32fc-91b7-4e8d-e2e1-1e733e171917', 'utag_main': '_st:1406883408970$ses_id:1406881306602%3Bexp-session', 'needlepin': 'N190d1405448840085428df001c216777a328777900add77900fd1001900000000000001177900b9e0000000009usrunning01177900bc72ea0000', '_unam': 'c0158ee-1474310f9da-28ebb10-1'}
#r = requests.session().post(link,headers=headers,cookies=cookie)
r = requests.get('http://store.nike.com/us/en_us/pd/free-4-flyknit-running-shoe/pid-1545960/pgid-1481072')


reg = re.compile('<input type="hidden" name="action" value="(.*?)"/>[^.]*<input type="hidden" name="lang_locale" value="(.*?)"/>[^.]*<input type="hidden" name="country" value="(.*?)"/>[^.]*<input type="hidden" name="catalogId" value="(.*?)"/>', re.MULTILINE)
matchObj = reg.search(r.text)

for group in matchObj.groups():
	print group









print(datetime.now()-startTime)