import sys
print ('Enter your old password')
oldPassword = raw_input()
entries = 0
theEnd = False

print ('Enter your newpassword')
newPassword = raw_input ()
entries += 1

while newPassword == oldPassword and theEnd == False:
        if entries < 3:
            print ('Your new password cannot be the same as your old password.')
            print ('Please choose a new password. Entries: ')+ str(entries)
            newPassword = raw_input()
            entries += 1
        elif entries == 3:
            print ('You have one more chance. Please choose a new password. Entries: ') + str (entries)
            newPassword = raw_input ()
            entries += 1
        elif entries == 4:
            print ('You have exceeded the number of entries.')
            theEnd = True
            break
       
        

if theEnd == True :
        print ('Your password is still ') + oldPassword + ('.')
        print ('TheEnd value: ') + str (theEnd)
        
        
elif newPassword != oldPassword:
    print ('Your new password is:') + newPassword


    

print ('Done')

