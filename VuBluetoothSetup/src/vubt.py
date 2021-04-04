# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.2
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_vubt', [dirname(__file__)])
        except ImportError:
            import _vubt
            return _vubt
        if fp is not None:
            try:
                _mod = imp.load_module('_vubt', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _vubt = swig_import_helper()
    del swig_import_helper
else:
    import _vubt
del version_info
try:
    _swig_property = property
except NameError:
    pass # Python < 2.2 doesn't have 'property'.
def _swig_setattr_nondynamic(self, class_type, name, value, static=1):
    if (name == "thisown"):
        return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name, None)
    if method:
        return method(self, value)
    if (not static):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)

def _swig_setattr(self, class_type, name, value):
    return _swig_setattr_nondynamic(self, class_type, name, value, 0)

def _swig_getattr(self, class_type, name):
    if (name == "thisown"):
        return self.this.own()
    method = class_type.__swig_getmethods__.get(name, None)
    if method:
        return method(self)
    raise AttributeError(name)

def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object:
        pass
    _newclass = 0


class Vu_PyBluetooth(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Vu_PyBluetooth, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Vu_PyBluetooth, name)
    __repr__ = _swig_repr
    def __init__(self): 
        this = _vubt.new_Vu_PyBluetooth()
        try:
            self.this.append(this)
        except:
            self.this = this
    __swig_destroy__ = _vubt.delete_Vu_PyBluetooth
    __del__ = lambda self: None
    def enable(self): return _vubt.Vu_PyBluetooth_enable(self)
    def disable(self): return _vubt.Vu_PyBluetooth_disable(self)
    def checkBTUSB(self): return _vubt.Vu_PyBluetooth_checkBTUSB(self)
    def getStatus(self): return _vubt.Vu_PyBluetooth_getStatus(self)
    def startScan(self, *args): return _vubt.Vu_PyBluetooth_startScan(self, *args)
    def StartScanTestMode(self): return _vubt.Vu_PyBluetooth_StartScanTestMode(self)
    def abortScan(self): return _vubt.Vu_PyBluetooth_abortScan(self)
    def resetScan(self): return _vubt.Vu_PyBluetooth_resetScan(self)
    def addEventCallback(self, *args): return _vubt.Vu_PyBluetooth_addEventCallback(self, *args)
    def removeEventCallback(self): return _vubt.Vu_PyBluetooth_removeEventCallback(self)
    def addBleEventCallback(self, *args): return _vubt.Vu_PyBluetooth_addBleEventCallback(self, *args)
    def removeBleEventCallback(self): return _vubt.Vu_PyBluetooth_removeBleEventCallback(self)
    def getSystemInfo(self): return _vubt.Vu_PyBluetooth_getSystemInfo(self)
    def getDiscDevice(self): return _vubt.Vu_PyBluetooth_getDiscDevice(self)
    def getPairedDevice(self): return _vubt.Vu_PyBluetooth_getPairedDevice(self)
    def requestPairing(self, *args): return _vubt.Vu_PyBluetooth_requestPairing(self, *args)
    def cancelPairing(self, *args): return _vubt.Vu_PyBluetooth_cancelPairing(self, *args)
    def removePairing(self, *args): return _vubt.Vu_PyBluetooth_removePairing(self, *args)
    def requestConnect(self, *args): return _vubt.Vu_PyBluetooth_requestConnect(self, *args)
    def requestDisconnect(self, *args): return _vubt.Vu_PyBluetooth_requestDisconnect(self, *args)
    def requestBLEConnect(self, *args): return _vubt.Vu_PyBluetooth_requestBLEConnect(self, *args)
    def requestBLEDisconnect(self, *args): return _vubt.Vu_PyBluetooth_requestBLEDisconnect(self, *args)
    def setDisCoverable(self, *args): return _vubt.Vu_PyBluetooth_setDisCoverable(self, *args)
    def playAudioDevice(self): return _vubt.Vu_PyBluetooth_playAudioDevice(self)
    def stopAudioDevice(self): return _vubt.Vu_PyBluetooth_stopAudioDevice(self)
    def setScanTime(self, *args): return _vubt.Vu_PyBluetooth_setScanTime(self, *args)
    def setVolume(self, *args): return _vubt.Vu_PyBluetooth_setVolume(self, *args)
    def setVoiceCheckDB(self, *args): return _vubt.Vu_PyBluetooth_setVoiceCheckDB(self, *args)
    def isVoiceRecording(self): return _vubt.Vu_PyBluetooth_isVoiceRecording(self)
    def cleanupBleClient(self): return _vubt.Vu_PyBluetooth_cleanupBleClient(self)
    def readBatteryLevel(self, *args): return _vubt.Vu_PyBluetooth_readBatteryLevel(self, *args)
    def updateBatteryLevel(self): return _vubt.Vu_PyBluetooth_updateBatteryLevel(self)
    def OTA_addEventCallback(self, *args): return _vubt.Vu_PyBluetooth_OTA_addEventCallback(self, *args)
    def OTA_removeEventCallback(self): return _vubt.Vu_PyBluetooth_OTA_removeEventCallback(self)
    def OTAInit(self): return _vubt.Vu_PyBluetooth_OTAInit(self)
    def OTADeInit(self): return _vubt.Vu_PyBluetooth_OTADeInit(self)
    def OTAStart(self): return _vubt.Vu_PyBluetooth_OTAStart(self)
    def OTAStop(self): return _vubt.Vu_PyBluetooth_OTAStop(self)
    def OTACheckFWVersion(self, *args): return _vubt.Vu_PyBluetooth_OTACheckFWVersion(self, *args)
Vu_PyBluetooth_swigregister = _vubt.Vu_PyBluetooth_swigregister
Vu_PyBluetooth_swigregister(Vu_PyBluetooth)

# This file is compatible with both classic and new-style classes.


