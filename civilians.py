
import random,math,string
#import matplotlib.pyplot as plt

class person():
    def __init__(self):
        global surnames
        global girlnames
        global boynames
        self.surname=random.choice(surnames)
        sex=random.getrandbits(1)
        if sex==0:
            self.forename=random.choice(boynames)
            self.sex='male'
        else:
            self.forename=random.choice(girlnames)
            self.sex='female'
        self.name=[self.surname,self.forename]
        self.age=random.choice(range(14,91))
        self.intelligence = float(random.getrandbits(8))/256
        self.willpower= float(random.getrandbits(8))/256
        self.awareness= float(random.getrandbits(8))/256
        self.radicalism= float(random.getrandbits(8))/256
        self.violence= float(random.getrandbits(8))/256
        self.faith= float(random.getrandbits(8))/256
        self.leftright= float(random.getrandbits(8))/256 # Economic left vs Economic right
        self.updown = float(random.getrandbits(8))/256 # Authoritarian vs Libertarian
        self.ideology = classify_ideology(self.leftright,self.updown)

def classify_ideology(leftright,autho):
    lr = int(round(leftright * 20))
    au = int(round(autho * 20))
    if lr in range(0,6) and au in range(14,21):
        ideology = 'Communist'
    elif lr in range(0,4) and au in range(4,11):
        ideology = 'Anarcho-Communist'
    elif lr in range(0,11) and au in range(0,4):
        ideology = 'Anarchist'
    elif lr in range(10,21) and au in range(0,4):
        ideology = 'Anarcho-Capitalist'
    elif lr in range(9,13) and au in range(9,13):
        ideology = 'Centrist'
    elif lr in range(10,21) and au in range(4,9):
        ideology = 'Libertarian'
    elif lr in range(9,16) and au in range(13,18):
        ideology = 'Nationalist'
    elif lr in range(6,18) and au in range(18,21):
        ideology = 'Fascist'
    elif (lr in range(0,6) and au in range(10,14)) or (lr in range(6,9) and au in range(10,18)):
        ideology = 'Socialist'
    elif (lr in range(3,9) and au in range(4,11)) or (lr in range(9,11) and au in range(4,9)):
        ideology = 'Liberal'
    elif (lr in range(13,16) and au in range(9,13)) or (lr in range(16,21) and au in range(9,15)):
        ideology = 'Conservative'
    elif (lr in range(16,19) and au in range(14,18)) or (lr in range(18,21) and au in range(14,21)):
        ideology = 'Traditionalist'
    else:
        raise Exception('UNDEFINED IDEOLOGY '+str(lr)+' '+str(au))
    return ideology

def opinion(guy):
    global govt_leftright
    global govt_updown
    global govt_violence
    gi = classify_ideology(govt_leftright,govt_updown)
    ii = classify_ideology(guy.leftright,guy.updown)
    modifier = ideology_relations[gi][ii]
    opin_leftright = ((1- abs(guy.leftright - govt_leftright) )*100)*modifier
    opin_updown = ((1- abs(guy.updown - govt_updown) )*100)*modifier
    genopinion= (opin_leftright+opin_updown)/2
    return [opin_leftright,opin_updown,genopinion]


