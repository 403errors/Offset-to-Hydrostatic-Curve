# Half-breadths for different dwaterlines
wl_0=[0,0,0,0,0.4,0.8,2.8,2.95,5.05,7.25,8.6,9.5,9.85,9.85,9.85,9.75,8.65,6.55,4.75,3.3,2.05,0.95,0.6,0.25,0.1,0]
wl_0_half=[0,0,0,0.8,1.6,2.5,4.3,6.6,8.8,10.4,11.2,11.7,12.15,12.15,12.15,11.5,10.25,8.85,7.3,5.75,4.05,2.5,1.8,1.25,0.85,0.4]
wl_1=[0,0,0,1.45,2.5,3.55,5.85,8.4,10.25,11.45,12.05,12.45,12.75,12.75,12.75,12.3,11.35,9.9,8.25,6.6,4.9,3.3,2.5,1.9,1.3,0.8]
wl_1_half=[0,0,0,2.1,3.3,4.55,7.05,9.5,11.15,12.05,12.4,12.8,13,13,13,12.65,11.8,10.5,8.9,7.2,5.5,3.85,3.05,2.35,1.75,1.15]
wl_2=[0,0,0,2.6,3.95,5.4,8.15,10.2,11.65,12.35,12.75,13,13.1,13.1,13.1,12.85,12.1,10.95,9.34,7.65,5.9,4.25,3.5,2.7,2,1.45]
wl_3=[0,0,3.35,5,6.6,7.9,9.9,11.15,12.1,12.65,13,13.12,13.12,13.12,13.12,13,12.5,11.7,10.85,8.65,6.7,4.75,3.9,2.9,2.1,1.55]
wl_lwl=[4.25,5.8,6.9,7.85,8.75,9.5,10.85,11.7,12.35,12.8,13.1,13.12,13.12,13.12,13.12,13.1,12.75,12.15,10.95,9.45,7.3,4.95,3.75,2.5,1.35,0]
wl_4=[7.95,8.6,9.25,9.9,10.4,10.9,11.7,12.25,12.6,12.9,13.12,13.12,13.12,13.12,13.12,13.12,12.9,12.5,11.65,10.3,8.1,5.6,4.35,3.05,1.7,0.4]
wl_5=[9.55,10.05,10.55,11,11.45,11.85,12.25,12.6,12.8,13.05,13.12,13.12,13.12,13.12,13.12,13.12,13.1,12.85,12.44,11.45,9.3,6.9,5.65,4.2,2.7,1.15]
wl_MDK=[10.4,10.7,11.2,11.55,12,12.3,12.65,12.8,12.95,13.12,13.12,13.12,13.12,13.12,13.12,13.12,13.12,13.1,12.8,12.2,10.35,8.5,7.2,5.7,4,2.25]


# Values used for calculating 
lengthOf_WL=[123.95, 127.31, 130.0, 131.22, 131.888, 131.54, 134.74, 136.04, 137.35, 139.87]
beamAtEach_WL=[19.7, 24.3, 25.5, 26, 26.2, 26.24, 26.24, 26.24, 26.24, 26.24]
DraftVal=[0, 1.095, 2.19, 3.285, 4.38, 6.57, 7.667, 8.76, 10.95, 13.14]
HalfMidshipAreaBelow_WL=[0, 12.2, 25.988, 40.056, 54.4, 83.119, 97.485, 111.85, 140.583, 169.315]

# constants
density_of_sea_water=1.025 # unit in tonne/m^3
dist_btw_two_stn=6.45  # unit in m

# Variables    
water_plane_area=[]
tonne_per_cm_immersion=[]
water_plane_area_coefficient=[]
volume_displacement=[]
mass_displacement=[]
longitudinal_centre_of_floation=[]
longitudinal_second_moment_area=[]

