import time
import cmath

######################## execution time array

exec_time_array = []

######################## general parameters
kv_base = 345
mva_base = 100

zbase = ((kv_base)^2)/mva_base
ybase = 1/zbase

gamma_ratio = 1.392
surge_ratio = 1.932
zero_seq_resis_ratio = 10.458

#%%%%%%%%%%%%%% line 26 to 30 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#%%%%%%%%% positive & negative sequence line parameters %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
r1_2630 = 0.00799
x1_2630 = 0.086
b1_2630 = 0.908
L = 1

z1_2630 = complex(r1_2630,x1_2630)*zbase
y1_2630 = complex(0,b1_2630)*ybase

g1_2630 = cmath.sqrt(y1_2630 * z1_2630)
g0_2630 = gamma_ratio * g1_2630

zlump1_2630 = z1_2630*L
ylump1_2630 = y1_2630*L

z_dash1_2630 = zlump1_2630 * (cmath.sinh(g1_2630*L)/g1_2630*L)
y_dash_by_2_1_2630 = (ylump1_2630/2) * (cmath.tanh(g1_2630*(L/2))/(g1_2630*(L/2)))

#%%%%%%% zero sequence line parameters %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
b0_2630 = (gamma_ratio/surge_ratio)*b1_2630
x0_2630 = gamma_ratio*surge_ratio*x1_2630
r0_2630 = zero_seq_resis_ratio*r1_2630
z0_2630 = complex(r0_2630,x0_2630)*zbase
y0_2630 = complex(0,b0_2630*ybase)

zlump0_2630 = z0_2630*L
ylump0_2630 = y0_2630*L

z_dash0_2630 = (zlump0_2630 * (cmath.sinh(g0_2630*L)/g0_2630*L))
y_dash_by_2_0_2630 = ((ylump0_2630/2) * (cmath.tanh(g0_2630*(L/2))/(g0_2630*(L/2))))




#line 08 to 30 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#%%%%%%%%% positive & negative sequence line parameters %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
r1_0830 = 0.00431
x1_0830 = 0.0504
b1_0830 = 0.514
L = 1

z1_0830 = complex(r1_0830,x1_0830)*zbase
y1_0830 = complex(0,b1_0830)*ybase

g1_0830 = cmath.sqrt(y1_0830 * z1_0830)
g0_0830 = gamma_ratio * g1_0830

zlump1_0830 = z1_0830*L
ylump1_0830 = y1_0830*L

z_dash1_0830 = zlump1_0830 * (cmath.sinh(g1_0830*L)/g1_0830*L)
y_dash_by_2_1_0830 = (ylump1_0830/2) * (cmath.tanh(g1_0830*(L/2))/(g1_0830*(L/2)))

#%%%%%%% zero sequence line parameters %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
b0_0830 = (gamma_ratio/surge_ratio)*b1_0830
x0_0830 = gamma_ratio*surge_ratio*x1_0830
r0_0830 = zero_seq_resis_ratio*r1_0830
z0_0830 = complex(r0_0830,x0_0830)*zbase
y0_0830 = complex(0,b0_0830*ybase)

zlump0_0830 = z0_0830*L
ylump0_0830 = y0_0830*L

z_dash0_0830 = (zlump0_0830 * (cmath.sinh(g0_0830*L)/g0_0830*L))
y_dash_by_2_0_0830 = ((ylump0_0830/2) * (cmath.tanh(g0_0830*(L/2))/(g0_0830*(L/2))))

#%%%%%%%% line parameters 30 to 38 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
r1_3038 = 0.00464
x1_3038 = 0.054
b1_3038 = 0.422
z1_3038 = complex(r1_3038,x1_3038)
y1_3038 = complex(0,b1_3038)
Zc1_3038_pu = cmath.sqrt(z1_3038/y1_3038)
Zc1_3038 = zbase * Zc1_3038_pu
g1_3038 = cmath.sqrt(y1_3038 * z1_3038)
L = 1

# %%%%%%%% line parameters 38 to 30 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
r1_3830 = 0.00464
x1_3830 = 0.054
b1_3830 = 0.422
z1_3830 = complex(r1_3830, x1_3830)
y1_3830 = complex(0, b1_3830)
Zc1_3830_pu = cmath.sqrt(z1_3830/y1_3830)
Zc1_3830 = zbase * Zc1_3830_pu
g1_3830 = cmath.sqrt(y1_3830 * z1_3830)
L = 1


