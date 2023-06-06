import subprocess
import json
import os
from datetime import date,datetime
from dateutil.relativedelta import relativedelta

def cmd_run(name: str,command: str):
    pass
    print(f'command run: \n{command}')

    upload_command(name=name,command=command)
    subprocess.run(command,shell=True)

    return True

def upload_command(name: str,command: str):
    pass 
    now = datetime.now()
    year,month,day,time = f'{now.year:02}',f'{now.month:02}',f'{now.day:02}',f'{now.hour:02}:{now.minute:02}:{now.second:02}'

    with open('runParameters.json') as file:
        runParameters = json.load(file)

        if name not in runParameters.keys():
            runParameters[name] = {f'{year}': {f'{month}': {f'{day}': {f'{time}': command}}}}
        elif year not in runParameters[name].keys():
            runParameters[name][year] = {f'{month}': {f'{day}': {f'{time}': command}}}
        elif month not in runParameters[name][year].keys():
            runParameters[name][year][month] = {f'{day}': {f'{time}': command}}        
        elif day not in runParameters[name][year][month].keys():
            runParameters[name][year][month][day] = {f'{time}': command}
        elif time not in runParameters[name][year][month][day].keys():
            runParameters[name][year][month][day][time] = command
        else:
            print('There\'s not an option to run the command')

    with open('runParameters.json','w') as outfile:
        json.dump(runParameters,outfile,indent=2)

    return True

try:
    commandType = int(input(f'Write if the video is: \n1.- Done\n2.- Process\n'))
except:
    print(f'You must to give an integer option')
    exit()

if commandType==1:
    status = f'done'
elif commandType==2:
    status = f'inProcess'
else:
    print(f'There\'s not these process')
    exit()

path = f'./projects/{status}'
ans = str(f'Wich file do you want to open:\n')

files = []
for file in os.listdir(path):
    if '.py' in file:
        files.append(file)  
        ans += f'{files.index(file)}.- {file}\n'

try:
    n = int(input(ans))
except:
    print(f'You must to give an integer option')
    exit()

try:
    name = files[n]
except:
    print(f'You must to give an integer between 0 to {len(files)}')
    exit()

try:
    renderOption = int(input(f'Wich quality do you want to get the video: \n1.- pl (lowest) \n2.- pm (medium) \n3.- p (highest)\n'))
except:
    print(f'You must to give an integer option')
    exit()

if renderOption==1:
    render = '-pl'
elif renderOption==2:
    render = '-pm'
elif renderOption==3:
    render = '-p'
else:
    print(f'There\'s not these option')
    exit()

cmd_run(name,f"python manim.py projects\{status}\{name} Video {render}")