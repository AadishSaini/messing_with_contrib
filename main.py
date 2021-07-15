import os
import random
t_days = [1, 3, 5, 7, 9, 11]

for a in range(365):
	month = random.randint(1, 12)
	if month == 2:
		date = random.randint(1, 29)
	elif month in t_days:
		date = random.randint(1, 31)
	else:
		date = random.randint(1,30)
	fmat = str(month)+"/"+str(date)+"/"+"2021"
	with open('file.txt', 'r') as f:
		chars_s = f.readlines()
		chars = len(chars_s[0])
	with open('file.txt', "w+") as f:
		f.seek(chars)
		f.write(fmat)
	os.system('git add file.txt')
	os.system('git commit -a --date="'+fmat+'" -m "commit"')
	#MM/DD/YYYY