import math
import cmath
print("Calculate the side width & Cross Sectional Area of Of Cut And Fill on a hill side section  : ".title().center(60))
print( )
road_width=float(input("Enter Road Width in ft : "))
Side_Slope_cut=float(input("Enter Your Side Slope in Cut : "))
Side_Slope_Fill=float(input("Enter Your Side Slope in Fill in : "))
existing_ground_slope=float(input("Enter Your existing ground Slope in Fill in : "  ))
center_height_Cut=float(input("Enter Your Center Height In Cut : "))
center_height_Fill=float(input("Enter Your Center Height In Fill : "))
BC= center_height_Cut + existing_ground_slope * (road_width / 2)
DE=-center_height_Cut + existing_ground_slope * (road_width / 2)

Height_Of_Bc = (existing_ground_slope)**-1 * (BC)
Height_Of_DE = (existing_ground_slope)**-1 * (DE)
#print("BC", BC.__round__(2) , "DE",DE.__round__(2),"Height Of BC",Height_Of_Bc.__round__(2),"Height of DC ",Height_Of_DE.__round__(2))
y1=(Side_Slope_cut-existing_ground_slope)**-1 * (BC)
y2=(Side_Slope_Fill-existing_ground_slope)**-1 * (DE)
w1=y1+(road_width/2)
W2=y2+(road_width/2)
#print("W1 is = ",w1 .__round__(2), "W2 is = ",W2 .__round__(2))

#Now Area of cut
Area_for_cut= 0.5*(BC * y1) + 0.5*(BC * Height_Of_Bc)
print("Area For Cut Is = ",Area_for_cut,)

#Now Area For Fill
Area_for_Fill= 0.5*(DE * y2) + 0.5*(DE * Height_Of_DE)
print("Area For Fill is ",Area_for_Fill,)

