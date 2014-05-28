import android,time, math
droid=android.Android()

earthRadius=3958.75
locnDetails=[]

def con(degrees):
#converts into radians
  radians = degrees * (3.14 / 180)
  return radians

def locator():
  droid.startLocating()
  droid.eventWaitFor("location")
  droid.makeToast ("Waiting for GPS fix")
  gpsread=droid.readLocation().result
  droid.stopLocating()
  latitude=float(gpsread['gps']['latitude'])
  longitude=float(gpsread['gps']['longitude'])
  altitude = float( gpsread['gps']['altitude'])
  if(len(locnDetails)==0):
    locnDetails.append({'lat':latitude,'long':longitude,'alt':altitude,'time':time.strftime("%H:%M:%S"),'distFromLaunchSite':0})
  elif(len(locnDetails==1)):
    distFromLaunchSite=distcal(locnDetails[0]['lat'],locnDetails[0]['long'])
    locnDetails.append({'lat':latitude,'long':longitude,'alt':altitude,'time':time.strftime("%H:%M:%S"),'distFromLaunchSite':distFromLaunchSite})
  else:
    ind=len(locnDetails)-1
    distFromLaunchSite=distcal(locnDetails[0]['lat'],locnDetails[0]['long'],locnDetails[ind]['lat'],locnDetails[ind]['long'])
    locnDetails.append({'lat':latitude,'long':longitude,'alt':altitude,'time':time.strftime("%H:%M:%S"),'distFromLaunchSite':distFromLaunchSite})
  print locnDetails



def distcal(l1,ln1,l2=0,ln2=0):
  dLat=con(l2-l1)
  dLong=con(lt2-lt1)
  a=((math.sin(dLat/2))* (math.sin(dLat/2)))+(math.cos(con(l1))* math.cos(con(l2)))*(math.sin(dLong/2)*math.sin(dLong/2))
  t1= math.sqrt(a)
  t2= math.sqrt(1-a)
  c=2*(math.atan2(t1,t2))
  d=earthRadius*c
  mc=1609
  sol=str((d*mc)/1000)
  return sol

droid.makeToast ("initiating launch sequence...")
#if all set for launch
droid.dialogCreateAlert("Ready","Would you like to continue?")
droid.dialogSetPositiveButtonText("Yes")
droid.dialogSetNegativeButtonText("No")
droid.dialogShow()
response=droid.dialogGetResponse().result
if response ['which']=='positive':
  locator()
  counter=int(droid.dialogGetInput('Enter the time remaining to launch','in seconds').result)
  while counter!=0:
    print 'Launch in '+counter+' seconds..'
    time.sleep(1)
    counter=counter-1
locator()
time.sleep(20)
camCount=0
location=str('/sdcard/hellballs/')+str(camCount)+('.jpg')
while(True):
   droid.cameraCapturePicture(location)
   count=count+1
   location=str('/sdcard/hellballs')+str(count)+('.jpg')
   locator()
   time.sleep(30)

