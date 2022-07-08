import os

def get_adapters():
    adaps = os.popen('netsh interface show interface').read()
    adaps = adaps.split('\n', 3)[3] #Remove first 3 lines
    adaps = adaps.split('\n') #Converts to a list
    adaps = list(filter(lambda x: 'Connected' in x, adaps))
    adaps = [e[47:] for e in adaps] #Remove first 47 character for each element in the list
    return adaps

def enable_internet(str):
    os.system('netsh interface set interface "' + str + '" admin=enabled')

def disable_internet(str):
    os.system('netsh interface set interface "' + str + '" admin=disabled')
