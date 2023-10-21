def game_dict():
    return {
        "home": {
            "team_name": "Cleveland Cavaliers",
            "colors": ["Wine", "Gold"],
            "players": [
                {
                    "name": "Jarrett Allen",
                    "number": 31,
                    "position": "Center",
                    "points_per_game": 16.1,
                    "rebounds_per_game": 10.8,
                    "assists_per_game": 1.6,
                    "steals_per_game": 0.8,
                    "blocks_per_game": 1.3,
                    "career_points": 3945,
                    "age": 24,
                    "height_inches": 82,
                    "shoe_brand": "Nike",
                },
                {
                    "name": "Darius Garland",
                    "number": 10,
                    "position": "Point Guard",
                    "points_per_game": 21.7,
                    "rebounds_per_game": 3.3,
                    "assists_per_game": 8.6,
                    "steals_per_game": 1.3,
                    "blocks_per_game": 0.1,
                    "career_points": 3142,
                    "age": 22,
                    "height_inches": 73,
                    "shoe_brand": "Nike",
                },
                {
                    "name": "Evan Mobley",
                    "number": 4,
                    "position": "Center",
                    "points_per_game": 15.0,
                    "rebounds_per_game": 8.3,
                    "assists_per_game": 2.5,
                    "steals_per_game": 0.8,
                    "blocks_per_game": 1.7,
                    "career_points": 1034,
                    "age": 21,
                    "height_inches": 83,
                    "shoe_brand": "Adidas",
                },
                {
                    "name": "Kevin Love",
                    "number": 0,
                    "position": "Power Forward",
                    "points_per_game": 13.6,
                    "rebounds_per_game": 7.2,
                    "assists_per_game": 2.2,
                    "steals_per_game": 0.4,
                    "blocks_per_game": 0.2,
                    "career_points": 14305,
                    "age": 34,
                    "height_inches": 80,
                    "shoe_brand": "Nike",
                },
                {
                    "name": "Isaac Okoro",
                    "number": 35,
                    "position": "Small Forward",
                    "points_per_game": 8.8,
                    "rebounds_per_game": 3.0,
                    "assists_per_game": 1.8,
                    "steals_per_game": 0.8,
                    "blocks_per_game": 0.3,
                    "career_points": 1234,
                    "age": 21,
                    "height_inches": 77,
                    "shoe_brand": "Nike",
                },
                {
                    "name": "Ricky Rubio",
                    "number": 99,
                    "position": "Point Guard",
                    "points_per_game": 13.1,
                    "rebounds_per_game": 4.1,
                    "assists_per_game": 6.6,
                    "steals_per_game": 1.4,
                    "blocks_per_game": 0.2,
                    "career_points": 7399,
                    "age": 31,
                    "height_inches": 74,
                    "shoe_brand": "Adidas",
                },
            ],
        },
            
        "away": {
            "team_name": "Washington Wizards",
            "colors": ["Red", "White", "Navy Blue"],
            "players": [   
                {
                    "name": "Bradley Beal",
                    "number": 3,
                    "position": "Shooting Guard",
                    "points_per_game": 23.2,
                    "rebounds_per_game": 4.7,
                    "assists_per_game": 6.6,
                    "steals_per_game": 0.9,
                    "blocks_per_game": 0.4,
                    "career_points": 14231,
                    "age": 29,
                    "height_inches": 76,
                    "shoe_brand": "Nike",
                },
                {
                    "name": "Kyle Kuzma",
                    "number": 33,
                    "position": "Power Forward",
                    "points_per_game": 17.1,
                    "rebounds_per_game": 8.5,
                    "assists_per_game": 3.5,
                    "steals_per_game": 0.6,
                    "blocks_per_game": 0.9,
                    "career_points": 5336,
                    "age": 27,
                    "height_inches": 81,
                    "shoe_brand": "Puma",
                },
                {
                    "name": "Kentavious Caldwell-Pope",
                    "number": 1,
                    "position": "Shooting Guard",
                    "points_per_game": 13.2,
                    "rebounds_per_game": 3.4,
                    "assists_per_game": 1.9,
                    "steals_per_game": 1.1,
                    "blocks_per_game": 0.3,
                    "career_points": 7911,
                    "age": 29,
                    "height_inches": 77,
                    "shoe_brand": "Nike",
                },
                {
                    "name": "Davis Bertans",
                    "number": 42,
                    "position": "Power Forward",
                    "points_per_game": 5.6,
                    "rebounds_per_game": 2.1,
                    "assists_per_game": 0.6,
                    "steals_per_game": 0.3,
                    "blocks_per_game": 0.3,
                    "career_points": 3165,
                    "age": 29,
                    "height_inches": 82,
                    "shoe_brand": "Nike",
                },
                {
                    "name": "Kristaps Porzingis",
                    "number": 6,
                    "position": "Power Forward",
                    "points_per_game": 22.1,
                    "rebounds_per_game": 8.8,
                    "assists_per_game": 2.9,
                    "steals_per_game": 0.7,
                    "blocks_per_game": 1.5,
                    "career_points": 6371,
                    "age": 27,
                    "height_inches": 87,
                    "shoe_brand": "Adidas",
                },
                {
                    "name": "Rui Hachimura",
                    "number": 8,
                    "position": "Power Forward",
                    "points_per_game": 11.3,
                    "rebounds_per_game": 3.8,
                    "assists_per_game": 1.1,
                    "steals_per_game": 0.5,
                    "blocks_per_game": 0.2,
                    "career_points": 1913,
                    "age": 24,
                    "height_inches": 80,
                    "shoe_brand": "Jordan",
                },
            ]
        }
    }

