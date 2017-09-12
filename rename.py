import os
def renamefile():
    #find names of all the files
    filelist=os.listdir('/Users/liwei/Downloads')
    savepath=os.getcwd()
    #print (filelist)
    print (savepath)
    os.chdir('/Users/liwei/Desktop')
    print (os.getcwd())
    #rename names of all the files
    #for filename in filelist#
        #os.rename(filename,filename.translate(None,'1234567890'))
    #os.chdir(savepath)
    #print (os.getcwd())
renamefile()

