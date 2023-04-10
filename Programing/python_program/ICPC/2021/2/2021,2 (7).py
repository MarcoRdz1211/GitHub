import datetime

n,t = input().split()
n,t = int(n),float(t)
times,subtitles = [],[]

for i in range(1,n+1):
    a = input()
    time = str(input())
    text = str(input())
    s = (int(time[0])+int(time[1]))*3600+(int(time[3])+int(time[4]))*60
    s += int(time[6])+int(time[7])+int(time[9])/10+int(time[10])/100+int(time[11])/1000
    s += t
    r = (int(time[17])+int(time[18]))*3600+(int(time[20])+int(time[21]))*60
    r += int(time[23])+int(time[24])+int(time[26])/10+int(time[27])/100+int(time[28])/1000
    r += t
    time0,time1 = str(datetime.timedelta(seconds=s)).replace("000","").replace(".",","),str(datetime.timedelta(seconds=r)).replace("000","").replace(".",",")
    
    if time0[1]==":":
        time0 = "0"+time0

    if time1[1]==":":
        time1 = "0"+time1
#    time0.replace("000",""),time1.replace("000","")

    times.append([time0,time1]),subtitles.append(text)
    
for i in range(0,n):
    print(i+1)
    print(times[i][0]+" --> "+times[i][1])
    print(subtitles[i])