# Function to calculate waterplane area and TPC and LCF
def type_1(waterline):
    water_plane_area_calc=(2/3*dist_btw_two_stn)*((0.5*waterline[1])+(2*waterline[2])+(1*waterline[3])+(2*waterline[4])+(1.5*waterline[5])+(4*waterline[6])+(2*waterline[7])+(4*waterline[8])+(2*waterline[9])+(4*waterline[10])+(2*waterline[11])+(4*waterline[12])+(2*waterline[13])+(4*waterline[14])+(2*waterline[15])+(4*waterline[16])+(2*waterline[17])+(4*waterline[18])+(2*waterline[19])+(4*waterline[20])+(1.5*waterline[21])+(2*waterline[22])+(1*waterline[23])+(2*waterline[24])+(0.5*waterline[25]))
    first_moment=(2/3*dist_btw_two_stn*2)*((0.5*waterline[1]*(-11))+(2*waterline[2]*(-10.5))+(1*waterline[3]*(-10))+(2*waterline[4]*(-9.5))+(1.5*waterline[5]*(-9))+(4*waterline[6]*(-8))+(2*waterline[7]*(-7))+(4*waterline[8]*(-6))+(2*waterline[9]*(-5))+(4*waterline[10]*(-4))+(2*waterline[11]*(-3))+(4*waterline[12]*(-2))+(2*waterline[13]*(-1))+(4*waterline[14]*(0))+(2*waterline[15]*1)+(4*waterline[16]*2)+(2*waterline[17]*3)+(4*waterline[18]*4)+(2*waterline[19]*5)+(4*waterline[20]*6)+(1.5*waterline[21]*7)+(2*waterline[22]*7.5)+(1*waterline[23]*8)+(2*waterline[24]*8.5)+(0.5*waterline[25]*9))
    second_moment=(2/3*dist_btw_two_stn*2)*((0.5*waterline[1]*(-11)*(-11))+(2*waterline[2]*(-10.5)*(-10.5))+(1*waterline[3]*(-10)*(-10))+(2*waterline[4]*(-9.5)*(-9.5))+(1.5*waterline[5]*(-9)*(-9))+(4*waterline[6]*(-8)*(-8))+(2*waterline[7]*(-7)*(-7))+(4*waterline[8]*(-6)*(-6))+(2*waterline[9]*(-5)*(-5))+(4*waterline[10]*(-4)*(-4))+(2*waterline[11]*(-3)*(-3))+(4*waterline[12]*(-2)*(-2))+(2*waterline[13]*(-1)*(-1))+(4*waterline[14]*(0)*(0))+(2*waterline[15]*1*1)+(4*waterline[16]*2*2)+(2*waterline[17]*3*3)+(4*waterline[18]*4*4)+(2*waterline[19]*5*5)+(4*waterline[20]*6*6)+(1.5*waterline[21]*7*7)+(2*waterline[22]*7.5*7.5)+(1*waterline[23]*8*8)+(2*waterline[24]*8.5*8.5)+(0.5*waterline[25]*9*9))
    water_plane_area.append(water_plane_area_calc)
    tonne_per_cm_immersion.append((density_of_sea_water*water_plane_area_calc)/100)
    longitudinal_centre_of_floation.append(first_moment/water_plane_area_calc)
    longitudinal_second_moment_area.append(second_moment)
