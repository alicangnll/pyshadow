<img src="pic/PY-removebg-preview-crop.png" />

#### Python ShadowCopy Analyzer for Cyber Security Researchers!

### Medium Link for Developers
<a href="https://alicann.medium.com/pyshadow-shadowcopy-editor-50357b055c4b">Click here</a>

### Example Code

<pre>
# List all ShadowCopy
'''
Example Result
ID : {e9a894be-dae7-49cb-9196-b5a22148210b}
Creation Date : 6.11.2022 19:58:20
Shadow Copy Location : \\?\GLOBALROOT\Device\HarddiskVolumeShadowCopy7
'''
list = ReShadowCode.VSS_ListShadows()
for shadowlist in list:
    print("ID : " + shadowlist["id"] + "\nCreation Date : " + shadowlist["creation_time"] + "\nShadow Copy Location : " + shadowlist["shadowcopy"] + "\n")
#Create a ShadowCopy
ReShadowCode.VSS_Create()
#Create a pipe/symlink with ShadowCopy() (Ex. \\?\GLOBALROOT\Device\HarddiskVolumeShadowCopy<b>id</b>)
ReShadowCode.VSS_Create_Pipe("C:\\Shadow1", "id")
#Get file list from ShadowCopy
'''
Example Result
Ali
Ali Can Gönüllü
Ali_000_vcRuntimeMinimum_x64.log
Ali_000_vcRuntimeMinimum_x86.log
Ali_001_vcRuntimeAdditional_x64.log
Ali_001_vcRuntimeAdditional_x86.log
All Users
Default
Default User
desktop.ini
Public
TEMP
'''
list = ReShadowCode.VSS_Get_FileList("C:\\Shadow1\\Users")
for files in list:
    print(files)
</pre>

### Images

<img src="pic/Shadow copy creation process.jpg" />
<img src="pic/Architectural diagram of Volume Shadow Copy Service.jpg" />