# %%%%%%%%%%%%%% line 65 to 38 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# %%%%%%%%% positive & negative sequence line parameters %%%%%%%%%%%%%%%%%%%
r1_6538 = 0.00901
x1_6538 = 0.0986
b1_6538 = 1.046
L = 1

z1_6538 = complex(r1_6538, x1_6538)*zbase
y1_6538 = complex(0, b1_6538)*ybase

g1_6538 = cmath.sqrt(y1_6538 * z1_6538)
g0_6538 = gamma_ratio * g1_6538

zlump1_6538 = z1_6538*L
ylump1_6538 = y1_6538*L

z_dash1_6538 = zlump1_6538 * (cmath.sinh(g1_6538*L)/g1_6538*L)
y_dash_by_2_1_6538 = (ylump1_6538/2) * (cmath.tanh(g1_6538*(L/2))/(g1_6538*(L/2)))

# %%%%%%% zero sequence line parameters %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
b0_6538 = (gamma_ratio/surge_ratio)*b1_6538
x0_6538 = gamma_ratio*surge_ratio*x1_6538
r0_6538 = zero_seq_resis_ratio*r1_6538
z0_6538 = complex(r0_6538, x0_6538)*zbase
y0_6538 = complex(0,b0_6538)*ybase

zlump0_6538 = z0_6538*L
ylump0_6538 = y0_6538*L

z_dash0_6538 = (zlump0_6538 * (cmath.sinh(g0_6538*L)/g0_6538*L))
y_dash_by_2_0_6538 = ((ylump0_6538/2) * (cmath.tanh(g0_6538*(L/2))/(g0_6538*(L/2))))



#%%%%%%% Transformer between 17 and 30 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
x1_pu_1730 = complex(0,0.0388)
x1_1730 = x1_pu_1730*zbase

x2_1730 = x1_1730
x0_1730 = x1_1730

# %%%%%%% Transformer between 37 and 38 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
x1_pu_3738 = complex(0,0.0375)
x1_3738 = x1_pu_3738*zbase

x2_3738 = x1_3738
x0_3738 = x1_3738


