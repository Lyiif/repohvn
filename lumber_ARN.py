<drac2>

# Setup the embed

# Load svars
settings = load_json(get_svar("SurvSettings", '{"cooldown": true, "coolTime": 0, "fluxCool": true, "fluxCoolTime": 10}'))

# Load data and seed variables
c = character()

cs = character().skills
rr_num = c.csettings.get("reroll", None)
args = &ARGS&
parse = argparse(args)
price = parse
base = f'embed -title "{name} is trying to chop down some trees!" -color {color} -thumb {"https://i.ibb.co/KzCNqKM/trees.png"} '
#flux - https://ibb.co/SryXh4Y
cab = cs.arcana
catch_string = cab.d20()
catch_check = roll("1d20") + strengthMod
ammount = roll("1d20")*2
if catch_check >= 15:
    base += f' -f "Chop Chop..."'
    base += f' -f "Nice! A tree falls, and you manage to gather a total of {ammount} lb\\\'s of wood!\n\nUse ``!bag + {ammount} Wood``"'
else:
    base += f' -f "Nah, that hit was too weak! Try again!"'





if settings.get('fluxCoolTime') is not None and settings.get('fluxCoolTime') > 0:
	period = settings.get('fluxCoolTime')
else:
	period=settings.get('coolTime')
if settings.get('cooldown') == True or settings.get('fluxCool') == True:
	last=float(get('last_fish',0))
	current=float(time())
	x = int(last+period)
	if (current-last) < period:
		if period < 91:
			errtext = f' "You chop trees only every {period} seconds!"'
		elif (current-last) <= 86400:
			errtext = f'''"You can do this again in {'<t:' + x + ':R'}"'''
		else:
			errtext = f'''"You can do this again on {'<t:' + x + ':D'} at {'<t:' + x + ':T'}"'''
		err(errtext)
	else:
		c.set_cvar('last_fish',current)

return base
</drac2>
