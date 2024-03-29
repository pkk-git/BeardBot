from prettytable import PrettyTable
import getdata as gd
import datetime
from datetime import timedelta
import pytz
from pytz import timezone
utc=pytz.UTC

def getStandings() :
	x=PrettyTable()
	x.border = False
	stand=gd.getData(3)
	stand.sort(reverse=True,key=lambda x: x['wins'])
	x.field_names = ["Team", "W", "L", "Division"]
	for i in range(0,len(stand),1) :
		x.add_row([stand[i]['team'].name.replace('_'," "),stand[i]['wins'],stand[i]['losses'],stand[i]['division'].name])
	return x

def getSchedule() :
	x=PrettyTable()
	x.border = False
	dtm=datetime.datetime.now()
	dtm=dtm-timedelta(days=1)
	fdtm=utc.localize(dtm)
	bs=gd.getData(2)
	x.field_names = ["Home","Away","Score","Date","Time"]
	val=0
	for i in range(0,len(bs),1) :
		ldtm=bs[i]['start_time']
		if(fdtm<ldtm and val<5) :
			a=bs[i]['home_team'].name.replace('_'," ")
			b=bs[i]['away_team'].name.replace('_'," ")
			index1=a.rfind(" ")
			index2=b.rfind(" ")
			a=a[index1:]
			b=b[index2:]
			c=bs[i]['home_team_score']
			d=bs[i]['away_team_score']
			e=str(c)+"-"+str(d)
			x.add_row([a,b,e,bs[i]['start_time'].strftime("%d %b"),bs[i]['start_time'].strftime("%H:%M")])
			val=val+1
	return x

def getTeams() :
	x=PrettyTable()
	x.border = False
	stand=gd.getData(3)
	stand.sort(reverse=True,key=lambda x: x['wins'])
	x.field_names = ["Team Name"]
	for i in range(0,len(stand),1) :
		x.add_row([stand[i]['team'].name.replace('_'," ")])
	return x

def getStandingsEast() :
	x=PrettyTable()
	x.border = False
	stand=gd.getData(3)
	stand.sort(reverse=True,key=lambda x: x['wins'])
	x.field_names = ["Team", "W", "L", "Division"]
	for i in range(0,len(stand),1) :
		if(str(stand[i]['conference'])==("Conference.EASTERN")) :
			x.add_row([stand[i]['team'].name.replace('_'," "),stand[i]['wins'],stand[i]['losses'],stand[i]['division'].name])
	return x

def getStandingsWest() :
	x=PrettyTable()
	x.border = False
	stand=gd.getData(3)
	stand.sort(reverse=True,key=lambda x: x['wins'])
	x.field_names = ["Team", "W", "L", "Division"]
	for i in range(0,len(stand),1) :
		if(str(stand[i]['conference'])==("Conference.WESTERN") or stand[i]['conference'] is None) :
			x.add_row([stand[i]['team'].name.replace('_'," "),stand[i]['wins'],stand[i]['losses'],stand[i]['division'].name])
	return x

def getTeamBoxScores() :
	x=PrettyTable()
	x.border = False
	stand=gd.getData(1)
	if(stand==[]) :
		return 0
	else :
		x.field_names = ["Team", "Outcome","FG%","3P%","AST","TREB","BLK","STL","TO"]
		for i in range(0,len(stand),1) :
			x.add_row([stand[i]['team'].name.replace('_'," "),stand[i]['outcome'].name,round(float(stand[i]['made_field_goals'])*100.0/float(stand[i]['attempted_field_goals'])),round(float(stand[i]['made_three_point_field_goals'])*100.0/float(stand[i]['attempted_three_point_field_goals'])),stand[i]['assists'],stand[i]['offensive_rebounds']+stand[i]['defensive_rebounds'],stand[i]['blocks'],stand[i]['steals'],stand[i]['turnovers']])
		return x
	