def sfva(ss8_dataset, ss26_dataset, ss17_dataset,
         ss30_dataset, ss38_dataset, ss37_dataset,
         ss65_dataset):

    t1 = time.perf_counter_ns()
    
    ####################bus 26 data
    data26 = ss26_dataset
    # print("data26 is: {}".format(data26))
    va26_1_re = data26[0]
    va26_1_im = data26[1]
    va26_2_re = data26[2]
    va26_2_im = data26[3]
    va26_0_re = data26[4]
    va26_0_im = data26[5]

    # print("v26_pos_re: {}".format(data26[0]))
    # print("v26_pos_im: {}".format(data26[1]))
    # print("v26_neg_re: {}".format(data26[2]))
    # print("v26_neg_im: {}".format(data26[3]))
    # print("v26_zero_re: {}".format(data26[4]))
    # print("v26_zero_im: {}".format(data26[5]))
    # data26 = ss26_dataset[3]
    # print("data26 is: {}".format(data26))
    # va26_1_re = data26[3]
    # va26_1_im = data26[4]
    # va26_2_re = data26[5]
    # va26_2_im = data26[6]
    # va26_0_re = data26[7]
    # va26_0_im = data26[8]
    # va26_1_re = -78.1044890236
    # va26_1_im = -151.493586093
    # va26_2_re = 4.35542605871
    # va26_2_im = 17.0979516936
    # va26_0_re = 15.7567836535
    # va26_0_im = 22.5999966622

    va26_1 = complex(va26_1_re,va26_1_im)
    va26_1_mag = abs(va26_1)/199.18584
    va26_2 = complex(va26_2_re,va26_2_im)
    va26_0 = complex(va26_0_re,va26_0_im)

    ##################### bus 30 data
    data30 = ss30_dataset
    # print("data30 is: {}".format(data30))
    va30_1_re = data30[0]
    va30_1_im = data30[1]
    va30_2_re = data30[2]
    va30_2_im = data30[3]
    va30_0_re = data30[4]
    va30_0_im = data30[5]

    # data30 = ss30_dataset[3]
    # print("data30 is: {}".format(data30))
    # va30_1_re = data30[3]
    # va30_1_im = data30[4]
    # va30_2_re = data30[5]
    # va30_2_im = data30[6]
    # va30_0_re = data30[7]
    # va30_0_im = data30[8]

    # va30_1_re = -75.8693271986
    # va30_1_im = -137.323010883
    # va30_2_re = 4.93128358009
    # va30_2_im = 24.4873283626
    # va30_0_re = 20.5127913535
    # va30_0_im = 38.544720748

    va30_1 = complex(va30_1_re,va30_1_im)
    va30_1_mag = abs(va30_1)/199.18584
    va30_2 = complex(va30_2_re,va30_2_im)
    va30_0 = complex(va30_0_re,va30_0_im)

    va30 = va30_1 + va30_2 + va30_0

    ######################## bus 08 data
    data8 = ss8_dataset
    # print("data8 is: {}".format(data8))
    va08_1_re = data8[0]
    va08_1_im = data8[1]
    va08_2_re = data8[2]
    va08_2_im = data8[3]
    va08_0_re = data8[4]
    va08_0_im = data8[5]

    # data8 = ss8_dataset[3]
    # print("data8 is: {}".format(data8))
    # va08_1_re = data8[3]
    # va08_1_im = data8[4]
    # va08_2_re = data8[5]
    # va08_2_im = data8[6]
    # va08_0_re = data8[7]
    # va08_0_im = data8[8]

    # va08_1_re = -86.7108142611
    # va08_1_im = -133.498889352
    # va08_2_re = 6.52982317905
    # va08_2_im = 18.0985055825
    # va08_0_re = 16.5237979745
    # va08_0_im = 19.9964231992

    va08_1 = complex(va08_1_re,va08_1_im)
    va08_1_mag = abs(va08_1)/199.18584
    va08_2 = complex(va08_2_re,va08_2_im)
    va08_0 = complex(va08_0_re,va08_0_im)

    ######################## bus 17 data
    data17 = ss17_dataset
    # print("data17 is: {}".format(data17))
    va17_1_re = data17[0]
    va17_1_im = data17[1]
    va17_2_re = data17[2]
    va17_2_im = data17[3]
    va17_0_re = data17[4]
    va17_0_im = data17[5]

    # data17 = ss17_dataset[3]
    # print("data17 is: {}".format(data17))
    # va17_1_re = data17[3]
    # va17_1_im = data17[4]
    # va17_2_re = data17[5]
    # va17_2_im = data17[6]
    # va17_0_re = data17[7]
    # va17_0_im = data17[8]

    # va17_1_re = -32.1604343812
    # va17_1_im = -58.3697997785
    # va17_2_re = 2.19081136642
    # va17_2_im = 8.65866169555
    # va17_0_re = 8.76658282709
    # va17_0_im = 14.3648919985


    va17_1 = complex(va17_1_re,va17_1_im)*(345/143.52)
    va17_1_mag = abs(va17_1)/79.67433
    va17_2 = complex(va17_2_re,va17_2_im)*(345/143.52)
    va17_0 = complex(va17_0_re,va17_0_im)*(345/143.52)


    #%%%%%%%% bus 37 voltage 
    #%0.54,-22.3502138188,-65.5284514209,1.53422418138,8.12634746772,7.44847631993,14.4354755641

    data37 = ss37_dataset
    # print("data37 is: {}".format(data37))
    va37_1_re = data37[0]
    va37_1_im = data37[1]
    va37_2_re = data37[2]
    va37_2_im = data37[3]
    va37_0_re = data37[4]
    va37_0_im = data37[5]

    # data37 = ss37_dataset[3]
    # print("data37 is: {}".format(data37))
    # va37_1_re = data37[3]
    # va37_1_im = data37[4]
    # va37_2_re = data37[5]
    # va37_2_im = data37[6]
    # va37_0_re = data37[7]
    # va37_0_im = data37[8]

    # va37_1_re = -22.019240975
    # va37_1_im = -67.0119480817
    # va37_2_re = 2.55176212101
    # va37_2_im = 6.49412356682
    # va37_0_re = 9.08829606037
    # va37_0_im = 11.5209101607

    va37_1 = complex(va37_1_re,va37_1_im)*(345/142.83)
    va37_1_mag = abs(va37_1)/79.67433
    va37_2 = complex(va37_2_re,va37_2_im)*(345/142.83)
    va37_0 = complex(va37_0_re,va37_0_im)*(345/142.83)

    # %%%%%%% bus 38 voltage
    # %0.54,-51.5261770653,-153.222847839,3.49461091354,23.1938291241,17.8841457017,39.3614296488

    data38 = ss38_dataset
    # print("data38 is: {}".format(data38))
    va38_1_re = data38[0]
    va38_1_im = data38[1]
    va38_2_re = data38[2]
    va38_2_im = data38[3]
    va38_0_re = data38[4]
    va38_0_im = data38[5]

    # data38 = ss38_dataset[3]
    # print("data38 is: {}".format(data38))
    # va38_1_re = data38[3]
    # va38_1_im = data38[4]
    # va38_2_re = data38[5]
    # va38_2_im = data38[6]
    # va38_0_re = data38[7]
    # va38_0_im = data38[8]

    # va38_1_re = -45.2195260092
    # va38_1_im = -152.322880038
    # va38_2_re = 7.87096687613
    # va38_2_im = 27.2877926606
    # va38_0_re = 25.6216617923
    # va38_0_im = 43.8927338323

    va38_1 = complex(va38_1_re, va38_1_im)
    va38_1_mag = abs(va38_1)/199.18584
    va38_2 = complex(va38_2_re, va38_2_im)
    va38_0 = complex(va38_0_re, va38_0_im)


    # %%%%%%% bus 65 voltage
    # %0.54,-16.1225787535,-191.962668361,0.200981046269,4.77625827918,-0.827590499322,3.07543614249

    data65 = ss65_dataset
    # print("data65 is: {}".format(data65))
    va65_1_re = data65[0]
    va65_1_im = data65[1]
    va65_2_re = data65[2]
    va65_2_im = data65[3]
    va65_0_re = data65[4]
    va65_0_im = data65[5]

    # data65 = ss65_dataset[3]
    # print("data65 is: {}".format(data65))
    # va65_1_re = data65[3]
    # va65_1_im = data65[4]
    # va65_2_re = data65[5]
    # va65_2_im = data65[6]
    # va65_0_re = data65[7]
    # va65_0_im = data65[8]

    # va65_1_re = -16.4416491016
    # va65_1_im = -191.876483156
    # va65_2_re = 0.917102907633
    # va65_2_im = 5.88654870358
    # va65_0_re = -0.623428133184
    # va65_0_im = 3.71598605538

    va65_1 = complex(va65_1_re, va65_1_im)
    va65_1_mag = abs(va65_1)/199.18584
    va65_2 = complex(va65_2_re, va65_2_im)
    va65_0 = complex(va65_0_re, va65_0_im)

    t2 = time.perf_counter_ns()

    ############### FDA execution


    bus_dict = {
                va26_1_mag : 'Bus 26',
                va30_1_mag : 'Bus 30',
                va08_1_mag : 'Bus 08',
                va17_1_mag : 'Bus 17',
                va37_1_mag : 'Bus 37',
                va38_1_mag : 'Bus 38',
                va65_1_mag : 'Bus 65'
    }

    pos_mag_bus_vol = [
                       va26_1_mag,
                       va30_1_mag,
                       va08_1_mag,
                       va17_1_mag,
                       va37_1_mag,
                       va38_1_mag,
                       va65_1_mag  
                    ]
    
    
    fault_count = 0
    
    for i in pos_mag_bus_vol:
        if i < 0.95:
            fault_count = fault_count + 1
            # print("Fault detected at {}". format(bus_dict[i]))
    
    if fault_count > 4:
        # print("Fault observed by {} buses. Hence, FDA votes 1".format(fault_count))
        FDA = 1
    else:
        # print("Fault observed by {} buses. Hence, FDA votes 0".format(fault_count))
        FDA = 0

    t3 = time.perf_counter_ns()

    ############### FCA execution
    #%%%%%%%%%%%%%% current calculation 17 to 30 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    ia1730_1 = (va17_1 - va30_1)/x1_1730
    ia1730_2 = (va17_2 - va30_2)/x2_1730
    ia1730_0 = (va17_0 - va30_0)/x0_1730

    #%%%%%%%%%%%%% current calculation 26 to 30 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    ia2630_1 = ((va26_1 - va30_1)/z_dash1_2630) - va30_1*y_dash_by_2_1_2630
    ia2630_2 = ((va26_2 - va30_2)/z_dash1_2630) - va30_2*y_dash_by_2_1_2630
    ia2630_0 = ((va26_0 - va30_0)/z_dash0_2630) - va30_0*y_dash_by_2_0_2630

    #%%%%%%%%%%%% current calculation 08 to 30 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%    
    ia0830_1 = ((va08_1 - va30_1)/z_dash1_0830) - va30_1*y_dash_by_2_1_0830
    ia0830_2 = ((va08_2 - va30_2)/z_dash1_0830) - va30_2*y_dash_by_2_1_0830
    ia0830_0 = ((va08_0 - va30_0)/z_dash0_0830) - va30_0*y_dash_by_2_0_0830
   
    #%%%%%%%%%% current summation %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    ia_1_30_ic = ia1730_1 + ia2630_1 + ia0830_1
    ia_2_30_ic = ia1730_2 + ia2630_2 + ia0830_2
    ia_0_30_ic = ia1730_0 + ia2630_0 + ia0830_0

    ##### ia30 and va30 calculation
    ia_30_ic = ia_1_30_ic + ia_2_30_ic + ia_0_30_ic
    va30 = va30_1 + va30_2 + va30_0
    
    ##### impedance calculation
    z30 = va30/((ia_30_ic + 1.6893*ia_0_30_ic)*Zc1_3038)
    dist_30 = (1/g1_3038)*cmath.atanh(z30)
    zberg_30 = z1_3038*zbase*dist_30
    zline = z1_3038*zbase*L
    fault_dist_from_30  = ((zberg_30).imag/(zline).imag)*100
    

    
    # %%%%%%%%%%%%%% current calculation 37 to 38 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    ia3738_1 = (va37_1 - va38_1)/x1_3738
    ia3738_2 = (va37_2 - va38_2)/x2_3738
    ia3738_0 = (va37_0 - va38_0)/x0_3738


    # %%%%%%%%%%%%% current calculation 65 to 38 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    ia6538_1 = ((va65_1 - va38_1)/z_dash1_6538) - va38_1*y_dash_by_2_1_6538
    ia6538_2 = ((va65_2 - va38_2)/z_dash1_6538) - va38_2*y_dash_by_2_1_6538
    ia6538_0 = ((va65_0 - va38_0)/z_dash0_6538) - va38_0*y_dash_by_2_0_6538


    # %%%%%%%%%% current summation %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    ia_1_38_ic = ia6538_1 + ia3738_1
    ia_2_38_ic = ia6538_2 + ia3738_2
    ia_0_38_ic = ia6538_0 + ia3738_0

    
    t4 = time.perf_counter_ns()

    ##### ia38 and va38 calculation
    ia_38_ic = ia_1_38_ic + ia_2_38_ic + ia_0_38_ic
    va38 = va38_1 + va38_2 + va38_0; 


    ##### impedance calculation
    z38 = va38/((ia_38_ic + 1.6893*ia_0_38_ic)*Zc1_3830)
    dist_38 = (1/g1_3830)*cmath.atanh(z38)
    zberg_38 = z1_3830*zbase*dist_38
    zline = z1_3830*zbase*L
    fault_dist_from_38  = (((zberg_38).imag)/((zline).imag))*100

    t5 = time.perf_counter_ns()
    
    exec_time = (t2 - t1) + 27*(t3-t2) + (t4 - t3) + 6*(t5-t4)
    
    exec_time_array.append(exec_time)
    print("FDA = {}".format(FDA))
    print("Fault distance from bus 30: {}".format(fault_dist_from_30))
    print("Fault distance from bus 38: {}".format(fault_dist_from_38))
    print("Voltage read time from memory: {}".format(t2-t1))
    print("FDA execution time: {}".format(27*(t3-t2)))
    print("Current estimation time: {}".format(t4-t3))
    print("FCA execution time: {}".format(6*(t5-t4)))    
    print("Total execution time in nanosec: {}".format(exec_time))

    return exec_time_array