import random

def format(id,year,finance,company,investors):
	global f
	temp = 'insert into `finances` values({},{},\'{}\',\'{}\',\'{}\');\n'
	x = temp.format(id,year,finance,company,investors)
	f.write(x)




f = open("my.txt","w")
id =3
year = 2015
finance = "fi_"
company ="com_"
investors = "inv_"
for id in range(3,300):
	yearT = year 
	financeT =finance+ str(int(id/20))
	companyT =company + str(random.randint(1,100))
	investorsT = investors + str(random.randint(1,100000))
	format(id,yearT,financeT,companyT,investorsT)


f.close()