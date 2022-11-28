#twinkel
f=open('poem.txt')
t=f.read()
if 'twinkel' in t:
    print('twinkel is present')
else:
    print("twinkel is not present")    
f.close()



###################################
def game():
    return 190


score=game()
with open("highscore.txt") as f:
    highscore=int(f.read()) 
if highscore <score:
    with open("highscore.txt",'w') as f:
        f.write(str(score))       



        