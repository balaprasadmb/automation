import re
import uuid
import string
import random
import os
from datetime import datetime

def random_id():
    l = list(range(255))
    while l[0] == 0:
        random.shuffle(l)
    length = random.randrange(6,255)
    return int(''.join(str(d) for d in l[:length]))
    
def get_string():
    return (''.join(random.choice(string.ascii_uppercase) for i in range(10)))

def get_uid():
    return uuid.uuid4()

def get_agency_group():
    files = open(os.path.dirname(__file__)+"/inbuilt_arguments.txt")
    file_text = files.read()
    list_of_match_text = re.findall(r'"(.*?)"', file_text)
    agency_group = list_of_match_text[0]
    return agency_group

def get_agency():
    files = open(os.path.dirname(__file__)+"/inbuilt_arguments.txt")
    file_text = files.read()
    list_of_match_text = re.findall(r'"(.*?)"', file_text)
    agency = list_of_match_text[1]
    return agency

def get_campaign():
    files = open(os.path.dirname(__file__)+"/inbuilt_arguments.txt")
    file_text = files.read()
    list_of_match_text = re.findall(r'"(.*?)"', file_text)
    campaign = list_of_match_text[3]
    return campaign

def get_media_plan():
    files = open(os.path.dirname(__file__)+"/inbuilt_arguments.txt")
    file_text = files.read()
    list_of_match_text = re.findall(r'"(.*?)"', file_text)
    media_plan = list_of_match_text[4]
    return media_plan
    
def get_inventory():
    files = open(os.path.dirname(__file__)+"/inbuilt_arguments.txt")
    file_text = files.read()
    list_of_match_text = re.findall(r'"(.*?)"', file_text)
    inventory = list_of_match_text[5]
    return inventory

def get_deal():
    files = open(os.path.dirname(__file__)+"/inbuilt_arguments.txt")
    file_text = files.read()
    list_of_match_text = re.findall(r'"(.*?)"', file_text)
    deal = list_of_match_text[6]
    return deal

def get_advertiser():
    files = open(os.path.dirname(__file__)+"/inbuilt_arguments.txt")
    file_text = files.read()
    list_of_match_text = re.findall(r'"(.*?)"', file_text)
    advertiser = list_of_match_text[2]
    return advertiser

def get_activity():
    files = open(os.path.dirname(__file__)+"/inbuilt_arguments.txt")
    file_text = files.read()
    list_of_match_text = re.findall(r'"(.*?)"', file_text)
    activity = list_of_match_text[7]
    return activity

def get_flight():
    files = open(os.path.dirname(__file__)+"/inbuilt_arguments.txt")
    file_text = files.read()
    list_of_match_text = re.findall(r'"(.*?)"', file_text)
    flight = list_of_match_text[8]
    return flight


def write_to_file(agency_group = None, agency = None, advertiser = None, campaign = None, media_plan = None, inventory = None, deal = None,\
                    activity = None,flight = None):
    with open(os.path.dirname(__file__)+"/inbuilt_arguments.txt",'r') as fobj:
        filedata = fobj.read()
    list_of_match_text = re.findall(r'"(.*?)"', filedata)
    if agency_group is not None:
        if filedata.find("agency_group") != -1:
            filedata = filedata.replace(list_of_match_text[0], agency_group)
    if agency is not None:
        if filedata.find("agency") != -1:
            filedata = filedata.replace(list_of_match_text[1], agency)
    if advertiser is not None:
        if filedata.find("advertiser") != -1:
            filedata = filedata.replace(list_of_match_text[2], advertiser)
    if campaign is not None:
        if filedata.find("campaign")!= -1:
            filedata = filedata.replace(list_of_match_text[3], campaign)
    if media_plan is not None:
        if filedata.find("media_plan")!= -1:
            filedata = filedata.replace(list_of_match_text[4], media_plan)
    if inventory is not None:
        if filedata.find("inventory")!= -1:
            filedata = filedata.replace(list_of_match_text[5], inventory)
    if deal is not None:
        if filedata.find("deal")!= -1:
            filedata = filedata.replace(list_of_match_text[6], deal)
    if activity is not None:
        if filedata.find("activity")!= -1:
            filedata = filedata.replace(list_of_match_text[7], activity)
    if flight is not None:
        if filedata.find("flight")!= -1:
            filedata = filedata.replace(list_of_match_text[8], flight)
    with open(os.path.dirname(__file__)+"/inbuilt_arguments.txt",'w') as fobj:
        fobj.seek(0)
        fobj.write(filedata)

def get_todaysdate():
    return datetime.today().strftime('%a, %d %b %Y')
