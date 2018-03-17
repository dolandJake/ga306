import maya.cmds as cmds
import polynoise


pathOfFiles = "/Users/student/Desktop/ga306/final_project/"
fileType = "obj"

files = cmds.getFileList(folder=pathOfFiles, filespec='*.%s' % fileType)
if len(files) == 0:
    cmds.warning("No files found")
else:
    for f in files:
        cmds.file(pathOfFiles + f, i=True)
        

    
Rhino = cmds.select("mesh02", r=True)
arPolyNoise(Rhino[0], 0.02)

myCube = maya.cmds.polyCube()[0]

cmds.connectAttr( myCube[0] + '.rotate', Rhino[1] + '.rotate' )
