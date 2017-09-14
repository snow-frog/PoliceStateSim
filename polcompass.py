import random

leftright= float(random.getrandbits(8))/256 # Economic left vs Economic right
autho = float(random.getrandbits(8))/256 # Authoritarian vs Libertarian
lr = int(round(leftright * 20))
au = int(round(autho * 20))
ideology = ''
if lr in range(0,6) and au in range(14,21):
    ideology = 'communist'
elif lr in range(0,11) and au in range(4,11):
    ideology = 'ancom'
elif lr in range(10,21) and au in range(0,4):
    ideology = 'ancap'
elif lr in range(0,11) and au in range(0,4):
    ideology = 'anarchist'
elif lr in range(9,13) and au in range(9,13):
    ideology = 'centrist'
elif lr in range(10,21) and au in range(4,9):
    ideology = 'libertarian'
elif lr in range(9,15) and au in range(13,18):
    ideology = 'nationalist'
elif lr in range(6,17) and au in range(18,21):
    ideology = 'fascist'
elif (lr in range(0,6) and au in range(10,14)) or (lr in range(6,9) and au in range(10,18)):
    ideology = 'socialist'
elif (lr in range(4,9) and au in range(4,11)) or (lr in range(9,11) and au in range(4,9)):
    ideology = 'liberal'
elif (lr in range(13,16) and au in range(9,12)) or (lr in range(16,21) and au in range(9,15)):
    ideology = 'conservative'
elif (lr in range(15,19) and au in range(15,18)) or (lr in range(18,21) and au in range(15,21)):
    ideology = 'trad'
else:
    ideology = 'UNDEFINED'

print ideology, lr, au

ideology_relations = {'Anarchist': {'Anarchist': 0, 'Centrist': 0, 'Liberal': 0, 'Nationalist': 0, 'Fascist': 0, 'Socialist': 0, 'Traditionalist': 0, 'Conservative': 0, 'Libertarian': 0, 'Communist': 0, 'Anarcho-Communist': 0, 'Anarcho-Capitalist': 0}, 'Centrist': {'Anarchist': 0, 'Centrist': 0, 'Liberal': 0, 'Nationalist': 0, 'Fascist': 0, 'Socialist': 0, 'Traditionalist': 0, 'Conservative': 0, 'Libertarian': 0, 'Communist': 0, 'Anarcho-Communist': 0, 'Anarcho-Capitalist': 0}, 'Liberal': {'Anarchist': 0, 'Centrist': 0, 'Liberal': 0, 'Nationalist': 0, 'Fascist': 0, 'Socialist': 0, 'Traditionalist': 0, 'Conservative': 0, 'Libertarian': 0, 'Communist': 0, 'Anarcho-Communist': 0, 'Anarcho-Capitalist': 0}, 'Nationalist': {'Anarchist': 0, 'Centrist': 0, 'Liberal': 0, 'Nationalist': 0, 'Fascist': 0, 'Socialist': 0, 'Traditionalist': 0, 'Conservative': 0, 'Libertarian': 0, 'Communist': 0, 'Anarcho-Communist': 0, 'Anarcho-Capitalist': 0}, 'Fascist': {'Anarchist': 0, 'Centrist': 0, 'Liberal': 0, 'Nationalist': 0, 'Fascist': 0, 'Socialist': 0, 'Traditionalist': 0, 'Conservative': 0, 'Libertarian': 0, 'Communist': 0, 'Anarcho-Communist': 0, 'Anarcho-Capitalist': 0}, 'Socialist': {'Anarchist': 0, 'Centrist': 0, 'Liberal': 0, 'Nationalist': 0, 'Fascist': 0, 'Socialist': 0, 'Traditionalist': 0, 'Conservative': 0, 'Libertarian': 0, 'Communist': 0, 'Anarcho-Communist': 0, 'Anarcho-Capitalist': 0}, 'Traditionalist': {'Anarchist': 0, 'Centrist': 0, 'Liberal': 0, 'Nationalist': 0, 'Fascist': 0, 'Socialist': 0, 'Traditionalist': 0, 'Conservative': 0, 'Libertarian': 0, 'Communist': 0, 'Anarcho-Communist': 0, 'Anarcho-Capitalist': 0}, 'Conservative': {'Anarchist': 0, 'Centrist': 0, 'Liberal': 0, 'Nationalist': 0, 'Fascist': 0, 'Socialist': 0, 'Traditionalist': 0, 'Conservative': 0, 'Libertarian': 0, 'Communist': 0, 'Anarcho-Communist': 0, 'Anarcho-Capitalist': 0}, 'Libertarian': {'Anarchist': 0, 'Centrist': 0, 'Liberal': 0, 'Nationalist': 0, 'Fascist': 0, 'Socialist': 0, 'Traditionalist': 0, 'Conservative': 0, 'Libertarian': 0, 'Communist': 0, 'Anarcho-Communist': 0, 'Anarcho-Capitalist': 0}, 'Communist': {'Anarchist': 0, 'Centrist': 0, 'Liberal': 0, 'Nationalist': 0, 'Fascist': 0, 'Socialist': 0, 'Traditionalist': 0, 'Conservative': 0, 'Libertarian': 0, 'Communist': 0, 'Anarcho-Communist': 0, 'Anarcho-Capitalist': 0}, 'Anarcho-Communist': {'Anarchist': 0, 'Centrist': 0, 'Liberal': 0, 'Nationalist': 0, 'Fascist': 0, 'Socialist': 0, 'Traditionalist': 0, 'Conservative': 0, 'Libertarian': 0, 'Communist': 0, 'Anarcho-Communist': 0, 'Anarcho-Capitalist': 0}, 'Anarcho-Capitalist': {'Anarchist': 0, 'Centrist': 0, 'Liberal': 0, 'Nationalist': 0, 'Fascist': 0, 'Socialist': 0, 'Traditionalist': 0, 'Conservative': 0, 'Libertarian': 0, 'Communist': 0, 'Anarcho-Communist': 0, 'Anarcho-Capitalist': 0}}

