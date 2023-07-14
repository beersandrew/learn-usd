from pxr import Usd, UsdGeom #This is the hard one... 
stage = Usd.Stage.CreateNew('HelloWorld.usda') 
xformPrim = UsdGeom.Xform.Define(stage, '/hello') 
spherePrim = UsdGeom.Sphere.Define(stage, '/hello/world') 
stage.GetRootLayer().Save()