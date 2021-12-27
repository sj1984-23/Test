# This script will do a code freeze by:
# 1. Updating the 'pist' with the next release
# 2. Creating a 'git branch' of the new SLKReleaseName
# 3.

import os
import plistlib
import csv

def main():

   fileName=os.path.expanduser('release.plist')

   if os.path.exists(fileName):

      pl=plistlib.readPlist(fileName)

      print '\n The plist full contents is %s\n' % pl

     # Increment 'version' to the next release

      if 'SLKReleaseName' and 'CFBundleShortVersionString' in pl:
         print 'Current release name is %s\n' % pl['SLKReleaseName']
         print 'Current release version is %s\n' % pl['CFBundleShortVersionString']
      else:
         print 'There is no release name in the plist\n'

   else:
      print '%s does not exist, so can\'t be read' % fileName

   with open('releng/release_info.csv', 'r') as file:
       reader = csv.reader(file)
       for row in reader:
           if row[0] == "Cake":
              next_release = row[0]+1





if __name__ == '__main__':
   main()