ideology_relations['Anarchist']['Anarchist'] = 1.0
ideology_relations['Anarchist']['Centrist'] = 0.25
ideology_relations['Anarchist']['Liberal'] = 0.3
ideology_relations['Anarchist']['Nationalist'] = 0.1 
ideology_relations['Anarchist']['Fascist'] = 0
ideology_relations['Anarchist']['Socialist'] = 0.5 
ideology_relations['Anarchist']['Traditionalist'] = 0 
ideology_relations['Anarchist']['Conservative'] = 0.1
ideology_relations['Anarchist']['Libertarian'] = 0.2
ideology_relations['Anarchist']['Communist'] = 0.5
ideology_relations['Anarchist']['Anarcho-Communist'] = 0.75
ideology_relations['Anarchist']['Anarcho-Capitalist'] = 0.5

ideology_relations['Centrist']['Anarchist'] = ideology_relations['Anarchist']['Centrist']
ideology_relations['Centrist']['Centrist'] = 1.0
ideology_relations['Centrist']['Liberal'] = 0.75
ideology_relations['Centrist']['Nationalist'] = 0.25
ideology_relations['Centrist']['Fascist'] = 0.1
ideology_relations['Centrist']['Socialist'] = 0.5
ideology_relations['Centrist']['Traditionalist'] = 0.1 
ideology_relations['Centrist']['Conservative'] = 0.75
ideology_relations['Centrist']['Libertarian'] = 0.5
ideology_relations['Centrist']['Communist'] = 0.1
ideology_relations['Centrist']['Anarcho-Communist'] = 0.1 
ideology_relations['Centrist']['Anarcho-Capitalist'] = 0.1

ideology_relations['Liberal']['Anarchist'] = ideology_relations['Anarchist']['Liberal']
ideology_relations['Liberal']['Centrist'] = ideology_relations['Centrist']['Liberal']
ideology_relations['Liberal']['Liberal'] = 1.0
ideology_relations['Liberal']['Nationalist'] = 0.1
ideology_relations['Liberal']['Fascist'] = 0
ideology_relations['Liberal']['Socialist'] = 0.75
ideology_relations['Liberal']['Traditionalist'] = 0.1 
ideology_relations['Liberal']['Conservative'] = 0.25
ideology_relations['Liberal']['Libertarian'] = 0.5
ideology_relations['Liberal']['Communist'] = 0.5
ideology_relations['Liberal']['Anarcho-Communist'] = 0.5 
ideology_relations['Liberal']['Anarcho-Capitalist'] = 0.2

ideology_relations['Nationalist']['Anarchist'] = ideology_relations['Anarchist']['Nationalist']
ideology_relations['Nationalist']['Centrist'] = ideology_relations['Centrist']['Nationalist']
ideology_relations['Nationalist']['Liberal'] = ideology_relations['Liberal']['Nationalist']
ideology_relations['Nationalist']['Nationalist'] = 1.0
ideology_relations['Nationalist']['Fascist'] = 0.8
ideology_relations['Nationalist']['Socialist'] = 0.5
ideology_relations['Nationalist']['Traditionalist'] = 0.75
ideology_relations['Nationalist']['Conservative'] = 0.5
ideology_relations['Nationalist']['Libertarian'] = 0.4
ideology_relations['Nationalist']['Communist'] = 0.1
ideology_relations['Nationalist']['Anarcho-Communist'] = 0.1
ideology_relations['Nationalist']['Anarcho-Capitalist'] = 0.3

