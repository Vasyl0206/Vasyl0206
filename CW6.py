def areYouPlayingBanjo(name):
    # Implement me!
    if name[0] == 'R' or name[0] == 'r':
        return name + " plays banjo"
    return name + " does not play banjo"
print (areYouPlayingBanjo("Roman"))