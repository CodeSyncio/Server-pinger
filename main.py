from subprocess import DEVNULL
import os
import subprocess
import colorama
from colorama import init, Fore,Style
import time
import sys



def checklist(useconfig = True):
    colorama.init(autoreset = True)
    IpList =[]
    if useconfig is True:
        with open('servers.txt','r') as configfile:
            for line in configfile:
                if line.startswith('' or '\n' or ' '):
                    pass
                else:
                    IpList.append(line.strip())
                
    else:
        IpList.append(useconfig)
    
    

    starttime = time.time()
    

    print(Fore.CYAN+f'Loaded {len(IpList)} server addresses.\n')
    
    global AliveList
    global DeadList
    
    AliveList= []
    DeadList = []
    
    TotLen = len(IpList)
    MaxLen = len(IpList)
    
    Donlen = 0
    
    print(Fore.CYAN+'|'+Donlen * '█'+MaxLen * '-'+'|   '+str(Donlen) +' / '+str(TotLen))
    
    for i in range(len(IpList)):
        
        arg = f'ping -n 1 {IpList[i]}'
        
        if subprocess.call(arg,stdout=DEVNULL, stderr=subprocess.STDOUT) == 0:
           AliveList.append(IpList[i])
        else:
            DeadList.append(IpList[i])
        
        os.system('cls')
        
        Donlen = Donlen + 1
        MaxLen = MaxLen -1
        
        print(Fore.CYAN+'|'+Donlen * '█'+MaxLen * '-'+'|   '+str(Donlen) +' / '+str(TotLen)+'   '+str(round(time.time() - starttime,ndigits=2))+' s')
    os.system('cls')      
    print(Fore.CYAN+f'DONE\n{len(AliveList)} / {TotLen} servers are ONLINE\n{len(DeadList)} / {TotLen} servers are OFFLINE\n')
    
    for i in range(len(IpList)):
        
        if IpList[i] in AliveList:
            
            print(Fore.GREEN+ Style.BRIGHT+f'{IpList[i]} is ONLINE')
          
        else:
            
            print(Fore.RED+ Style.BRIGHT+f'{IpList[i]} is OFFLINE')
    
    endtime = time.time() - starttime
    
    print(Fore.CYAN+f'\nTook {round(endtime,ndigits=2)} seconds to complete')


if __name__ == '__main__':
    if len(sys.argv) == 1:
        Type = True
    else:
        Type = sys.argv[1]
    checklist(Type)