ideology_relations['Fascist']['Anarchist'] = ideology_relations['Anarchist']['Fascist']
ideology_relations['Fascist']['Centrist'] = ideology_relations['Centrist']['Fascist']
ideology_relations['Fascist']['Liberal'] = ideology_relations['Liberal']['Fascist']
ideology_relations['Fascist']['Nationalist'] = ideology_relations['Nationalist']['Fascist']
ideology_relations['Fascist']['Fascist'] = 1.0
ideology_relations['Fascist']['Socialist'] = 0
ideology_relations['Fascist']['Traditionalist'] = 0.8 
ideology_relations['Fascist']['Conservative'] = 0.2
ideology_relations['Fascist']['Libertarian'] = 0.3
ideology_relations['Fascist']['Communist'] = 0
ideology_relations['Fascist']['Anarcho-Communist'] = 0
ideology_relations['Fascist']['Anarcho-Capitalist'] = 0.1

ideology_relations['Socialist']['Anarchist'] = ideology_relations['Anarchist']['Socialist']
ideology_relations['Socialist']['Centrist'] = ideology_relations['Centrist']['Socialist']
ideology_relations['Socialist']['Liberal'] = ideology_relations['Liberal']['Socialist']
ideology_relations['Socialist']['Nationalist'] = ideology_relations['Nationalist']['Socialist']
ideology_relations['Socialist']['Fascist'] = ideology_relations['Fascist']['Socialist']
ideology_relations['Socialist']['Socialist'] = 1.0
ideology_relations['Socialist']['Traditionalist'] = 0.1
ideology_relations['Socialist']['Conservative'] = 0.2
ideology_relations['Socialist']['Libertarian'] = 0.2
ideology_relations['Socialist']['Communist'] = 0.8
ideology_relations['Socialist']['Anarcho-Communist'] = 0.8
ideology_relations['Socialist']['Anarcho-Capitalist'] = 0.1

ideology_relations['Traditionalist']['Anarchist'] = ideology_relations['Anarchist']['Traditionalist']
ideology_relations['Traditionalist']['Centrist'] = ideology_relations['Centrist']['Traditionalist']
ideology_relations['Traditionalist']['Liberal'] = ideology_relations['Liberal']['Traditionalist']
ideology_relations['Traditionalist']['Nationalist'] = ideology_relations['Nationalist']['Traditionalist']
ideology_relations['Traditionalist']['Fascist'] = ideology_relations['Fascist']['Traditionalist']
ideology_relations['Traditionalist']['Socialist'] = ideology_relations['Socialist']['Traditionalist']
ideology_relations['Traditionalist']['Traditionalist'] = 1.0
ideology_relations['Traditionalist']['Conservative'] = 0.6
ideology_relations['Traditionalist']['Libertarian'] = 0.4
ideology_relations['Traditionalist']['Communist'] = 0
ideology_relations['Traditionalist']['Anarcho-Communist'] = 0
ideology_relations['Traditionalist']['Anarcho-Capitalist'] = 0.2

ideology_relations['Conservative']['Anarchist'] = ideology_relations['Anarchist']['Conservative']
ideology_relations['Conservative']['Centrist'] = ideology_relations['Centrist']['Conservative']
ideology_relations['Conservative']['Liberal'] = ideology_relations['Liberal']['Conservative']
ideology_relations['Conservative']['Nationalist'] = ideology_relations['Nationalist']['Conservative']
ideology_relations['Conservative']['Fascist'] = ideology_relations['Fascist']['Conservative']
ideology_relations['Conservative']['Socialist'] = ideology_relations['Socialist']['Conservative']
ideology_relations['Conservative']['Traditionalist'] = ideology_relations['Traditionalist']['Conservative']
ideology_relations['Conservative']['Conservative'] = 1.0
ideology_relations['Conservative']['Libertarian'] = 0.8
ideology_relations['Conservative']['Communist'] = 0.1
ideology_relations['Conservative']['Anarcho-Communist'] = 0.1
ideology_relations['Conservative']['Anarcho-Capitalist'] = 0.6

