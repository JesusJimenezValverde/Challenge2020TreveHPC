# state file generated using paraview version 5.8.0-RC1

# ----------------------------------------------------------------
# setup views used in the visualization
# ----------------------------------------------------------------

# trace generated using paraview version 5.8.0-RC1
#
# To ensure correct image size when batch processing, please search 
# for and uncomment the line `# renderView*.ViewSize = [*,*]`

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# get the material library
materialLibrary1 = GetMaterialLibrary()

# Create a new 'Render View'
renderView1 = CreateView('RenderView')
renderView1.ViewSize = [1041, 491]
renderView1.AxesGrid = 'GridAxes3DActor'
renderView1.CenterOfRotation = [30.004038197396, 30.0060745588305, 30.0553748614745]
renderView1.StereoType = 'Crystal Eyes'
renderView1.CameraPosition = [-47.599639082535575, 155.8655566758647, 222.57415632307638]
renderView1.CameraFocalPoint = [30.004038197395996, 30.006074558830473, 30.055374861474483]
renderView1.CameraViewUp = [-0.7680335899682343, 0.34839091882721174, -0.537352930911554]
renderView1.CameraFocalDisk = 1.0
renderView1.CameraParallelScale = 51.92373120761379
renderView1.Background = [0.0, 0.0, 0.0]
renderView1.BackEnd = 'OSPRay raycaster'
renderView1.OSPRayMaterialLibrary = materialLibrary1

# init the 'GridAxes3DActor' selected for 'AxesGrid'
renderView1.AxesGrid.Visibility = 1

SetActiveView(None)

# ----------------------------------------------------------------
# setup view layouts
# ----------------------------------------------------------------

# create new layout object 'Layout #1'
layout1 = CreateLayout(name='Layout #1')
layout1.AssignView(0, renderView1)

# ----------------------------------------------------------------
# restore active view
SetActiveView(renderView1)
# ----------------------------------------------------------------

# ----------------------------------------------------------------
# setup the data processing pipelines
# ----------------------------------------------------------------

# create a new 'CSV Reader'
cenatMD_ = CSVReader(FileName=[
'../Results/cenatMD_25.txt',
'../Results/cenatMD_50.txt', 
'../Results/cenatMD_75.txt', 
'../Results/cenatMD_100.txt', 
'../Results/cenatMD_125.txt', 
'../Results/cenatMD_150.txt', 
'../Results/cenatMD_175.txt', 
'../Results/cenatMD_200.txt', 
'../Results/cenatMD_225.txt', 
'../Results/cenatMD_250.txt', 
'../Results/cenatMD_275.txt', 
'../Results/cenatMD_300.txt',
'../Results/cenatMD_325.txt', 
'../Results/cenatMD_350.txt', 
'../Results/cenatMD_375.txt', 
'../Results/cenatMD_400.txt',  
'../Results/cenatMD_425.txt', 
'../Results/cenatMD_450.txt', 
'../Results/cenatMD_475.txt', 
'../Results/cenatMD_500.txt'])

# create a new 'Table To Points'
tableToPoints1 = TableToPoints(Input=cenatMD_)
tableToPoints1.XColumn = 'x'
tableToPoints1.YColumn = 'y'
tableToPoints1.ZColumn = 'z'

# create a new 'Glyph'
glyph1 = Glyph(Input=tableToPoints1,
    GlyphType='Sphere')
glyph1.OrientationArray = ['POINTS', 'No orientation array']
glyph1.ScaleArray = ['POINTS', 'No scale array']
glyph1.ScaleFactor = 1.79963280035508
glyph1.GlyphTransform = 'Transform2'

# ----------------------------------------------------------------
# setup the visualization in view 'renderView1'
# ----------------------------------------------------------------

# show data from tableToPoints1
tableToPoints1Display = Show(tableToPoints1, renderView1, 'GeometryRepresentation')

