# Friend or Foe Codewards Challenge Solution

def friend(x):
    
    true_friends = []
    
    for name in x:
        if len(name) == 4:
            true_friends.append(name)
    
    return true_friends