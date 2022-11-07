#!/usr/bin/python
import sys, os, re
import win32com.client as client
import win32com.shell.shell as shell
from subprocess import call, Popen, PIPE, check_call

class ReShadowCode():
    
    def run_as_admin():
        ASADMIN = 'asadmin'
        if sys.argv[-1] != ASADMIN:
            script = os.path.abspath(sys.argv[0])
            params = ' '.join([script] + sys.argv[1:] + [ASADMIN])
            try:
                shell.ShellExecuteEx(lpVerb='runas', lpFile=sys.executable, lpParameters=params)
                ret = True
            except:
                ret = False
        else:
            ret = False

        return ret

    def VSSParser(vssadmin_out):
        ret = []
        current = None
        fix1 = re.compile("Contained .* copies at ")
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
            return "You dont have any permissions!"

    def DiskPart_Command(exec):
        p = Popen(["diskpart"], stdin=PIPE, stdout=PIPE)
        p.stdin.write(b'' + exec + '\n')
        p.stdin.close()
        return p.communicate()[0].decode("utf-8").splitlines()

    def VSS_Create():
        wmi = client.GetObject("winmgmts:\\\\.\\root\\cimv2:Win32_ShadowCopy")
        createmethod = wmi.Methods_("Create")
        createparams = createmethod.InParameters
        createparams.Properties_[1].value="c:\\"
        results = wmi.ExecMethod_("Create", createparams)
        return results.Properties_[1].value

    def VSS_Create_Pipe(location, id_and_directory):
        if(ReShadowCode.run_as_admin()):
            try:
                call(['mklink', '/D', '/J', str(location), "\\\?\\\GLOBALROOT\\\Device\\\HarddiskVolumeShadowCopy" + id_and_directory + ""], shell=True)
            except:
                return "An error occured!"
        else:
            return "You dont have any permissions!"

    def VSS_Create_PipeForeach(location, id_and_directory):
        if(ReShadowCode.run_as_admin()):
            try:
                call(['mklink', '/D', '/J', str(location), str(id_and_directory)], shell=True)
            except:
                return "An error occured!"
        else:
            return "You dont have any permissions!"

    def VSS_Get_FileList(directory):
        if(ReShadowCode.run_as_admin()):
            listdir = os.listdir(directory)
            return listdir
        else:
            return "You dont have any permissions!"

    def VSS_GavePermission(path):
        return check_call(["attrib", "-r", path])

    def VSS_CreateDir_AfterSymlink(symlinklocation, directoryname):
        if(ReShadowCode.run_as_admin()):
            try:
                os.mkdir(symlinklocation + "\\" + directoryname)
            except:
                return "An error occured!"
        else:
            return "You dont have any permissions!"

    def VHD_Create(location, vhdname, size):
        return ReShadowCode.DiskPart_Command('CREATE VDISK FILE="' + location + vhdname + '" MAXIMUM=' + size + '')