# trace defaults for the display properties.
tableToPoints1Display.Representation = 'Surface'
tableToPoints1Display.ColorArrayName = [None, '']
tableToPoints1Display.OSPRayScaleFunction = 'PiecewiseFunction'
tableToPoints1Display.SelectOrientationVectors = 'None'
tableToPoints1Display.ScaleFactor = 5.999192360520801
tableToPoints1Display.SelectScaleArray = 'None'
tableToPoints1Display.GlyphType = 'Arrow'
tableToPoints1Display.GlyphTableIndexArray = 'None'
tableToPoints1Display.GaussianRadius = 0.29995961802604
tableToPoints1Display.SetScaleArray = [None, '']
tableToPoints1Display.ScaleTransferFunction = 'PiecewiseFunction'
tableToPoints1Display.OpacityArray = [None, '']
tableToPoints1Display.OpacityTransferFunction = 'PiecewiseFunction'
tableToPoints1Display.DataAxesGrid = 'GridAxesRepresentation'
tableToPoints1Display.PolarAxes = 'PolarAxesRepresentation'

# show data from glyph1
glyph1Display = Show(glyph1, renderView1, 'GeometryRepresentation')

# get color transfer function/color map for 'Normals'
normalsLUT = GetColorTransferFunction('Normals')
normalsLUT.RGBPoints = [1.0, 0.0, 0.0, 0.5625, 1.0000000057115335, 0.0, 0.0, 1.0, 1.0000000187664926, 0.0, 1.0, 1.0, 1.0000000252939594, 0.5, 1.0, 0.5, 1.0000000318214262, 1.0, 1.0, 0.0, 1.0000000448763855, 1.0, 0.0, 0.0, 1.0000000514038523, 0.5, 0.0, 0.0]
normalsLUT.ColorSpace = 'RGB'
normalsLUT.ScalarRangeInitialized = 1.0

# trace defaults for the display properties.
glyph1Display.Representation = 'Surface'
glyph1Display.ColorArrayName = ['POINTS', 'Normals']
glyph1Display.LookupTable = normalsLUT
glyph1Display.OSPRayScaleFunction = 'PiecewiseFunction'
glyph1Display.SelectOrientationVectors = 'None'
glyph1Display.ScaleFactor = 6.577980472147465
glyph1Display.SelectScaleArray = 'None'
glyph1Display.GlyphType = 'Arrow'
glyph1Display.GlyphTableIndexArray = 'None'
glyph1Display.GaussianRadius = 0.3288990236073732
glyph1Display.SetScaleArray = [None, '']
glyph1Display.ScaleTransferFunction = 'PiecewiseFunction'
glyph1Display.OpacityArray = [None, '']
glyph1Display.OpacityTransferFunction = 'PiecewiseFunction'
glyph1Display.DataAxesGrid = 'GridAxesRepresentation'
glyph1Display.PolarAxes = 'PolarAxesRepresentation'

# setup the color legend parameters for each legend in this view

# get color legend/bar for normalsLUT in view renderView1
normalsLUTColorBar = GetScalarBar(normalsLUT, renderView1)
normalsLUTColorBar.WindowLocation = 'AnyLocation'
normalsLUTColorBar.Position = [0.8866474543707973, 0.4704684317718941]
normalsLUTColorBar.Title = 'Normals'
normalsLUTColorBar.ComponentTitle = 'Magnitude'
normalsLUTColorBar.ScalarBarLength = 0.32999999999999985

# set color bar visibility
normalsLUTColorBar.Visibility = 1

# show color legend
glyph1Display.SetScalarBarVisibility(renderView1, True)

# ----------------------------------------------------------------
# setup color maps and opacity mapes used in the visualization
# note: the Get..() functions create a new object, if needed
# ----------------------------------------------------------------

# get opacity transfer function/opacity map for 'Normals'
normalsPWF = GetOpacityTransferFunction('Normals')
normalsPWF.Points = [1.0, 0.0, 0.5, 0.0, 1.0000000514038523, 1.0, 0.5, 0.0]
normalsPWF.ScalarRangeInitialized = 1

# ----------------------------------------------------------------
# finally, restore active source
SetActiveSource(glyph1)
# ----------------------------------------------------------------
