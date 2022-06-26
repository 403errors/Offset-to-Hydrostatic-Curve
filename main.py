from turtle import position
import numpy
import matplotlib.pyplot as plt
import mplcursors
from scipy.interpolate import make_interp_spline

draft = numpy.array([0, 0.5*2.187, 1*2.187, 1.5*2.187, 2*2.187, 3*2.187, 3.384*2.187, 4*2.187, 5*2.187, 6*2.187])

# line 1 points
m1 = 1/30 # multiplier 1
waterplaneArea = m1*numpy.array([1332.0325, 1861.685, 2093.7775, 2237.8275000000003, 2339.028, 2543.4069999999992, 2737.60575, 2916.6255000000006, 3072.9735000000005, 3188.0415000000007])
waterplaneAreaNEW = numpy.linspace(waterplaneArea.min(), waterplaneArea.max(), 300) 
draft_smooth_1 = make_interp_spline(waterplaneArea, draft)(waterplaneAreaNEW)
plt.plot(waterplaneAreaNEW , draft_smooth_1, label = "Waterplane Area:30")

# line 2 points
m2 = 4 # multiplier 2
tpc = m2*numpy.array([13.653333125, 19.082271249999998, 21.461219375, 22.937731875, 23.975036999999997, 26.06992174999999, 28.060458937499998, 29.895411375000002, 31.497978375000002, 32.677425375000006])
tpcNEW = numpy.linspace(tpc.min(), tpc.max(), 300) 
draft_smooth_2 = make_interp_spline(tpc, draft)(tpcNEW)
plt.plot(tpcNEW, draft_smooth_2, label = "TPC(tonnes)*4")

# line 3 points
m3 = 1/300
massDisplacement = m3*numpy.array([0.0, 2089.508701875, 4700.007043125, 7535.044920937501, 10501.066205999998, 17127.938589749992, 21513.95386738125, 26188.3803645, 34490.286320625004, 42938.13694275])
massDisplacmentNEW = numpy.linspace(massDisplacement.min(), massDisplacement.max(), 300) 
draft_smooth_3 = make_interp_spline(massDisplacement, draft)(massDisplacmentNEW)
plt.plot(massDisplacmentNEW+5, draft_smooth_3, label = "[Mass Displacement(tonnes):300]+5")

# line 4 points
m4 = 1/300
volDisplacement = m4*numpy.array([0.0, 2038.545075, 4585.372725, 7351.263337500001, 10244.94264, 16710.183989999994, 20989.223285250002, 25549.639380000004, 33649.059825000004, 41890.86531000001])
volDisplacmentNEW = numpy.linspace(volDisplacement.min(), volDisplacement.max(), 300) 
draft_smooth_4 = make_interp_spline(massDisplacement, draft)(massDisplacmentNEW)
plt.plot(volDisplacmentNEW, draft_smooth_4, label = "Volume Displacement:300")

# line 5 points
m5 = 100
Cw = m5*numpy.array([0.5455091806709353, 0.601779525884292, 0.631607088989442, 0.6559235517568852, 0.6769067531738704, 0.7368756304305097, 0.7743022667639936, 0.8170529728971395, 0.8526412128086518, 0.868631472037624])
CwNEW = numpy.linspace(Cw.min(), Cw.max(), 300) 
draft_smooth_5 = make_interp_spline(Cw, draft)(CwNEW)
plt.plot(CwNEW, draft_smooth_5, label = "Cw*100")

# line 6 points
m6 = 150 #Cb[0] is 0 actually but for smootness it has been taken as 0.55
Cb = m6*numpy.array([0.55, 0.6017795258842921, 0.631607088989442, 0.6559235517568852, 0.6769067531738704, 0.7368756304305096, 0.7743022667639936, 0.8170529728971395, 0.8526412128086518, 0.8686314720376239])
CbNEW = numpy.linspace(Cb.min(), Cb.max(), 300) 
draft_smooth_6 = make_interp_spline(Cb, draft)(CbNEW)
plt.plot(CbNEW+20, draft_smooth_6, label = "(Cb*100)+20")

# line 7 points
m7 = 100
Cm = m7*numpy.array([0.89, 0.9170002067008662, 0.930718954248366, 0.9379697927643132, 0.9480985743664819, 0.9642754389872666, 0.9691221007358112, 0.9731909176968483, 0.9785541262946876, 0.9821237981215429])
CmNEW = numpy.linspace(Cm.min(), Cm.max(), 300) 
draft_smooth_7 = make_interp_spline(Cm, draft)(CmNEW)
plt.plot(CmNEW, draft_smooth_7, label = "Cm*100")

# line 8 points
m8 = 200 #Cp[0] is 0 actually but for smootness it has been taken as 0.62
Cp = m8*numpy.array([0.62, 0.6562479719054175, 0.6786227852203975, 0.6993013600403881, 0.7139624206546018, 0.7641754633970721, 0.7989728705764737, 0.839560828239926, 0.871327594353102, 0.8844419346104943])
CpNEW = numpy.linspace(Cp.min(), Cp.max(), 300) 
draft_smooth_8 = make_interp_spline(Cp, draft)(CpNEW)
plt.plot(CpNEW+10, draft_smooth_8, label = "(Cp*100)+10")

