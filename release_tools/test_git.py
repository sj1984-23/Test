import os

def main():

    rel_branch=raw_input("Enter the release \n")
    #os.system("git branch | grep  > temp.txt" )
    os.system('git branch | grep %s' % ( rel_branch ) + ">temp.txt")
    file=open("temp.txt", "r")

    for line in file:
        if rel_branch in line:
           print("%s is an existing branch" % rel_branch)
           quit()
    #if [ os.system("git branch | grep %s" % (rel_branch))]:
    #    print("Branch exists..This is an old release")
    #else:
    #    print("Branch doesnot exist..Createing a new Branch")
    #if [ os.system("git branch | grep %s" % (rel_branch)) == rel_branch ]:
     #  print("Branch exists..exiting")
    #print(branch)


    #if rel_name in (os.system("git branch")):
    #    print("Release branch is already created")
    #if [ ]:
     #  print("Branch exists")
     #  return -1
    #else:
    #  print("Branch exists %s" % rel_name)
    #grep_value=os.system("git branch | grep %s" % (rel_name))
    #print("Grep value is")
    #print(grep_value)
    #if(os.system("git branch | grep rel_name") == rel_name):
        #print("Branch already exists")
    #    quit()

if __name__ == '__main__':
   main()
