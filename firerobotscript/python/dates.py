import re
import os
from datetime import timedelta
from datetime import datetime

def change_dates():
	file = os.getcwd()
	with open("{0}/Common_Variables.txt".format(file),'r') as fobj:
		filedata = fobj.read()
	match_result=re.findall(r'\${start_date}.*',filedata)
	filedata = filedata.replace(match_result[0], '${start_date}			%s'%(datetime.today()+timedelta(days=2)).strftime('%m/%d/%Y'))
	match_result=re.findall(r'\${end_date}.*',filedata)
	filedata = filedata.replace(match_result[0], '${end_date}			%s'%(datetime.today()+timedelta(days=28)).strftime('%m/%d/%Y'))
	match_result=re.findall(r'\${past_start_date}.*',filedata)
	filedata = filedata.replace(match_result[0], '${past_start_date}		%s'%(datetime.today()+timedelta(days=-3)).strftime('%m/%d/%Y'))
	match_result=re.findall(r'\${past_end_date}.*',filedata)
	filedata = filedata.replace(match_result[0], '${past_end_date}		%s'%(datetime.today()+timedelta(days=-2)).strftime('%m/%d/%Y'))
	with open("{0}/Common_Variables.txt".format(file),'w') as fobj:
		fobj.seek(0)
		fobj.write(filedata)
    	print filedata
