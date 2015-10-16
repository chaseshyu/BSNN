#  dynamic.py
#  
#
#  Created by Phoenix on 10/16/15.
#
from ctypes import cdll
from _ctypes import dlclose
import os, time, sys

def so_test():
    
    # load dynamic-link library.
    sotest = cdll.LoadLibrary("./so/sointerface.so")
    
    # execute the function in linked library
    print (sotest.sum(1,2))
    
    # before reload, need to delete the dynamic-link library.
    dlclose(sotest._handle)
    # in win32: _ctypes.FreeLibrary(sotest._handle)
    del sotest
    
    # update the library
    os.system('make test2')
    #    time.sleep(1)
    
    # reload the updated library.
    sotest = cdll.LoadLibrary("./so/sointerface.so")
    
    # execute the function in updated library
    print (sotest.sum(1,2))

from importlib import reload

def reload_test():
    
    # disable automic cache .pyc bytecode of the modules load below.
    # so that every reload can be updated immediately.
    sys.dont_write_bytecode = True
    
    # load library.
    import reloadtest
    
    # execute the function in linked library
    print (reloadtest.test123())
    
    # update the library
    os.system('cp reloadtest2.py reloadtest.py')
    
    # reload the updated library.
    reload(reloadtest)
    print (reloadtest.test123())
    
    
    os.system('cp reloadtest1.py reloadtest.py')
