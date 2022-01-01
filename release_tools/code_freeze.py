###################################
# author: Swapna Jandhyala

#This script will do a code freeze by:
# Create a 'branch' for the 'current' release that the user enters
# Generate feature flag report between 'current' and 'previous' branch
# Update the 'plist' file to next version

###################################
import os
import plistlib
import csv

def create_branch(rel_branch,curr_release_branch,prev_release_branch):
    #os.system("git branch | grep %s" % (rel_branch))

    os.system('git branch | grep %s' % ( rel_branch ) + ">temp.txt")
    file=open("temp.txt", "r")

    for line in file:
        if rel_branch in line:
           print("%s is an existing branch" % rel_branch)
           quit()
    os.system("git remote -v")
    os.system("git rm temp.txt")
    os.system("git checkout main")
    os.system("git checkout -b %s" % (rel_branch))
    os.system("cp ../featureflags/FF.csv diff.txt")
    os.system("git diff %s:featureflags/FF.csv %s:featureflags/FF.csv > diff.txt" % (curr_release_branch,prev_release_branch))
    os.system("git add *")
    os.system("git commit -m 'Creating new branch for 'CodeFreeze''")
    os.system("git push https://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@github.com/sj1984-23/Test.git")
    print("Created a new branch for %s" %(rel_branch))

def main():

   array1 = []
   rel_names = []
   rel_ver = []

 # Create a branch with current release for code freeze
   rel_name=raw_input("Enter the release name \n")
   rel_number=raw_input("Enter the release number \n")


   # Find the previous release
   # Search for this release in 'release.csv', one entry
   # before is the previous release
   with open('../releng/release_info.csv', 'r') as file:
    reader = csv.reader(file)

    for row in reader:
        items = (row[0] + "/" + row[1])
        rel_names.append(row[0])
        rel_ver.append(row[1])
        array1.append(items)

    rel_branch=rel_name + "/" +rel_number
    curr_releaseName_index=rel_names.index(rel_name)
    curr_version_index=rel_ver.index(rel_number)
    curr_release_branch=rel_name + "/" + rel_number
    print("Current release branch is")
    print(curr_release_branch)
    curr_release_index=array1.index(curr_release_branch)
    #curr_release_branch=array1[curr_release_index]

    prev_release_index=curr_release_index-1
    prev_release_branch=array1[prev_release_index]
    print("Previous release is ")
    print(array1[prev_release_index])

    create_branch(rel_branch,curr_release_branch,prev_release_branch)
    # Print diff of FF.csv in 'diff.txt'


    next_release_index=curr_releaseName_index+1
    next_version_index=curr_version_index+1
    next_release_branch=rel_names[next_release_index] + "/" + rel_ver[next_release_index]
    print("Next release is ")
    print(next_release_branch)

    # Increment the release version in release.plist
    fileName=os.path.expanduser('../release.plist')
    if os.path.exists(fileName):
       pl=plistlib.readPlist(fileName)

       # Update with next release name and version
       pl['SLKReleaseName']=rel_names[next_release_index]
       plistlib.writePlist(pl, fileName)
       pl['CFBundleShortVersionString']=rel_ver[next_release_index]
       plistlib.writePlist(pl, fileName)
       if 'SLKReleaseName' and 'CFBundleShortVersionString' in pl:
          print 'Next release name is %s\n' % pl['SLKReleaseName']
          print 'Next release version is %s\n' % pl['CFBundleShortVersionString']
       else:
          print 'There is no release name in the plist\n'
    else:
       print '%s does not exist, so can\'t be read' % fileName

if __name__ == '__main__':
   main()
