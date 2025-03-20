from OCC.Core.BRepPrimAPI import BRepPrimAPI_MakeSphere, BRepPrimAPI_MakeCylinder, BRepPrimAPI_MakeBox
from OCC.Core.BRepAlgoAPI import BRepAlgoAPI_Fuse
from OCC.Core.gp import gp_Pnt, gp_Ax2, gp_Dir
from OCC.Display.SimpleGui import init_display

def create_sergius():
    display, start_display, add_menu, add_function_to_menu = init_display()

    # Head
    head = BRepPrimAPI_MakeSphere(gp_Pnt(0, 0, 60), 12).Shape()

    # Torso
    torso = BRepPrimAPI_MakeCylinder(20, 40).Shape()

    # Arms
    left_arm = BRepPrimAPI_MakeCylinder(gp_Ax2(gp_Pnt(-25, 0, 30), gp_Dir(1, 0, 0)), 6, 30).Shape()
    right_arm = BRepPrimAPI_MakeCylinder(gp_Ax2(gp_Pnt(25, 0, 30), gp_Dir(1, 0, 0)), 6, 30).Shape()

    # Legs
    left_leg = BRepPrimAPI_MakeCylinder(gp_Ax2(gp_Pnt(-10, 0, 0), gp_Dir(0, 0, 1)), 8, 40).Shape()
    right_leg = BRepPrimAPI_MakeCylinder(gp_Ax2(gp_Pnt(10, 0, 0), gp_Dir(0, 0, 1)), 8, 40).Shape()

    # Pole Weapon
    pole = BRepPrimAPI_MakeCylinder(gp_Ax2(gp_Pnt(0, 40, 30), gp_Dir(0, 1, 0)), 2, 60).Shape()

    # Combine shapes
    body = BRepAlgoAPI_Fuse(torso, head).Shape()
    body = BRepAlgoAPI_Fuse(body, left_arm).Shape()
    body = BRepAlgoAPI_Fuse(body, right_arm).Shape()
    body = BRepAlgoAPI_Fuse(body, left_leg).Shape()
    body = BRepAlgoAPI_Fuse(body, right_leg).Shape()
    body = BRepAlgoAPI_Fuse(body, pole).Shape()

    # Display the model
    display.DisplayShape(body, update=True)
    start_display()

create_sergius()