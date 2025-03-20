from OCC.Core.BRepPrimAPI import BRepPrimAPI_MakeSphere, BRepPrimAPI_MakeCylinder, BRepPrimAPI_MakeBox
from OCC.Core.BRepAlgoAPI import BRepAlgoAPI_Fuse
from OCC.Core.gp import gp_Pnt, gp_Ax2, gp_Dir, gp_Trsf, gp_Ax1
from OCC.Core.BRepBuilderAPI import BRepBuilderAPI_Transform
from OCC.Display.SimpleGui import init_display

def create_sergius_v2():
    display, start_display, add_menu, add_function_to_menu = init_display()

    # Head
    head = BRepPrimAPI_MakeSphere(gp_Pnt(0, 5, 60), 13).Shape() # Tilt head forward slightly

    # Torso
    torso_main = BRepPrimAPI_MakeCylinder(22, 45).Shape()
    torso_pos = gp_Pnt(0, 0, 20)
    torso = BRepPrimAPI_MakeCylinder(gp_Ax2(torso_pos, gp_Dir(0, 0, 1)), 22, 45).Shape()

    # Muscle Definition (Chest & Abs)
    chest_muscle_l = BRepPrimAPI_MakeSphere(gp_Pnt(-12, 0, 45), 8).Shape()
    chest_muscle_r = BRepPrimAPI_MakeSphere(gp_Pnt(12, 0, 45), 8).Shape()
    abs_muscle_mid = BRepPrimAPI_MakeSphere(gp_Pnt(0, 0, 30), 6).Shape()
    abs_muscle_l = BRepPrimAPI_MakeSphere(gp_Pnt(-8, 0, 30), 5).Shape()
    abs_muscle_r = BRepPrimAPI_MakeSphere(gp_Pnt(8, 0, 30), 5).Shape()


    # Arms
    arm_length = 35
    arm_radius = 7

    # Left Arm
    left_arm_base = gp_Pnt(-30, 0, 35)
    left_arm = BRepPrimAPI_MakeCylinder(gp_Ax2(left_arm_base, gp_Dir(1, 0, 0)), arm_radius, arm_length).Shape()
    bicep_l = BRepPrimAPI_MakeSphere(gp_Pnt(-30 + arm_length/2, 0, 35), arm_radius * 0.8).Shape()

    # Right Arm
    right_arm_base = gp_Pnt(30, 0, 35)
    right_arm = BRepPrimAPI_MakeCylinder(gp_Ax2(right_arm_base, gp_Dir(1, 0, 0)), arm_radius, arm_length).Shape()
    bicep_r = BRepPrimAPI_MakeSphere(gp_Pnt(30 + arm_length/2, 0, 35), arm_radius * 0.8).Shape()


    # Legs
    leg_radius = 9
    leg_length = 42
    calf_muscle_l = BRepPrimAPI_MakeSphere(gp_Pnt(-12, 0, leg_length/2), leg_radius * 0.7).Shape()
    calf_muscle_r = BRepPrimAPI_MakeSphere(gp_Pnt(12, 0, leg_length/2), leg_radius * 0.7).Shape()

    left_leg = BRepPrimAPI_MakeCylinder(gp_Ax2(gp_Pnt(-12, 0, 0), gp_Dir(0, 0, 1)), leg_radius, leg_length).Shape()
    right_leg = BRepPrimAPI_MakeCylinder(gp_Ax2(gp_Pnt(12, 0, 0), gp_Dir(0, 0, 1)), leg_radius, leg_length).Shape()


    # Hands and Feet (Simplified)
    hand_size = 6
    foot_size = 8
    left_hand = BRepPrimAPI_MakeBox(gp_Pnt(-30 - arm_length, -hand_size/2, 35 - hand_size/2), gp_Pnt(-30 - arm_length + hand_size, hand_size/2, 35 + hand_size/2)).Shape()
    right_hand = BRepPrimAPI_MakeBox(gp_Pnt(30 + arm_length, -hand_size/2, 35 - hand_size/2), gp_Pnt(30 + arm_length + hand_size, hand_size/2, 35 + hand_size/2)).Shape()

    left_foot =  BRepPrimAPI_MakeBox(gp_Pnt(-12 - foot_size/2, 0, -leg_length), gp_Pnt(-12 + foot_size/2, 0 + foot_size/2, -leg_length + foot_size)).Shape()
    right_foot = BRepPrimAPI_MakeBox(gp_Pnt(12 - foot_size/2, 0, -leg_length), gp_Pnt(12 + foot_size/2, 0 + foot_size/2, -leg_length + foot_size)).Shape()


    # Pole Weapon
    pole = BRepPrimAPI_MakeCylinder(gp_Ax2(gp_Pnt(0, 40, 30), gp_Dir(0, 1, 0)), 2, 60).Shape()

    # Combine shapes
    body = BRepAlgoAPI_Fuse(torso, head).Shape()
    body = BRepAlgoAPI_Fuse(body, chest_muscle_l).Shape()
    body = BRepAlgoAPI_Fuse(body, chest_muscle_r).Shape()
    body = BRepAlgoAPI_Fuse(body, abs_muscle_mid).Shape()
    body = BRepAlgoAPI_Fuse(body, abs_muscle_l).Shape()
    body = BRepAlgoAPI_Fuse(body, abs_muscle_r).Shape()
    body = BRepAlgoAPI_Fuse(body, left_arm).Shape()
    body = BRepAlgoAPI_Fuse(body, right_arm).Shape()
    body = BRepAlgoAPI_Fuse(body, bicep_l).Shape()
    body = BRepAlgoAPI_Fuse(body, bicep_r).Shape()

    body = BRepAlgoAPI_Fuse(body, left_leg).Shape()
    body = BRepAlgoAPI_Fuse(body, right_leg).Shape()
    body = BRepAlgoAPI_Fuse(body, calf_muscle_l).Shape()
    body = BRepAlgoAPI_Fuse(body, calf_muscle_r).Shape()

    body = BRepAlgoAPI_Fuse(body, left_hand).Shape()
    body = BRepAlgoAPI_Fuse(body, right_hand).Shape()
    body = BRepAlgoAPI_Fuse(body, left_foot).Shape()
    body = BRepAlgoAPI_Fuse(body, right_foot).Shape()

    body = BRepAlgoAPI_Fuse(body, pole).Shape()



    # Display the model
    display.DisplayShape(body, update=True)
    start_display()

create_sergius_v2()