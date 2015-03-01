import requests

r = requests.session()
cookie = input('Input the Cookie (WC):')
r.cookies.set('WC', cookie)

key = r.get('http://www.wechall.net/challenge/training/programming1/index.php?action=request').text
r.get('http://www.wechall.net/challenge/training/programming1/index.php', params={"answer":key})
