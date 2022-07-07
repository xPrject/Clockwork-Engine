# ClockworkEngine
# xProject Clockwork Engine
#
# Use config.ini file to change server and gmt settings
#-------------------------------------------------------------------------------
from urllib.request import urlopen
from datetime import date
from datetime import datetime
from configparser import ConfigParser
from ClockworkEngine import *

# Instantiate config parser
config = ConfigParser()
config.read('config.ini')
gmtOffset= config.getint('Clockwork_Configuration', 'gmtOffset')


#Print Local Date Time
print('System :', systemDateTime)
print('Local Date:', localDate)
print('Local Time:', localTime)
print()

#Print Server Date Time
print('Epoch:',epoch)
print('Server Date:',epochDate)
print('Epoch Time:',epochTime, '(GMT+'+str(gmtOffset)+')')

#-------------------------------------------------------------------------------


