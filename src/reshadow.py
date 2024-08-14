#!/usr/bin/python
import os, shutil
import win32com.client as client
import win32com.shell.shell as shell
from ctypes import windll
from subprocess import call, Popen, PIPE, check_call

class TerminalColor():
    def __init__():
        os.system("cls")
        os.system("color a")

class ReShadowCode():
    def run_as_admin():
        try:
            ret = os.getuid() == 0
        except AttributeError:
            ret = windll.shell32.IsUserAnAdmin() != 0
        return ret

    def VSSParser(vssadmin_out):
        ret = []
        current = None
        for line in vssadmin_out.splitlines():
            if line == "":
                if current:
                    ret.append(current)
                    current = None
                continue
            if line.startswith("Contents of shadow copy set ID:"):
                current = {}
                id = line.split(":")[1][1:]
                current['id'] = id
                continue
            if not current:
                continue
            line = line.strip()
            colon = line.find(':')
            if colon >= 0:
                name = line[0:colon]
                value = line[colon+2:]
                if name.endswith("creation time"):
                    name = "creation_time"
                    current[name] = value
                    continue
                if line.startswith("Shadow Copy Volume:"):
                    shadowcopy = line.split(":")[1][1:]
                    current['shadowcopy'] = shadowcopy
        return ret

    def VSS_ListShadows():
        if(ReShadowCode.run_as_admin()):
            list_output = Popen(["vssadmin", "list", "shadows"], stdout=PIPE).communicate()[0]
            list_output = list_output.decode("utf-8")
            return ReShadowCode.VSSParser(list_output)
        else:
            raise PermissionError("You dont have permission!")

    def DiskPart_Command(exec):
        try:
            p = Popen(["diskpart"], stdin=PIPE, stdout=PIPE)
            p.stdin.write(b'' + exec + '\n')
            p.stdin.close()
            return p.communicate()[0].decode("utf-8").splitlines()
        except Exception as e:
            return str(e)

    def VSS_Create():
        try:
            wmi = client.GetObject("winmgmts:\\\\.\\root\\cimv2:Win32_ShadowCopy")
            createmethod = wmi.Methods_("Create")
            createparams = createmethod.InParameters
            createparams.Properties_[1].value="c:\\"
            results = wmi.ExecMethod_("Create", createparams)
            return results.Properties_[1].value
        except Exception as e:
            return str(e)

    def VSS_Create_Pipe(location, id_and_directory):
        if(ReShadowCode.run_as_admin()):
            try:
                if os.path.isfile(str(location)) or os.path.isdir(str(location)):
                    os.remove(str(location))
                call(['mklink', '/D', '/J', str(location), "\\\?\\\GLOBALROOT\\\Device\\\HarddiskVolumeShadowCopy" + id_and_directory], shell=True)
            except:
                raise Exception("An error occured!")
        else:
            raise PermissionError("You dont have permission!")

    def VSS_Create_PipeForeach(location, id_and_directory):
        if(ReShadowCode.run_as_admin()):
            try:
                if os.path.isfile(str(location)) or os.path.isdir(str(location)):
                    os.remove(str(location))
                call(['mklink', '/D', '/J', str(location), str(id_and_directory).replace("{", "").replace("}", "")], shell=True)
            except:
                raise Exception("An error occured!")
        else:
            raise PermissionError("You dont have permission!")

    def VSS_Get_FileList(directory):
        if(ReShadowCode.run_as_admin()):
            return os.listdir(directory)
        else:
            raise PermissionError("You dont have permission!")
        
    def VSS_CopyFile(src, dest, shadowid):
        if(ReShadowCode.run_as_admin()):
            shutil.copy("\\\?\\GLOBALROOT\\Device\\HarddiskVolumeShadowCopy" + str(shadowid).replace("{", "").replace("}", "") + "\\" + src, dest)
        else:
            raise PermissionError("You dont have permission!")
        
    def VSS_GavePermission(path):
        return check_call(["attrib", "-r", path])

    def VSS_CreateDir_AfterSymlink(symlinklocation, directoryname):
        if(ReShadowCode.run_as_admin()):
            try:
                os.mkdir(symlinklocation + "\\" + directoryname)
            except:
                return "An error occured!"
        else:
            raise PermissionError("You dont have permission!")

    def VHD_Create(location, vhdname, size):
        return ReShadowCode.DiskPart_Command('CREATE VDISK FILE="' + location + vhdname + '" MAXIMUM=' + size + '')