<drac2>

# Setup the embed

# Load svars
settings = load_json(get_svar("SurvSettings", '{"cooldown": true, "coolTime": 0, "transmutateCool": true, "transmutateCoolTime": 10}'))

# Load data and seed variables
c = character()
cs = character().skills
rr_num = c.csettings.get("reroll", None)
args = &ARGS&
parse = argparse(args)
base = f'embed -title "{name} is trying to transmutate {args[0]}!" -color {color} -thumb {"https://i.postimg.cc/TYFp4wbS/photo-2022-02-06-11-10-56.jpg"} -desc "Transmutating is a complicated process. You need to concentrate, choose the transmutable item and start a ritual using your stone. Transmutable items will be removed right away, but you will have to wait until the process is finished to get your gold. There is also a chance to fail a ritual completely!"'
#flux - https://ibb.co/SryXh4Y
loot_added = False

cab = cs.arcana
catch_string = cab.d20()
catch_check = vroll(catch_string)
transmutable_item = str(args[0])
if len(args) > 2 or (len(args) == 2 and "-o" not in args):
    transmutable_item_quantity = int(args[1])
else:
    transmutable_item_quantity = 1
beingLevel = ""
q='o'
if int(level) >= 15:
    beingLevel = "IV"
else:
    beingLevel = "I" * (1 + int(level) // 5)
if catch_check.total != 1:
    base += f' -f "Starting transmutation..."'
else:
    base += f' -f "ritual collapses! Sadly, you get nothing and lose your transmutables."'
    base += f' -f "White mist surrounds the place.. someone is in here.. You can *literally* smell the hatred. A horrifying dark humanoid creature appears in front of you. It also seems completely immune to magic.. Its presence seem to deny all spells.."'
    base += f' -f "run ``!init begin``, ``!init madd \\\"Flux Being {beingLevel}\\\"``, ``!init join`` in the ooc channel your character is currently in!"'

bag = load_json(get('bags', []))
coinpouch = None
itemfound = False
for bagpair in bag:
    if bagpair[0] == "Coin Pouch":
        coinpouch = bagpair[1]
for bagpair in bag: #bagpair = [bagname, {'bedroll':1, 'slaves':300, etc}]
    subbag = bagpair[1]
    for i, item in enumerate(subbag.keys()):
        if transmutable_item.lower() == item.lower() and itemfound != True:
            transmutable_item = item
            itemfound = True
            if subbag[transmutable_item] >= transmutable_item_quantity:
                subbag[transmutable_item] -= transmutable_item_quantity
                if subbag[transmutable_item] == 0:
                    subbag.pop(transmutable_item)
                if "meat" in transmutable_item.lower():
                    coinpouch["sp"] += 1 * transmutable_item_quantity
                    base+=f' -f "you succesfully transmutated some meat and got {1 * transmutable_item_quantity} sp for this!\n\nadd it to your coin pouch using ``!coins + {1 * transmutable_item_quantity} sp``"'
                if "wood" in transmutable_item.lower():
                    coinpouch["sp"] += 1 * transmutable_item_quantity
                    base+=f' -f "you succesfully transmutated some wood and got {5 * transmutable_item_quantity} cp for this!\n\nadd it to your coin pouch using ``!coins + {5 * transmutable_item_quantity} cp``"'

                base += f' -f "Transmutation Success!"'
                c.set_cvar('bags', dump_json(bag))
                break
            else:
                base+= f' -f "You do not have enough {args[0]} in any of your bags."'
if itemfound == True:
    itemfound = False

else:
    base+= f' -f "You do not have {args[0]} in any of your bags."'




# Find a good spot (or not), catch it (or not), harvest it and add to bag (or not)

# Cooldown handling
if settings.get('transmutateCoolTime') is not None and settings.get('transmutateCoolTime') > 0:
	period = settings.get('transmutateCoolTime')
else:
	period=settings.get('coolTime')
if settings.get('cooldown') == True or settings.get('transmutateCool') == True:
	last=float(get('last_fish',0))
	current=float(time())
	x = int(last+period)
	if (current-last) < period:
		if period < 91:
			errtext = f' "You can transmutate items only every {period} seconds!"'
		elif (current-last) <= 86400:
			errtext = f'''"You can do this again in {'<t:' + x + ':R'}"'''
		else:
			errtext = f'''"You can do this again on {'<t:' + x + ':D'} at {'<t:' + x + ':T'}"'''
		err(errtext)
	else:
		c.set_cvar('last_fish',current)

return base
</drac2>
