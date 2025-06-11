#!/usr/bin/python
# =======================
# pyShadow - Example Usage
# =======================

from src.reshadow import ReShadowCode, TerminalColor

TerminalColor.__init__()

def list_shadowcopies():
    shadows = ReShadowCode.VSS_ListShadows()
    for shadow in shadows:
        print(f"ID: {shadow['id'].strip('{}')}\nCreated: {shadow['creation_time']}\nLocation: {shadow['shadowcopy']}\n{'='*60}")
    return shadows

def rescue_file():
    shadows = list_shadowcopies()
    shadow_id = input("Enter ShadowCopy ID to recover from: ").strip()
    if not shadow_id:
        print("❌ ERROR: ShadowCopy ID is required.")
        return

    src_path = input("Enter relative path to the file inside the ShadowCopy: ").strip()
    dst_path = input("Enter full destination path to save the recovered file: ").strip()
    drive_letter = input("Enter drive letter (e.g., C, D): ").strip().upper()

    mount_path = f"{drive_letter}:\\{shadow_id}"
    shadow = next((s for s in shadows if shadow_id in s["id"]), None)

    if not shadow:
        print("❌ ERROR: No matching ShadowCopy found.")
        return

    try:
        print(f"🔄 Mounting {shadow_id}...")
        ReShadowCode.VSS_Create_PipeForeach(mount_path, shadow["shadowcopy"])
        ReShadowCode.VSS_CopyFile(f"{mount_path}\\{src_path}", dst_path)
        print("✅ File recovered successfully.")
    except Exception as e:
        print(f"❌ Recovery failed: {e}")
    finally:
        ReShadowCode.VSS_RemoveSymlink(mount_path)

def create_pipes():
    drive = input("Enter drive letter (e.g., C, D): ").strip().upper()
    shadows = ReShadowCode.VSS_ListShadows()
    for shadow in shadows:
        mount_path = f"{drive}:\\{shadow['id'].strip('{}')}"
        print(f"🔗 Creating pipe at {mount_path}")
        ReShadowCode.VSS_Create_PipeForeach(mount_path, shadow["shadowcopy"])

def create_vss():
    try:
        ReShadowCode.VSS_Create()
        print("✅ New ShadowCopy created.")
    except Exception as e:
        print(f"❌ Failed to create VSS: {e}")

def main():
    menu = """
=============================================================
 pyShadow - The ShadowCopy Extractor / File Rescue Tool
 Version 1.0.0 | (c) 2024, Reshadow
=============================================================
 1. Rescue File from ShadowCopy
 2. Create Pipe / Symlink for ShadowCopy
 3. List ShadowCopies
 4. Create VSS Snapshot
 5. Exit
=============================================================
"""
    while True:
        print(menu)
        try:
            choice = int(input("Select an option (1-5): ").strip())
            if choice == 1:
                rescue_file()
            elif choice == 2:
                create_pipes()
            elif choice == 3:
                list_shadowcopies()
            elif choice == 4:
                create_vss()
            elif choice == 5:
                print("👋 Exiting.")
                break
            else:
                print("❗ Invalid option. Please select 1-5.")
        except ValueError:
            print("❗ Please enter a number.")

if __name__ == "__main__":
    main()