def type_2(waterline):
    water_plane_area_calc=((dist_btw_two_stn*2/12)*((5*waterline[0])+(8*waterline[1])-(1*waterline[2])))+((2/3*dist_btw_two_stn)*((0.5*waterline[1])+(2*waterline[2])+(1*waterline[3])+(2*waterline[4])+(1.5*waterline[5])+(4*waterline[6])+(2*waterline[7])+(4*waterline[8])+(2*waterline[9])+(4*waterline[10])+(2*waterline[11])+(4*waterline[12])+(2*waterline[13])+(4*waterline[14])+(2*waterline[15])+(4*waterline[16])+(2*waterline[17])+(4*waterline[18])+(2*waterline[19])+(4*waterline[20])+(1.5*waterline[21])+(2*waterline[22])+(1*waterline[23])+(2*waterline[24])+(0.5*waterline[25])))
    first_moment=((dist_btw_two_stn*2/12)*((5*waterline[0]*(-11.5))+(8*waterline[1]*(-11))-(1*waterline[2]*(-10.5))))+((2/3*dist_btw_two_stn*2)*((0.5*waterline[1]*(-11))+(2*waterline[2]*(-10.5))+(1*waterline[3]*(-10))+(2*waterline[4]*(-9.5))+(1.5*waterline[5]*(-9))+(4*waterline[6]*(-8))+(2*waterline[7]*(-7))+(4*waterline[8]*(-6))+(2*waterline[9]*(-5))+(4*waterline[10]*(-4))+(2*waterline[11]*(-3))+(4*waterline[12]*(-2))+(2*waterline[13*(-1)])+(4*waterline[14]*0)+(2*waterline[15]*1)+(4*waterline[16]*2)+(2*waterline[17]*3)+(4*waterline[18]*4)+(2*waterline[19]*5)+(4*waterline[20])*6+(1.5*waterline[21]*7)+(2*waterline[22]*7.5)+(1*waterline[23]*8)+(2*waterline[24]*8.5)+(0.5*waterline[25]*9)))
    second_moment=((dist_btw_two_stn*2/12)*((5*waterline[0]*(-11.5)*(-11.5))+(8*waterline[1]*(-11)*(-11))-(1*waterline[2]*(-10.5)*(-10.5))))+(2/3*dist_btw_two_stn*2)*((0.5*waterline[1]*(-11)*(-11))+(2*waterline[2]*(-10.5)*(-10.5))+(1*waterline[3]*(-10)*(-10))+(2*waterline[4]*(-9.5)*(-9.5))+(1.5*waterline[5]*(-9)*(-9))+(4*waterline[6]*(-8)*(-8))+(2*waterline[7]*(-7)*(-7))+(4*waterline[8]*(-6)*(-6))+(2*waterline[9]*(-5)*(-5))+(4*waterline[10]*(-4)*(-4))+(2*waterline[11]*(-3)*(-3))+(4*waterline[12]*(-2)*(-2))+(2*waterline[13]*(-1)*(-1))+(4*waterline[14]*(0)*(0))+(2*waterline[15]*1*1)+(4*waterline[16]*2*2)+(2*waterline[17]*3*3)+(4*waterline[18]*4*4)+(2*waterline[19]*5*5)+(4*waterline[20]*6*6)+(1.5*waterline[21]*7*7)+(2*waterline[22]*7.5*7.5)+(1*waterline[23]*8*8)+(2*waterline[24]*8.5*8.5)+(0.5*waterline[25]*9*9))
    water_plane_area.append(water_plane_area_calc)
    tonne_per_cm_immersion.append((density_of_sea_water*water_plane_area_calc)/100)
    longitudinal_centre_of_floation.append(first_moment/water_plane_area_calc)
    longitudinal_second_moment_area.append(second_moment)

# Calling function to calculate waterplane area and TPC for different waterlines
type_1(wl_0)
type_1(wl_0_half)
type_1(wl_1)
type_1(wl_1_half)
type_1(wl_2)
type_1(wl_3)
type_2(wl_lwl)
type_2(wl_4)
type_2(wl_5)
type_2(wl_MDK)

# calculation for water plane area coefficient
for i in range(0,10):
    water_plane_area_coefficient.append(water_plane_area[i]/(lengthOf_WL[i]*beamAtEach_WL[i]))

# calculation of volume of displacement
for i in range(0,10):
    volume_displacement.append(water_plane_area[i]*DraftVal[i])

# calculation of mass of displacement
for i in range(0,10):
    mass_displacement.append(volume_displacement[i]*density_of_sea_water)

# calculation of block coefficient
block_coefficient=[]
def Block_coeff(length_of_waterline,beam_at_each_wl,vol_displacement,draft_val):
    i=1
    block_coefficient.append(0)
    while i<=9:
        v=vol_displacement[i]
        l=length_of_waterline[i]
        b=beam_at_each_wl[i]
        t=draft_val[i]
        x=v/(l*b*t)
        block_coefficient.append(x)
        i=i+1
