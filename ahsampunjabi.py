#-------------------------------------#
#-----------AHSAM
import os, time, platform
os.system("cd $HOME/")
try:
    import requests
except ImportError:
    os.system("pip2 install requests")
    os.syatem("pip install requests")
try:
    import mechanize
except ImportError:
    os.system("pip2 install mechanize")
    os.syatem("pip install mechanize")
rana=platform.architecture()[0]
if rana=="64bit":
    import s64
    s64.login()
elif rana=="32bit":
    import s32
    s32.AHSAM#81FF00()
#-------------------------------------#
