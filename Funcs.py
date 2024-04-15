
def sentencegenerator(md):
    if md=='Sad':
        snt="Oh! So sorry to hear that!"
    if(md=='Happy'):
        snt="Oh! I would like to hear more!"
    if(md=='Mad'):
        snt='Oh! Do you want to talk about it ?'
    if md=='Confusing':
        snt='Oh dear!what makes you feel that way?'
    return snt