Block_coeff(lengthOf_WL,beamAtEach_WL,volume_displacement,DraftVal)

# calculation of mid-ship area coefficient 
midship_area_coefficient=[]
def midship_area_coeff(half_midship_area_below_wl,beam_at_each_wl,draft_val,Cm):
    i=1
    Cm.append(0)
    while i<=9:
        b=beam_at_each_wl[i]
        t=draft_val[i]
        Am=half_midship_area_below_wl[i]*2
        x=Am/(b*t)
        Cm.append(x)
        i=i+1
midship_area_coeff(HalfMidshipAreaBelow_WL,beamAtEach_WL,DraftVal,midship_area_coefficient)

# Calculation of prismatic coefficient
prismatic_coefficient=[]
def PrismaticCoeff(c_block,CM,CP):
    i=1
    CP.append(0)
    while i<=9:
        cb=c_block[i]
        cm=CM[i]
        x=cb/cm
        CP.append(x)
        i=i+1
PrismaticCoeff(block_coefficient,midship_area_coefficient,prismatic_coefficient)

# Calculation of wetted surface area
wetted_surface_area=[0]
for i in range(1,10):
    wsa=1.7*lengthOf_WL[i]*DraftVal[i] + volume_displacement[i]/DraftVal[i]
    wetted_surface_area.append(wsa)


# Calculation of vertical centre of buoyancy
vertical_centre_of_buoyancy=[]
for i in range(0,10):
    kb=((DraftVal[i]/2)+(volume_displacement[i]/water_plane_area[i]))/3
    vertical_centre_of_buoyancy.append(kb)

# Calculation of longitudinal metacentric radius
longitudinal_metacentric_radius=[300]
for i in range(1,10):
    bml=longitudinal_second_moment_area[i]/volume_displacement[i]
    longitudinal_metacentric_radius.append(bml)

# Calculation of transverse metacentric radius
transverse_metacentric_radius=[300]
for i in range(1,10):
    bmt=(water_plane_area_coefficient[i]*water_plane_area_coefficient[i]*beamAtEach_WL[i]*beamAtEach_WL[i])/(12*block_coefficient[i]*DraftVal[i])
    transverse_metacentric_radius.append(bmt)

# Calculation of longitudinal metacentric height
metacentric_height=[]
for i in range(1,10):
    metacentric_height.append(vertical_centre_of_buoyancy[i]+longitudinal_metacentric_radius[i])

# Calculation of transverse metacentric height
transverse_metacentric_height=[]
for i in range(1,10):
    transverse_metacentric_height.append(vertical_centre_of_buoyancy[i]+transverse_metacentric_radius[i])

# Calculation of Moment Causing Trim
moment_causing_trim=[0]
for i in range(1,10):
    mct=(mass_displacement[i]*longitudinal_metacentric_radius[i])/(lengthOf_WL[i]*100)
    moment_causing_trim.append(mct)

# Calculation of LCB
Longitudinal_centre_of_buoyancy=[]
for i in range(0,10):
    lcb=-0.135+(0.194*prismatic_coefficient[i])
    Longitudinal_centre_of_buoyancy.append(lcb)

# Output for hydrostatic properties
print("Waterplane Area : ",water_plane_area)
print("TPC : ",tonne_per_cm_immersion)
print("Vol. Displacement : ",volume_displacement)
print("Mass Displacement : ",mass_displacement)
print("Cwp : ",water_plane_area_coefficient)
print("Cb : ",block_coefficient)
print("Cm : ",midship_area_coefficient)
print("Cp : ",prismatic_coefficient)
print("LCF : ",longitudinal_centre_of_floation)
print("WSA : ",wetted_surface_area)
print("MCT : ",moment_causing_trim)
print("VCB : ",vertical_centre_of_buoyancy)
print("Longitudinal KM : ",metacentric_height)
print("Longitudinal BM : ",longitudinal_metacentric_radius)
print("Transverse BM : ",transverse_metacentric_radius)
print("Transverse KM : ",transverse_metacentric_height)
print("LCB : ",Longitudinal_centre_of_buoyancy)

