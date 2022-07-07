#DT ACQUISITION

from urllib.request import urlopen
from datetime import date
from datetime import datetime


#DATE AND TIME SERVER (THIS IS GMT)
server = urlopen('http://just-the-time.appspot.com/')
dateServer = urlopen('https://just-the-time.appspot.com/?f=%Y-%m-%d')
#FETCH TIME (MINUTE AND SECONDS ONLY)
timeServer = urlopen('https://just-the-time.appspot.com/?f=:%M:%S')
#FETCH TIME (HOUR ONLY GMT+0)
gmtServer = urlopen('https://just-the-time.appspot.com/?f=%H')

#GMT OFFSET
#USE THIS TO ADAPT TO OTHER ZONES
gmtOffset= 8


#GET SYSTEM TIME
systemDateTime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
localDate = str(date.today())
localTime = datetime.now().strftime("%H:%M:%S")
print('System :', systemDateTime)
print('Local Date:', localDate)
print('Local Time:', localTime)
print()

#ACQUIRE EPOCH
clockwork = server.read().strip()
epoch = clockwork.decode('utf-8')

datework = dateServer.read().strip()
epochDate = datework.decode('utf-8')

print('Epoch:',epoch)
print('Server Date:',epochDate)

#ACQUIRE TIME AND ADJUST
hourServer = gmtServer.read().strip().decode('utf-8')
minServer = timeServer.read().strip().decode('utf-8')
gmtFix = (int(hourServer) + gmtOffset)
epochTime = str(gmtFix) + minServer


print('Epoch Time:',epochTime)

#DATE COMPARE
date_sys = datetime.strptime(localDate, '%Y-%m-%d')
date_svr = datetime.strptime(epochDate, '%Y-%m-%d')

expDate = '2022-07-01'
date_exp = datetime.strptime(expDate, '%Y-%m-%d')
print('Expiry Date:',date_exp)

print('\n*** Checking Date ***')
print('Local Date past Epoch Date: ',  date_sys > date_svr)
print('Expire Date past Epoch Date: ',  date_exp < date_svr)

if date_svr > date_exp:
    allowed = False
else:
    allowed = True

print('Allowed:',allowed)



##DEPRECATED TO ACQUIRE INDIVIDUALLY
##ACQUIRE EPOCH IN ITS ENTIRETY
#clockwork = server.read().strip()
#epoch = clockwork.decode('utf-8')

#print result
#print('Epoch: ' + epoch)

##Splits Epoch String using <SPACE> as separator (default)
#clockwork2 = epoch.split()
#serverDate = clockwork2[0]
#serverTime = clockwork2[1]

#print('Date: ' + serverDate)
#print('Time: ' + serverTime)

