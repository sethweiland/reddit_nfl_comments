from pymongo import MongoClient
from bs4 import BeautifulSoup
import requests
import re
import logging
import os

#logging.basicConfig('download_clean.log',filemode='w',format='%(name)s - %(levelname)s - %(message)s')

# this will be used to delete all comments with subreddits that do not include the below subreddit names
filter_reg_ex = re.compile("^((?!Colts|DenverBroncos|buffalobills|ravens|Patriots|bengals|miamidolphins|Jaguars|KansasCityChiefs|Browns|Texans|oaklandraiders|nyjets|steelers|Tennesseetitans|Chargers|cowboys|CHIBears|falcons|AZCardinals|NYGiants|detroitlions|panthers|49ers|eagles|GreenBayPackers|Saints|Seahawks|Redskins|minnesotavikings|buccaneers|LosAngelesRams|bostonceltics|chicagobulls|AtlantaHawks|GoNets|clevelandcavs|CharlotteHornets|NYKnicks|DetroitPistons|heat|sixers|pacers|OrlandoMagic|torontoraptors|MkeBucks|washingtonwizards|denvernuggets|warriors|Mavericks|timberwolves|LAClippers|rockets|Thunder|lakers|memphisgrizzlies|ripcity|suns|NOLAPelicans|UtahJazz|kings|NBASpurs|angelsbaseball|whitesox|orioles|Astros|WahoosTipi|redsox|OaklandAthletics|motorcitykitties|NYYankees|Mariners|KCRoyals|tampabayrays|TexasRangers|minnesotatwins|Torontobluejays|azdiamondbacks|Cubs|Braves|ColoradoRockies|Reds|letsgofish|Dodgers|Brewers|NewYorkMets|Padres|buccos|phillies|SFGiants|Cardinals|Nationals|AnaheimDucks|Coyotes|BostonBruins|sabres|CalgaryFlames|canes|hawks|ColoradoAvalanche|BlueJackets|DallasStars|DetroitRedWings|EdmontonOilers|losangeleskings|wildhockey|Habs|Predators|devils|NewYorkIslanders|rangers|OttawaSenators|Flyers|penguins|SanJoseSharks|stlouisblues|TampaBayLightning|leafs|canucks|goldenknights|caps|winnipegjets|FloridaPanthers).)*$")

#client = MongoClient()
#db = client.reddit_comments_sports


http = "https://files.pushshift.io/reddit/comments/"
endpoints = ["RC_2017-08.bz2","RC_2017-09.bz2","RC_2017-10.bz2",
             "RC_2017-11.bz2","RC_2017-12.xz","RC_2018-01.xz",
             "RC_2018-02.xz","RC_2018-03.xz","RC_2018-04.xz",
             "RC_2018-05.xz","RC_2018-06.xz","RC_2018-07.xz",
             "RC_2018-08.xz","RC_2018-09.xz","RC_2018-10.xz",
             "RC_2018-11.zst","RC_2018-12.zst","RC_2019-01.zst",
             "RC_2019-02.zst","RC_2019-03.zst","RC_2019-04.zst",
             "RC_2019-05.zst"
        ]

for endpoint in endpoints[10:]: 
    os.system("wget " + http + endpoint)
    file_name,file_extension = os.path.splitext(endpoint)

    #use different command to unzip based on file extension
    if file_extension == ".bz2":
        os.system("bunzip2 " + endpoint) 
    elif file_extension == ".xz":
        os.system("unxz " + endpoint)
    elif file_extension ==".zst":
        os.system("unzstd " + endpoint)
    #remove zipped file
    os.system(f"rm {endpoint}")
    os.system(f"grep -E 'Colts|DenverBroncos|buffalobills|ravens|Patriots|bengals|miamidolphins|Jaguars|KansasCityChiefs|Browns|Texans|oaklandraiders|nyjets|steelers|Tennesseetitans|Chargers|cowboys|CHIBears|falcons|AZCardinals|NYGiants|detroitlions|panthers|49ers|eagles|GreenBayPackers|Saints|Seahawks|Redskins|minnesotavikings|buccaneers|LosAngelesRams|bostonceltics|chicagobulls|AtlantaHawks|GoNets|clevelandcavs|CharlotteHornets|NYKnicks|DetroitPistons|heat|sixers|pacers|OrlandoMagic|torontoraptors|MkeBucks|washingtonwizards|denvernuggets|warriors|Mavericks|timberwolves|LAClippers|rockets|Thunder|lakers|memphisgrizzlies|ripcity|suns|NOLAPelicans|UtahJazz|kings|NBASpurs|angelsbaseball|whitesox|orioles|Astros|WahoosTipi|redsox|OaklandAthletics|motorcitykitties|NYYankees|Mariners|KCRoyals|tampabayrays|TexasRangers|minnesotatwins|Torontobluejays|azdiamondbacks|Cubs|Braves|ColoradoRockies|Reds|letsgofish|Dodgers|Brewers|NewYorkMets|Padres|buccos|phillies|SFGiants|Cardinals|Nationals|AnaheimDucks|Coyotes|BostonBruins|sabres|CalgaryFlames|canes|hawks|ColoradoAvalanche|BlueJackets|DallasStars|DetroitRedWings|EdmontonOilers|losangeleskings|wildhockey|Habs|Predators|devils|NewYorkIslanders|rangers|OttawaSenators|Flyers|penguins|SanJoseSharks|stlouisblues|TampaBayLightning|leafs|canucks|goldenknights|caps|winnipegjets|FloridaPanthers' {file_name} > holder_file")  
    os.system(f"mongoimport --db reddit_comments_sports --collection All_Data --type json --file holder_file") 
    client = MongoClient()
    print("Succesfully wrote to db")
    db = client.reddit_comments_sports
    #only because grep will include all reddit comments with metadata that includes name of subreddits we want
    db.All_Data.delete_many({'subreddit':filter_reg_ex})
    #release the memory of deleted mongoDB back to OS
    db.command({"compact":'All_Data'})  
    #remove the unzipped file after we have written to the mongodb
    os.system(f"rm {file_name}")
    os.system(f"rm holder_file")
