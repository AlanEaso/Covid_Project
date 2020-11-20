#for creating dummy data
import namegenerator
import datetime
import random

location = 'Areekara'
pincode = 689505
f= open("datset.csv","a")
#f.write("Patient_Name,Location,Latitude,Longitude,Pincode,Time_Stamp")
#f.write('\n')
for i in range(50):
    longitude = random.uniform(76.632866,76.633252)
    latitude = random.uniform(9.280354,9.282303)
    ct = datetime.datetime.now()
    name = namegenerator.gen()
    row= '{},{},{},{},{},{}'.format(name,location,latitude,longitude,pincode,ct)
    f.write(row)
    f.write('\n')

f.close()