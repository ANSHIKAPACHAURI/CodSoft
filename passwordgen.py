import random
import string

passlist = []

lc = string.ascii_lowercase
nlclist = []  # lower character list
nlclist.extend(list(lc))
# print(nlclist)
random.shuffle(nlclist)

uc = string.ascii_uppercase
nuclist = []  # upper character list
nuclist.extend(list(uc))
# print(nuclist)
random.shuffle(nuclist)

no = string.digits
ndlist = [] # digits list
ndlist.extend(list(no))
# print(ndlist)
random.shuffle(ndlist)

p = string.punctuation
nslist = [] # symbols list
nslist.extend(list(p))
# print(nslist)
random.shuffle(nslist)


def ranpass():
    length = int(input("enter desired length of the password u want:"))
    if length != 0:
        ns = int(input("enter number of symbols u want:"))  # no. of symbols
        nlc = int(input("enter number of lowercase characters u want:"))  # no. of lower character
        nuc = int(input("enter number of uppercase characters u want:"))  # no. of upper characters
        nd = int(input("enter number of digits u want:"))  # no. of digits

        if (ns + nlc + nuc + nd) == length:
            p1 = "".join(nlclist[0:nlc])
            p2 = "".join(nuclist[0:nuc])
            p3 = "".join(ndlist[0:nd])
            p4 = "".join(nslist[0:ns])
            # print(p1)
            # print(p2)
            # print(p3)
            # print(p4)
            passlist.extend(list(p1))
            passlist.extend(list(p2))
            passlist.extend(list(p3))
            passlist.extend(list(p4))
            random.shuffle(passlist)
            password = "".join(passlist[0:length])
            print("Your Password is:", password)

        else:
            print("enter correct no. of choices....")
            ranpass()
    else:
        print("Length cannot be zero!!!")
        ranpass()


print("GENERATE A STRONG RANDOM PASSWORD WITH YOUR CHOICE!!!!!")
print("-------------------------------------------------------")
ranpass()
