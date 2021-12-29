# Exercise Instructions

### Implementation Details

#### Files
- The script is located on the 'dev' branch at:
  -'release_tools/code_freeze.py'  
  -'diff.txt' gives the difference in the 'FF.csv' from previous branch to the current create_branch.

#### Assumptions
- The 'base' branch is assumed to be 'main'
- All the 'development' happens on the 'main'.
- When we do the 'code_freeze', a new branch is cut from the 'current' release and named after the branch name.

#### Setup
The script is interactive. It asks the user for the 'current' release details:
- Enter the 'current' release name
- Enter the 'current' release number
- A 'branch' is created for the same using the format, 'rel_name'/'rel_number'

### script
- The script is divided into '3' portions:
  1. A 'branch' is created using the credentials given by the user.
  2. It will calculate 'previous' release based on the 'release.csv' file and calculate the differences between the 'FF.csv'
  file in the previous release and current release, and create a file 'diff.txt'
  3. Update the 'release.plist' with the 'next' release thats listed in the 'release.csv'.
