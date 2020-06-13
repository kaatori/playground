print('\033[31m' + 'some red text')
print('\033[39m') # and reset to default color
print('some red text') #line 1 is turning it red, line 2 is resetting it

print("\n")

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m' #3m makes it look italic; 1m was original code
    UNDERLINE = '\033[4m'
    CHARTREUSE = '\033'


print(bcolors.WARNING + "Warning: No active frommets remain. Continue?" + bcolors.ENDC)
print(f"{bcolors.WARNING}Warning: No active frommets remain. Continue?{bcolors.ENDC}")

print(bcolors.UNDERLINE + "Underline")
print(bcolors.FAIL + "fail")
print(bcolors.CHARTREUSE + "chartreuse")
print(bcolors.OKBLUE + "okblue")
print(bcolors.BOLD + "bold")