#########################################
surnames=['Wilson','Roussin','Tremblay','Gagnon','Cote','Gagne','Ouellet','Levesque','Boucher','Pelletier','Caron','Paquette','Leblanc','Belanger','Morin','Gauthier','Morin','Perron']
girlnames=['Anais','Sabrina','Emily','Arielle','Elizabeth','Ariane','Lea','Florence','Chloe','Jade','Victoria','Stephanie','Isabelle','Emilie','Megan','Sophie','Blanche','Jennifer','Rose','Veronique']
boynames=['Jean','Edouard','Henri','Alexis','William','Antoine','Nicholas','Etienne','Tristan','Leo','Dylan','Louis','Raphael','Xavier','Mathieu','Maxime','Renaud','Jean-Francois','Frederic','Alexandre']
ideologies=['Socialist', 'Conservative', 'Anarchist', 'Communist', 'Centrist', 'Liberal', 'Nationalist', 'Fascist', 'Traditionalist', 'Libertarian', 'Anarcho-Communist', 'Anarcho-Capitalist']
ideology_relations = {'Socialist': {'Socialist': 1.0, 'Conservative': 0.2, 'Communist': 0.8, 'Anarchist': 0.5, 'Centrist': 0.5, 'Liberal': 0.75, 'Nationalist': 0.5, 'Fascist': 0, 'Traditionalist': 0.1, 'Libertarian': 0.2, 'Anarcho-Communist': 0.8, 'Anarcho-Capitalist': 0.1}, 'Conservative': {'Socialist': 0.2, 'Conservative': 1.0, 'Communist': 0.1, 'Anarchist': 0.1, 'Centrist': 0.75, 'Liberal': 0.25, 'Nationalist': 0.5, 'Fascist': 0.2, 'Traditionalist': 0.6, 'Libertarian': 0.8, 'Anarcho-Communist': 0.1, 'Anarcho-Capitalist': 0.6}, 'Communist': {'Socialist': 0.8, 'Conservative': 0.1, 'Communist': 1.0, 'Anarchist': 0.5, 'Centrist': 0.1, 'Liberal': 0.5, 'Nationalist': 0.1, 'Fascist': 0, 'Traditionalist': 0, 'Libertarian': 0.1, 'Anarcho-Communist': 0.8, 'Anarcho-Capitalist': 0.1}, 'Anarchist': {'Socialist': 0.5, 'Conservative': 0.1, 'Communist': 0.5, 'Anarchist': 1.0, 'Centrist': 0.25, 'Liberal': 0.3, 'Nationalist': 0.1, 'Fascist': 0, 'Traditionalist': 0, 'Libertarian': 0.2, 'Anarcho-Communist': 0.75, 'Anarcho-Capitalist': 0.5}, 'Centrist': {'Socialist': 0.5, 'Conservative': 0.75, 'Communist': 0.1, 'Anarchist': 0.25, 'Centrist': 1.0, 'Liberal': 0.75, 'Nationalist': 0.25, 'Fascist': 0.1, 'Traditionalist': 0.1, 'Libertarian': 0.5, 'Anarcho-Communist': 0.1, 'Anarcho-Capitalist': 0.1}, 'Liberal': {'Socialist': 0.75, 'Conservative': 0.25, 'Communist': 0.5, 'Anarchist': 0.3, 'Centrist': 0.75, 'Liberal': 1.0, 'Nationalist': 0.1, 'Fascist': 0, 'Traditionalist': 0.1, 'Libertarian': 0.5, 'Anarcho-Communist': 0.5, 'Anarcho-Capitalist': 0.2}, 'Nationalist': {'Socialist': 0.5, 'Conservative': 0.5, 'Communist': 0.1, 'Anarchist': 0.1, 'Centrist': 0.25, 'Liberal': 0.1, 'Nationalist': 1.0, 'Fascist': 0.8, 'Traditionalist': 0.75, 'Libertarian': 0.4, 'Anarcho-Communist': 0.1, 'Anarcho-Capitalist': 0.3}, 'Fascist': {'Socialist': 0, 'Conservative': 0.2, 'Communist': 0, 'Anarchist': 0, 'Centrist': 0.1, 'Liberal': 0, 'Nationalist': 0.8, 'Fascist': 1.0, 'Traditionalist': 0.8, 'Libertarian': 0.3, 'Anarcho-Communist': 0, 'Anarcho-Capitalist': 0.1}, 'Traditionalist': {'Socialist': 0.1, 'Conservative': 0.6, 'Communist': 0, 'Anarchist': 0, 'Centrist': 0.1, 'Liberal': 0.1, 'Nationalist': 0.75, 'Fascist': 0.8, 'Traditionalist': 1.0, 'Libertarian': 0.4, 'Anarcho-Communist': 0, 'Anarcho-Capitalist': 0.2}, 'Libertarian': {'Socialist': 0.2, 'Conservative': 0.8, 'Communist': 0.1, 'Anarchist': 0.2, 'Centrist': 0.5, 'Liberal': 0.5, 'Nationalist': 0.4, 'Fascist': 0.3, 'Traditionalist': 0.4, 'Libertarian': 1.0, 'Anarcho-Communist': 0.1, 'Anarcho-Capitalist': 0.8}, 'Anarcho-Communist': {'Socialist': 0.8, 'Conservative': 0.1, 'Communist': 0.8, 'Anarchist': 0.75, 'Centrist': 0.1, 'Liberal': 0.5, 'Nationalist': 0.1, 'Fascist': 0, 'Traditionalist': 0, 'Libertarian': 0.1, 'Anarcho-Communist': 1.0, 'Anarcho-Capitalist': 0.1}, 'Anarcho-Capitalist': {'Socialist': 0.1, 'Conservative': 0.6, 'Communist': 0.1, 'Anarchist': 0.5, 'Centrist': 0.1, 'Liberal': 0.2, 'Nationalist': 0.3, 'Fascist': 0.1, 'Traditionalist': 0.2, 'Libertarian': 0.8, 'Anarcho-Communist': 0.1, 'Anarcho-Capitalist': 1.0}}

popul=[]
poplog=[]
for i in range(1000):
    popul.append(person())
npop=len(popul)
n=0
txt=''

govt_leftright = float(0.6)
govt_updown = float(0.4)
govt_radicalism = float(0.25)

avg_leftright=0
avg_radicalism=0
avg_violence=0
for i in popul:
    avg_leftright += i.leftright
    avg_radicalism += i.radicalism
    avg_violence += i.violence
    
avg_leftright=avg_leftright/npop
avg_radicalism=avg_radicalism/npop
avg_violence=avg_violence/npop
appr=[]

parties={}
for i in ideologies:
    parties[i]=0

for i in popul:
    opn=opinion(i)
    print ''
    print i.name[1],i.name[0]
    #print 'Age',i['age']
    #print 'Awareness',round(i['aware'],3)
    #print 'Left/Right:',round(i['leftright'],3)
    #print 'Autho/Libert:',round(i['updown'],3)
    print 'Ideology:',i.ideology
    #print 'Radicalism:',round(i['radicalism'],3)
    #print 'Violence:',round(i['violence'],3)
    print 'Approval economics:',round(opn[0],3),'%'
    print 'Approval liberty:',round(opn[1],3),'%'
    print 'Approval rating:',round(opn[2],3),'%'
    appr.append(opn[2])
    parties[i.ideology]+=1

print ''
print 'Average Politics:',avg_leftright
print 'Average Radicalism:',avg_radicalism
print 'Average Violence:',avg_violence
print 'Government Politics:',govt_leftright
print 'Government Radicalism:',govt_radicalism
print 'Government Authoritarianism:',govt_updown
print 'Government Ideology:',classify_ideology(govt_leftright,govt_updown)
print 'Approval rating',(sum(appr)/len(appr)),'%'
print ''
print 'Political Parties'
for i in parties:
    print i,':',parties[i]
