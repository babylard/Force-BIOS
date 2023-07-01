import subprocess

answer = input("Would you like to force boot into BIOS Setup? (y/n): ")

if answer == 'y':
    subprocess.call("shutdown /r /fw /f /t 0")

else:
    print("You may now safely close this window.")
