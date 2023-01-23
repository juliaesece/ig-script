import requests
import json
import time
from bs4 import BeautifulSoup

from followers_array import accounts 

partida = input("Donde empezar: ")
partida = int(partida)
quedan = len(accounts) - partida
print("quedan " + str(quedan))
quedan = quedan - 1


accounts =  accounts[partida:-1]

accountsFolNb = []
counting = 0
print("comenzo en " + str(partida))

for i in accounts:
    time.sleep(1)
    url = "https://www.instagram.com/{}/?__a=1".format(i)
    print(url)
    print("@" + str(i))
    try:
        r = requests.get(url)
        r.raise_for_status()  # raises exception when not a 2xx response
    except requests.exceptions.HTTPError as errh:
        print ("Http Error:",errh)
                #if error, save and exit 
        print("problema con conexión u otro")
        print("interrumpido")
        accountsFolNb.append({"account": i, "followers" : "n existe plus?"})
        print(accountsFolNb)
        print("length: " + str(len(accountsFolNb)))
        prox = len(accountsFolNb) + partida
        print("prox parte en " + str(prox))
        titre = "accounts_interrumpido_" + str(partida) + "+" + str(len(accountsFolNb)) + ".json"
        file = open(titre, "w")
        jsoneado = json.dumps(accountsFolNb)
        jsoneado = repr(jsoneado)
        jsoneado = jsoneado[1:]
        jsoneado = jsoneado[:-1]
        strAccounts = jsoneado
        file.write(strAccounts)
        file.cl
    except requests.exceptions.ConnectionError as errc:
        print ("Error Connecting:",errc)
                #if error, save and exit 
        print("problema con conexión u otro")
        print("interrumpido")
        print(accountsFolNb)
        print("length: " + str(len(accountsFolNb)))
        prox = len(accountsFolNb) + partida
        print("prox parte en " + str(prox))
        titre = "accounts_interrumpido_" + str(partida) + "+" + str(len(accountsFolNb)) + ".json"
        file = open(titre, "w")
        jsoneado = json.dumps(accountsFolNb)
        jsoneado = repr(jsoneado)
        jsoneado = jsoneado[1:]
        jsoneado = jsoneado[:-1]
        strAccounts = jsoneado
        file.write(strAccounts)
        file.cl
    except requests.exceptions.Timeout as errt:
        print ("Timeout Error:",errt)
                #if error, save and exit 
        print("problema con conexión u otro")
        print("interrumpido")
        print(accountsFolNb)
        print("length: " + str(len(accountsFolNb)))
        prox = len(accountsFolNb) + partida
        print("prox parte en " + str(prox))
        titre = "accounts_interrumpido_" + str(partida) + "+" + str(len(accountsFolNb)) + ".json"
        file = open(titre, "w")
        jsoneado = json.dumps(accountsFolNb)
        jsoneado = repr(jsoneado)
        jsoneado = jsoneado[1:]
        jsoneado = jsoneado[:-1]
        strAccounts = jsoneado
        file.write(strAccounts)
        file.cl
    except requests.exceptions.RequestException as e: 
        #if error, save and exit 
        print("problema con conexión u otro")
        print("interrumpido")
        print(accountsFolNb)
        print("length: " + str(len(accountsFolNb)))
        prox = len(accountsFolNb) + partida
        print("prox parte en " + str(prox))
        titre = "accounts_interrumpido_" + str(partida) + "+" + str(len(accountsFolNb)) + ".json"
        file = open(titre, "w")
        jsoneado = json.dumps(accountsFolNb)
        jsoneado = repr(jsoneado)
        jsoneado = jsoneado[1:]
        jsoneado = jsoneado[:-1]
        strAccounts = jsoneado
        file.write(strAccounts)
        file.close()
        break
    print(r.headers["content-type"])
    if r.headers["content-type"] != "application/json; charset=utf-8":
        print("problema con headers")
        print("interrumpido")
        print(accountsFolNb)
        print("length: " + str(len(accountsFolNb)))
        prox = len(accountsFolNb) + partida
        print("prox parte en " + str(prox))
        titre = "accounts_interrumpido_" + str(partida) + "+" + str(len(accountsFolNb)) + ".json"
        file = open(titre, "w")
        jsoneado = json.dumps(accountsFolNb)
        jsoneado = repr(jsoneado)
        jsoneado = jsoneado[1:]
        jsoneado = jsoneado[:-1]
        strAccounts = jsoneado
        file.write(strAccounts)
        file.close()
        break
    cont = r.json()
    keyTest = 'graphql'
    if keyTest in cont:
        folNb = cont['graphql']['user']['edge_followed_by']['count']
        accountsFolNb.append({"account": i, "followers" : folNb})
        print("followers: " + str(folNb))
        print("en proceso")
    else:
        accountsFolNb.append({"account": i, "followers" : "private"})
        print("cuenta privada")
    counting += 1
    print("loop nro. " + str(counting))
    if counting >= quedan:
        print("terminado")
        print(accountsFolNb)
        titre = "accounts_"  + str(partida) + "+" + str(len(accountsFolNb)) + ".json"
        file = open(titre, "w")
        jsoneado = json.dumps(accountsFolNb)
        jsoneado = repr(jsoneado)
        jsoneado = jsoneado[1:]
        jsoneado = jsoneado[:-1]
        strAccounts = jsoneado
        prox = len(accountsFolNb) + partida
        print("prox parte en " + str(prox))
        file.write(strAccounts)
        file.close()
        break
