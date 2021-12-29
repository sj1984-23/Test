# This script will do a code freeze by:
# Create a 'branch' for the 'current' release that the user enters
# Generate feature flag report between 'current' and 'previous' branch
# Update the 'plist' file to next version

import os
import plistlib
import csv

def create_branch(rel_name,rel_number):
    os.system("git checkout main")
    os.system("git checkout -b %s/%s" % (rel_name,rel_number))
    os.system("git add *")
    os.system("git commit -m 'Creating new branch'")
    os.system("git remote remove origin")
    os.system("git remote add origin https://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@github.com/sj1984-23/Test.git")
    os.system("git push --set-upstream %s/%s" % (rel_name,rel_number))
    print("Created a new branch for %s/%s" %(rel_name,rel_number))

def main():

   array1 = []

 # Create a branch with current release for code freeze
   rel_name=raw_input("Enter the release name \n")
   rel_number=raw_input("Enter the release number \n")
   create_branch(rel_name,rel_number)

   # Find the previous release
   # Search for this release in 'release.csv', one entry
   # before is the previous release
   with open('../releng/release_info.csv', 'r') as file:
    reader = csv.reader(file)

    for row in reader:
        items = (row[0] + "/" + row[1])
        array1.append(items)

    curr_release_branch=rel_name + "/" + rel_number
    print("Current release branch is")
    print(curr_release_branch)
    curr_release_index=array1.index(curr_release_branch)
    #curr_release_branch=array1[curr_release_index]

    prev_release_index=curr_release_index-1
    prev_release_branch=array1[prev_release_index]
    print("Previous release is ")
    print(array1[prev_release_index])

    # Print diff of FF.csv in 'diff.txt'
    os.system("git diff %s:../featureflags/FF.csv %s:../featureflags/FF.csv > diff.txt" % (curr_release_branch,prev_release_branch))

    # Increment the release version in release.plist
    fileName=os.path.expanduser('../release.plist')
    if os.path.exists(fileName):
       pl=plistlib.readPlist(fileName)

       # Update with new release name and version
       pl['SLKReleaseName']=rel_name
       plistlib.writePlist(pl, fileName)
       pl['CFBundleShortVersionString']=rel_number
       plistlib.writePlist(pl, fileName)
       if 'SLKReleaseName' and 'CFBundleShortVersionString' in pl:
          print 'New release name is %s\n' % pl['SLKReleaseName']
          print 'New release version is %s\n' % pl['CFBundleShortVersionString']
          print '\n The plist full contents is %s\n' % pl
       else:
          print 'There is no release name in the plist\n'
    else:
       print '%s does not exist, so can\'t be read' % fileName

if __name__ == '__main__':
   main()
