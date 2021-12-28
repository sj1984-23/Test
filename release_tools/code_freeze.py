# This script will do a code freeze by:
# Create a 'branch' for the 'current' release thats found in 'release.plist'
# Generate feature flag report with 'current' and 'previous'
# Generate 'FF' report which shows the diff between new and old release
# After 'branch' is created, change the 'verison' to next version in the plist file

import os
import plistlib
import csv

def main():

   os.system("git checkout main")
   #os.system("git status")
   #os.system("git remote -v")




if __name__ == '__main__':
   main()
