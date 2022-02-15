import time
import cmath
import math


def sfva(ss8_dataset, ss26_dataset, ss17_dataset,
         ss30_dataset, ss38_dataset, ss37_dataset,
         ss65_dataset):

    t3 = time.perf_counter_ns()
    
    ####################bus 26 data
    
    va26_1_re = -78.1044890236
    va26_1_im = -151.493586093
    va26_2_re = 4.35542605871
    va26_2_im = 17.0979516936
    va26_0_re = 15.7567836535
    va26_0_im = 22.5999966622

    va26_1 = complex(va26_1_re,va26_1_im)
    va26_2 = complex(va26_2_re,va26_2_im)
    va26_0 = complex(va26_0_re,va26_0_im)

    ##################### bus 30 data
    
    va30_1_re = -75.8693271986
    va30_1_im = -137.323010883
    va30_2_re = 4.93128358009
    va30_2_im = 24.4873283626
    va30_0_re = 20.5127913535
    va30_0_im = 38.544720748

    va30_1 = complex(va30_1_re,va30_1_im)
    va30_2 = complex(va30_2_re,va30_2_im)
    va30_0 = complex(va30_0_re,va30_0_im)

    va30 = va30_1 + va30_2 + va30_0

    ######################## bus 08 data
    va08_1_re = -86.7108142611
    va08_1_im = -133.498889352
    va08_2_re = 6.52982317905
    va08_2_im = 18.0985055825
    va08_0_re = 16.5237979745
    va08_0_im = 19.9964231992

    va08_1 = complex(va08_1_re,va08_1_im)
    va08_2 = complex(va08_2_re,va08_2_im)
    va08_0 = complex(va08_0_re,va08_0_im)

    ######################## bus 17 data
    va17_1_re = -32.1604343812
    va17_1_im = -58.3697997785
    va17_2_re = 2.19081136642
    va17_2_im = 8.65866169555
    va17_0_re = 8.76658282709
    va17_0_im = 14.3648919985

    va17_1 = complex(va17_1_re,va17_1_im)*(345/143.52)
    va17_2 = complex(va17_2_re,va17_2_im)*(345/143.52)
    va17_0 = complex(va17_0_re,va17_0_im)*(345/143.52)

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



    #%%%%%%% Transformer between 17 and 30 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    x1_pu_1730 = complex(0,0.01)
    x1_1730 = x1_pu_1730*zbase

    x2_1730 = x1_1730
    x0_1730 = x1_1730


    t1 = time.time_ns()

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

    ia_30_ic = ia_1_30_ic + ia_2_30_ic + ia_0_30_ic


    #%%%%%%%% line parameters 30 to 38 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    va30 = va30_1 + va30_2 + va30_0
    r1_3038 = 0.00464
    x1_3038 = 0.054
    b1_3038 = 0.422
    z1_3038 = complex(r1_3038,x1_3038)
    y1_3038 = complex(0,b1_3038)
    Zc1_3038_pu = cmath.sqrt(z1_3038/y1_3038)
    Zc1_3038 = zbase * Zc1_3038_pu
    g1_3038 = cmath.sqrt(y1_3038 * z1_3038)
    L = 1
    z30 = va30/((ia_30_ic + 1.6893*ia_0_30_ic)*Zc1_3038)

    t6 = time.perf_counter_ns()
    dist_30 = (1/g1_3038)*cmath.atanh(z30)
    p = cmath.atanh(z30)
    q = cmath.log(((1+z30)*cmath.sqrt(1/(1-(z30*z30)))))
    r = 0.5*cmath.log((1 + z30)/(1 - z30))

    print("p = {}".format(p))
    print("q = {}".format(q))
    print("r = {}".format(r))
    t7 = time.perf_counter_ns()

    zberg_30 = z1_3038*zbase*dist_30

    zline = z1_3038*zbase*L
    fault_dist_from_30  = ((zberg_30).imag/(zline).imag)*100
    t2 = time.perf_counter_ns()
    t4 = time.perf_counter_ns()
    j = 0
    for i in range(1,8):
        x = 5;
        arr = [2, 1, 1, 6, 7, 8, 9]
        for k in range(len(arr)):
            if arr[k] > 0.8:
                j = j + 1
    t5 = time.perf_counter_ns()
    print(k)
    print(fault_dist_from_30)
    print(t3)
    print(t2)
    print(t4)
    print(t5)
    print(t2 - t3)
    print("Total execution time in nanosec: {}".format(t5 - t3))
    print(t7 - t6)
    print("z30 = {} ".format(z30))
