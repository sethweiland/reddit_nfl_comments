array_teams=('nyjets' 'CHIBears' 'cowboys' 'Texans' 'panthers' 'Patriots'
       'LosAngelesRams' 'DenverBroncos' 'steelers' 'Browns'
       'buffalobills' 'miamidolphins' 'GreenBayPackers' 'Seahawks'
       'eagles' 'ravens' 'falcons' 'Tennesseetitans'
       'KansasCityChiefs' '49ers' 'NYGiants' 'bengals' 'detroitlions'
       'minnesotavikings' 'Chargers' 'Jaguars' 'Colts' 'Redskins'
       'oaklandraiders' 'Saints' 'buccaneers' 'AZCardinals')
for i in "${array_teams[@]}"
do
    end=".csv"
    new="new"
    file=$i$end
    new_file=$i$new$end
    #awk -F, 'length>NF+1' $file 
    awk -F, 'length>NF+1' $file > $new_file
done	