# line 9 points
m9 = 30
lcf = m9*numpy.array([-2.112662416269873, -2.213419563459984, -2.327976587770191, -2.4135081904212905, -2.4952570041914846, -2.9375644558656964, -3.5823486910049027, -3.839595450290068, -3.684063416101702, -3.422515359351502])
# lcfNEW = numpy.linspace(lcf.min(), lcf.max(), 300) 
# draft_smooth_9 = make_interp_spline(lcf, draft)(lcfNEW)
plt.plot((lcf)+220, draft, label = "(LCF*3)+100")

# line 10 points
m10 = 1/35
WSA = numpy.array([0, 2098.672565, 2577.7675, 2970.6255900000006, 3321.0660479999997, 4012.5772599999987, 4493.793436, 4942.53318, 5629.74375, 6312.457560000001])
# CwNEW = numpy.linspace(Cw.min(), Cw.max(), 300) 
# draft_smooth_5 = make_interp_spline(Cw, draft)(CwNEW)
plt.plot(WSA*m10, draft, label = "WSA:35")

# line 11 points
m11 = 10
MTC = m11*numpy.array([0.0, 5.291994648888538, 6.397876144230768, 7.2289616960067065, 7.865971223689797, 9.759992259008666, 11.655942502342473, 13.303807829268964, 14.506162313432835, 15.19997291413455])
# CwNEW = numpy.linspace(Cw.min(), Cw.max(), 300) 
# draft_smooth_5 = make_interp_spline(Cw, draft)(CwNEW)
plt.plot(MTC+20, draft, label = "(MTC*10)+20")

# line 12 points
m12 = 20
VCB = m12*numpy.array([0.0, 0.5475, 1.095, 1.6425, 2.19, 3.285, 3.8334999999999995, 4.38, 5.474999999999999, 6.57])
# CwNEW = numpy.linspace(Cw.min(), Cw.max(), 300) 
# draft_smooth_5 = make_interp_spline(Cw, draft)(CwNEW)
plt.plot(VCB+10, draft, label = "(VCB*20)+10")

# line 13 points
m13 = 1 #200 for making graph purpose only
BM_longitudinal = m13*numpy.array([200, 32.243169800893405, 17.696226646439083, 12.58896746738941, 9.8792559955221, 7.495527701846689, 7.30001422540372, 6.910889455184161, 5.7767609559058455, 4.951356446449111])
# BM_longitudinalNEW = numpy.linspace(BM_longitudinal.min(), BM_longitudinal.max(), 300) 
# draft_smooth_13 = make_interp_spline(BM_longitudinal, draft)(BM_longitudinalNEW)
plt.plot(BM_longitudinal+10, draft, label = "(BM_L)+10")

# line 14 points
m14 = 1 #200 for making graph purpose only
KM_longitudinal = m14*numpy.array([200, 32.790669800893404, 18.791226646439082, 14.23146746738941, 12.0692559955221, 10.78052770184669, 11.133514225403719, 11.29088945518416, 11.251760955905844, 11.521356446449111])
# CwNEW = numpy.linspace(Cw.min(), Cw.max(), 300) 
# draft_smooth_5 = make_interp_spline(Cw, draft)(CwNEW)
plt.plot(KM_longitudinal+25, draft, label = "(KM_L)+25")

# line 15 points
m15 = 1 #200 for making graph purpose only
BM_transverse = m15*numpy.array([200, 27.042982666622184, 15.627949376536709, 11.24820702657672, 8.840484620408517, 6.4353954601104775, 5.794707017436632, 5.351709408594572, 4.467850337354325, 3.7930329086837435])
# BM_transverseNEW = numpy.linspace(BM_transverse.min(), BM_transverse.max(), 300) 
# draft_smooth_15 = make_interp_spline(BM_transverse, draft)(BM_transverseNEW)
plt.plot(BM_transverse+40, draft, label = "(BM_T)+40")

# line 16 points
m16 = 1 #200 for making graph purpose only
KM_transverse = m16*numpy.array([200,27.590482666622183, 16.722949376536707, 12.89070702657672, 11.030484620408517, 9.720395460110478, 9.628207017436631, 9.731709408594572, 9.942850337354324, 10.363032908683744])
# CwNEW = numpy.linspace(Cw.min(), Cw.max(), 300) 
# draft_smooth_5 = make_interp_spline(Cw, draft)(CwNEW)
plt.plot(KM_transverse+15, draft, label = "(KM_T)+15")

# line 17 points
m17 = 10
LCB = m17*(numpy.array([-0.135, -0.007687893450349009, -0.0033471796672428777, 0.0006644638478352782, 0.0035087096069927326, 0.013250039899031979, 0.020000736891835902, 0.02787480067854564, 0.03403755330450178, 0.03658173531443587])+10)
# CwNEW = numpy.linspace(Cw.min(), Cw.max(), 300) 
# draft_smooth_5 = make_interp_spline(Cw, draft)(CwNEW)
plt.plot(LCB, draft, label = "(LCB+10)*10")


plt.xlabel('')
plt.ylabel('Draft (m)')
plt.title('Hydrostatic Curve (LBP=129m)')

# show a legend on the plot
plt.legend()
# mplcursors.cursor(hover=True)

# function to show the plot
plt.show()
