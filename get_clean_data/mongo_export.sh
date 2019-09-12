mongoexport --collection good_length --db reddit_comments_sports --query '{"subreddit": 
{$regex:"Colts|DenverBroncos|buffalobills|ravens|Patriots|bengals|miamidolphins|Jaguars|
KansasCityChiefs|Browns|Texans|oaklandraiders|nyjets|steelers|Tennesseetitans|Chargers|
cowboys|CHIBears|falcons|AZCardinals|NYGiants|detroitlions|panthers|49ers|eagles|
GreenBayPackers|Saints|Seahawks|Redskins|minnesotavikings|buccaneers|LosAngelesRams"}}' 
--type csv --limit $1 --out sample.csv --fields "_id, author, author_flair_text,
body,can_gild,collapsed,collapsed_reason,controversiality,created_utc,distinguished,
edited,gilded,id,is_submitter,link_id,parent_id,retrieved_on,score,stickied,subreddit,
subreddit_id"






