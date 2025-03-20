from OCC.Core.BRepPrimAPI import BRepPrimAPI_MakeSphere, BRepPrimAPI_MakeCylinder, BRepPrimAPI_MakeBox
from OCC.Core.BRepAlgoAPI import BRepAlgoAPI_Fuse
from OCC.Core.gp import gp_Pnt, gp_Ax2, gp_Dir
from OCC.Display.SimpleGui import init_display

def create_sergius_refined():
    display, start_display, add_menu, add_function_to_menu = init_display()

    # Head
    head = BRepPrimAPI_MakeSphere(gp_Pnt(0, 0, 60), 13).Shape()  # Slightly larger

    # Torso
    torso_main = BRepPrimAPI_MakeCylinder(22, 45).Shape()  # Wider and taller
    torso_pos = gp_Pnt(0, 0, 20)
    torso = BRepPrimAPI_MakeCylinder(gp_Ax2(torso_pos, gp_Dir(0, 0, 1)), 22, 45).Shape()

    # Muscle Definition (Chest)
    chest_muscle_l = BRepPrimAPI_MakeSphere(gp_Pnt(-12, 0, 45), 8).Shape()
    chest_muscle_r = BRepPrimAPI_MakeSphere(gp_Pnt(12, 0, 45), 8).Shape()

    # Arms
    arm_length = 35  # Longer arms
    arm_radius = 7
    left_arm = BRepPrimAPI_MakeCylinder(gp_Ax2(gp_Pnt(-30, 0, 35), gp_Dir(1, 0, 0)), arm_radius, arm_length).Shape()
    right_arm = BRepPrimAPI_MakeCylinder(gp_Ax2(gp_Pnt(30, 0, 35), gp_Dir(1, 0, 0)), arm_radius, arm_length).Shape()

    # Legs
    leg_radius = 9
    leg_length = 42
    left_leg = BRepPrimAPI_MakeCylinder(gp_Ax2(gp_Pnt(-12, 0, 0), gp_Dir(0, 0, 1)), leg_radius, leg_length).Shape()
    right_leg = BRepPrimAPI_MakeCylinder(gp_Ax2(gp_Pnt(12, 0, 0), gp_Dir(0, 0, 1)), leg_radius, leg_length).Shape()

    # Pole Weapon
    pole = BRepPrimAPI_MakeCylinder(gp_Ax2(gp_Pnt(0, 40, 30), gp_Dir(0, 1, 0)), 2, 60).Shape()

    # Combine shapes
    body = BRepAlgoAPI_Fuse(torso, head).Shape()
    body = BRepAlgoAPI_Fuse(body, chest_muscle_l).Shape()
    body = BRepAlgoAPI_Fuse(body, chest_muscle_r).Shape()
    body = BRepAlgoAPI_Fuse(body, left_arm).Shape()
    body = BRepAlgoAPI_Fuse(body, right_arm).Shape()
    body = BRepAlgoAPI_Fuse(body, left_leg).Shape()
    body = BRepAlgoAPI_Fuse(body, right_leg).Shape()
    body = BRepAlgoAPI_Fuse(body, pole).Shape()

    # Display the model
    display.DisplayShape(body, update=True)
    start_display()

create_sergius_refined()