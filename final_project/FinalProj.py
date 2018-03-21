import maya.cmds as cmds
import maya.OpenMaya as om
import random, time

def arPolyNoise(geoObject, maxDisplacement):
    """Apply noise to the supplied geometry object using the supplied max displacement."""
    # get the dag path for the shapeNode using an API selection list
    selection = om.MSelectionList()
    dagPath = om.MDagPath()
    try:
        selection.add(geoObject)
        selection.getDagPath(0, dagPath)
    except: raise
    # apply noise to the shape's points
    try:        
        # initialize a geometry iterator
        geoIter = om.MItGeometry(dagPath)
        # get the positions of all the vertices in world space
        pArray = om.MPointArray()
        geoIter.allPositions(pArray)
        # displace each of the vertices
        for i in xrange(pArray.length()):
            displacement = om.MVector.one * random.random() * maxDisplacement
            pArray[i].x += displacement.x
            pArray[i].y += displacement.y
            pArray[i].z += displacement.z
        # update the surface of the geometry with the changes
        geoIter.setAllPositions(pArray)
        meshFn = om.MFnMesh(dagPath)
        meshFn.updateSurface()
    except: raise


pathOfFiles = "/Users/student/Desktop/ga306/final_project/"
fileType = "obj"

files = cmds.getFileList(folder=pathOfFiles, filespec='*.%s' % fileType)
if len(files) == 0:
    cmds.warning("No files found")
else:
    for f in files:   
        cmds.file(pathOfFiles + f, i=True)
        

    
Rhino = cmds.ls(sl=True)


myCube = maya.cmds.polyCube()[0]
print(myCube)
print(Rhino)
cmds.connectAttr( myCube + '.rotate', "mesh02.translate" )
cmds.select( 'pCubeShape1' )
cmds.rotate( '80deg', 0, -81, r=True )


# save the current scene to an ascii file named "RHINOSTUFF.ma"
#
cmds.file( rename='RHINOSTUFF' )
cmds.file( save=True, type='mayaAscii' )






