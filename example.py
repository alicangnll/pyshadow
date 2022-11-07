import reshadow

for shadowlist in reshadow.ReShadowCode.VSS_ListShadows():
    print("ID : " + shadowlist["id"] + "\nCreation Date : " + shadowlist["creation_time"] + "\nShadow Copy Location : " + shadowlist["shadowcopy"] + "\n")
    print(reshadow.ReShadowCode.VSS_Create_PipeForeach("C:\\" + shadowlist["id"].replace("{", "").replace("}", ""), shadowlist["shadowcopy"]))