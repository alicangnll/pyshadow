
# =======================
# pyShadow - Example Codes
# =======================

from src.reshadow import ReShadowCode, TerminalColor

# Global variables
TerminalColor.__init__()
shadowcopy_list = ReShadowCode.VSS_ListShadows()

def rescue_file(disk):
    try:
        for shadowlist in shadowcopy_list:
            print(ReShadowCode.VSS_Create_PipeForeach(disk + ":\\" + shadowlist["id"], shadowlist["shadowcopy"]))
            # Rescue file from ShadowCopy
            rescue_file = input(TerminalColor.OK + "Directory of the file to be recovered : ")
            dest = input("The directory to which the recovered files will be copied : ")
            ReShadowCode.VSS_CopyFile(rescue_file, dest, shadowlist["id"])
            print("File recovered successfully")
    except Exception as e:
        print(f"Error: {e}")

def create_pipe(disk):
    try:
        for shadowlist in shadowcopy_list:
            print("ID : " + shadowlist["id"] + "\nCreation Date : " + shadowlist["creation_time"] + "\nShadow Copy Location : " + shadowlist["shadowcopy"] + "\n")
            ReShadowCode.VSS_Create_PipeForeach(disk + ":\\" + shadowlist["id"].replace("{", "").replace("}", ""), shadowlist["shadowcopy"])
    except Exception as e:
        print(f"Error: {e}")

def list_shadowcopy():
    try:
        for shadowlist in shadowcopy_list:
            print("ID : " + shadowlist["id"] + "\nCreation Date : " + shadowlist["creation_time"] + "\nShadow Copy Location : " + shadowlist["shadowcopy"] + "\n")
    except Exception as e:
        print(f"Error: {e}")

def create_vss():
    try:
        ReShadowCode.VSS_Create()
    except Exception as e:
        print(f"Error: {e}")

def main():
    print("=============================================================")
    print(" pyShadow - The ShadowCopy Extractor / File Rescue Tool\n Version 1.0.0\n Copyright (c) 2022, Reshadow")
    print("=============================================================")
    print("1. Rescue File from ShadowCopy")
    print("2. Create Pipe / Symlink for ShadowCopy")
    print("3. List ShadowCopy")
    print("4. Create VSS")
    print("5. Exit")
    choice = int(input("Enter your choice : "))
    if choice == 1:
        disk = input("Write Windows Disk Drive (Example : C, D, E) : ")
        if len(disk) >= 2:
            return main()
        else:
            rescue_file(disk.upper())
    elif choice == 2:
        disk = input("Write Windows Disk Drive (Example : C, D, E) : ")
        if len(disk) >= 2:
            return main()
        else:
            create_pipe(disk.upper())
    elif choice == 3:
        list_shadowcopy()
    elif choice == 4:
        create_vss()
    elif choice == 5:
        exit()
    else:
        return main()
    
if __name__ == '__main__':
    main()