ideology_relations['Libertarian']['Anarchist'] = ideology_relations['Anarchist']['Libertarian']
ideology_relations['Libertarian']['Centrist'] = ideology_relations['Centrist']['Libertarian']
ideology_relations['Libertarian']['Liberal'] = ideology_relations['Liberal']['Libertarian']
ideology_relations['Libertarian']['Nationalist'] = ideology_relations['Nationalist']['Libertarian']
ideology_relations['Libertarian']['Fascist'] = ideology_relations['Fascist']['Libertarian']
ideology_relations['Libertarian']['Socialist'] = ideology_relations['Socialist']['Libertarian']
ideology_relations['Libertarian']['Traditionalist'] = ideology_relations['Traditionalist']['Libertarian']
ideology_relations['Libertarian']['Conservative'] = ideology_relations['Conservative']['Libertarian']
ideology_relations['Libertarian']['Libertarian'] = 1.0
ideology_relations['Libertarian']['Communist'] = 0.1
ideology_relations['Libertarian']['Anarcho-Communist'] = 0.1
ideology_relations['Libertarian']['Anarcho-Capitalist'] = 0.8

ideology_relations['Communist']['Anarchist'] = ideology_relations['Anarchist']['Communist']
ideology_relations['Communist']['Centrist'] = ideology_relations['Centrist']['Communist']
ideology_relations['Communist']['Liberal'] = ideology_relations['Liberal']['Communist']
ideology_relations['Communist']['Nationalist'] = ideology_relations['Nationalist']['Communist']
ideology_relations['Communist']['Fascist'] = ideology_relations['Fascist']['Communist']
ideology_relations['Communist']['Socialist'] = ideology_relations['Socialist']['Communist']
ideology_relations['Communist']['Traditionalist'] = ideology_relations['Traditionalist']['Communist']
ideology_relations['Communist']['Conservative'] = ideology_relations['Conservative']['Communist']
ideology_relations['Communist']['Libertarian'] = ideology_relations['Libertarian']['Communist']
ideology_relations['Communist']['Communist'] = 1.0
ideology_relations['Communist']['Anarcho-Communist'] = 0.8
ideology_relations['Communist']['Anarcho-Capitalist'] = 0.1

ideology_relations['Anarcho-Communist']['Anarchist'] = ideology_relations['Anarchist']['Anarcho-Communist']
ideology_relations['Anarcho-Communist']['Centrist'] = ideology_relations['Centrist']['Anarcho-Communist']
ideology_relations['Anarcho-Communist']['Liberal'] = ideology_relations['Liberal']['Anarcho-Communist']
ideology_relations['Anarcho-Communist']['Nationalist'] = ideology_relations['Nationalist']['Anarcho-Communist']
ideology_relations['Anarcho-Communist']['Fascist'] = ideology_relations['Fascist']['Anarcho-Communist']
ideology_relations['Anarcho-Communist']['Socialist'] = ideology_relations['Socialist']['Anarcho-Communist']
ideology_relations['Anarcho-Communist']['Traditionalist'] = ideology_relations['Traditionalist']['Anarcho-Communist']
ideology_relations['Anarcho-Communist']['Conservative'] = ideology_relations['Conservative']['Anarcho-Communist']
ideology_relations['Anarcho-Communist']['Libertarian'] = ideology_relations['Libertarian']['Anarcho-Communist']
ideology_relations['Anarcho-Communist']['Communist'] = ideology_relations['Communist']['Anarcho-Communist']
ideology_relations['Anarcho-Communist']['Anarcho-Communist'] = 1.0
ideology_relations['Anarcho-Communist']['Anarcho-Capitalist'] = 0.1

ideology_relations['Anarcho-Capitalist']['Anarchist'] = ideology_relations['Anarchist']['Anarcho-Capitalist']
ideology_relations['Anarcho-Capitalist']['Centrist'] = ideology_relations['Centrist']['Anarcho-Capitalist']
ideology_relations['Anarcho-Capitalist']['Liberal'] = ideology_relations['Liberal']['Anarcho-Capitalist']
ideology_relations['Anarcho-Capitalist']['Nationalist'] = ideology_relations['Nationalist']['Anarcho-Capitalist']
ideology_relations['Anarcho-Capitalist']['Fascist'] = ideology_relations['Fascist']['Anarcho-Capitalist']
ideology_relations['Anarcho-Capitalist']['Socialist'] = ideology_relations['Socialist']['Anarcho-Capitalist']
ideology_relations['Anarcho-Capitalist']['Traditionalist'] = ideology_relations['Traditionalist']['Anarcho-Capitalist']
ideology_relations['Anarcho-Capitalist']['Conservative'] = ideology_relations['Conservative']['Anarcho-Capitalist']
ideology_relations['Anarcho-Capitalist']['Libertarian'] = ideology_relations['Libertarian']['Anarcho-Capitalist']
ideology_relations['Anarcho-Capitalist']['Communist'] = ideology_relations['Communist']['Anarcho-Capitalist']
ideology_relations['Anarcho-Capitalist']['Anarcho-Communist'] = ideology_relations['Anarcho-Communist']['Anarcho-Capitalist']
ideology_relations['Anarcho-Capitalist']['Anarcho-Capitalist'] = 1.0
