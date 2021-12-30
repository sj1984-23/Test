# Exercise Instructions

### Implementation Details

#### Files
- The script is located on the 'dev' branch at: 'release_tools/code_freeze.py'
  It does three things:
    - Creates a 'branch' of the 'current' release with the format: 'rel_name'/'rel_number' based
      on the 'user' input.
    - Calculates 'diff' between the 'current' and 'previous' release and outputs as 'diff_curr_prev.txt' format. This is helpful when we look back at other releases in future.
    - Updates the 'release.plist' with the 'next' release information.

#### Assumptions
- The 'base' branch is assumed to be 'main'.
- By default, the 'script' is on the 'dev' branch.

#### Environment
- The script is written using Python 2.7. Some functions may not work with Python 3.0 or higher.

#### Setup
The script is interactive. It asks the user for the 'current' release details:
- Enter the 'current' release name
- Enter the 'current' release number
- A 'branch' is created for the same using the format, 'rel_name'/'rel_number'
