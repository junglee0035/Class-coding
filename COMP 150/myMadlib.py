storyFormat = """                                       
The doorbell rings. You get up out of bed to see 
{person} at the door, holding a {single object}. 
{person} insists on going to {place} to go {action} 
with the {single object}. You and {person} head 
over to {place} but for some reason, a {animal} 
is chilling in the middle of traffic, watching {tv show}
on the new iPad pro. You and {person} beg the {animal} 
to get out of the way. The {animal} suggests that if {person} 
beats the {animal} in {game} then the {animal} will 
move. If {person} loses, then the world will end.
{person} wins with a landslide and the {animal} becomes 
impressed by {person}’s skills. The three of you go back 
to your place to chill, watch {tv show}, and eat {food}.

The End
"""

def tellStory():
    userPicks = dict()
    addPick('person', userPicks)
    addPick('single object', userPicks)
    addPick('place', userPicks)
    addPick('action', userPicks)
    addPick('food', userPicks)
    addPick('animal', userPicks)
    addPick('game', userPicks)
    addPick('tv show', userPicks)
    story = storyFormat.format(**userPicks)
    print(story)

def addPick(cue, dictionary):
    prompt = 'Pick a ' + cue + ': '
    response = input(prompt).strip()
    dictionary[cue] = response

tellStory()