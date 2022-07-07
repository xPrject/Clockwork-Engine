# ClockworkEngine
# xProject Clockwork Engine
#
# Use config.ini file to change server and gmt settings
#------------------------------------------------------------------------------
from urllib.request import urlopen
from datetime import date
from datetime import datetime
from configparser import ConfigParser

# Instantiate config parser
config = ConfigParser()
config.read('config.ini')

# read serverUrl as string
serverUrl = config.get('Clockwork_Configuration', 'server')
# read gmtOffset as int
gmtOffset= config.getint('Clockwork_Configuration', 'gmtOffset')

#DATE AND TIME SERVER (THIS IS GMT)
server = urlopen(serverUrl)
dateServer = urlopen(serverUrl + '?f=%Y-%m-%d')
#FETCH TIME (HOUR ONLY GMT+0)
gmtServer = urlopen(serverUrl + '?f=%H')
#FETCH TIME (MINUTE AND SECONDS ONLY)
timeServer = urlopen(serverUrl + '?f=:%M:%S')


#GET SYSTEM TIME
systemDateTime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
localDate = str(date.today())
localTime = datetime.now().strftime("%H:%M:%S")

#ACQUIRE EPOCH
clockwork = server.read().strip()
epoch = clockwork.decode('utf-8')

datework = dateServer.read().strip()
epochDate = datework.decode('utf-8')


#ACQUIRE TIME AND ADJUST
hourServer = gmtServer.read().strip().decode('utf-8')
minServer = timeServer.read().strip().decode('utf-8')
gmtFix = (int(hourServer) + gmtOffset)
epochTime = str(gmtFix) + minServer


#DATE COMPARE
date_sys = datetime.strptime(localDate, '%Y-%m-%d')
date_svr = datetime.strptime(epochDate, '%Y-%m-%d')

expDate = '2022-07-01'
date_exp = datetime.strptime(expDate, '%Y-%m-%d')


if date_svr > date_exp:
    allowed = False
else:
    allowed = True

#------------------------------------------------------------------------------