mygdct = game_dict();

def getTeamTypeForPlayer(name):
    if (name == None or len(name) < 1): return "";
    else: pass;
    global mygdct;
    myhps = mygdct["home"]["players"];
    myaps = mygdct["away"]["players"];
    for n in range(len(myhps)):
        if (myhps[n]["name"] == name): return "home";
        else: pass;
    for n in range(len(myaps)):
        if (myaps[n]["name"] == name): return "away";
        else: pass;
    return "";

def team_names():
    global mygdct;
    return [mygdct["home"]["team_name"], mygdct["away"]["team_name"]];

def getTypeOfTeamFromName(tmname):
    tmnms = team_names();
    teamtype = "";
    if (tmnms[0] == tmname): teamtype = "home";
    elif (tmnms[1] == tmname): teamtype = "away";
    else: pass;
    return teamtype;

def team_colors(name):
    if (name == None or len(name) < 1): return [];
    else: pass;
    teamtype = getTypeOfTeamFromName(name);
    if (teamtype == "home" or teamtype == "away"): pass;
    else: return [];
    global mygdct;
    return mygdct[teamtype]["colors"];

def getPlayersOnTeamType(type):
    global mygdct;
    if (type == None or len(type) < 1): return [];
    elif (type == "home" or type == "away"): return mygdct[type]["players"];
    else: return [];

def player_numbers(tmname):
    mps = getPlayersOnTeamType(getTypeOfTeamFromName(tmname));
    if (mps == None or len(mps) < 1): return [];
    else: return [mp["number"] for mp in mps];

def getAllPlayers():
    global mygdct;
    mhps = mygdct["home"]["players"];
    maps = mygdct["away"]["players"];
    return mhps + maps;

def player_stats(name):
    if (name == None or len(name) < 1): return None;
    else: pass;
    mps = getAllPlayers();
    for mp in mps:
        if (mp["name"] == name): return mp;
        else: pass;
    return None;

def num_points_per_game(name):
    mp = player_stats(name);
    if (mp == None): return 0;
    else: return mp["points_per_game"];

def player_age(name):
    mp = player_stats(name);
    if (mp == None): return 0;
    else: return mp["age"];

def getPlayerInfoForKey(key):
    if (key == None or len(key) < 1): raise Exception("invalid key found and used here!");
    else: pass;
    mps = getAllPlayers();
    mkeys = mps[0].keys();
    useit = False;
    for mkey in mkeys:
        if (mkey == key):
            useit = True;
            break;
        else: pass;
    if (useit): return [mp[key] for mp in mps];
    else: raise Exception("invalid key found and used here!");

def getAllPlayerNames():
    return getPlayerInfoForKey("name");

def getShoeBrandsForEachPlayer():
    return getPlayerInfoForKey("shoe_brand");

def getReboundsForEachPlayer():
    return getPlayerInfoForKey("rebounds_per_game");

def getCommonJerseyNumbers():
    tmnms = team_names();
    pnumshtm = player_numbers(tmnms[0]);
    pnumsatm = player_numbers(tmnms[1]);
    cnums = [];
    for hnum in pnumshtm:
        for anum in pnumsatm:
            if (hnum == anum):
                cnums.append(hnum);
                break;
            else: pass;
    return cnums;

def getLongestPlayerName():
    mpnames = getAllPlayerNames();
    mynamelens = [len(name) for name in mpnames];
    return max(mynamelens);

def getUniqueShoeBrands():
    msbs = getShoeBrandsForEachPlayer()
    if (len(msbs) < 1): return [];
    else: pass;
    usbs = [];
    for msb in msbs:
        addit = True;
        if (len(usbs) < 1): pass;
        else:
            for n in range(len(usbs)):
                if (usbs[n] == msb):
                    addit = False;
                    break;
                else: pass;
        if (addit): usbs.append(msb);
        else: pass;
    return usbs;

def getReboundsForUniqueShoeBrand():
    usbs = getUniqueShoeBrands();
    msbs = getShoeBrandsForEachPlayer();
    rbspp = getReboundsForEachPlayer();
    rbsperusbs = [];
    for usb in usbs:
        mlist = [];
        for i in range(len(msbs)):
            if (usb == msbs[i]):
                mlist.append(rbspp[i]);
        rbsperusbs.append(mlist);
    return rbsperusbs;

def average(values):
    if (values == None or len(values) < 1): return 0;
    else: return (sum(values) / len(values));

def average_rebounds_by_shoe_brand():
    usbs = getUniqueShoeBrands();
    rbsperusbs = getReboundsForUniqueShoeBrand();
    arbsperusbs = [average(rb) for rb in rbsperusbs];
    #print(usbs);
    #print(rbsperusbs);
    #for i in range(len(usbs)): print(average(rbsperusbs[i]));
    #print(arbsperusbs);
    for i in range(len(usbs)):
        print(f"{usbs[i]}:  {arbsperusbs[i]:.2f}");
    return arbsperusbs;

#print(game_dict()['home']['team_name']);
