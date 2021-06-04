from basketball_reference_web_scraper import client
from basketball_reference_web_scraper.data import OutputType
import json
import datetime
from datetime import timedelta
import pytz
from pytz import timezone
hawaii=timezone('US/Hawaii')
finstr="/Users/pranavkrishnakumar/repos/BeardBot/Data/"
dtm=datetime.datetime.now()
dtm=hawaii.localize(dtm)
dtm=dtm-timedelta(days=1)
curd=dtm.strftime("%d")
curm=dtm.strftime("%m")
cury=dtm.year
print(curd,curm,cury)
def getData(val,d=curd,m=curm,y=cury) :
	global finstr
	if (val==0) :
		return client.player_box_scores(day=d, month=m, year=y)
	elif (val==1) :
		return client.team_box_scores(day=d, month=m, year=y)
	elif (val==2) :
		return client.season_schedule(season_end_year=y)
	elif (val==3) :
		return client.standings(season_end_year=y)

def getDataLocal(val,d=curd,m=curm,y=cury) :
	global finstr
	if (val==0) :
		fstr=str(d)+"_"+str(m)+"_"+str(y)+"_"+"player_box_scores.json"
		finstr=finstr+fstr
		client.player_box_scores(
    		day=d, month=m, year=y,
    		output_type=OutputType.JSON, 
    		output_file_path="/Users/pranavkrishnakumar/repos/BeardBot/Data/player_box_scores/"+fstr
		)
	elif (val==1) :
		fstr=str(d)+"_"+str(m)+"_"+str(y)+"_"+"team_box_scores.json"
		finstr=finstr+fstr
		client.team_box_scores(
    		day=d, month=m, year=y, 
    		output_type=OutputType.JSON, 
    		output_file_path="/Users/pranavkrishnakumar/repos/BeardBot/Data/team_box_scores/"+fstr
		)
	elif (val==2) :
		fstr=str(y)+"_"+"season_schedule"+".json"
		finstr=finstr+fstr
		client.season_schedule(
    		season_end_year=y, 
    		output_type=OutputType.JSON, 
    		output_file_path="/Users/pranavkrishnakumar/repos/BeardBot/Data/season_schedule/"+fstr
		)
	elif (val==3) :
		fstr=str(y)+"_"+"season_standings"+".json"
		finstr=finstr+fstr
		client.standings(
    		season_end_year=y,
    		output_type=OutputType.JSON, 
    		output_file_path="/Users/pranavkrishnakumar/repos/BeardBot/Data/season_standings/"+fstr
		)
	return val
