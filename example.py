from reshadow import ReShadowCode

# Create a ShadowCopy
# ReShadowCode.VSS_Create()

# Create a pipe/symlink with ShadowCopy() (Ex. \\?\GLOBALROOT\Device\HarddiskVolumeShadowCopyid)
# ReShadowCode.VSS_Create_Pipe("C:\\Shadow1", "id")

# List all ShadowCopies
shadowcopy_list = ReShadowCode.VSS_ListShadows()

for shadowlist in shadowcopy_list:
    print("ID : " + shadowlist["id"] + "\nCreation Date : " + shadowlist["creation_time"] + "\nShadow Copy Location : " + shadowlist["shadowcopy"] + "\n")
    print(ReShadowCode.VSS_Create_PipeForeach("C:\\" + shadowlist["id"].replace("{", "").replace("}", ""), shadowlist["shadowcopy"]))