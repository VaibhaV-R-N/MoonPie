import json
import sys
import subprocess
from pynput import keyboard

lis = ""
flag = 0
jf = open('Spawn.json','r')
po = json.load(jf)
jf2 = open('SmogonStrat.json','r')
po2 = json.load(jf2)

def listen(key):
    global flag,po,lis
    try:
        if key.char == '3':
            subprocess.run(["notify-send","Exiting..."])
            sys.exit()
        if key.char == '1':
            flag = 1
            subprocess.run(['notify-send','Spawn Fetcher Activated.','Please Type...'])
            return

        if key.char == '2':
            flag = 2
            subprocess.run(['notify-send','Smogon Strategy Dex Activated.','Please Type...'])
            return

        if key.char =='0' and flag == 1:
            res = po[lis.lower()]
            s = "\n"
            if res:
                for loc in res:
                    s+=loc.strip()+"\n"
                subprocess.run(['notify-send',f'Spawn Location : {lis} ',s])
            lis = ""
            flag = 0

        if key.char == '0' and flag == 2:
            res = po2[lis.lower()]
            s = "\n"
            if res:
                temp = []
                for i in range(len(res[0])):
                    temp.append([res[0][i],res[1][i]])
                for i,j in enumerate(temp):
                    s+=f"[Strategy {i+1}] \n\n"
                    for k,l in enumerate(j):
                        if k == 1:
                            for ke,val in l.items():
                                s+=f"{ke} : {val}\n"
                            continue
                        for l,st in enumerate(l):
                            s+=f"move {l+1} : {st}\n"
                        s+="\n"
                    s+="\n"
                subprocess.run(['notify-send',f'Smogon Strategies for : {lis}',s])
            lis = ""
            flag = 0
            

        if flag in [1,2]:
            lis+=key.char
            subprocess.run(['notify-send',lis])

    except AttributeError:
        if key.name == 'backspace':
            print(key.name)
            lizt = [*lis]
            try:
                lizt[len(lizt)-1] = ''
                lis = ''.join(lizt)
            except IndexError:
                 subprocess.run(['notify-send','[]'])

            subprocess.run(['notify-send',lis])
    except KeyError:
        subprocess.run(['notify-send',f'Data Not Found for : {lis}'])
        lis = ""
        flag = 0
    

    
listener = keyboard.Listener(on_press=listen)
listener.start()

while True:
    pass