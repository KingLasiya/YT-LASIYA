from pytube import YouTube
import os,time,sys
from time import sleep
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def down():
    os.system("clear")
    print("")
    print("")
    print("\t\033[36m██╗░░░░░░█████╗░░██████╗██╗██╗░░░██╗░█████╗░░░░░░░██╗░░░██╗████████╗\033[0m")
    print("\t\033[36m██║░░░░░██╔══██╗██╔════╝██║╚██╗░██╔╝██╔══██╗░░░░░░╚██╗░██╔╝╚══██╔══╝\033[0m")
    print("\t\033[36m██║░░░░░███████║╚█████╗░██║░╚████╔╝░███████║█████╗░╚████╔╝░░░░██║░░░\033[0m")
    print("\t\033[36m██║░░░░░██╔══██║░╚═══██╗██║░░╚██╔╝░░██╔══██║╚════╝░░╚██╔╝░░░░░██║░░░\033[0m")
    print("\t\033[36m███████╗██║░░██║██████╔╝██║░░░██║░░░██║░░██║░░░░░░░░░██║░░░░░░██║░░░\033[0m")
    print("\t\033[36m╚══════╝╚═╝░░╚═╝╚═════╝░╚═╝░░░╚═╝░░░╚═╝░░╚═╝░░░░░░░░░╚═╝░░░░░░╚═╝░░░\033[0m")
    print("\n\033[31m\033[01m\t\t   \033[04m+ TOOL BY KING LASIYA \033[0m ")
    print("\n\033[93m\t     \033[40m🔰 Coded By JLASIYA \033[49m\n")
    print("\n\033[93m\t     \033[40m👑 Owner of the KING LASIYA™ \033[49m\n")
    print("\n\033[93m\t     \033[40m📌 COMMUNITY BY LASIYA \033[49m\n")
    print("")

    link = str(input(bcolors.OKBLUE + "Enter your YouTube video link >> >> >> " + bcolors.OKGREEN))
    print()
    print(bcolors.WARNING + "Getting Data...!")
    print()
    yt = YouTube(link)
    vname = yt.title
    vdescrip = yt.description
    print("Success")
    print()
    print(bcolors.FAIL + "------------Video Title------------")
    print(bcolors.OKCYAN + vname)
    print()
    print(bcolors.FAIL + "------------Video Description------------")
    print(bcolors.OKCYAN + vdescrip)
    print()
    print(bcolors.FAIL + "[1] Hd Download      [2] Low Download      [3] Audio Download")
    print()
    chq = str(input(bcolors.OKBLUE + "Enter your choice >> >> >> " + bcolors.OKGREEN))
    print()
    if chq == '1':
       print("Downloading...!")
       print()
       yt.streams.get_highest_resolution().download('/sdcard/LASIYA-YT')
       print("Succces..! Check ")
       print(bcolors.ENDC)
    elif chq == '2':
       print("Downloading...!")
       print(bcolors.ENDC)
       yt.streams.get_lowest_resolution().download('/sdcard/LASIYA-YT')
       print("Succces..! Check ")
       print(bcolors.ENDC)
    elif chq == "3":
       print("Downloading...!")
       print(bcolors.ENDC)
       yt.streams.get_audio_only().download('/sdcard/LASIYA-YT')
       print("Succces..! Check ")
       print(bcolors.ENDC)
    else:
       print("Your input is not valid.. Restart programme" + bcolors.ENDC)
       print()

def lasiya():
    os.system("xdg-open https://youtube.com/channel/UCtW7Y0Ucqx6vjj3lcu87j5Q")



os.system("clear")
print('')
print("")
print("")
print("\t\033[36m██╗░░░░░░█████╗░░██████╗██╗██╗░░░██╗░█████╗░░░░░░░██╗░░░██╗████████╗\033[0m")
print("\t\033[36m██║░░░░░██╔══██╗██╔════╝██║╚██╗░██╔╝██╔══██╗░░░░░░╚██╗░██╔╝╚══██╔══╝\033[0m")
print("\t\033[36m██║░░░░░███████║╚█████╗░██║░╚████╔╝░███████║█████╗░╚████╔╝░░░░██║░░░\033[0m")
print("\t\033[36m██║░░░░░██╔══██║░╚═══██╗██║░░╚██╔╝░░██╔══██║╚════╝░░╚██╔╝░░░░░██║░░░\033[0m")
print("\t\033[36m███████╗██║░░██║██████╔╝██║░░░██║░░░██║░░██║░░░░░░░░░██║░░░░░░██║░░░\033[0m")
print("\t\033[36m╚══════╝╚═╝░░╚═╝╚═════╝░╚═╝░░░╚═╝░░░╚═╝░░╚═╝░░░░░░░░░╚═╝░░░░░░╚═╝░░░\033[0m")
print("\n\033[31m\033[01m\t\t   \033[04m+ TOOL BY KING LASIYA \033[0m ")
print("\n\033[93m\t     \033[40m🔰 Coded By JLASIYA \033[49m\n")
print("\n\033[93m\t     \033[40m👑 Owner of the KING LASIYA™ \033[49m\n")
print("\n\033[93m\t     \033[40m📌 COMMUNITY BY LASIYA \033[49m\n")
print("")
print('')
print('')
print('\n\t\t\t[1] Download video url\033[0m')
print('\n\t\t\t[2] Update Tool \033[0m')
print('\n\t\t\t[3] About\033[0m')
print('')
choices=int(input('Enter You number :'))
if choices == 1:
   down()
elif choices == 2:
   lasiya()
elif choices == 3:
   pass
   
else:
     print('[*] please Enter a valid number')
