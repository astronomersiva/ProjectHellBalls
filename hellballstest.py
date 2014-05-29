import android,time, math, datetime
droid=android.Android()
droid.setScreenBrightness(0) #To save battery levels

#constants and variables that will be used in the code
earthRadius=6369.62785
locnDetails=[]
landingChecker=[]
altDropIndicator=0
contactNumber='XXXXXXXXXX'


def convertToRadians(degrees):
#converts degrees into radians for distance calculation
  radians = degrees * (3.14 / 180)
  return radians

def batteryMonitor():
  battery=droid.batteryGetLevel().result
  droid.eventWaitFor('battery',None)
  return batlevel 

def hasLanded():
  altRange=len(landingChecker)-1
  if (landingChecker[altRange]<landingChecker[altRange-1]):
    altDropIndicator=altDropIndicator+1
    if altDropIndicator>15:
      landingSpotMessage="A suspected crash landing at"+str(locnDetails[altRange]['lat'])+" "+str(locnDetails[altRange]['long'])+"at a height of "+str(locnDetails[altRange]['alt'])
      droid.makeToast("A suspected crash landing at"+str(locnDetails[altRange]['lat'])+" "+str(locnDetails[altRange]['long'])+"at a height of "+str(locnDetails[altRange]['alt']))
      #droid.smsSend(contactNumber,"Suspect that it has landed..terminating all functions")
      return True
    else:
      return False



def locator():
  droid.startLocating()
  droid.eventWaitFor("location")
  droid.makeToast ("Waiting for GPS fix")
  gpsread=droid.readLocation().result
  latitude=float(gpsread['gps']['latitude'])
  longitude=float(gpsread['gps']['longitude'])
  altitude = float( gpsread['gps']['altitude'])
  battery=batteryMonitor()
  if(len(locnDetails)==0):
    locnDetails.append({'lat':latitude,'long':longitude,'alt':altitude,'time':datetime.datetime.now(),'distFromLaunchSite':0,'batterylevel':battery})
    landingChecker.append(altitude)
    print locnDetails[0]
    #droid.smsSend(contactNumber,locnDetails[0])
  elif(len(locnDetails==1)):
    distFromLaunchSite=distcal(locnDetails[0]['lat'],locnDetails[0]['long'])
    locnDetails.append({'lat':latitude,'long':longitude,'alt':altitude,'time':datetime.datetime.now(),'distFromLaunchSite':distFromLaunchSite,'batterylevel':battery})
    landingChecker.append(altitude)
    print locnDetails[1]
    #droid.smsSend(contactNumber,locnDetails[1])
  else:
    ind=len(locnDetails)-1
    distFromLaunchSite=distcal(locnDetails[0]['lat'],locnDetails[0]['long'],locnDetails[ind]['lat'],locnDetails[ind]['long'])
    locnDetails.append({'lat':latitude,'long':longitude,'alt':altitude,'time':datetime.datetime.now(),'distFromLaunchSite':distFromLaunchSite,'batterylevel':battery})
    landingChecker.append(altitude)
    print locnDetails[ind]
    #droid.smsSend(contactNumber,locnDetails[ind])


def distcal(l1,ln1,l2=0,ln2=0):
  dLat=convertToRadians(l2-l1)
  dLong=convertToRadians(lt2-lt1)
  a=((math.sin(dLat/2))* (math.sin(dLat/2)))+(math.cos(convertToRadians(l1))* math.cos(convertToRadians(l2)))*(math.sin(dLong/2)*math.sin(dLong/2))
  t1= math.sqrt(a)
  t2= math.sqrt(1-a)
  c=2*(math.atan2(t1,t2))
  d=earthRadius*c
  return d


#main code
droid.makeToast ("initiating launch sequence...")
droid.dialogCreateAlert("Ready","Would you like to continue?")
droid.dialogSetPositiveButtonText("Yes")
droid.dialogSetNegativeButtonText("No")
droid.dialogShow()
response=droid.dialogGetResponse().result
if response ['which']=='positive':
  locator()
  counter=int(droid.dialogGetInput('Enter the time remaining to launch','in seconds').result)
  while counter!=0: #to get some time for the launch process
    print 'Launch in '+counter+' seconds..'
    time.sleep(1)
    counter=counter-1
locator()
camCount=0 
rocketFuel=True
location=str('/sdcard/hellballs/')+str(camCount)+('.jpg') #To get unique filenames for the photos. Stops overwriting of previous photos
while(rocketFuel):
   droid.cameraCapturePicture(location)
   count=count+1
   location=str('/sdcard/hellballs')+str(count)+('.jpg')
   locator()
   time.sleep(30) #takes a pic every 30 seconds. Can be changed as needed.
   blevel=batteryMonitor()
   if blevel<30:
      droid.makeToast("Low battery")
      #droid.smsSend('contactNumber','Warning: Low battery')
      rocketFuel=False
   if (hasLanded()):
      rocketFuel=False
droid.stopLocating()


