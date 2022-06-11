<drac2>

# Setup the embed

# Load svars
settings = load_json(get_svar("SurvSettings", '{"cooldown": true, "coolTime": 0, "fluxCool": true, "fluxCoolTime": 1}'))

# Load data and seed variables
c = character()

cs = character().skills
rr_num = c.csettings.get("reroll", None)
args = &ARGS&
parse = argparse(args)
price = parse
if len(args) == 2:
    base = f'embed -title "{name} is trying to flux {args[1]} into {args[0]}!" -color {color} -thumb {"https://i.postimg.cc/tgYyQtHN/image-2022-02-06-224714.png"} '
else:
    base = f'embed -title "{name} is trying to flux {args[1]+args[2]} into {args[0]}!" -color {color} -thumb {"https://i.postimg.cc/tgYyQtHN/image-2022-02-06-224714.png"} '
#flux - https://ibb.co/SryXh4Y
cab = cs.arcana
catch_string = cab.d20()
catch_check = vroll(catch_string)
beingLevel = ""
damage = 0
savePassed = False
q='o'
if int(level) >= 15:
    beingLevel = "IV"
else:
    beingLevel = "I" * (1 + int(level) // 5)
if catch_check.total > 3:
    base += f' -f "The ritual is going steadily.. So far.."'
elif catch_check.total == 2 or catch_check.total == 3:
    base += f' -f "Ritual collapses! Sadly, you get nothing and lose your precious coins.."'
    base += f' -f "White mist surrounds the place.. someone is in here.. You can *literally* smell the hatred. A horrifying dark humanoid creature appears in front of you. It also seems completely immune to magic.. Its presence seem to deny all spells.."'
    base += f' -f "run ``!init begin``, ``!init madd \\\"Flux Being {beingLevel}\\\"``, ``!init join`` in the ooc channel your character is currently in!"'
elif catch_check.total == 1:
    base += f' -f "Ritual collapses! Sadly, you get nothing and lose your precious coins.."'
    base += f' -f "Explosion occurs! Dark fire burns your skin.."'
    if save("con") >= 12:
        damage = (3d6) / 2
        savePassed = True
    else:
        damage = 3d6
    c.modify_hp(damage)
    base += f' -f ""'





if settings.get('fluxCoolTime') is not None and settings.get('fluxCoolTime') > 0:
	period = settings.get('fluxCoolTime')
else:
	period=settings.get('coolTime')
if settings.get('cooldown') == True or settings.get('fluxCool') == True:
	last=float(get('last_fish',0))
	current=float(time())
	x = int(last+period)
	if (current-last) < period:
		if period < 900:
			errtext = f' "You can transmutate items only every {period/60} minutes!"'
		elif (current-last) <= 86400:
			errtext = f'''"You can do this again in {'<t:' + x + ':R'}"'''
		else:
			errtext = f'''"You can do this again on {'<t:' + x + ':D'} at {'<t:' + x + ':T'}"'''
		err(errtext)
	else:
		c.set_cvar('last_fish',current)

return base
</drac2>
