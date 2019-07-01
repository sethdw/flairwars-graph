import json
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
import matplotlib.dates as mdates
import datetime
import ast

file = open("dataFinal.txt","r")
contents = file.readline()
file.close()
data = ast.literal_eval(contents)

start = datetime.datetime(2018,4,7)
dates = [start + datetime.timedelta(days=x) for x in range(0,len(data))]
subs = ["flairwars","InTheRed","DSRRed","TheOrangeArmyHQ","HouseYellow","TrueYellow","YellowOnlineUnion",
		"TheGreenArmy","BlueUnited","UnitedBlueRepublic","THEBLUEDAWN","PurpleImperium"]

#plt.xticks([datetime.datetime(2018,x,1) for x in range(4,13)]+[datetime.datetime(2019,x,1) for x in range(1,7)])

# Graph setup
graph, ax = plt.subplots()
ax.yaxis.set_major_locator(MultipleLocator(500))
ax.xaxis.set_major_locator(mdates.MonthLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter("%b %Y"))

# Season endings
for x in range(2,8):
	ax.axvline(datetime.datetime(2019,x,1),color="#4f535e")

#NORA = ax.axvline(datetime.datetime(2019,3,10),color="#aaaaaa",label="NORA introduced")

# Plots
plots = [0]
plots += [plt.plot(dates,[data[x][2] for x in range(len(data))],color="#aa0000",label="InTheRed")]
plots += [plt.plot(dates,[data[x][3] for x in range(len(data))],color="#ff0000",label="DSRRed")]
plots += [plt.plot(dates,[data[x][4] for x in range(len(data))],color="#ff6600",label="TheOrangeArmyHQ")]
plots += [plt.plot(dates,[data[x][5] for x in range(len(data))],color="#f4d93d",label="HouseYellow")]
plots += [plt.plot(dates,[data[x][6] for x in range(len(data))],color="#dab420",label="trueyellow")]
plots += [plt.plot(dates,[data[x][7] for x in range(len(data))],color="#ffee00",label="YellowOnlineUnion")]
plots += [plt.plot(dates,[data[x][8] for x in range(len(data))],color="#0e8e00",label="TheGreenArmy")]
plots += [plt.plot(dates,[data[x][9] for x in range(len(data))],color="#00f2ff",label="BlueUnited")]
plots += [plt.plot(dates,[data[x][10] for x in range(len(data))],color="#5694ff",label="UnitedBlueRepublic")]
plots += [plt.plot(dates,[data[x][11] for x in range(len(data))],color="#1e5aff",label="THEBLUEDAWN")]
plots += [plt.plot(dates,[data[x][12] for x in range(len(data))],color="#af29d1",label="PurpleImperium")]
plots[0] = plt.plot(dates,[data[x][1] for x in range(len(data))],color="white",label="flairwars")

# Annotations
plt.xlabel("Date")
plt.ylabel("Posts")
plt.title("Posts per day on /r/flairwars and associated subreddits")
plt.ylim(bottom=0)
plt.xlim(left=datetime.datetime(2018,4,7))

# Legends
colourLegend = plt.legend([x[0] for x in plots],subs,loc="upper left",ncol=4,fancybox=True,shadow=True,title="Subreddits")

# Proxy season ending
seasonEnd = plt.plot([],[],color="#4f535e",label="Totem Season Ending")
# Highlight No-alliance period
noAlliance = plt.axvspan(datetime.datetime(2019,1,1),datetime.datetime(2019,1,10),color="#565b66",label="No alliance period")

eventLegend = plt.legend([seasonEnd[0],noAlliance],["Totem season end","No-alliance period"],fancybox=True,shadow=True,loc="upper left",bbox_to_anchor=(0,0.8),title="Events")
ax.add_artist(colourLegend)


# First datetime is point to point at, second is bottom left corner of text
plt.annotate(s="First raid - TheGreenArmy (15 posts)",xy=(datetime.datetime(2018,4,23),20),
			 xytext=(datetime.datetime(2018,4,9),400),arrowprops=dict(width=1,headwidth=2,headlength=2,color="white"),bbox=dict(facecolor="white",edgecolor="black",boxstyle="round"))

plt.annotate(s="RR1 - trueyellow (152 posts)",xy=(datetime.datetime(2018,6,6),160),
			 xytext=(datetime.datetime(2018,4,27),700),arrowprops=dict(width=1,headwidth=4,headlength=4,color="white"),bbox=dict(facecolor="white",edgecolor="black",boxstyle="round"))

plt.annotate(s="Rainbow Raid 2 - THEBLUEDAWN (181 posts)",xy=(datetime.datetime(2018,6,14),190),
			 xytext=(datetime.datetime(2018,5,10),1000),arrowprops=dict(width=1,headwidth=4,headlength=4,color="white"),bbox=dict(facecolor="white",edgecolor="black",boxstyle="round"))

plt.annotate(s="Rainbow Raid 4 - BlueUnited (253 posts)",xy=(datetime.datetime(2018,8,4),260),
			 xytext=(datetime.datetime(2018,5,27),1300),arrowprops=dict(width=1,headwidth=4,headlength=4,color="white"),bbox=dict(facecolor="white",edgecolor="black",boxstyle="round"))

plt.annotate(s="Rainbow Raid 5 - flairwars (97 posts)",xy=(datetime.datetime(2018,8,16),100),
			 xytext=(datetime.datetime(2018,6,15),1600),arrowprops=dict(width=1,headwidth=4,headlength=4,color="white"),bbox=dict(facecolor="white",edgecolor="black",boxstyle="round"))

plt.annotate(s="TBOMBTV (561 posts on Yellow, 526 posts on Purple)",xy=(datetime.datetime(2018,8,20),570),
			 xytext=(datetime.datetime(2018,5,23),1900),arrowprops=dict(width=1,headwidth=4,headlength=4,color="white"),bbox=dict(facecolor="white",edgecolor="black",boxstyle="round"))

plt.annotate(s="Flair War 1 - all subs (4,578‬ total posts)",xy=(datetime.datetime(2018,10,20),1860),
			 xytext=(datetime.datetime(2018,8,1),2200),arrowprops=dict(width=1,headwidth=4,headlength=4,color="white"),bbox=dict(facecolor="white",edgecolor="black",boxstyle="round"))

plt.annotate(s="Rainbow Raid 6 - InTheRed (1331 posts)",xy=(datetime.datetime(2018,10,27),1350),
			 xytext=(datetime.datetime(2018,8,25),2500),arrowprops=dict(width=1,headwidth=4,headlength=4,color="white"),bbox=dict(facecolor="white",edgecolor="black",boxstyle="round"))

plt.annotate(s="Biggest raid ever - TheGreenArmy (4786 posts)",xy=(datetime.datetime(2019,4,30),4790),
			 xytext=(datetime.datetime(2019,1,31),4800),arrowprops=dict(width=1,headwidth=4,headlength=4,color="white"),bbox=dict(facecolor="white",edgecolor="black",boxstyle="round"))

# Display and savea
figure = plt.gcf()
figure.set_size_inches(27,8)
ax.set_facecolor("#36393f")
ax.spines["bottom"].set_color("black")
ax.spines["top"].set_color("black")
ax.spines["right"].set_color("black")
ax.spines["left"].set_color("black")
figure.patch.set_facecolor("#36393f")
plt.savefig("graph.png",dpi=100,bbox_inches="tight") # dpi 100 for testing, higher for uploading
plt.show()