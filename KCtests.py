def success(): return "Test at line number " + str(inspect.currentframe().f_back.f_back.f_lineno) + ' SUCCESS.'
def fail()   : return "Test at line number " + str(inspect.currentframe().f_back.f_back.f_lineno) + ' FAILED.'

def equals(a, b):
    if type(a) != type(b):
        print fail()
        print '^^^ Expected type was ' + str(type(b)) + ' but got type ' + str(type(a)) + ' instead. \n'
        return False

    if a == b    : print success()
    else : 
        print fail()
        print 'A: ' + str(a) + ' != \nB: ' + str(b) + '\n'

def assert_true(a): 
    if a == True : print success()
    else         : print fail()

def assert_false(a):
    if a == False: print success()
    else         : print fail()