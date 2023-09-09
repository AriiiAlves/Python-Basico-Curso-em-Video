#from webbrowser import webbrowser.open .open_new .open_new_tab
#webbrowser é para abrir sites no pc

import urllib.request

url = 'http://pudim.com.br'
try:
    urllib.request.urlopen(url)
except:
    print('O site não está disponível no momento.')
else:
    print('O site está disponível!')