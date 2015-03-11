from geopy.geocoders import Nominatim
import csv

geolocator = Nominatim()

#source file
costcos = csv.reader(open('costcos-limited.csv', 'r'), delimiter=',')
#target file
writer = csv.writer(open('costcos-withgeo.csv', 'w'), delimiter=',')
header_skipped = False


for row in costcos:
	# Print header
	if not header_skipped:
		data = ["Warehouse Number","Address","City","State","Zip Code","Latitude","Longitude"]
		header_skipped = True
		writer.writerow(data)
		continue


	full_addy = row[0]+','+ row[1] + ',' + row[2] + ',' + row[3] + ',' + row[4]
#    print full_addy
	full_addy2 = row[1] + ',' + row[2] + ',' + row[3]
#    print full_addy2

	try:
		location, (lat, lng) = geolocator.geocode(full_addy2)
		#print(full_addy + ',' + str(lat) + ',' + str(lng))
		data = [row[0],row[1],row[2],row[3],row[4],str(lat),str(lng)]
	except:
		tempStr = full_addy + ',' + ',NULL,NULL'
		print(full_addy + ",NULL,NULL")
		data = [row[0],row[1],row[2],row[3],row[4],"NULL","NULL"]

	writer.writerow(data)
