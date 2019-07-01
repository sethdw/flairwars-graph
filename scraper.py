import praw
from psaw import PushshiftAPI
import datetime
#import matplotlib.pyplot as plt

api = PushshiftAPI()

cd = int(datetime.datetime(2018,4,7).timestamp())
now = int(datetime.datetime.now().timestamp())

subs = ["flairwars","InTheRed","DSRRed","TheOrangeArmyHQ","HouseYellow","TrueYellow","YellowOnlineUnion",
		"TheGreenArmy","BlueUnited","UnitedBlueRepublic","THEBLUEDAWN","PurpleImperium"]


data = []
open("data.txt","w").close()

while cd < now:
	print(datetime.datetime.fromtimestamp(cd).strftime('%c'))
	counts = [datetime.datetime.fromtimestamp(cd).strftime("%d%m%y")]
	for sub in subs:
		counts += [len(list(api.search_submissions(after=cd,before=cd+86400,subreddit=sub)))]
	cd += 86400
	data += [counts]
	file = open("data.txt","a+")
	file.write(str(counts))
	file.write("\n")
	file.close()

file = open("dataFinal.txt","w")
file.write(str(data))
file.close()