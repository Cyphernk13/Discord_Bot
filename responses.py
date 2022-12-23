import random
import math
def get_response(message: str)-> str:
    p_message= message.lower()
    p_message= p_message.split()
    s=list(p_message)
    ##### CALCULATOR ######
    for i in s:
        if i=="add":
            return str(float(s[1])+float(s[2]))
        if i=="sub":
            return str(float(s[1])-float(s[2]))
        if i=="mul":
            return str(float(s[1])*float(s[2]))
        if i=="div":
          if float(s[2])==0:
            return "hmm this is difficult to solve 🤔"
          else:
            return str(float(s[1])/float(s[2]))
        if i=="rando":
            return str(random.randint(int(s[1]),int(s[2])))
        if i=="sqrt":
          return str(math.sqrt(float(s[1])))
        if i=="log":
          return str(math.log(int(s[1]),int(s[2])))
        if i=="fact":
          return str(math.factorial(int(s[1])))
        if i=="gcd":
          return str(math.gcd(int(s[1]),int(s[2])))
        if i=="pow":
          return str(math.pow(float(s[1]),float(s[2])))
        if i=="sin":
          return str(math.sin(float(s[1])))
        if i=="cos":
          return str(math.cos(float(s[1])))
        if i=="tan":
          return str(math.tan(float(s[1])))

        
          
        
      ##### MESSAGES REACTIONS #####
        if i=="hello":
          return "Hey there!"
        if i=="rolls":
          return str(random.randint(1,6))
        if i=="!help":
          return "Aw shoot the help section is still in making :("
        if i=="cat":
          return "catto here is milkkk 🥛!!"
        if i=="cake":
          return "Cakey's a cool girl <:reicool:1008116823591505940>"
        if i=="dio":
          return "Where is the horny spray >.<"
        if i=="senn":
          return "<:senn:901151065859313674>"
        if i=="alex":
          return "I want to stretch his cheeks >//<"
        if i=="larad":
          return "Children's lover <:GawrGuraO_O:1029145789936713868>"
        if i=="toki":
          return "he is cute >.<"
        if i=="rikka":
          return "I miss her :("
        if i=="akela":
          return "Uncle with a candy and van!!!"
        if i=="imp":
          return "Sussy baka!!! >\<"
        if i=="aillz":
          return "Please don't delete me aillz-sama 😭"
        if i=="madara":
          return "The man, the myth, the legend!!!"
        if i=="yankee":
          return "His hands >///<"
        if i=="sakura":
          return "ayooo the eren simp!!!"
        if i=="leyla":
          return "Ok I pull-up"
        if i=="akio":
          return "yayy that's me!!"
        if i=="mi":
          return "._."
        if i=="moup":
          return "rawwwrr!!"
        if i=="potato":
          return "wait asian one or russian one? "
        if i=="kajka":
          return "senpaiii 🍵"
        if i=="groot":
          return "itachi fan <:goodjob:982077930521886761>"
        if i=="pat":
          return "pat me too <:IrizchuPat:1029146890580803635> "
        if i=="gay":
          return "do you mean larad? <:gura_think:863439463091142706> "
        if i=="baseball":
          return "Woah! That's a baseball <:Noela_woah:1029145477398151190> "
        if i=="riz":
          return "hehe his voice is sooo cute <:RemShy:1029145732483121263>"
    return