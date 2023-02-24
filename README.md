# pyxfoil
Run XFoil from within Python and work with output results.

See example below:

#
``` python
# Import Dependencies
from pyxfoil import Xfoil, set_workdir
set_workdir('C:/Xfoil_WIP') # Sets the working directory for pyxfoil
```

#
``` python
# Creates Xfoil object from reading dat file.
xfoil = Xfoil('NACA 0012')
xfoil.points_from_dat('../files/NACA_0012_180.dat')
xfoil.set_ppar(180)
```

#
``` python
# Runs xfoil for the following parameters
al = [-2.0, 0.0, 4.0, 6.0]
mach = 0.1
re = 100000.0
for ali in al:
    rescase = xfoil.run_result(ali, mach=mach, re=re)
```

#
``` python
# Plots xfoil airfoil profile
ax1 = xfoil.plot_profile(ls='-')
```

<svg xmlns:xlink="http://www.w3.org/1999/xlink" width="721.645312pt" height="126.554946pt" viewBox="0 0 721.645312 126.554946" xmlns="http://www.w3.org/2000/svg" version="1.1">
 <metadata>
  <rdf:RDF xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:cc="http://creativecommons.org/ns#" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
   <cc:Work>
    <dc:type rdf:resource="http://purl.org/dc/dcmitype/StillImage"/>
    <dc:date>2023-02-24T16:11:40.613316</dc:date>
    <dc:format>image/svg+xml</dc:format>
    <dc:creator>
     <cc:Agent>
      <dc:title>Matplotlib v3.6.2, https://matplotlib.org/</dc:title>
     </cc:Agent>
    </dc:creator>
   </cc:Work>
  </rdf:RDF>
 </metadata>
 <defs>
  <style type="text/css">*{stroke-linejoin: round; stroke-linecap: butt}</style>
 </defs>
 <g id="figure_1">
  <g id="patch_1">
   <path d="M 0 126.554946
L 721.645312 126.554946
L 721.645312 0
L 0 0
z
" style="fill: #ffffff"/>
  </g>
  <g id="axes_1">
   <g id="patch_2">
    <path d="M 44.845313 102.676821
L 714.445312 102.676821
L 714.445312 22.318125
L 44.845313 22.318125
z
" style="fill: #ffffff"/>
   </g>
   <g id="matplotlib.axis_1">
    <g id="xtick_1">
     <g id="line2d_1">
      <path d="M 75.281676 102.676821
L 75.281676 22.318125
" clip-path="url(#p515bfc4500)" style="fill: none; stroke: #b0b0b0; stroke-width: 0.8; stroke-linecap: square"/>
     </g>
     <g id="line2d_2">
      <defs>
       <path id="m5e3366256d" d="M 0 0
L 0 3.5
" style="stroke: #000000; stroke-width: 0.8"/>
      </defs>
      <g>
       <use xlink:href="#m5e3366256d" x="75.281676" y="102.676821" style="stroke: #000000; stroke-width: 0.8"/>
      </g>
     </g>
     <g id="text_1">
      <!-- 0.0 -->
      <g transform="translate(67.330114 117.275258) scale(0.1 -0.1)">
       <defs>
        <path id="DejaVuSans-30" d="M 2034 4250
Q 1547 4250 1301 3770
Q 1056 3291 1056 2328
Q 1056 1369 1301 889
Q 1547 409 2034 409
Q 2525 409 2770 889
Q 3016 1369 3016 2328
Q 3016 3291 2770 3770
Q 2525 4250 2034 4250
z
M 2034 4750
Q 2819 4750 3233 4129
Q 3647 3509 3647 2328
Q 3647 1150 3233 529
Q 2819 -91 2034 -91
Q 1250 -91 836 529
Q 422 1150 422 2328
Q 422 3509 836 4129
Q 1250 4750 2034 4750
z
" transform="scale(0.015625)"/>
        <path id="DejaVuSans-2e" d="M 684 794
L 1344 794
L 1344 0
L 684 0
L 684 794
z
" transform="scale(0.015625)"/>
       </defs>
       <use xlink:href="#DejaVuSans-30"/>
       <use xlink:href="#DejaVuSans-2e" x="63.623047"/>
       <use xlink:href="#DejaVuSans-30" x="95.410156"/>
      </g>
     </g>
    </g>
    <g id="xtick_2">
     <g id="line2d_3">
      <path d="M 197.027131 102.676821
L 197.027131 22.318125
" clip-path="url(#p515bfc4500)" style="fill: none; stroke: #b0b0b0; stroke-width: 0.8; stroke-linecap: square"/>
     </g>
     <g id="line2d_4">
      <g>
       <use xlink:href="#m5e3366256d" x="197.027131" y="102.676821" style="stroke: #000000; stroke-width: 0.8"/>
      </g>
     </g>
     <g id="text_2">
      <!-- 0.2 -->
      <g transform="translate(189.075568 117.275258) scale(0.1 -0.1)">
       <defs>
        <path id="DejaVuSans-32" d="M 1228 531
L 3431 531
L 3431 0
L 469 0
L 469 531
Q 828 903 1448 1529
Q 2069 2156 2228 2338
Q 2531 2678 2651 2914
Q 2772 3150 2772 3378
Q 2772 3750 2511 3984
Q 2250 4219 1831 4219
Q 1534 4219 1204 4116
Q 875 4013 500 3803
L 500 4441
Q 881 4594 1212 4672
Q 1544 4750 1819 4750
Q 2544 4750 2975 4387
Q 3406 4025 3406 3419
Q 3406 3131 3298 2873
Q 3191 2616 2906 2266
Q 2828 2175 2409 1742
Q 1991 1309 1228 531
z
" transform="scale(0.015625)"/>
       </defs>
       <use xlink:href="#DejaVuSans-30"/>
       <use xlink:href="#DejaVuSans-2e" x="63.623047"/>
       <use xlink:href="#DejaVuSans-32" x="95.410156"/>
      </g>
     </g>
    </g>
    <g id="xtick_3">
     <g id="line2d_5">
      <path d="M 318.772585 102.676821
L 318.772585 22.318125
" clip-path="url(#p515bfc4500)" style="fill: none; stroke: #b0b0b0; stroke-width: 0.8; stroke-linecap: square"/>
     </g>
     <g id="line2d_6">
      <g>
       <use xlink:href="#m5e3366256d" x="318.772585" y="102.676821" style="stroke: #000000; stroke-width: 0.8"/>
      </g>
     </g>
     <g id="text_3">
      <!-- 0.4 -->
      <g transform="translate(310.821023 117.275258) scale(0.1 -0.1)">
       <defs>
        <path id="DejaVuSans-34" d="M 2419 4116
L 825 1625
L 2419 1625
L 2419 4116
z
M 2253 4666
L 3047 4666
L 3047 1625
L 3713 1625
L 3713 1100
L 3047 1100
L 3047 0
L 2419 0
L 2419 1100
L 313 1100
L 313 1709
L 2253 4666
z
" transform="scale(0.015625)"/>
       </defs>
       <use xlink:href="#DejaVuSans-30"/>
       <use xlink:href="#DejaVuSans-2e" x="63.623047"/>
       <use xlink:href="#DejaVuSans-34" x="95.410156"/>
      </g>
     </g>
    </g>
    <g id="xtick_4">
     <g id="line2d_7">
      <path d="M 440.51804 102.676821
L 440.51804 22.318125
" clip-path="url(#p515bfc4500)" style="fill: none; stroke: #b0b0b0; stroke-width: 0.8; stroke-linecap: square"/>
     </g>
     <g id="line2d_8">
      <g>
       <use xlink:href="#m5e3366256d" x="440.51804" y="102.676821" style="stroke: #000000; stroke-width: 0.8"/>
      </g>
     </g>
     <g id="text_4">
      <!-- 0.6 -->
      <g transform="translate(432.566477 117.275258) scale(0.1 -0.1)">
       <defs>
        <path id="DejaVuSans-36" d="M 2113 2584
Q 1688 2584 1439 2293
Q 1191 2003 1191 1497
Q 1191 994 1439 701
Q 1688 409 2113 409
Q 2538 409 2786 701
Q 3034 994 3034 1497
Q 3034 2003 2786 2293
Q 2538 2584 2113 2584
z
M 3366 4563
L 3366 3988
Q 3128 4100 2886 4159
Q 2644 4219 2406 4219
Q 1781 4219 1451 3797
Q 1122 3375 1075 2522
Q 1259 2794 1537 2939
Q 1816 3084 2150 3084
Q 2853 3084 3261 2657
Q 3669 2231 3669 1497
Q 3669 778 3244 343
Q 2819 -91 2113 -91
Q 1303 -91 875 529
Q 447 1150 447 2328
Q 447 3434 972 4092
Q 1497 4750 2381 4750
Q 2619 4750 2861 4703
Q 3103 4656 3366 4563
z
" transform="scale(0.015625)"/>
       </defs>
       <use xlink:href="#DejaVuSans-30"/>
       <use xlink:href="#DejaVuSans-2e" x="63.623047"/>
       <use xlink:href="#DejaVuSans-36" x="95.410156"/>
      </g>
     </g>
    </g>
    <g id="xtick_5">
     <g id="line2d_9">
      <path d="M 562.263494 102.676821
L 562.263494 22.318125
" clip-path="url(#p515bfc4500)" style="fill: none; stroke: #b0b0b0; stroke-width: 0.8; stroke-linecap: square"/>
     </g>
     <g id="line2d_10">
      <g>
       <use xlink:href="#m5e3366256d" x="562.263494" y="102.676821" style="stroke: #000000; stroke-width: 0.8"/>
      </g>
     </g>
     <g id="text_5">
      <!-- 0.8 -->
      <g transform="translate(554.311932 117.275258) scale(0.1 -0.1)">
       <defs>
        <path id="DejaVuSans-38" d="M 2034 2216
Q 1584 2216 1326 1975
Q 1069 1734 1069 1313
Q 1069 891 1326 650
Q 1584 409 2034 409
Q 2484 409 2743 651
Q 3003 894 3003 1313
Q 3003 1734 2745 1975
Q 2488 2216 2034 2216
z
M 1403 2484
Q 997 2584 770 2862
Q 544 3141 544 3541
Q 544 4100 942 4425
Q 1341 4750 2034 4750
Q 2731 4750 3128 4425
Q 3525 4100 3525 3541
Q 3525 3141 3298 2862
Q 3072 2584 2669 2484
Q 3125 2378 3379 2068
Q 3634 1759 3634 1313
Q 3634 634 3220 271
Q 2806 -91 2034 -91
Q 1263 -91 848 271
Q 434 634 434 1313
Q 434 1759 690 2068
Q 947 2378 1403 2484
z
M 1172 3481
Q 1172 3119 1398 2916
Q 1625 2713 2034 2713
Q 2441 2713 2670 2916
Q 2900 3119 2900 3481
Q 2900 3844 2670 4047
Q 2441 4250 2034 4250
Q 1625 4250 1398 4047
Q 1172 3844 1172 3481
z
" transform="scale(0.015625)"/>
       </defs>
       <use xlink:href="#DejaVuSans-30"/>
       <use xlink:href="#DejaVuSans-2e" x="63.623047"/>
       <use xlink:href="#DejaVuSans-38" x="95.410156"/>
      </g>
     </g>
    </g>
    <g id="xtick_6">
     <g id="line2d_11">
      <path d="M 684.008949 102.676821
L 684.008949 22.318125
" clip-path="url(#p515bfc4500)" style="fill: none; stroke: #b0b0b0; stroke-width: 0.8; stroke-linecap: square"/>
     </g>
     <g id="line2d_12">
      <g>
       <use xlink:href="#m5e3366256d" x="684.008949" y="102.676821" style="stroke: #000000; stroke-width: 0.8"/>
      </g>
     </g>
     <g id="text_6">
      <!-- 1.0 -->
      <g transform="translate(676.057386 117.275258) scale(0.1 -0.1)">
       <defs>
        <path id="DejaVuSans-31" d="M 794 531
L 1825 531
L 1825 4091
L 703 3866
L 703 4441
L 1819 4666
L 2450 4666
L 2450 531
L 3481 531
L 3481 0
L 794 0
L 794 531
z
" transform="scale(0.015625)"/>
       </defs>
       <use xlink:href="#DejaVuSans-31"/>
       <use xlink:href="#DejaVuSans-2e" x="63.623047"/>
       <use xlink:href="#DejaVuSans-30" x="95.410156"/>
      </g>
     </g>
    </g>
   </g>
   <g id="matplotlib.axis_2">
    <g id="ytick_1">
     <g id="line2d_13">
      <path d="M 44.845313 92.933837
L 714.445312 92.933837
" clip-path="url(#p515bfc4500)" style="fill: none; stroke: #b0b0b0; stroke-width: 0.8; stroke-linecap: square"/>
     </g>
     <g id="line2d_14">
      <defs>
       <path id="m577a9256be" d="M 0 0
L -3.5 0
" style="stroke: #000000; stroke-width: 0.8"/>
      </defs>
      <g>
       <use xlink:href="#m577a9256be" x="44.845313" y="92.933837" style="stroke: #000000; stroke-width: 0.8"/>
      </g>
     </g>
     <g id="text_7">
      <!-- −0.05 -->
      <g transform="translate(7.2 96.733055) scale(0.1 -0.1)">
       <defs>
        <path id="DejaVuSans-2212" d="M 678 2272
L 4684 2272
L 4684 1741
L 678 1741
L 678 2272
z
" transform="scale(0.015625)"/>
        <path id="DejaVuSans-35" d="M 691 4666
L 3169 4666
L 3169 4134
L 1269 4134
L 1269 2991
Q 1406 3038 1543 3061
Q 1681 3084 1819 3084
Q 2600 3084 3056 2656
Q 3513 2228 3513 1497
Q 3513 744 3044 326
Q 2575 -91 1722 -91
Q 1428 -91 1123 -41
Q 819 9 494 109
L 494 744
Q 775 591 1075 516
Q 1375 441 1709 441
Q 2250 441 2565 725
Q 2881 1009 2881 1497
Q 2881 1984 2565 2268
Q 2250 2553 1709 2553
Q 1456 2553 1204 2497
Q 953 2441 691 2322
L 691 4666
z
" transform="scale(0.015625)"/>
       </defs>
       <use xlink:href="#DejaVuSans-2212"/>
       <use xlink:href="#DejaVuSans-30" x="83.789062"/>
       <use xlink:href="#DejaVuSans-2e" x="147.412109"/>
       <use xlink:href="#DejaVuSans-30" x="179.199219"/>
       <use xlink:href="#DejaVuSans-35" x="242.822266"/>
      </g>
     </g>
    </g>
    <g id="ytick_2">
     <g id="line2d_15">
      <path d="M 44.845313 62.497473
L 714.445312 62.497473
" clip-path="url(#p515bfc4500)" style="fill: none; stroke: #b0b0b0; stroke-width: 0.8; stroke-linecap: square"/>
     </g>
     <g id="line2d_16">
      <g>
       <use xlink:href="#m577a9256be" x="44.845313" y="62.497473" style="stroke: #000000; stroke-width: 0.8"/>
      </g>
     </g>
     <g id="text_8">
      <!-- 0.00 -->
      <g transform="translate(15.579688 66.296692) scale(0.1 -0.1)">
       <use xlink:href="#DejaVuSans-30"/>
       <use xlink:href="#DejaVuSans-2e" x="63.623047"/>
       <use xlink:href="#DejaVuSans-30" x="95.410156"/>
       <use xlink:href="#DejaVuSans-30" x="159.033203"/>
      </g>
     </g>
    </g>
    <g id="ytick_3">
     <g id="line2d_17">
      <path d="M 44.845313 32.061109
L 714.445312 32.061109
" clip-path="url(#p515bfc4500)" style="fill: none; stroke: #b0b0b0; stroke-width: 0.8; stroke-linecap: square"/>
     </g>
     <g id="line2d_18">
      <g>
       <use xlink:href="#m577a9256be" x="44.845313" y="32.061109" style="stroke: #000000; stroke-width: 0.8"/>
      </g>
     </g>
     <g id="text_9">
      <!-- 0.05 -->
      <g transform="translate(15.579688 35.860328) scale(0.1 -0.1)">
       <use xlink:href="#DejaVuSans-30"/>
       <use xlink:href="#DejaVuSans-2e" x="63.623047"/>
       <use xlink:href="#DejaVuSans-30" x="95.410156"/>
       <use xlink:href="#DejaVuSans-35" x="159.033203"/>
      </g>
     </g>
    </g>
   </g>
   <g id="line2d_19">
    <path d="M 684.008949 62.497473
L 653.205523 58.162117
L 625.880364 54.540799
L 598.586251 51.117317
L 567.030438 47.387036
L 531.827131 43.502747
L 503.440961 40.582074
L 473.698546 37.730795
L 442.926165 35.019524
L 411.459835 32.523133
L 390.267603 31.016533
L 369.023022 29.663333
L 347.83079 28.486663
L 326.793176 27.509656
L 306.013053 26.755442
L 285.592079 26.243503
L 265.628868 25.993316
L 246.220817 26.019491
L 227.463494 26.334812
L 209.447602 26.947192
L 192.260187 27.8615
L 175.986472 29.077737
L 160.704374 30.590424
L 146.489375 32.390431
L 133.410261 34.466191
L 127.316292 35.602685
L 121.530339 36.801269
L 116.05849 38.060117
L 110.908049 39.376794
L 106.085102 40.748256
L 101.59513 42.172678
L 97.444219 43.647016
L 93.637238 45.168834
L 90.17845 46.735698
L 87.072115 48.344564
L 84.322494 49.993606
L 81.93263 51.680389
L 79.905569 53.403088
L 78.243743 55.159874
L 76.94898 56.949533
L 76.023106 58.769018
L 75.467338 60.618941
L 75.281676 62.497473
L 75.467338 64.376005
L 76.023106 66.225928
L 76.94898 68.045413
L 78.243743 69.835072
L 79.905569 71.591858
L 81.93263 73.314557
L 84.322494 75.00134
L 87.072115 76.650382
L 90.17845 78.259248
L 93.637238 79.826112
L 97.444219 81.34793
L 101.59513 82.822268
L 106.085102 84.24669
L 110.908049 85.618152
L 116.05849 86.934829
L 121.530339 88.193677
L 127.316292 89.392261
L 133.410261 90.528755
L 139.803723 91.600115
L 153.459302 93.53952
L 168.216678 95.197693
L 184.004019 96.563069
L 200.744628 97.628341
L 218.356934 98.391685
L 236.755107 98.854927
L 255.849665 99.024153
L 275.546862 98.910321
L 295.751128 98.526823
L 316.36446 97.891312
L 337.285808 97.023266
L 358.414123 95.943384
L 379.645313 94.676014
L 400.876502 93.242461
L 432.497449 90.834945
L 463.539497 88.186981
L 493.661757 85.374661
L 522.535518 82.469206
L 549.843023 79.540619
L 583.304152 75.71416
L 612.80125 72.117799
L 643.232135 68.178116
L 672.21851 64.189735
L 684.008949 62.497473
L 684.008949 62.497473
" clip-path="url(#p515bfc4500)" style="fill: none; stroke: #1f77b4; stroke-width: 1.5; stroke-linecap: square"/>
   </g>
   <g id="patch_3">
    <path d="M 44.845313 102.676821
L 44.845313 22.318125
" style="fill: none; stroke: #000000; stroke-width: 0.8; stroke-linejoin: miter; stroke-linecap: square"/>
   </g>
   <g id="patch_4">
    <path d="M 714.445312 102.676821
L 714.445312 22.318125
" style="fill: none; stroke: #000000; stroke-width: 0.8; stroke-linejoin: miter; stroke-linecap: square"/>
   </g>
   <g id="patch_5">
    <path d="M 44.845313 102.676821
L 714.445313 102.676821
" style="fill: none; stroke: #000000; stroke-width: 0.8; stroke-linejoin: miter; stroke-linecap: square"/>
   </g>
   <g id="patch_6">
    <path d="M 44.845313 22.318125
L 714.445313 22.318125
" style="fill: none; stroke: #000000; stroke-width: 0.8; stroke-linejoin: miter; stroke-linecap: square"/>
   </g>
   <g id="text_10">
    <!-- Airfoil profile for NACA_0012_180. -->
    <g transform="translate(277.958438 16.318125) scale(0.12 -0.12)">
     <defs>
      <path id="DejaVuSans-41" d="M 2188 4044
L 1331 1722
L 3047 1722
L 2188 4044
z
M 1831 4666
L 2547 4666
L 4325 0
L 3669 0
L 3244 1197
L 1141 1197
L 716 0
L 50 0
L 1831 4666
z
" transform="scale(0.015625)"/>
      <path id="DejaVuSans-69" d="M 603 3500
L 1178 3500
L 1178 0
L 603 0
L 603 3500
z
M 603 4863
L 1178 4863
L 1178 4134
L 603 4134
L 603 4863
z
" transform="scale(0.015625)"/>
      <path id="DejaVuSans-72" d="M 2631 2963
Q 2534 3019 2420 3045
Q 2306 3072 2169 3072
Q 1681 3072 1420 2755
Q 1159 2438 1159 1844
L 1159 0
L 581 0
L 581 3500
L 1159 3500
L 1159 2956
Q 1341 3275 1631 3429
Q 1922 3584 2338 3584
Q 2397 3584 2469 3576
Q 2541 3569 2628 3553
L 2631 2963
z
" transform="scale(0.015625)"/>
      <path id="DejaVuSans-66" d="M 2375 4863
L 2375 4384
L 1825 4384
Q 1516 4384 1395 4259
Q 1275 4134 1275 3809
L 1275 3500
L 2222 3500
L 2222 3053
L 1275 3053
L 1275 0
L 697 0
L 697 3053
L 147 3053
L 147 3500
L 697 3500
L 697 3744
Q 697 4328 969 4595
Q 1241 4863 1831 4863
L 2375 4863
z
" transform="scale(0.015625)"/>
      <path id="DejaVuSans-6f" d="M 1959 3097
Q 1497 3097 1228 2736
Q 959 2375 959 1747
Q 959 1119 1226 758
Q 1494 397 1959 397
Q 2419 397 2687 759
Q 2956 1122 2956 1747
Q 2956 2369 2687 2733
Q 2419 3097 1959 3097
z
M 1959 3584
Q 2709 3584 3137 3096
Q 3566 2609 3566 1747
Q 3566 888 3137 398
Q 2709 -91 1959 -91
Q 1206 -91 779 398
Q 353 888 353 1747
Q 353 2609 779 3096
Q 1206 3584 1959 3584
z
" transform="scale(0.015625)"/>
      <path id="DejaVuSans-6c" d="M 603 4863
L 1178 4863
L 1178 0
L 603 0
L 603 4863
z
" transform="scale(0.015625)"/>
      <path id="DejaVuSans-20" transform="scale(0.015625)"/>
      <path id="DejaVuSans-70" d="M 1159 525
L 1159 -1331
L 581 -1331
L 581 3500
L 1159 3500
L 1159 2969
Q 1341 3281 1617 3432
Q 1894 3584 2278 3584
Q 2916 3584 3314 3078
Q 3713 2572 3713 1747
Q 3713 922 3314 415
Q 2916 -91 2278 -91
Q 1894 -91 1617 61
Q 1341 213 1159 525
z
M 3116 1747
Q 3116 2381 2855 2742
Q 2594 3103 2138 3103
Q 1681 3103 1420 2742
Q 1159 2381 1159 1747
Q 1159 1113 1420 752
Q 1681 391 2138 391
Q 2594 391 2855 752
Q 3116 1113 3116 1747
z
" transform="scale(0.015625)"/>
      <path id="DejaVuSans-65" d="M 3597 1894
L 3597 1613
L 953 1613
Q 991 1019 1311 708
Q 1631 397 2203 397
Q 2534 397 2845 478
Q 3156 559 3463 722
L 3463 178
Q 3153 47 2828 -22
Q 2503 -91 2169 -91
Q 1331 -91 842 396
Q 353 884 353 1716
Q 353 2575 817 3079
Q 1281 3584 2069 3584
Q 2775 3584 3186 3129
Q 3597 2675 3597 1894
z
M 3022 2063
Q 3016 2534 2758 2815
Q 2500 3097 2075 3097
Q 1594 3097 1305 2825
Q 1016 2553 972 2059
L 3022 2063
z
" transform="scale(0.015625)"/>
      <path id="DejaVuSans-4e" d="M 628 4666
L 1478 4666
L 3547 763
L 3547 4666
L 4159 4666
L 4159 0
L 3309 0
L 1241 3903
L 1241 0
L 628 0
L 628 4666
z
" transform="scale(0.015625)"/>
      <path id="DejaVuSans-43" d="M 4122 4306
L 4122 3641
Q 3803 3938 3442 4084
Q 3081 4231 2675 4231
Q 1875 4231 1450 3742
Q 1025 3253 1025 2328
Q 1025 1406 1450 917
Q 1875 428 2675 428
Q 3081 428 3442 575
Q 3803 722 4122 1019
L 4122 359
Q 3791 134 3420 21
Q 3050 -91 2638 -91
Q 1578 -91 968 557
Q 359 1206 359 2328
Q 359 3453 968 4101
Q 1578 4750 2638 4750
Q 3056 4750 3426 4639
Q 3797 4528 4122 4306
z
" transform="scale(0.015625)"/>
      <path id="DejaVuSans-5f" d="M 3263 -1063
L 3263 -1509
L -63 -1509
L -63 -1063
L 3263 -1063
z
" transform="scale(0.015625)"/>
     </defs>
     <use xlink:href="#DejaVuSans-41"/>
     <use xlink:href="#DejaVuSans-69" x="68.408203"/>
     <use xlink:href="#DejaVuSans-72" x="96.191406"/>
     <use xlink:href="#DejaVuSans-66" x="137.304688"/>
     <use xlink:href="#DejaVuSans-6f" x="172.509766"/>
     <use xlink:href="#DejaVuSans-69" x="233.691406"/>
     <use xlink:href="#DejaVuSans-6c" x="261.474609"/>
     <use xlink:href="#DejaVuSans-20" x="289.257812"/>
     <use xlink:href="#DejaVuSans-70" x="321.044922"/>
     <use xlink:href="#DejaVuSans-72" x="384.521484"/>
     <use xlink:href="#DejaVuSans-6f" x="423.384766"/>
     <use xlink:href="#DejaVuSans-66" x="484.566406"/>
     <use xlink:href="#DejaVuSans-69" x="519.771484"/>
     <use xlink:href="#DejaVuSans-6c" x="547.554688"/>
     <use xlink:href="#DejaVuSans-65" x="575.337891"/>
     <use xlink:href="#DejaVuSans-20" x="636.861328"/>
     <use xlink:href="#DejaVuSans-66" x="668.648438"/>
     <use xlink:href="#DejaVuSans-6f" x="703.853516"/>
     <use xlink:href="#DejaVuSans-72" x="765.035156"/>
     <use xlink:href="#DejaVuSans-20" x="806.148438"/>
     <use xlink:href="#DejaVuSans-4e" x="837.935547"/>
     <use xlink:href="#DejaVuSans-41" x="912.740234"/>
     <use xlink:href="#DejaVuSans-43" x="979.398438"/>
     <use xlink:href="#DejaVuSans-41" x="1049.222656"/>
     <use xlink:href="#DejaVuSans-5f" x="1117.630859"/>
     <use xlink:href="#DejaVuSans-30" x="1167.630859"/>
     <use xlink:href="#DejaVuSans-30" x="1231.253906"/>
     <use xlink:href="#DejaVuSans-31" x="1294.876953"/>
     <use xlink:href="#DejaVuSans-32" x="1358.5"/>
     <use xlink:href="#DejaVuSans-5f" x="1422.123047"/>
     <use xlink:href="#DejaVuSans-31" x="1472.123047"/>
     <use xlink:href="#DejaVuSans-38" x="1535.746094"/>
     <use xlink:href="#DejaVuSans-30" x="1599.369141"/>
     <use xlink:href="#DejaVuSans-2e" x="1662.992188"/>
    </g>
   </g>
  </g>
 </g>
 <defs>
  <clipPath id="p515bfc4500">
   <rect x="44.845313" y="22.318125" width="669.6" height="80.358696"/>
  </clipPath>
 </defs>
</svg>


#
``` python
# Shows plots for cases in xfoil cases
ax2 = None
for resname in xfoil.results:
    ax2 = xfoil.results[resname].plot_result(yaxis='cp', ax=ax2, ls='-x')
_ = ax2.legend()
```

<svg xmlns:xlink="http://www.w3.org/1999/xlink" width="728.960937pt" height="503.39625pt" viewBox="0 0 728.960937 503.39625" xmlns="http://www.w3.org/2000/svg" version="1.1">
 <metadata>
  <rdf:RDF xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:cc="http://creativecommons.org/ns#" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
   <cc:Work>
    <dc:type rdf:resource="http://purl.org/dc/dcmitype/StillImage"/>
    <dc:date>2023-02-24T16:11:40.870667</dc:date>
    <dc:format>image/svg+xml</dc:format>
    <dc:creator>
     <cc:Agent>
      <dc:title>Matplotlib v3.6.2, https://matplotlib.org/</dc:title>
     </cc:Agent>
    </dc:creator>
   </cc:Work>
  </rdf:RDF>
 </metadata>
 <defs>
  <style type="text/css">*{stroke-linejoin: round; stroke-linecap: butt}</style>
 </defs>
 <g id="figure_1">
  <g id="patch_1">
   <path d="M 0 503.39625
L 728.960937 503.39625
L 728.960937 0
L 0 0
z
" style="fill: #ffffff"/>
  </g>
  <g id="axes_1">
   <g id="patch_2">
    <path d="M 52.160938 465.84
L 721.760938 465.84
L 721.760938 22.32
L 52.160938 22.32
z
" style="fill: #ffffff"/>
   </g>
   <g id="matplotlib.axis_1">
    <g id="xtick_1">
     <g id="line2d_1">
      <path d="M 82.591214 465.84
L 82.591214 22.32
" clip-path="url(#pfa2ce86669)" style="fill: none; stroke: #b0b0b0; stroke-width: 0.8; stroke-linecap: square"/>
     </g>
     <g id="line2d_2">
      <defs>
       <path id="m3f63193ba4" d="M 0 0
L 0 3.5
" style="stroke: #000000; stroke-width: 0.8"/>
      </defs>
      <g>
       <use xlink:href="#m3f63193ba4" x="82.591214" y="465.84" style="stroke: #000000; stroke-width: 0.8"/>
      </g>
     </g>
     <g id="text_1">
      <!-- 0.00 -->
      <g transform="translate(71.458402 480.438437) scale(0.1 -0.1)">
       <defs>
        <path id="DejaVuSans-30" d="M 2034 4250
Q 1547 4250 1301 3770
Q 1056 3291 1056 2328
Q 1056 1369 1301 889
Q 1547 409 2034 409
Q 2525 409 2770 889
Q 3016 1369 3016 2328
Q 3016 3291 2770 3770
Q 2525 4250 2034 4250
z
M 2034 4750
Q 2819 4750 3233 4129
Q 3647 3509 3647 2328
Q 3647 1150 3233 529
Q 2819 -91 2034 -91
Q 1250 -91 836 529
Q 422 1150 422 2328
Q 422 3509 836 4129
Q 1250 4750 2034 4750
z
" transform="scale(0.015625)"/>
        <path id="DejaVuSans-2e" d="M 684 794
L 1344 794
L 1344 0
L 684 0
L 684 794
z
" transform="scale(0.015625)"/>
       </defs>
       <use xlink:href="#DejaVuSans-30"/>
       <use xlink:href="#DejaVuSans-2e" x="63.623047"/>
       <use xlink:href="#DejaVuSans-30" x="95.410156"/>
       <use xlink:href="#DejaVuSans-30" x="159.033203"/>
      </g>
     </g>
    </g>
    <g id="xtick_2">
     <g id="line2d_3">
      <path d="M 158.67908 465.84
L 158.67908 22.32
" clip-path="url(#pfa2ce86669)" style="fill: none; stroke: #b0b0b0; stroke-width: 0.8; stroke-linecap: square"/>
     </g>
     <g id="line2d_4">
      <g>
       <use xlink:href="#m3f63193ba4" x="158.67908" y="465.84" style="stroke: #000000; stroke-width: 0.8"/>
      </g>
     </g>
     <g id="text_2">
      <!-- 0.25 -->
      <g transform="translate(147.546267 480.438437) scale(0.1 -0.1)">
       <defs>
        <path id="DejaVuSans-32" d="M 1228 531
L 3431 531
L 3431 0
L 469 0
L 469 531
Q 828 903 1448 1529
Q 2069 2156 2228 2338
Q 2531 2678 2651 2914
Q 2772 3150 2772 3378
Q 2772 3750 2511 3984
Q 2250 4219 1831 4219
Q 1534 4219 1204 4116
Q 875 4013 500 3803
L 500 4441
Q 881 4594 1212 4672
Q 1544 4750 1819 4750
Q 2544 4750 2975 4387
Q 3406 4025 3406 3419
Q 3406 3131 3298 2873
Q 3191 2616 2906 2266
Q 2828 2175 2409 1742
Q 1991 1309 1228 531
z
" transform="scale(0.015625)"/>
        <path id="DejaVuSans-35" d="M 691 4666
L 3169 4666
L 3169 4134
L 1269 4134
L 1269 2991
Q 1406 3038 1543 3061
Q 1681 3084 1819 3084
Q 2600 3084 3056 2656
Q 3513 2228 3513 1497
Q 3513 744 3044 326
Q 2575 -91 1722 -91
Q 1428 -91 1123 -41
Q 819 9 494 109
L 494 744
Q 775 591 1075 516
Q 1375 441 1709 441
Q 2250 441 2565 725
Q 2881 1009 2881 1497
Q 2881 1984 2565 2268
Q 2250 2553 1709 2553
Q 1456 2553 1204 2497
Q 953 2441 691 2322
L 691 4666
z
" transform="scale(0.015625)"/>
       </defs>
       <use xlink:href="#DejaVuSans-30"/>
       <use xlink:href="#DejaVuSans-2e" x="63.623047"/>
       <use xlink:href="#DejaVuSans-32" x="95.410156"/>
       <use xlink:href="#DejaVuSans-35" x="159.033203"/>
      </g>
     </g>
    </g>
    <g id="xtick_3">
     <g id="line2d_5">
      <path d="M 234.766945 465.84
L 234.766945 22.32
" clip-path="url(#pfa2ce86669)" style="fill: none; stroke: #b0b0b0; stroke-width: 0.8; stroke-linecap: square"/>
     </g>
     <g id="line2d_6">
      <g>
       <use xlink:href="#m3f63193ba4" x="234.766945" y="465.84" style="stroke: #000000; stroke-width: 0.8"/>
      </g>
     </g>
     <g id="text_3">
      <!-- 0.50 -->
      <g transform="translate(223.634133 480.438437) scale(0.1 -0.1)">
       <use xlink:href="#DejaVuSans-30"/>
       <use xlink:href="#DejaVuSans-2e" x="63.623047"/>
       <use xlink:href="#DejaVuSans-35" x="95.410156"/>
       <use xlink:href="#DejaVuSans-30" x="159.033203"/>
      </g>
     </g>
    </g>
    <g id="xtick_4">
     <g id="line2d_7">
      <path d="M 310.854811 465.84
L 310.854811 22.32
" clip-path="url(#pfa2ce86669)" style="fill: none; stroke: #b0b0b0; stroke-width: 0.8; stroke-linecap: square"/>
     </g>
     <g id="line2d_8">
      <g>
       <use xlink:href="#m3f63193ba4" x="310.854811" y="465.84" style="stroke: #000000; stroke-width: 0.8"/>
      </g>
     </g>
     <g id="text_4">
      <!-- 0.75 -->
      <g transform="translate(299.721998 480.438437) scale(0.1 -0.1)">
       <defs>
        <path id="DejaVuSans-37" d="M 525 4666
L 3525 4666
L 3525 4397
L 1831 0
L 1172 0
L 2766 4134
L 525 4134
L 525 4666
z
" transform="scale(0.015625)"/>
       </defs>
       <use xlink:href="#DejaVuSans-30"/>
       <use xlink:href="#DejaVuSans-2e" x="63.623047"/>
       <use xlink:href="#DejaVuSans-37" x="95.410156"/>
       <use xlink:href="#DejaVuSans-35" x="159.033203"/>
      </g>
     </g>
    </g>
    <g id="xtick_5">
     <g id="line2d_9">
      <path d="M 386.942676 465.84
L 386.942676 22.32
" clip-path="url(#pfa2ce86669)" style="fill: none; stroke: #b0b0b0; stroke-width: 0.8; stroke-linecap: square"/>
     </g>
     <g id="line2d_10">
      <g>
       <use xlink:href="#m3f63193ba4" x="386.942676" y="465.84" style="stroke: #000000; stroke-width: 0.8"/>
      </g>
     </g>
     <g id="text_5">
      <!-- 1.00 -->
      <g transform="translate(375.809864 480.438437) scale(0.1 -0.1)">
       <defs>
        <path id="DejaVuSans-31" d="M 794 531
L 1825 531
L 1825 4091
L 703 3866
L 703 4441
L 1819 4666
L 2450 4666
L 2450 531
L 3481 531
L 3481 0
L 794 0
L 794 531
z
" transform="scale(0.015625)"/>
       </defs>
       <use xlink:href="#DejaVuSans-31"/>
       <use xlink:href="#DejaVuSans-2e" x="63.623047"/>
       <use xlink:href="#DejaVuSans-30" x="95.410156"/>
       <use xlink:href="#DejaVuSans-30" x="159.033203"/>
      </g>
     </g>
    </g>
    <g id="xtick_6">
     <g id="line2d_11">
      <path d="M 463.030542 465.84
L 463.030542 22.32
" clip-path="url(#pfa2ce86669)" style="fill: none; stroke: #b0b0b0; stroke-width: 0.8; stroke-linecap: square"/>
     </g>
     <g id="line2d_12">
      <g>
       <use xlink:href="#m3f63193ba4" x="463.030542" y="465.84" style="stroke: #000000; stroke-width: 0.8"/>
      </g>
     </g>
     <g id="text_6">
      <!-- 1.25 -->
      <g transform="translate(451.897729 480.438437) scale(0.1 -0.1)">
       <use xlink:href="#DejaVuSans-31"/>
       <use xlink:href="#DejaVuSans-2e" x="63.623047"/>
       <use xlink:href="#DejaVuSans-32" x="95.410156"/>
       <use xlink:href="#DejaVuSans-35" x="159.033203"/>
      </g>
     </g>
    </g>
    <g id="xtick_7">
     <g id="line2d_13">
      <path d="M 539.118408 465.84
L 539.118408 22.32
" clip-path="url(#pfa2ce86669)" style="fill: none; stroke: #b0b0b0; stroke-width: 0.8; stroke-linecap: square"/>
     </g>
     <g id="line2d_14">
      <g>
       <use xlink:href="#m3f63193ba4" x="539.118408" y="465.84" style="stroke: #000000; stroke-width: 0.8"/>
      </g>
     </g>
     <g id="text_7">
      <!-- 1.50 -->
      <g transform="translate(527.985595 480.438437) scale(0.1 -0.1)">
       <use xlink:href="#DejaVuSans-31"/>
       <use xlink:href="#DejaVuSans-2e" x="63.623047"/>
       <use xlink:href="#DejaVuSans-35" x="95.410156"/>
       <use xlink:href="#DejaVuSans-30" x="159.033203"/>
      </g>
     </g>
    </g>
    <g id="xtick_8">
     <g id="line2d_15">
      <path d="M 615.206273 465.84
L 615.206273 22.32
" clip-path="url(#pfa2ce86669)" style="fill: none; stroke: #b0b0b0; stroke-width: 0.8; stroke-linecap: square"/>
     </g>
     <g id="line2d_16">
      <g>
       <use xlink:href="#m3f63193ba4" x="615.206273" y="465.84" style="stroke: #000000; stroke-width: 0.8"/>
      </g>
     </g>
     <g id="text_8">
      <!-- 1.75 -->
      <g transform="translate(604.073461 480.438437) scale(0.1 -0.1)">
       <use xlink:href="#DejaVuSans-31"/>
       <use xlink:href="#DejaVuSans-2e" x="63.623047"/>
       <use xlink:href="#DejaVuSans-37" x="95.410156"/>
       <use xlink:href="#DejaVuSans-35" x="159.033203"/>
      </g>
     </g>
    </g>
    <g id="xtick_9">
     <g id="line2d_17">
      <path d="M 691.294139 465.84
L 691.294139 22.32
" clip-path="url(#pfa2ce86669)" style="fill: none; stroke: #b0b0b0; stroke-width: 0.8; stroke-linecap: square"/>
     </g>
     <g id="line2d_18">
      <g>
       <use xlink:href="#m3f63193ba4" x="691.294139" y="465.84" style="stroke: #000000; stroke-width: 0.8"/>
      </g>
     </g>
     <g id="text_9">
      <!-- 2.00 -->
      <g transform="translate(680.161326 480.438437) scale(0.1 -0.1)">
       <use xlink:href="#DejaVuSans-32"/>
       <use xlink:href="#DejaVuSans-2e" x="63.623047"/>
       <use xlink:href="#DejaVuSans-30" x="95.410156"/>
       <use xlink:href="#DejaVuSans-30" x="159.033203"/>
      </g>
     </g>
    </g>
    <g id="text_10">
     <!-- $x$ -->
     <g transform="translate(383.960938 494.116562) scale(0.1 -0.1)">
      <defs>
       <path id="DejaVuSans-Oblique-78" d="M 3841 3500
L 2234 1784
L 3219 0
L 2559 0
L 1819 1388
L 531 0
L -166 0
L 1556 1844
L 641 3500
L 1300 3500
L 1972 2234
L 3144 3500
L 3841 3500
z
" transform="scale(0.015625)"/>
      </defs>
      <use xlink:href="#DejaVuSans-Oblique-78" transform="translate(0 0.3125)"/>
     </g>
    </g>
   </g>
   <g id="matplotlib.axis_2">
    <g id="ytick_1">
     <g id="line2d_19">
      <path d="M 52.160938 42.872549
L 721.760938 42.872549
" clip-path="url(#pfa2ce86669)" style="fill: none; stroke: #b0b0b0; stroke-width: 0.8; stroke-linecap: square"/>
     </g>
     <g id="line2d_20">
      <defs>
       <path id="m4e63299b62" d="M 0 0
L -3.5 0
" style="stroke: #000000; stroke-width: 0.8"/>
      </defs>
      <g>
       <use xlink:href="#m4e63299b62" x="52.160938" y="42.872549" style="stroke: #000000; stroke-width: 0.8"/>
      </g>
     </g>
     <g id="text_11">
      <!-- −2.5 -->
      <g transform="translate(20.878125 46.671768) scale(0.1 -0.1)">
       <defs>
        <path id="DejaVuSans-2212" d="M 678 2272
L 4684 2272
L 4684 1741
L 678 1741
L 678 2272
z
" transform="scale(0.015625)"/>
       </defs>
       <use xlink:href="#DejaVuSans-2212"/>
       <use xlink:href="#DejaVuSans-32" x="83.789062"/>
       <use xlink:href="#DejaVuSans-2e" x="147.412109"/>
       <use xlink:href="#DejaVuSans-35" x="179.199219"/>
      </g>
     </g>
    </g>
    <g id="ytick_2">
     <g id="line2d_21">
      <path d="M 52.160938 100.420467
L 721.760938 100.420467
" clip-path="url(#pfa2ce86669)" style="fill: none; stroke: #b0b0b0; stroke-width: 0.8; stroke-linecap: square"/>
     </g>
     <g id="line2d_22">
      <g>
       <use xlink:href="#m4e63299b62" x="52.160938" y="100.420467" style="stroke: #000000; stroke-width: 0.8"/>
      </g>
     </g>
     <g id="text_12">
      <!-- −2.0 -->
      <g transform="translate(20.878125 104.219686) scale(0.1 -0.1)">
       <use xlink:href="#DejaVuSans-2212"/>
       <use xlink:href="#DejaVuSans-32" x="83.789062"/>
       <use xlink:href="#DejaVuSans-2e" x="147.412109"/>
       <use xlink:href="#DejaVuSans-30" x="179.199219"/>
      </g>
     </g>
    </g>
    <g id="ytick_3">
     <g id="line2d_23">
      <path d="M 52.160938 157.968385
L 721.760938 157.968385
" clip-path="url(#pfa2ce86669)" style="fill: none; stroke: #b0b0b0; stroke-width: 0.8; stroke-linecap: square"/>
     </g>
     <g id="line2d_24">
      <g>
       <use xlink:href="#m4e63299b62" x="52.160938" y="157.968385" style="stroke: #000000; stroke-width: 0.8"/>
      </g>
     </g>
     <g id="text_13">
      <!-- −1.5 -->
      <g transform="translate(20.878125 161.767603) scale(0.1 -0.1)">
       <use xlink:href="#DejaVuSans-2212"/>
       <use xlink:href="#DejaVuSans-31" x="83.789062"/>
       <use xlink:href="#DejaVuSans-2e" x="147.412109"/>
       <use xlink:href="#DejaVuSans-35" x="179.199219"/>
      </g>
     </g>
    </g>
    <g id="ytick_4">
     <g id="line2d_25">
      <path d="M 52.160938 215.516303
L 721.760938 215.516303
" clip-path="url(#pfa2ce86669)" style="fill: none; stroke: #b0b0b0; stroke-width: 0.8; stroke-linecap: square"/>
     </g>
     <g id="line2d_26">
      <g>
       <use xlink:href="#m4e63299b62" x="52.160938" y="215.516303" style="stroke: #000000; stroke-width: 0.8"/>
      </g>
     </g>
     <g id="text_14">
      <!-- −1.0 -->
      <g transform="translate(20.878125 219.315521) scale(0.1 -0.1)">
       <use xlink:href="#DejaVuSans-2212"/>
       <use xlink:href="#DejaVuSans-31" x="83.789062"/>
       <use xlink:href="#DejaVuSans-2e" x="147.412109"/>
       <use xlink:href="#DejaVuSans-30" x="179.199219"/>
      </g>
     </g>
    </g>
    <g id="ytick_5">
     <g id="line2d_27">
      <path d="M 52.160938 273.06422
L 721.760938 273.06422
" clip-path="url(#pfa2ce86669)" style="fill: none; stroke: #b0b0b0; stroke-width: 0.8; stroke-linecap: square"/>
     </g>
     <g id="line2d_28">
      <g>
       <use xlink:href="#m4e63299b62" x="52.160938" y="273.06422" style="stroke: #000000; stroke-width: 0.8"/>
      </g>
     </g>
     <g id="text_15">
      <!-- −0.5 -->
      <g transform="translate(20.878125 276.863439) scale(0.1 -0.1)">
       <use xlink:href="#DejaVuSans-2212"/>
       <use xlink:href="#DejaVuSans-30" x="83.789062"/>
       <use xlink:href="#DejaVuSans-2e" x="147.412109"/>
       <use xlink:href="#DejaVuSans-35" x="179.199219"/>
      </g>
     </g>
    </g>
    <g id="ytick_6">
     <g id="line2d_29">
      <path d="M 52.160938 330.612138
L 721.760938 330.612138
" clip-path="url(#pfa2ce86669)" style="fill: none; stroke: #b0b0b0; stroke-width: 0.8; stroke-linecap: square"/>
     </g>
     <g id="line2d_30">
      <g>
       <use xlink:href="#m4e63299b62" x="52.160938" y="330.612138" style="stroke: #000000; stroke-width: 0.8"/>
      </g>
     </g>
     <g id="text_16">
      <!-- 0.0 -->
      <g transform="translate(29.257813 334.411357) scale(0.1 -0.1)">
       <use xlink:href="#DejaVuSans-30"/>
       <use xlink:href="#DejaVuSans-2e" x="63.623047"/>
       <use xlink:href="#DejaVuSans-30" x="95.410156"/>
      </g>
     </g>
    </g>
    <g id="ytick_7">
     <g id="line2d_31">
      <path d="M 52.160938 388.160056
L 721.760938 388.160056
" clip-path="url(#pfa2ce86669)" style="fill: none; stroke: #b0b0b0; stroke-width: 0.8; stroke-linecap: square"/>
     </g>
     <g id="line2d_32">
      <g>
       <use xlink:href="#m4e63299b62" x="52.160938" y="388.160056" style="stroke: #000000; stroke-width: 0.8"/>
      </g>
     </g>
     <g id="text_17">
      <!-- 0.5 -->
      <g transform="translate(29.257813 391.959275) scale(0.1 -0.1)">
       <use xlink:href="#DejaVuSans-30"/>
       <use xlink:href="#DejaVuSans-2e" x="63.623047"/>
       <use xlink:href="#DejaVuSans-35" x="95.410156"/>
      </g>
     </g>
    </g>
    <g id="ytick_8">
     <g id="line2d_33">
      <path d="M 52.160938 445.707974
L 721.760938 445.707974
" clip-path="url(#pfa2ce86669)" style="fill: none; stroke: #b0b0b0; stroke-width: 0.8; stroke-linecap: square"/>
     </g>
     <g id="line2d_34">
      <g>
       <use xlink:href="#m4e63299b62" x="52.160938" y="445.707974" style="stroke: #000000; stroke-width: 0.8"/>
      </g>
     </g>
     <g id="text_18">
      <!-- 1.0 -->
      <g transform="translate(29.257813 449.507193) scale(0.1 -0.1)">
       <use xlink:href="#DejaVuSans-31"/>
       <use xlink:href="#DejaVuSans-2e" x="63.623047"/>
       <use xlink:href="#DejaVuSans-30" x="95.410156"/>
      </g>
     </g>
    </g>
    <g id="text_19">
     <!-- $c_p$ -->
     <g transform="translate(13.778125 249.23) rotate(-90) scale(0.1 -0.1)">
      <defs>
       <path id="DejaVuSans-Oblique-63" d="M 3431 3366
L 3316 2797
Q 3109 2947 2876 3022
Q 2644 3097 2394 3097
Q 2119 3097 1870 3000
Q 1622 2903 1453 2725
Q 1184 2453 1037 2087
Q 891 1722 891 1331
Q 891 859 1127 628
Q 1363 397 1844 397
Q 2081 397 2348 469
Q 2616 541 2906 684
L 2797 116
Q 2547 13 2283 -39
Q 2019 -91 1741 -91
Q 1044 -91 669 257
Q 294 606 294 1253
Q 294 1797 489 2255
Q 684 2713 1069 3078
Q 1331 3328 1684 3456
Q 2038 3584 2456 3584
Q 2700 3584 2940 3529
Q 3181 3475 3431 3366
z
" transform="scale(0.015625)"/>
       <path id="DejaVuSans-Oblique-70" d="M 3175 2156
Q 3175 2616 2975 2859
Q 2775 3103 2400 3103
Q 2144 3103 1911 2972
Q 1678 2841 1497 2591
Q 1319 2344 1212 1994
Q 1106 1644 1106 1300
Q 1106 863 1306 627
Q 1506 391 1875 391
Q 2147 391 2380 519
Q 2613 647 2778 891
Q 2956 1147 3065 1494
Q 3175 1841 3175 2156
z
M 1394 2969
Q 1625 3272 1939 3428
Q 2253 3584 2638 3584
Q 3175 3584 3472 3232
Q 3769 2881 3769 2247
Q 3769 1728 3584 1258
Q 3400 788 3053 416
Q 2822 169 2531 39
Q 2241 -91 1919 -91
Q 1547 -91 1294 64
Q 1041 219 916 525
L 556 -1331
L -19 -1331
L 922 3500
L 1497 3500
L 1394 2969
z
" transform="scale(0.015625)"/>
      </defs>
      <use xlink:href="#DejaVuSans-Oblique-63"/>
      <use xlink:href="#DejaVuSans-Oblique-70" transform="translate(54.980469 -16.40625) scale(0.7)"/>
     </g>
    </g>
   </g>
   <g id="line2d_35">
    <path d="M 386.942676 339.237508
L 385.259613 339.348178
L 371.256402 339.332688
L 353.774454 339.09355
L 340.297771 338.70105
L 326.772392 338.025241
L 317.748371 337.354006
L 308.71522 336.469986
L 299.685112 335.372869
L 290.651961 334.079926
L 281.621853 332.574145
L 268.087343 330.072859
L 250.069737 326.712433
L 236.593054 324.369789
L 218.688058 321.598282
L 205.327028 319.791817
L 192.039043 318.280093
L 178.851495 317.217005
L 174.481008 316.951761
L 161.466939 316.557039
L 152.896402 316.676494
L 148.647655 316.946891
L 144.432388 317.328861
L 140.250599 318.001399
L 136.114462 318.553643
L 132.027022 319.497908
L 128.000452 320.67149
L 124.04997 321.96135
L 120.193837 323.728431
L 116.459445 325.741457
L 109.483709 331.028408
L 106.318454 334.301979
L 103.411898 338.194393
L 100.785345 342.484633
L 98.441838 346.890254
L 96.369205 351.98247
L 94.543096 357.341824
L 92.939164 362.768277
L 90.282176 375.753674
L 89.180423 382.121535
L 87.329966 396.850788
L 85.856905 412.872953
L 84.694283 428.682439
L 83.446442 445.056583
L 83.154264 445.441908
L 82.926001 442.675454
L 82.758607 433.630894
L 82.597301 405.085713
L 82.649041 361.495235
L 82.926001 310.969989
L 83.446442 268.008002
L 83.799489 250.570078
L 84.694283 227.075025
L 85.242115 220.110468
L 85.856905 214.647452
L 86.550827 210.897899
L 88.200412 207.442854
L 89.180423 207.167879
L 90.282176 207.75739
L 91.530017 208.864885
L 94.543096 212.073491
L 96.369205 214.526759
L 100.785345 219.646153
L 103.411898 222.476179
L 109.483709 228.316922
L 116.459445 234.017807
L 120.193837 236.824339
L 128.000452 242.050653
L 136.114462 246.814544
L 144.432388 251.324667
L 152.896402 255.587855
L 161.466939 259.537454
L 170.125738 263.283344
L 178.851495 266.816148
L 187.632034 270.135341
L 196.46127 273.231889
L 205.327028 276.096958
L 214.226265 278.713514
L 223.155937 281.089567
L 232.109957 283.227134
L 241.079195 285.146885
L 250.069737 286.882214
L 259.072453 288.449402
L 272.594789 290.517098
L 286.135385 292.32939
L 304.198644 294.495368
L 322.261904 296.583065
L 331.282881 306.21403
L 335.79337 310.386557
L 340.297771 313.858386
L 344.799129 316.649682
L 349.291357 318.882482
L 353.774454 320.688284
L 358.236246 322.207074
L 375.292102 327.320209
L 379.029538 328.661122
L 382.368274 330.255065
L 385.259613 332.359516
L 386.973112 339.237508
L 390.64359 342.667668
L 392.926226 345.006513
L 395.567997 347.054422
L 398.629773 348.794234
L 402.172424 350.065855
L 406.278125 350.681785
L 411.032095 350.520662
L 416.540856 349.580515
L 422.920063 348.019596
L 430.306673 346.093069
L 438.861992 344.069871
L 448.768632 342.133361
L 460.245726 340.381263
L 473.536754 338.834181
L 488.930851 337.492438
L 506.75976 336.337634
L 527.406963 335.348076
L 551.322901 334.510235
L 579.018884 333.800914
L 611.097528 333.205435
L 648.249711 332.711037
L 691.275878 332.256696
L 691.275878 332.256696
" clip-path="url(#pfa2ce86669)" style="fill: none; stroke: #1f77b4; stroke-width: 1.5; stroke-linecap: square"/>
   </g>
   <g id="line2d_36">
    <path d="M 386.942676 330.872108
L 385.259613 329.287046
L 379.029538 322.068735
L 353.774454 321.378271
L 335.79337 320.681087
L 322.261904 319.945862
L 308.71522 318.9453
L 299.685112 318.083828
L 290.651961 317.039395
L 281.621853 315.804913
L 272.594789 314.402316
L 263.576855 312.80426
L 254.571095 311.019796
L 241.079195 308.080503
L 223.155937 303.90606
L 183.234156 294.476898
L 161.466939 289.55334
L 157.169496 288.761369
L 148.647655 286.971436
L 140.250599 285.543587
L 136.114462 284.912982
L 128.000452 283.877417
L 120.193837 283.300971
L 116.459445 283.339251
L 109.483709 283.85558
L 106.318454 284.70069
L 103.411898 285.758037
L 100.785345 287.179524
L 98.441838 288.96828
L 96.369205 291.069908
L 94.543096 293.451373
L 92.939164 296.554242
L 91.530017 300.272783
L 89.180423 308.78943
L 88.200412 314.596479
L 87.329966 321.126935
L 86.550827 328.32196
L 85.856905 335.994043
L 84.694283 356.784259
L 84.216451 367.264486
L 83.799489 381.09081
L 82.926001 420.94859
L 82.597301 445.247235
L 83.154264 407.688819
L 83.799489 382.911246
L 84.216451 368.162676
L 84.694283 355.830747
L 85.856905 336.557429
L 86.550827 328.003259
L 88.200412 314.023406
L 89.180423 309.248498
L 90.282176 304.434464
L 91.530017 300.280545
L 94.543096 293.416953
L 96.369205 291.024545
L 98.441838 288.979025
L 100.785345 287.292969
L 103.411898 285.861138
L 106.318454 284.616278
L 109.483709 284.106618
L 112.877228 283.328314
L 116.459445 283.454062
L 120.193837 283.328314
L 124.04997 283.473193
L 128.000452 284.016594
L 136.114462 284.866725
L 140.250599 285.472978
L 161.466939 289.631086
L 170.125738 291.501854
L 209.773603 300.738175
L 232.109957 306.031509
L 245.574466 309.1081
L 259.072453 311.951982
L 268.087343 313.646417
L 277.108321 315.146238
L 286.135385 316.464362
L 295.165493 317.603431
L 304.198644 318.551224
L 313.231796 319.329117
L 326.772392 320.229636
L 340.297771 320.892125
L 358.236246 321.528952
L 379.029538 322.075892
L 385.259613 329.287046
L 386.973112 330.872108
L 392.926226 337.994067
L 398.629773 345.853074
L 402.172424 349.27313
L 406.278125 351.691429
L 411.035138 352.834275
L 416.540856 352.61289
L 422.920063 351.183109
L 438.861992 346.407623
L 448.771676 343.916229
L 460.24877 341.672094
L 473.542841 339.732862
L 488.936938 338.092028
L 506.768891 336.71877
L 527.419137 335.57787
L 551.338119 334.634644
L 579.040189 333.853113
L 611.12492 333.212262
L 648.286234 332.685946
L 691.324574 332.21784
L 691.324574 332.21784
" clip-path="url(#pfa2ce86669)" style="fill: none; stroke: #ff7f0e; stroke-width: 1.5; stroke-linecap: square"/>
   </g>
   <g id="line2d_37">
    <path d="M 386.942676 343.734305
L 385.259613 339.100196
L 382.368274 336.608981
L 379.029538 334.32236
L 375.292102 332.151542
L 371.256402 330.049785
L 367.016786 328.035847
L 362.661517 326.105449
L 353.774454 322.521626
L 344.799129 319.230201
L 335.79337 316.193459
L 322.261904 311.964389
L 308.71522 308.042743
L 286.135385 302.011586
L 268.087343 297.42819
L 263.576855 296.124177
L 259.072453 294.585063
L 254.571095 292.584386
L 250.069737 289.885638
L 245.574466 286.110615
L 241.079195 281.026243
L 236.593054 274.618312
L 232.109957 267.166095
L 227.629903 264.784317
L 209.773603 260.776698
L 200.889584 258.599436
L 192.039043 256.187959
L 183.234156 253.445807
L 178.851495 251.919521
L 174.481008 250.276232
L 170.125738 248.508512
L 165.785686 246.602667
L 161.466939 244.544651
L 157.169496 242.320022
L 152.896402 239.913902
L 148.647655 237.317118
L 144.432388 234.520124
L 140.250599 231.509831
L 136.114462 228.25681
L 132.027022 224.787963
L 128.000452 221.056962
L 124.04997 217.064422
L 120.193837 212.761711
L 116.459445 208.170937
L 112.877228 203.291555
L 109.483709 198.062143
L 106.318454 192.640412
L 103.411898 186.994342
L 100.785345 181.226664
L 98.441838 175.328371
L 96.369205 169.579001
L 94.543096 163.852002
L 91.530017 152.996743
L 90.282176 148.105114
L 89.180423 143.034847
L 87.329966 135.983862
L 86.550827 133.937605
L 85.856905 132.439318
L 85.242115 133.702668
L 84.694283 136.825367
L 84.216451 142.444761
L 83.799489 155.239059
L 83.446442 169.614654
L 83.154264 188.768655
L 82.926001 214.451718
L 82.649041 276.987197
L 82.597301 340.91788
L 82.758607 396.886776
L 83.154264 429.807086
L 83.446442 440.271729
L 83.799489 444.540382
L 84.216451 445.648875
L 84.694283 443.88535
L 85.242115 440.462138
L 87.329966 423.240701
L 88.200412 416.528611
L 89.180423 409.862282
L 90.282176 403.17798
L 91.530017 396.847789
L 92.939164 390.382255
L 94.543096 383.672365
L 96.369205 377.667796
L 98.441838 371.923205
L 100.785345 366.28083
L 103.411898 361.025958
L 106.318454 356.285821
L 109.483709 351.859872
L 112.877228 347.815902
L 116.459445 344.614256
L 120.193837 341.501319
L 124.04997 338.902934
L 128.000452 336.698609
L 132.027022 334.738641
L 136.114462 333.009628
L 140.250599 331.634212
L 144.432388 330.407176
L 148.647655 329.412029
L 157.169496 327.863546
L 165.785686 326.817737
L 170.125738 326.410306
L 178.851495 325.943482
L 187.632034 325.727356
L 196.46127 325.772007
L 205.327028 325.99044
L 214.226265 326.377494
L 227.629903 327.217464
L 241.079195 328.284762
L 254.571095 329.585506
L 268.087343 331.111112
L 281.621853 332.86608
L 295.165493 334.856144
L 331.282881 340.390071
L 340.297771 341.426835
L 349.291357 342.286161
L 358.236246 342.931041
L 367.016786 343.378652
L 379.029538 343.740805
L 385.259613 343.812292
L 386.973112 343.734305
L 388.674436 344.497725
L 390.64359 345.10123
L 392.926226 345.644988
L 395.567997 346.099493
L 398.629773 346.418314
L 402.172424 346.538007
L 406.278125 346.407623
L 411.032095 345.988107
L 416.537813 345.269028
L 438.855905 341.820861
L 448.762545 340.513345
L 460.236596 339.250791
L 473.521537 338.071994
L 488.909547 337.000829
L 506.732368 336.041234
L 527.370441 335.192491
L 551.274205 334.446874
L 578.95497 333.798644
L 611.01231 333.241846
L 691.129789 332.295544
L 691.129789 332.295544
" clip-path="url(#pfa2ce86669)" style="fill: none; stroke: #2ca02c; stroke-width: 1.5; stroke-linecap: square"/>
   </g>
   <g id="line2d_38">
    <path d="M 386.942676 345.152875
L 385.259613 343.154969
L 382.368274 341.380817
L 375.292102 337.503598
L 367.016786 333.289625
L 358.236246 329.050783
L 349.291357 324.959949
L 340.297771 321.038308
L 326.772392 315.457419
L 313.231796 310.144337
L 259.072453 289.405836
L 241.079195 282.051691
L 218.688058 272.210304
L 200.889584 263.810402
L 183.234156 255.280045
L 174.481008 251.348599
L 170.125738 249.516607
L 165.785686 247.540123
L 161.466939 244.85494
L 157.169496 240.34153
L 152.896402 231.113974
L 148.647655 213.945689
L 144.432388 190.290024
L 136.114462 185.428589
L 132.027022 183.062409
L 128.000452 180.601684
L 124.04997 177.960986
L 120.193837 175.038986
L 116.459445 171.717686
L 112.877228 167.868504
L 109.483709 163.372699
L 106.318454 158.080777
L 103.411898 151.94223
L 100.785345 144.991449
L 98.441838 137.33801
L 96.369205 129.057903
L 94.543096 120.273404
L 92.939164 111.090103
L 91.530017 101.822799
L 90.282176 92.432945
L 88.200412 73.92777
L 85.242115 45.65347
L 84.694283 42.48
L 84.216451 43.052839
L 83.799489 48.33978
L 83.446442 60.735186
L 83.154264 79.175731
L 82.926001 102.685685
L 82.649041 176.445638
L 82.597301 255.564186
L 82.758607 334.070858
L 83.154264 394.690247
L 83.446442 415.262241
L 83.799489 429.724843
L 84.216451 438.864612
L 84.694283 444.093951
L 85.242115 445.68
L 85.856905 445.008449
L 86.550827 442.363679
L 87.329966 438.716194
L 90.282176 422.960147
L 92.939164 410.937047
L 94.543096 404.502427
L 96.369205 398.334616
L 98.441838 392.188267
L 100.785345 386.058865
L 103.411898 380.241168
L 106.318454 374.801111
L 109.483709 369.749181
L 112.877228 365.086959
L 116.459445 360.893615
L 120.193837 357.206634
L 124.04997 353.951636
L 128.000452 351.00362
L 132.027022 348.392485
L 136.114462 346.189414
L 140.250599 344.13043
L 144.432388 342.371244
L 148.647655 340.814622
L 152.896402 339.474272
L 161.466939 337.222191
L 165.785686 336.286017
L 170.125738 335.47652
L 178.851495 334.197777
L 187.632034 333.196332
L 196.46127 332.528497
L 205.327028 332.044053
L 214.226265 331.783122
L 227.629903 331.670876
L 241.079195 331.792283
L 259.072453 332.366369
L 272.594789 333.021017
L 286.135385 333.875805
L 299.682069 334.971327
L 313.231796 336.346609
L 322.261904 337.429932
L 335.79337 339.326048
L 358.236246 342.667668
L 367.016786 343.706136
L 375.292102 344.497725
L 382.368274 345.002207
L 386.973112 345.152875
L 388.674436 344.799703
L 398.626729 344.430797
L 406.278125 343.881589
L 416.534769 342.889707
L 438.846775 340.561754
L 448.750371 339.640071
L 460.218334 338.70105
L 473.497189 337.773494
L 488.876068 336.886706
L 506.686716 336.054716
L 527.309571 335.291717
L 551.19203 334.600721
L 578.845404 333.986961
L 610.869265 333.446544
L 690.889351 332.398347
L 690.889351 332.398347
" clip-path="url(#pfa2ce86669)" style="fill: none; stroke: #d62728; stroke-width: 1.5; stroke-linecap: square"/>
   </g>
   <g id="patch_3">
    <path d="M 52.160938 465.84
L 52.160938 22.32
" style="fill: none; stroke: #000000; stroke-width: 0.8; stroke-linejoin: miter; stroke-linecap: square"/>
   </g>
   <g id="patch_4">
    <path d="M 721.760938 465.84
L 721.760938 22.32
" style="fill: none; stroke: #000000; stroke-width: 0.8; stroke-linejoin: miter; stroke-linecap: square"/>
   </g>
   <g id="patch_5">
    <path d="M 52.160938 465.84
L 721.760937 465.84
" style="fill: none; stroke: #000000; stroke-width: 0.8; stroke-linejoin: miter; stroke-linecap: square"/>
   </g>
   <g id="patch_6">
    <path d="M 52.160938 22.32
L 721.760937 22.32
" style="fill: none; stroke: #000000; stroke-width: 0.8; stroke-linejoin: miter; stroke-linecap: square"/>
   </g>
   <g id="text_20">
    <!-- Result plot for $\alpha = -2$ and $Re = 100000$ and $M = 0.1$ -->
    <g transform="translate(229.700938 16.32) scale(0.12 -0.12)">
     <defs>
      <path id="DejaVuSans-52" d="M 2841 2188
Q 3044 2119 3236 1894
Q 3428 1669 3622 1275
L 4263 0
L 3584 0
L 2988 1197
Q 2756 1666 2539 1819
Q 2322 1972 1947 1972
L 1259 1972
L 1259 0
L 628 0
L 628 4666
L 2053 4666
Q 2853 4666 3247 4331
Q 3641 3997 3641 3322
Q 3641 2881 3436 2590
Q 3231 2300 2841 2188
z
M 1259 4147
L 1259 2491
L 2053 2491
Q 2509 2491 2742 2702
Q 2975 2913 2975 3322
Q 2975 3731 2742 3939
Q 2509 4147 2053 4147
L 1259 4147
z
" transform="scale(0.015625)"/>
      <path id="DejaVuSans-65" d="M 3597 1894
L 3597 1613
L 953 1613
Q 991 1019 1311 708
Q 1631 397 2203 397
Q 2534 397 2845 478
Q 3156 559 3463 722
L 3463 178
Q 3153 47 2828 -22
Q 2503 -91 2169 -91
Q 1331 -91 842 396
Q 353 884 353 1716
Q 353 2575 817 3079
Q 1281 3584 2069 3584
Q 2775 3584 3186 3129
Q 3597 2675 3597 1894
z
M 3022 2063
Q 3016 2534 2758 2815
Q 2500 3097 2075 3097
Q 1594 3097 1305 2825
Q 1016 2553 972 2059
L 3022 2063
z
" transform="scale(0.015625)"/>
      <path id="DejaVuSans-73" d="M 2834 3397
L 2834 2853
Q 2591 2978 2328 3040
Q 2066 3103 1784 3103
Q 1356 3103 1142 2972
Q 928 2841 928 2578
Q 928 2378 1081 2264
Q 1234 2150 1697 2047
L 1894 2003
Q 2506 1872 2764 1633
Q 3022 1394 3022 966
Q 3022 478 2636 193
Q 2250 -91 1575 -91
Q 1294 -91 989 -36
Q 684 19 347 128
L 347 722
Q 666 556 975 473
Q 1284 391 1588 391
Q 1994 391 2212 530
Q 2431 669 2431 922
Q 2431 1156 2273 1281
Q 2116 1406 1581 1522
L 1381 1569
Q 847 1681 609 1914
Q 372 2147 372 2553
Q 372 3047 722 3315
Q 1072 3584 1716 3584
Q 2034 3584 2315 3537
Q 2597 3491 2834 3397
z
" transform="scale(0.015625)"/>
      <path id="DejaVuSans-75" d="M 544 1381
L 544 3500
L 1119 3500
L 1119 1403
Q 1119 906 1312 657
Q 1506 409 1894 409
Q 2359 409 2629 706
Q 2900 1003 2900 1516
L 2900 3500
L 3475 3500
L 3475 0
L 2900 0
L 2900 538
Q 2691 219 2414 64
Q 2138 -91 1772 -91
Q 1169 -91 856 284
Q 544 659 544 1381
z
M 1991 3584
L 1991 3584
z
" transform="scale(0.015625)"/>
      <path id="DejaVuSans-6c" d="M 603 4863
L 1178 4863
L 1178 0
L 603 0
L 603 4863
z
" transform="scale(0.015625)"/>
      <path id="DejaVuSans-74" d="M 1172 4494
L 1172 3500
L 2356 3500
L 2356 3053
L 1172 3053
L 1172 1153
Q 1172 725 1289 603
Q 1406 481 1766 481
L 2356 481
L 2356 0
L 1766 0
Q 1100 0 847 248
Q 594 497 594 1153
L 594 3053
L 172 3053
L 172 3500
L 594 3500
L 594 4494
L 1172 4494
z
" transform="scale(0.015625)"/>
      <path id="DejaVuSans-20" transform="scale(0.015625)"/>
      <path id="DejaVuSans-70" d="M 1159 525
L 1159 -1331
L 581 -1331
L 581 3500
L 1159 3500
L 1159 2969
Q 1341 3281 1617 3432
Q 1894 3584 2278 3584
Q 2916 3584 3314 3078
Q 3713 2572 3713 1747
Q 3713 922 3314 415
Q 2916 -91 2278 -91
Q 1894 -91 1617 61
Q 1341 213 1159 525
z
M 3116 1747
Q 3116 2381 2855 2742
Q 2594 3103 2138 3103
Q 1681 3103 1420 2742
Q 1159 2381 1159 1747
Q 1159 1113 1420 752
Q 1681 391 2138 391
Q 2594 391 2855 752
Q 3116 1113 3116 1747
z
" transform="scale(0.015625)"/>
      <path id="DejaVuSans-6f" d="M 1959 3097
Q 1497 3097 1228 2736
Q 959 2375 959 1747
Q 959 1119 1226 758
Q 1494 397 1959 397
Q 2419 397 2687 759
Q 2956 1122 2956 1747
Q 2956 2369 2687 2733
Q 2419 3097 1959 3097
z
M 1959 3584
Q 2709 3584 3137 3096
Q 3566 2609 3566 1747
Q 3566 888 3137 398
Q 2709 -91 1959 -91
Q 1206 -91 779 398
Q 353 888 353 1747
Q 353 2609 779 3096
Q 1206 3584 1959 3584
z
" transform="scale(0.015625)"/>
      <path id="DejaVuSans-66" d="M 2375 4863
L 2375 4384
L 1825 4384
Q 1516 4384 1395 4259
Q 1275 4134 1275 3809
L 1275 3500
L 2222 3500
L 2222 3053
L 1275 3053
L 1275 0
L 697 0
L 697 3053
L 147 3053
L 147 3500
L 697 3500
L 697 3744
Q 697 4328 969 4595
Q 1241 4863 1831 4863
L 2375 4863
z
" transform="scale(0.015625)"/>
      <path id="DejaVuSans-72" d="M 2631 2963
Q 2534 3019 2420 3045
Q 2306 3072 2169 3072
Q 1681 3072 1420 2755
Q 1159 2438 1159 1844
L 1159 0
L 581 0
L 581 3500
L 1159 3500
L 1159 2956
Q 1341 3275 1631 3429
Q 1922 3584 2338 3584
Q 2397 3584 2469 3576
Q 2541 3569 2628 3553
L 2631 2963
z
" transform="scale(0.015625)"/>
      <path id="DejaVuSans-Oblique-3b1" d="M 2619 1628
L 2622 2350
Q 2625 3088 2069 3091
Q 1653 3094 1394 2747
Q 1069 2319 959 1747
Q 825 1059 994 731
Q 1169 397 1547 397
Q 1966 397 2319 1063
L 2619 1628
z
M 2166 3578
Q 3141 3594 3128 2584
Q 3128 2584 3616 3500
L 4128 3500
L 3119 1603
L 3109 919
Q 3109 766 3194 638
Q 3291 488 3391 488
L 3669 488
L 3575 0
L 3228 0
Q 2934 0 2722 263
Q 2622 394 2619 669
Q 2416 334 2066 50
Q 1900 -81 1453 -78
Q 722 -72 456 397
Q 184 884 353 1747
Q 534 2675 1009 3097
Q 1544 3569 2166 3578
z
" transform="scale(0.015625)"/>
      <path id="DejaVuSans-3d" d="M 678 2906
L 4684 2906
L 4684 2381
L 678 2381
L 678 2906
z
M 678 1631
L 4684 1631
L 4684 1100
L 678 1100
L 678 1631
z
" transform="scale(0.015625)"/>
      <path id="DejaVuSans-61" d="M 2194 1759
Q 1497 1759 1228 1600
Q 959 1441 959 1056
Q 959 750 1161 570
Q 1363 391 1709 391
Q 2188 391 2477 730
Q 2766 1069 2766 1631
L 2766 1759
L 2194 1759
z
M 3341 1997
L 3341 0
L 2766 0
L 2766 531
Q 2569 213 2275 61
Q 1981 -91 1556 -91
Q 1019 -91 701 211
Q 384 513 384 1019
Q 384 1609 779 1909
Q 1175 2209 1959 2209
L 2766 2209
L 2766 2266
Q 2766 2663 2505 2880
Q 2244 3097 1772 3097
Q 1472 3097 1187 3025
Q 903 2953 641 2809
L 641 3341
Q 956 3463 1253 3523
Q 1550 3584 1831 3584
Q 2591 3584 2966 3190
Q 3341 2797 3341 1997
z
" transform="scale(0.015625)"/>
      <path id="DejaVuSans-6e" d="M 3513 2113
L 3513 0
L 2938 0
L 2938 2094
Q 2938 2591 2744 2837
Q 2550 3084 2163 3084
Q 1697 3084 1428 2787
Q 1159 2491 1159 1978
L 1159 0
L 581 0
L 581 3500
L 1159 3500
L 1159 2956
Q 1366 3272 1645 3428
Q 1925 3584 2291 3584
Q 2894 3584 3203 3211
Q 3513 2838 3513 2113
z
" transform="scale(0.015625)"/>
      <path id="DejaVuSans-64" d="M 2906 2969
L 2906 4863
L 3481 4863
L 3481 0
L 2906 0
L 2906 525
Q 2725 213 2448 61
Q 2172 -91 1784 -91
Q 1150 -91 751 415
Q 353 922 353 1747
Q 353 2572 751 3078
Q 1150 3584 1784 3584
Q 2172 3584 2448 3432
Q 2725 3281 2906 2969
z
M 947 1747
Q 947 1113 1208 752
Q 1469 391 1925 391
Q 2381 391 2643 752
Q 2906 1113 2906 1747
Q 2906 2381 2643 2742
Q 2381 3103 1925 3103
Q 1469 3103 1208 2742
Q 947 2381 947 1747
z
" transform="scale(0.015625)"/>
      <path id="DejaVuSans-Oblique-52" d="M 1613 4147
L 1294 2491
L 2106 2491
Q 2584 2491 2879 2755
Q 3175 3019 3175 3444
Q 3175 3784 2976 3965
Q 2778 4147 2406 4147
L 1613 4147
z
M 2772 2241
Q 2972 2194 3105 2009
Q 3238 1825 3413 1275
L 3809 0
L 3144 0
L 2778 1197
Q 2638 1659 2453 1815
Q 2269 1972 1888 1972
L 1191 1972
L 806 0
L 172 0
L 1081 4666
L 2503 4666
Q 3150 4666 3495 4373
Q 3841 4081 3841 3531
Q 3841 3044 3547 2687
Q 3253 2331 2772 2241
z
" transform="scale(0.015625)"/>
      <path id="DejaVuSans-Oblique-65" d="M 3078 2063
Q 3088 2113 3092 2166
Q 3097 2219 3097 2272
Q 3097 2653 2873 2875
Q 2650 3097 2266 3097
Q 1838 3097 1509 2826
Q 1181 2556 1013 2059
L 3078 2063
z
M 3578 1613
L 903 1613
Q 884 1494 878 1425
Q 872 1356 872 1306
Q 872 872 1139 634
Q 1406 397 1894 397
Q 2269 397 2603 481
Q 2938 566 3225 728
L 3116 159
Q 2806 34 2476 -28
Q 2147 -91 1806 -91
Q 1078 -91 686 257
Q 294 606 294 1247
Q 294 1794 489 2264
Q 684 2734 1063 3103
Q 1306 3334 1642 3459
Q 1978 3584 2356 3584
Q 2950 3584 3301 3228
Q 3653 2872 3653 2272
Q 3653 2128 3634 1964
Q 3616 1800 3578 1613
z
" transform="scale(0.015625)"/>
      <path id="DejaVuSans-Oblique-4d" d="M 1081 4666
L 2028 4666
L 2572 1522
L 4378 4666
L 5350 4666
L 4441 0
L 3828 0
L 4622 4091
L 2791 897
L 2175 897
L 1581 4103
L 788 0
L 172 0
L 1081 4666
z
" transform="scale(0.015625)"/>
     </defs>
     <use xlink:href="#DejaVuSans-52" transform="translate(0 0.015625)"/>
     <use xlink:href="#DejaVuSans-65" transform="translate(69.482422 0.015625)"/>
     <use xlink:href="#DejaVuSans-73" transform="translate(131.005859 0.015625)"/>
     <use xlink:href="#DejaVuSans-75" transform="translate(183.105469 0.015625)"/>
     <use xlink:href="#DejaVuSans-6c" transform="translate(246.484375 0.015625)"/>
     <use xlink:href="#DejaVuSans-74" transform="translate(274.267578 0.015625)"/>
     <use xlink:href="#DejaVuSans-20" transform="translate(313.476562 0.015625)"/>
     <use xlink:href="#DejaVuSans-70" transform="translate(345.263672 0.015625)"/>
     <use xlink:href="#DejaVuSans-6c" transform="translate(408.740234 0.015625)"/>
     <use xlink:href="#DejaVuSans-6f" transform="translate(436.523438 0.015625)"/>
     <use xlink:href="#DejaVuSans-74" transform="translate(497.705078 0.015625)"/>
     <use xlink:href="#DejaVuSans-20" transform="translate(536.914062 0.015625)"/>
     <use xlink:href="#DejaVuSans-66" transform="translate(568.701172 0.015625)"/>
     <use xlink:href="#DejaVuSans-6f" transform="translate(603.90625 0.015625)"/>
     <use xlink:href="#DejaVuSans-72" transform="translate(665.087891 0.015625)"/>
     <use xlink:href="#DejaVuSans-20" transform="translate(706.201172 0.015625)"/>
     <use xlink:href="#DejaVuSans-Oblique-3b1" transform="translate(737.988281 0.015625)"/>
     <use xlink:href="#DejaVuSans-3d" transform="translate(823.388672 0.015625)"/>
     <use xlink:href="#DejaVuSans-2212" transform="translate(946.142578 0.015625)"/>
     <use xlink:href="#DejaVuSans-32" transform="translate(1049.414062 0.015625)"/>
     <use xlink:href="#DejaVuSans-20" transform="translate(1113.037109 0.015625)"/>
     <use xlink:href="#DejaVuSans-61" transform="translate(1144.824219 0.015625)"/>
     <use xlink:href="#DejaVuSans-6e" transform="translate(1206.103516 0.015625)"/>
     <use xlink:href="#DejaVuSans-64" transform="translate(1269.482422 0.015625)"/>
     <use xlink:href="#DejaVuSans-20" transform="translate(1332.958984 0.015625)"/>
     <use xlink:href="#DejaVuSans-Oblique-52" transform="translate(1364.746094 0.015625)"/>
     <use xlink:href="#DejaVuSans-Oblique-65" transform="translate(1434.228516 0.015625)"/>
     <use xlink:href="#DejaVuSans-3d" transform="translate(1515.234375 0.015625)"/>
     <use xlink:href="#DejaVuSans-31" transform="translate(1618.505859 0.015625)"/>
     <use xlink:href="#DejaVuSans-30" transform="translate(1682.128906 0.015625)"/>
     <use xlink:href="#DejaVuSans-30" transform="translate(1745.751953 0.015625)"/>
     <use xlink:href="#DejaVuSans-30" transform="translate(1809.375 0.015625)"/>
     <use xlink:href="#DejaVuSans-30" transform="translate(1872.998047 0.015625)"/>
     <use xlink:href="#DejaVuSans-30" transform="translate(1936.621094 0.015625)"/>
     <use xlink:href="#DejaVuSans-20" transform="translate(2000.244141 0.015625)"/>
     <use xlink:href="#DejaVuSans-61" transform="translate(2032.03125 0.015625)"/>
     <use xlink:href="#DejaVuSans-6e" transform="translate(2093.310547 0.015625)"/>
     <use xlink:href="#DejaVuSans-64" transform="translate(2156.689453 0.015625)"/>
     <use xlink:href="#DejaVuSans-20" transform="translate(2220.166016 0.015625)"/>
     <use xlink:href="#DejaVuSans-Oblique-4d" transform="translate(2251.953125 0.015625)"/>
     <use xlink:href="#DejaVuSans-3d" transform="translate(2357.714844 0.015625)"/>
     <use xlink:href="#DejaVuSans-30" transform="translate(2460.986328 0.015625)"/>
     <use xlink:href="#DejaVuSans-2e" transform="translate(2524.609375 0.015625)"/>
     <use xlink:href="#DejaVuSans-31" transform="translate(2556.396484 0.015625)"/>
    </g>
   </g>
   <g id="legend_1">
    <g id="patch_7">
     <path d="M 531.760938 89.0325
L 714.760938 89.0325
Q 716.760938 89.0325 716.760938 87.0325
L 716.760938 29.32
Q 716.760938 27.32 714.760938 27.32
L 531.760938 27.32
Q 529.760938 27.32 529.760938 29.32
L 529.760938 87.0325
Q 529.760938 89.0325 531.760938 89.0325
z
" style="fill: #ffffff; opacity: 0.8; stroke: #cccccc; stroke-linejoin: miter"/>
    </g>
    <g id="line2d_39">
     <path d="M 533.760938 35.418437
L 543.760938 35.418437
L 553.760938 35.418437
" style="fill: none; stroke: #1f77b4; stroke-width: 1.5; stroke-linecap: square"/>
    </g>
    <g id="text_21">
     <!-- $\alpha = -2$; $Re = 100000$; $M = 0.1$ -->
     <g transform="translate(561.760938 38.918437) scale(0.1 -0.1)">
      <defs>
       <path id="DejaVuSans-3b" d="M 750 3309
L 1409 3309
L 1409 2516
L 750 2516
L 750 3309
z
M 750 794
L 1409 794
L 1409 256
L 897 -744
L 494 -744
L 750 256
L 750 794
z
" transform="scale(0.015625)"/>
      </defs>
      <use xlink:href="#DejaVuSans-Oblique-3b1" transform="translate(0 0.78125)"/>
      <use xlink:href="#DejaVuSans-3d" transform="translate(85.400391 0.78125)"/>
      <use xlink:href="#DejaVuSans-2212" transform="translate(208.154297 0.78125)"/>
      <use xlink:href="#DejaVuSans-32" transform="translate(311.425781 0.78125)"/>
      <use xlink:href="#DejaVuSans-3b" transform="translate(375.048828 0.78125)"/>
      <use xlink:href="#DejaVuSans-20" transform="translate(408.740234 0.78125)"/>
      <use xlink:href="#DejaVuSans-Oblique-52" transform="translate(440.527344 0.78125)"/>
      <use xlink:href="#DejaVuSans-Oblique-65" transform="translate(510.009766 0.78125)"/>
      <use xlink:href="#DejaVuSans-3d" transform="translate(591.015625 0.78125)"/>
      <use xlink:href="#DejaVuSans-31" transform="translate(694.287109 0.78125)"/>
      <use xlink:href="#DejaVuSans-30" transform="translate(757.910156 0.78125)"/>
      <use xlink:href="#DejaVuSans-30" transform="translate(821.533203 0.78125)"/>
      <use xlink:href="#DejaVuSans-30" transform="translate(885.15625 0.78125)"/>
      <use xlink:href="#DejaVuSans-30" transform="translate(948.779297 0.78125)"/>
      <use xlink:href="#DejaVuSans-30" transform="translate(1012.402344 0.78125)"/>
      <use xlink:href="#DejaVuSans-3b" transform="translate(1076.025391 0.78125)"/>
      <use xlink:href="#DejaVuSans-20" transform="translate(1109.716797 0.78125)"/>
      <use xlink:href="#DejaVuSans-Oblique-4d" transform="translate(1141.503906 0.78125)"/>
      <use xlink:href="#DejaVuSans-3d" transform="translate(1247.265625 0.78125)"/>
      <use xlink:href="#DejaVuSans-30" transform="translate(1350.537109 0.78125)"/>
      <use xlink:href="#DejaVuSans-2e" transform="translate(1414.160156 0.78125)"/>
      <use xlink:href="#DejaVuSans-31" transform="translate(1445.947266 0.78125)"/>
     </g>
    </g>
    <g id="line2d_40">
     <path d="M 533.760938 50.096563
L 543.760938 50.096563
L 553.760938 50.096563
" style="fill: none; stroke: #ff7f0e; stroke-width: 1.5; stroke-linecap: square"/>
    </g>
    <g id="text_22">
     <!-- $\alpha = 0$; $Re = 100000$; $M = 0.1$ -->
     <g transform="translate(561.760938 53.596563) scale(0.1 -0.1)">
      <use xlink:href="#DejaVuSans-Oblique-3b1" transform="translate(0 0.78125)"/>
      <use xlink:href="#DejaVuSans-3d" transform="translate(85.400391 0.78125)"/>
      <use xlink:href="#DejaVuSans-30" transform="translate(188.671875 0.78125)"/>
      <use xlink:href="#DejaVuSans-3b" transform="translate(252.294922 0.78125)"/>
      <use xlink:href="#DejaVuSans-20" transform="translate(285.986328 0.78125)"/>
      <use xlink:href="#DejaVuSans-Oblique-52" transform="translate(317.773438 0.78125)"/>
      <use xlink:href="#DejaVuSans-Oblique-65" transform="translate(387.255859 0.78125)"/>
      <use xlink:href="#DejaVuSans-3d" transform="translate(468.261719 0.78125)"/>
      <use xlink:href="#DejaVuSans-31" transform="translate(571.533203 0.78125)"/>
      <use xlink:href="#DejaVuSans-30" transform="translate(635.15625 0.78125)"/>
      <use xlink:href="#DejaVuSans-30" transform="translate(698.779297 0.78125)"/>
      <use xlink:href="#DejaVuSans-30" transform="translate(762.402344 0.78125)"/>
      <use xlink:href="#DejaVuSans-30" transform="translate(826.025391 0.78125)"/>
      <use xlink:href="#DejaVuSans-30" transform="translate(889.648438 0.78125)"/>
      <use xlink:href="#DejaVuSans-3b" transform="translate(953.271484 0.78125)"/>
      <use xlink:href="#DejaVuSans-20" transform="translate(986.962891 0.78125)"/>
      <use xlink:href="#DejaVuSans-Oblique-4d" transform="translate(1018.75 0.78125)"/>
      <use xlink:href="#DejaVuSans-3d" transform="translate(1124.511719 0.78125)"/>
      <use xlink:href="#DejaVuSans-30" transform="translate(1227.783203 0.78125)"/>
      <use xlink:href="#DejaVuSans-2e" transform="translate(1291.40625 0.78125)"/>
      <use xlink:href="#DejaVuSans-31" transform="translate(1323.193359 0.78125)"/>
     </g>
    </g>
    <g id="line2d_41">
     <path d="M 533.760938 64.774687
L 543.760938 64.774687
L 553.760938 64.774687
" style="fill: none; stroke: #2ca02c; stroke-width: 1.5; stroke-linecap: square"/>
    </g>
    <g id="text_23">
     <!-- $\alpha = 4$; $Re = 100000$; $M = 0.1$ -->
     <g transform="translate(561.760938 68.274687) scale(0.1 -0.1)">
      <defs>
       <path id="DejaVuSans-34" d="M 2419 4116
L 825 1625
L 2419 1625
L 2419 4116
z
M 2253 4666
L 3047 4666
L 3047 1625
L 3713 1625
L 3713 1100
L 3047 1100
L 3047 0
L 2419 0
L 2419 1100
L 313 1100
L 313 1709
L 2253 4666
z
" transform="scale(0.015625)"/>
      </defs>
      <use xlink:href="#DejaVuSans-Oblique-3b1" transform="translate(0 0.78125)"/>
      <use xlink:href="#DejaVuSans-3d" transform="translate(85.400391 0.78125)"/>
      <use xlink:href="#DejaVuSans-34" transform="translate(188.671875 0.78125)"/>
      <use xlink:href="#DejaVuSans-3b" transform="translate(252.294922 0.78125)"/>
      <use xlink:href="#DejaVuSans-20" transform="translate(285.986328 0.78125)"/>
      <use xlink:href="#DejaVuSans-Oblique-52" transform="translate(317.773438 0.78125)"/>
      <use xlink:href="#DejaVuSans-Oblique-65" transform="translate(387.255859 0.78125)"/>
      <use xlink:href="#DejaVuSans-3d" transform="translate(468.261719 0.78125)"/>
      <use xlink:href="#DejaVuSans-31" transform="translate(571.533203 0.78125)"/>
      <use xlink:href="#DejaVuSans-30" transform="translate(635.15625 0.78125)"/>
      <use xlink:href="#DejaVuSans-30" transform="translate(698.779297 0.78125)"/>
      <use xlink:href="#DejaVuSans-30" transform="translate(762.402344 0.78125)"/>
      <use xlink:href="#DejaVuSans-30" transform="translate(826.025391 0.78125)"/>
      <use xlink:href="#DejaVuSans-30" transform="translate(889.648438 0.78125)"/>
      <use xlink:href="#DejaVuSans-3b" transform="translate(953.271484 0.78125)"/>
      <use xlink:href="#DejaVuSans-20" transform="translate(986.962891 0.78125)"/>
      <use xlink:href="#DejaVuSans-Oblique-4d" transform="translate(1018.75 0.78125)"/>
      <use xlink:href="#DejaVuSans-3d" transform="translate(1124.511719 0.78125)"/>
      <use xlink:href="#DejaVuSans-30" transform="translate(1227.783203 0.78125)"/>
      <use xlink:href="#DejaVuSans-2e" transform="translate(1291.40625 0.78125)"/>
      <use xlink:href="#DejaVuSans-31" transform="translate(1323.193359 0.78125)"/>
     </g>
    </g>
    <g id="line2d_42">
     <path d="M 533.760938 79.452812
L 543.760938 79.452812
L 553.760938 79.452812
" style="fill: none; stroke: #d62728; stroke-width: 1.5; stroke-linecap: square"/>
    </g>
    <g id="text_24">
     <!-- $\alpha = 6$; $Re = 100000$; $M = 0.1$ -->
     <g transform="translate(561.760938 82.952812) scale(0.1 -0.1)">
      <defs>
       <path id="DejaVuSans-36" d="M 2113 2584
Q 1688 2584 1439 2293
Q 1191 2003 1191 1497
Q 1191 994 1439 701
Q 1688 409 2113 409
Q 2538 409 2786 701
Q 3034 994 3034 1497
Q 3034 2003 2786 2293
Q 2538 2584 2113 2584
z
M 3366 4563
L 3366 3988
Q 3128 4100 2886 4159
Q 2644 4219 2406 4219
Q 1781 4219 1451 3797
Q 1122 3375 1075 2522
Q 1259 2794 1537 2939
Q 1816 3084 2150 3084
Q 2853 3084 3261 2657
Q 3669 2231 3669 1497
Q 3669 778 3244 343
Q 2819 -91 2113 -91
Q 1303 -91 875 529
Q 447 1150 447 2328
Q 447 3434 972 4092
Q 1497 4750 2381 4750
Q 2619 4750 2861 4703
Q 3103 4656 3366 4563
z
" transform="scale(0.015625)"/>
      </defs>
      <use xlink:href="#DejaVuSans-Oblique-3b1" transform="translate(0 0.78125)"/>
      <use xlink:href="#DejaVuSans-3d" transform="translate(85.400391 0.78125)"/>
      <use xlink:href="#DejaVuSans-36" transform="translate(188.671875 0.78125)"/>
      <use xlink:href="#DejaVuSans-3b" transform="translate(252.294922 0.78125)"/>
      <use xlink:href="#DejaVuSans-20" transform="translate(285.986328 0.78125)"/>
      <use xlink:href="#DejaVuSans-Oblique-52" transform="translate(317.773438 0.78125)"/>
      <use xlink:href="#DejaVuSans-Oblique-65" transform="translate(387.255859 0.78125)"/>
      <use xlink:href="#DejaVuSans-3d" transform="translate(468.261719 0.78125)"/>
      <use xlink:href="#DejaVuSans-31" transform="translate(571.533203 0.78125)"/>
      <use xlink:href="#DejaVuSans-30" transform="translate(635.15625 0.78125)"/>
      <use xlink:href="#DejaVuSans-30" transform="translate(698.779297 0.78125)"/>
      <use xlink:href="#DejaVuSans-30" transform="translate(762.402344 0.78125)"/>
      <use xlink:href="#DejaVuSans-30" transform="translate(826.025391 0.78125)"/>
      <use xlink:href="#DejaVuSans-30" transform="translate(889.648438 0.78125)"/>
      <use xlink:href="#DejaVuSans-3b" transform="translate(953.271484 0.78125)"/>
      <use xlink:href="#DejaVuSans-20" transform="translate(986.962891 0.78125)"/>
      <use xlink:href="#DejaVuSans-Oblique-4d" transform="translate(1018.75 0.78125)"/>
      <use xlink:href="#DejaVuSans-3d" transform="translate(1124.511719 0.78125)"/>
      <use xlink:href="#DejaVuSans-30" transform="translate(1227.783203 0.78125)"/>
      <use xlink:href="#DejaVuSans-2e" transform="translate(1291.40625 0.78125)"/>
      <use xlink:href="#DejaVuSans-31" transform="translate(1323.193359 0.78125)"/>
     </g>
    </g>
   </g>
  </g>
 </g>
 <defs>
  <clipPath id="pfa2ce86669">
   <rect x="52.160938" y="22.32" width="669.6" height="443.52"/>
  </clipPath>
 </defs>
</svg>


#
``` python
# Shows plots for cases in xfoil cases
ax3 = None
for resname in xfoil.results:
    ax3 = xfoil.results[resname].plot_result(yaxis='ds', ax=ax3, ls='-o')
_ = ax3.legend()
```

<svg xmlns:xlink="http://www.w3.org/1999/xlink" width="726.94375pt" height="503.39625pt" viewBox="0 0 726.94375 503.39625" xmlns="http://www.w3.org/2000/svg" version="1.1">
 <metadata>
  <rdf:RDF xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:cc="http://creativecommons.org/ns#" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
   <cc:Work>
    <dc:type rdf:resource="http://purl.org/dc/dcmitype/StillImage"/>
    <dc:date>2023-02-24T16:11:41.074462</dc:date>
    <dc:format>image/svg+xml</dc:format>
    <dc:creator>
     <cc:Agent>
      <dc:title>Matplotlib v3.6.2, https://matplotlib.org/</dc:title>
     </cc:Agent>
    </dc:creator>
   </cc:Work>
  </rdf:RDF>
 </metadata>
 <defs>
  <style type="text/css">*{stroke-linejoin: round; stroke-linecap: butt}</style>
 </defs>
 <g id="figure_1">
  <g id="patch_1">
   <path d="M 0 503.39625
L 726.94375 503.39625
L 726.94375 0
L 0 0
z
" style="fill: #ffffff"/>
  </g>
  <g id="axes_1">
   <g id="patch_2">
    <path d="M 50.14375 465.84
L 719.74375 465.84
L 719.74375 22.32
L 50.14375 22.32
z
" style="fill: #ffffff"/>
   </g>
   <g id="matplotlib.axis_1">
    <g id="xtick_1">
     <g id="line2d_1">
      <path d="M 80.574027 465.84
L 80.574027 22.32
" clip-path="url(#p2dd438812b)" style="fill: none; stroke: #b0b0b0; stroke-width: 0.8; stroke-linecap: square"/>
     </g>
     <g id="line2d_2">
      <defs>
       <path id="m2395bae119" d="M 0 0
L 0 3.5
" style="stroke: #000000; stroke-width: 0.8"/>
      </defs>
      <g>
       <use xlink:href="#m2395bae119" x="80.574027" y="465.84" style="stroke: #000000; stroke-width: 0.8"/>
      </g>
     </g>
     <g id="text_1">
      <!-- 0.00 -->
      <g transform="translate(69.441214 480.438437) scale(0.1 -0.1)">
       <defs>
        <path id="DejaVuSans-30" d="M 2034 4250
Q 1547 4250 1301 3770
Q 1056 3291 1056 2328
Q 1056 1369 1301 889
Q 1547 409 2034 409
Q 2525 409 2770 889
Q 3016 1369 3016 2328
Q 3016 3291 2770 3770
Q 2525 4250 2034 4250
z
M 2034 4750
Q 2819 4750 3233 4129
Q 3647 3509 3647 2328
Q 3647 1150 3233 529
Q 2819 -91 2034 -91
Q 1250 -91 836 529
Q 422 1150 422 2328
Q 422 3509 836 4129
Q 1250 4750 2034 4750
z
" transform="scale(0.015625)"/>
        <path id="DejaVuSans-2e" d="M 684 794
L 1344 794
L 1344 0
L 684 0
L 684 794
z
" transform="scale(0.015625)"/>
       </defs>
       <use xlink:href="#DejaVuSans-30"/>
       <use xlink:href="#DejaVuSans-2e" x="63.623047"/>
       <use xlink:href="#DejaVuSans-30" x="95.410156"/>
       <use xlink:href="#DejaVuSans-30" x="159.033203"/>
      </g>
     </g>
    </g>
    <g id="xtick_2">
     <g id="line2d_3">
      <path d="M 156.661892 465.84
L 156.661892 22.32
" clip-path="url(#p2dd438812b)" style="fill: none; stroke: #b0b0b0; stroke-width: 0.8; stroke-linecap: square"/>
     </g>
     <g id="line2d_4">
      <g>
       <use xlink:href="#m2395bae119" x="156.661892" y="465.84" style="stroke: #000000; stroke-width: 0.8"/>
      </g>
     </g>
     <g id="text_2">
      <!-- 0.25 -->
      <g transform="translate(145.52908 480.438437) scale(0.1 -0.1)">
       <defs>
        <path id="DejaVuSans-32" d="M 1228 531
L 3431 531
L 3431 0
L 469 0
L 469 531
Q 828 903 1448 1529
Q 2069 2156 2228 2338
Q 2531 2678 2651 2914
Q 2772 3150 2772 3378
Q 2772 3750 2511 3984
Q 2250 4219 1831 4219
Q 1534 4219 1204 4116
Q 875 4013 500 3803
L 500 4441
Q 881 4594 1212 4672
Q 1544 4750 1819 4750
Q 2544 4750 2975 4387
Q 3406 4025 3406 3419
Q 3406 3131 3298 2873
Q 3191 2616 2906 2266
Q 2828 2175 2409 1742
Q 1991 1309 1228 531
z
" transform="scale(0.015625)"/>
        <path id="DejaVuSans-35" d="M 691 4666
L 3169 4666
L 3169 4134
L 1269 4134
L 1269 2991
Q 1406 3038 1543 3061
Q 1681 3084 1819 3084
Q 2600 3084 3056 2656
Q 3513 2228 3513 1497
Q 3513 744 3044 326
Q 2575 -91 1722 -91
Q 1428 -91 1123 -41
Q 819 9 494 109
L 494 744
Q 775 591 1075 516
Q 1375 441 1709 441
Q 2250 441 2565 725
Q 2881 1009 2881 1497
Q 2881 1984 2565 2268
Q 2250 2553 1709 2553
Q 1456 2553 1204 2497
Q 953 2441 691 2322
L 691 4666
z
" transform="scale(0.015625)"/>
       </defs>
       <use xlink:href="#DejaVuSans-30"/>
       <use xlink:href="#DejaVuSans-2e" x="63.623047"/>
       <use xlink:href="#DejaVuSans-32" x="95.410156"/>
       <use xlink:href="#DejaVuSans-35" x="159.033203"/>
      </g>
     </g>
    </g>
    <g id="xtick_3">
     <g id="line2d_5">
      <path d="M 232.749758 465.84
L 232.749758 22.32
" clip-path="url(#p2dd438812b)" style="fill: none; stroke: #b0b0b0; stroke-width: 0.8; stroke-linecap: square"/>
     </g>
     <g id="line2d_6">
      <g>
       <use xlink:href="#m2395bae119" x="232.749758" y="465.84" style="stroke: #000000; stroke-width: 0.8"/>
      </g>
     </g>
     <g id="text_3">
      <!-- 0.50 -->
      <g transform="translate(221.616945 480.438437) scale(0.1 -0.1)">
       <use xlink:href="#DejaVuSans-30"/>
       <use xlink:href="#DejaVuSans-2e" x="63.623047"/>
       <use xlink:href="#DejaVuSans-35" x="95.410156"/>
       <use xlink:href="#DejaVuSans-30" x="159.033203"/>
      </g>
     </g>
    </g>
    <g id="xtick_4">
     <g id="line2d_7">
      <path d="M 308.837623 465.84
L 308.837623 22.32
" clip-path="url(#p2dd438812b)" style="fill: none; stroke: #b0b0b0; stroke-width: 0.8; stroke-linecap: square"/>
     </g>
     <g id="line2d_8">
      <g>
       <use xlink:href="#m2395bae119" x="308.837623" y="465.84" style="stroke: #000000; stroke-width: 0.8"/>
      </g>
     </g>
     <g id="text_4">
      <!-- 0.75 -->
      <g transform="translate(297.704811 480.438437) scale(0.1 -0.1)">
       <defs>
        <path id="DejaVuSans-37" d="M 525 4666
L 3525 4666
L 3525 4397
L 1831 0
L 1172 0
L 2766 4134
L 525 4134
L 525 4666
z
" transform="scale(0.015625)"/>
       </defs>
       <use xlink:href="#DejaVuSans-30"/>
       <use xlink:href="#DejaVuSans-2e" x="63.623047"/>
       <use xlink:href="#DejaVuSans-37" x="95.410156"/>
       <use xlink:href="#DejaVuSans-35" x="159.033203"/>
      </g>
     </g>
    </g>
    <g id="xtick_5">
     <g id="line2d_9">
      <path d="M 384.925489 465.84
L 384.925489 22.32
" clip-path="url(#p2dd438812b)" style="fill: none; stroke: #b0b0b0; stroke-width: 0.8; stroke-linecap: square"/>
     </g>
     <g id="line2d_10">
      <g>
       <use xlink:href="#m2395bae119" x="384.925489" y="465.84" style="stroke: #000000; stroke-width: 0.8"/>
      </g>
     </g>
     <g id="text_5">
      <!-- 1.00 -->
      <g transform="translate(373.792676 480.438437) scale(0.1 -0.1)">
       <defs>
        <path id="DejaVuSans-31" d="M 794 531
L 1825 531
L 1825 4091
L 703 3866
L 703 4441
L 1819 4666
L 2450 4666
L 2450 531
L 3481 531
L 3481 0
L 794 0
L 794 531
z
" transform="scale(0.015625)"/>
       </defs>
       <use xlink:href="#DejaVuSans-31"/>
       <use xlink:href="#DejaVuSans-2e" x="63.623047"/>
       <use xlink:href="#DejaVuSans-30" x="95.410156"/>
       <use xlink:href="#DejaVuSans-30" x="159.033203"/>
      </g>
     </g>
    </g>
    <g id="xtick_6">
     <g id="line2d_11">
      <path d="M 461.013354 465.84
L 461.013354 22.32
" clip-path="url(#p2dd438812b)" style="fill: none; stroke: #b0b0b0; stroke-width: 0.8; stroke-linecap: square"/>
     </g>
     <g id="line2d_12">
      <g>
       <use xlink:href="#m2395bae119" x="461.013354" y="465.84" style="stroke: #000000; stroke-width: 0.8"/>
      </g>
     </g>
     <g id="text_6">
      <!-- 1.25 -->
      <g transform="translate(449.880542 480.438437) scale(0.1 -0.1)">
       <use xlink:href="#DejaVuSans-31"/>
       <use xlink:href="#DejaVuSans-2e" x="63.623047"/>
       <use xlink:href="#DejaVuSans-32" x="95.410156"/>
       <use xlink:href="#DejaVuSans-35" x="159.033203"/>
      </g>
     </g>
    </g>
    <g id="xtick_7">
     <g id="line2d_13">
      <path d="M 537.10122 465.84
L 537.10122 22.32
" clip-path="url(#p2dd438812b)" style="fill: none; stroke: #b0b0b0; stroke-width: 0.8; stroke-linecap: square"/>
     </g>
     <g id="line2d_14">
      <g>
       <use xlink:href="#m2395bae119" x="537.10122" y="465.84" style="stroke: #000000; stroke-width: 0.8"/>
      </g>
     </g>
     <g id="text_7">
      <!-- 1.50 -->
      <g transform="translate(525.968408 480.438437) scale(0.1 -0.1)">
       <use xlink:href="#DejaVuSans-31"/>
       <use xlink:href="#DejaVuSans-2e" x="63.623047"/>
       <use xlink:href="#DejaVuSans-35" x="95.410156"/>
       <use xlink:href="#DejaVuSans-30" x="159.033203"/>
      </g>
     </g>
    </g>
    <g id="xtick_8">
     <g id="line2d_15">
      <path d="M 613.189086 465.84
L 613.189086 22.32
" clip-path="url(#p2dd438812b)" style="fill: none; stroke: #b0b0b0; stroke-width: 0.8; stroke-linecap: square"/>
     </g>
     <g id="line2d_16">
      <g>
       <use xlink:href="#m2395bae119" x="613.189086" y="465.84" style="stroke: #000000; stroke-width: 0.8"/>
      </g>
     </g>
     <g id="text_8">
      <!-- 1.75 -->
      <g transform="translate(602.056273 480.438437) scale(0.1 -0.1)">
       <use xlink:href="#DejaVuSans-31"/>
       <use xlink:href="#DejaVuSans-2e" x="63.623047"/>
       <use xlink:href="#DejaVuSans-37" x="95.410156"/>
       <use xlink:href="#DejaVuSans-35" x="159.033203"/>
      </g>
     </g>
    </g>
    <g id="xtick_9">
     <g id="line2d_17">
      <path d="M 689.276951 465.84
L 689.276951 22.32
" clip-path="url(#p2dd438812b)" style="fill: none; stroke: #b0b0b0; stroke-width: 0.8; stroke-linecap: square"/>
     </g>
     <g id="line2d_18">
      <g>
       <use xlink:href="#m2395bae119" x="689.276951" y="465.84" style="stroke: #000000; stroke-width: 0.8"/>
      </g>
     </g>
     <g id="text_9">
      <!-- 2.00 -->
      <g transform="translate(678.144139 480.438437) scale(0.1 -0.1)">
       <use xlink:href="#DejaVuSans-32"/>
       <use xlink:href="#DejaVuSans-2e" x="63.623047"/>
       <use xlink:href="#DejaVuSans-30" x="95.410156"/>
       <use xlink:href="#DejaVuSans-30" x="159.033203"/>
      </g>
     </g>
    </g>
    <g id="text_10">
     <!-- $x$ -->
     <g transform="translate(381.94375 494.116562) scale(0.1 -0.1)">
      <defs>
       <path id="DejaVuSans-Oblique-78" d="M 3841 3500
L 2234 1784
L 3219 0
L 2559 0
L 1819 1388
L 531 0
L -166 0
L 1556 1844
L 641 3500
L 1300 3500
L 1972 2234
L 3144 3500
L 3841 3500
z
" transform="scale(0.015625)"/>
      </defs>
      <use xlink:href="#DejaVuSans-Oblique-78" transform="translate(0 0.3125)"/>
     </g>
    </g>
   </g>
   <g id="matplotlib.axis_2">
    <g id="ytick_1">
     <g id="line2d_19">
      <path d="M 50.14375 447.225005
L 719.74375 447.225005
" clip-path="url(#p2dd438812b)" style="fill: none; stroke: #b0b0b0; stroke-width: 0.8; stroke-linecap: square"/>
     </g>
     <g id="line2d_20">
      <defs>
       <path id="mcc456d89dd" d="M 0 0
L -3.5 0
" style="stroke: #000000; stroke-width: 0.8"/>
      </defs>
      <g>
       <use xlink:href="#mcc456d89dd" x="50.14375" y="447.225005" style="stroke: #000000; stroke-width: 0.8"/>
      </g>
     </g>
     <g id="text_11">
      <!-- 0.00 -->
      <g transform="translate(20.878125 451.024224) scale(0.1 -0.1)">
       <use xlink:href="#DejaVuSans-30"/>
       <use xlink:href="#DejaVuSans-2e" x="63.623047"/>
       <use xlink:href="#DejaVuSans-30" x="95.410156"/>
       <use xlink:href="#DejaVuSans-30" x="159.033203"/>
      </g>
     </g>
    </g>
    <g id="ytick_2">
     <g id="line2d_21">
      <path d="M 50.14375 369.974747
L 719.74375 369.974747
" clip-path="url(#p2dd438812b)" style="fill: none; stroke: #b0b0b0; stroke-width: 0.8; stroke-linecap: square"/>
     </g>
     <g id="line2d_22">
      <g>
       <use xlink:href="#mcc456d89dd" x="50.14375" y="369.974747" style="stroke: #000000; stroke-width: 0.8"/>
      </g>
     </g>
     <g id="text_12">
      <!-- 0.01 -->
      <g transform="translate(20.878125 373.773965) scale(0.1 -0.1)">
       <use xlink:href="#DejaVuSans-30"/>
       <use xlink:href="#DejaVuSans-2e" x="63.623047"/>
       <use xlink:href="#DejaVuSans-30" x="95.410156"/>
       <use xlink:href="#DejaVuSans-31" x="159.033203"/>
      </g>
     </g>
    </g>
    <g id="ytick_3">
     <g id="line2d_23">
      <path d="M 50.14375 292.724488
L 719.74375 292.724488
" clip-path="url(#p2dd438812b)" style="fill: none; stroke: #b0b0b0; stroke-width: 0.8; stroke-linecap: square"/>
     </g>
     <g id="line2d_24">
      <g>
       <use xlink:href="#mcc456d89dd" x="50.14375" y="292.724488" style="stroke: #000000; stroke-width: 0.8"/>
      </g>
     </g>
     <g id="text_13">
      <!-- 0.02 -->
      <g transform="translate(20.878125 296.523707) scale(0.1 -0.1)">
       <use xlink:href="#DejaVuSans-30"/>
       <use xlink:href="#DejaVuSans-2e" x="63.623047"/>
       <use xlink:href="#DejaVuSans-30" x="95.410156"/>
       <use xlink:href="#DejaVuSans-32" x="159.033203"/>
      </g>
     </g>
    </g>
    <g id="ytick_4">
     <g id="line2d_25">
      <path d="M 50.14375 215.474229
L 719.74375 215.474229
" clip-path="url(#p2dd438812b)" style="fill: none; stroke: #b0b0b0; stroke-width: 0.8; stroke-linecap: square"/>
     </g>
     <g id="line2d_26">
      <g>
       <use xlink:href="#mcc456d89dd" x="50.14375" y="215.474229" style="stroke: #000000; stroke-width: 0.8"/>
      </g>
     </g>
     <g id="text_14">
      <!-- 0.03 -->
      <g transform="translate(20.878125 219.273448) scale(0.1 -0.1)">
       <defs>
        <path id="DejaVuSans-33" d="M 2597 2516
Q 3050 2419 3304 2112
Q 3559 1806 3559 1356
Q 3559 666 3084 287
Q 2609 -91 1734 -91
Q 1441 -91 1130 -33
Q 819 25 488 141
L 488 750
Q 750 597 1062 519
Q 1375 441 1716 441
Q 2309 441 2620 675
Q 2931 909 2931 1356
Q 2931 1769 2642 2001
Q 2353 2234 1838 2234
L 1294 2234
L 1294 2753
L 1863 2753
Q 2328 2753 2575 2939
Q 2822 3125 2822 3475
Q 2822 3834 2567 4026
Q 2313 4219 1838 4219
Q 1578 4219 1281 4162
Q 984 4106 628 3988
L 628 4550
Q 988 4650 1302 4700
Q 1616 4750 1894 4750
Q 2613 4750 3031 4423
Q 3450 4097 3450 3541
Q 3450 3153 3228 2886
Q 3006 2619 2597 2516
z
" transform="scale(0.015625)"/>
       </defs>
       <use xlink:href="#DejaVuSans-30"/>
       <use xlink:href="#DejaVuSans-2e" x="63.623047"/>
       <use xlink:href="#DejaVuSans-30" x="95.410156"/>
       <use xlink:href="#DejaVuSans-33" x="159.033203"/>
      </g>
     </g>
    </g>
    <g id="ytick_5">
     <g id="line2d_27">
      <path d="M 50.14375 138.223971
L 719.74375 138.223971
" clip-path="url(#p2dd438812b)" style="fill: none; stroke: #b0b0b0; stroke-width: 0.8; stroke-linecap: square"/>
     </g>
     <g id="line2d_28">
      <g>
       <use xlink:href="#mcc456d89dd" x="50.14375" y="138.223971" style="stroke: #000000; stroke-width: 0.8"/>
      </g>
     </g>
     <g id="text_15">
      <!-- 0.04 -->
      <g transform="translate(20.878125 142.023189) scale(0.1 -0.1)">
       <defs>
        <path id="DejaVuSans-34" d="M 2419 4116
L 825 1625
L 2419 1625
L 2419 4116
z
M 2253 4666
L 3047 4666
L 3047 1625
L 3713 1625
L 3713 1100
L 3047 1100
L 3047 0
L 2419 0
L 2419 1100
L 313 1100
L 313 1709
L 2253 4666
z
" transform="scale(0.015625)"/>
       </defs>
       <use xlink:href="#DejaVuSans-30"/>
       <use xlink:href="#DejaVuSans-2e" x="63.623047"/>
       <use xlink:href="#DejaVuSans-30" x="95.410156"/>
       <use xlink:href="#DejaVuSans-34" x="159.033203"/>
      </g>
     </g>
    </g>
    <g id="ytick_6">
     <g id="line2d_29">
      <path d="M 50.14375 60.973712
L 719.74375 60.973712
" clip-path="url(#p2dd438812b)" style="fill: none; stroke: #b0b0b0; stroke-width: 0.8; stroke-linecap: square"/>
     </g>
     <g id="line2d_30">
      <g>
       <use xlink:href="#mcc456d89dd" x="50.14375" y="60.973712" style="stroke: #000000; stroke-width: 0.8"/>
      </g>
     </g>
     <g id="text_16">
      <!-- 0.05 -->
      <g transform="translate(20.878125 64.772931) scale(0.1 -0.1)">
       <use xlink:href="#DejaVuSans-30"/>
       <use xlink:href="#DejaVuSans-2e" x="63.623047"/>
       <use xlink:href="#DejaVuSans-30" x="95.410156"/>
       <use xlink:href="#DejaVuSans-35" x="159.033203"/>
      </g>
     </g>
    </g>
    <g id="text_17">
     <!-- $\delta^*$ -->
     <g transform="translate(14.798437 250.78) rotate(-90) scale(0.1 -0.1)">
      <defs>
       <path id="DejaVuSans-Oblique-3b4" d="M 3472 4053
Q 3197 4272 2450 4272
Q 1659 4272 1588 3906
Q 1531 3619 2328 3469
Q 2953 3353 3253 3003
Q 3616 2581 3447 1716
Q 3284 888 2763 400
Q 2238 -91 1488 -91
Q 741 -91 406 400
Q 72 888 241 1747
Q 363 2384 891 2900
Q 1097 3100 1353 3213
Q 913 3459 1000 3900
Q 1166 4750 2544 4750
Q 3234 4750 3566 4531
L 3472 4053
z
M 1753 3056
Q 1525 2966 1306 2738
Q 969 2384 847 1747
Q 722 1113 919 756
Q 1119 397 1584 397
Q 2044 397 2381 759
Q 2722 1122 2838 1716
Q 2956 2338 2731 2638
Q 2491 2959 2103 2994
Q 1906 3013 1753 3056
z
" transform="scale(0.015625)"/>
       <path id="DejaVuSans-2a" d="M 3009 3897
L 1888 3291
L 3009 2681
L 2828 2375
L 1778 3009
L 1778 1831
L 1422 1831
L 1422 3009
L 372 2375
L 191 2681
L 1313 3291
L 191 3897
L 372 4206
L 1422 3572
L 1422 4750
L 1778 4750
L 1778 3572
L 2828 4206
L 3009 3897
z
" transform="scale(0.015625)"/>
      </defs>
      <use xlink:href="#DejaVuSans-Oblique-3b4" transform="translate(0 0.765625)"/>
      <use xlink:href="#DejaVuSans-2a" transform="translate(82.019857 39.046875) scale(0.7)"/>
     </g>
    </g>
   </g>
   <g id="line2d_31">
    <path d="M 384.925489 212.137018
L 383.242425 227.865171
L 380.351086 237.498278
L 377.012351 246.907359
L 373.274915 256.455491
L 369.239215 266.173574
L 364.999599 275.907107
L 360.644329 285.524764
L 356.219059 294.902945
L 351.757267 303.972126
L 347.27417 312.72458
L 342.781942 321.121683
L 338.280584 329.14026
L 333.776182 336.76486
L 329.265693 343.964584
L 324.755205 350.808957
L 320.244716 357.220729
L 315.731184 363.192174
L 311.214608 368.769642
L 306.698033 373.922235
L 302.181457 378.680851
L 297.667925 383.04549
L 293.148305 387.016154
L 288.634773 390.623741
L 284.118198 393.868252
L 279.604665 396.803761
L 275.091133 399.391645
L 270.577601 401.786403
L 266.070156 403.87216
L 261.559667 405.818867
L 257.055266 407.533822
L 252.553907 409.109728
L 243.557278 411.906187
L 234.575867 414.331845
L 221.138749 417.475931
L 212.209078 419.353112
L 185.614847 424.397554
L 172.46382 426.707336
L 168.108551 427.387139
L 159.449752 428.916694
L 150.879214 430.399899
L 125.983265 434.617763
L 114.442257 436.82712
L 110.860041 437.398772
L 92.525909 441.508486
L 90.921976 442.103313
L 88.264988 442.69814
L 87.163236 443.192542
L 86.183224 443.377942
L 85.312779 443.779644
L 83.839718 444.17362
L 83.224928 444.536696
L 82.677095 444.590771
L 81.429254 445.231948
L 80.908813 445.185598
L 80.74142 445.68
L 80.631853 445.401899
L 80.631853 445.440524
L 81.782302 444.668022
L 82.199263 444.366746
L 82.677095 444.17362
L 83.224928 443.764194
L 88.264988 441.22266
L 90.921976 440.071631
L 98.768157 437.190197
L 104.301267 435.459791
L 107.466522 434.470987
L 134.097275 427.410314
L 146.630468 424.127178
L 172.46382 416.850203
L 181.216968 414.107819
L 194.444083 409.472804
L 203.309841 406.073792
L 212.209078 402.42758
L 234.575867 392.045145
L 266.070156 376.564194
L 275.091133 372.524005
L 279.604665 370.685449
L 284.118198 369.001393
L 288.634773 367.487288
L 293.148305 366.189484
L 297.664881 365.18523
L 302.181457 364.466803
L 306.698033 364.165527
L 311.214608 364.327753
L 315.731184 365.162055
L 320.244716 366.877011
L 324.755205 369.364469
L 329.265693 372.632155
L 338.280584 379.607854
L 342.781942 382.767389
L 347.27417 385.440248
L 351.757267 387.587805
L 356.219059 389.217786
L 360.644329 390.353365
L 364.999599 391.071792
L 369.239215 391.349893
L 373.274915 391.249468
L 377.012351 390.693266
L 380.351086 389.434087
L 383.242425 387.047054
L 384.925489 373.953135
L 384.955924 138.865148
L 386.657249 172.020959
L 388.626403 189.155066
L 390.909039 206.080598
L 393.550809 223.964033
L 396.612585 242.959871
L 400.155236 262.820913
L 404.260937 282.898255
L 409.014907 302.249445
L 414.523669 319.877954
L 420.902875 335.02673
L 428.289485 347.409946
L 436.844805 357.182104
L 446.751445 364.744904
L 458.228539 370.561848
L 471.519567 375.019188
L 486.913664 378.425925
L 504.742573 381.036984
L 525.389776 383.022315
L 549.305714 384.544145
L 577.001697 385.710624
L 609.080341 386.599002
L 646.232524 387.286529
L 689.25869 387.850456
L 689.25869 387.850456
" clip-path="url(#p2dd438812b)" style="fill: none; stroke: #1f77b4; stroke-width: 1.5; stroke-linecap: square"/>
   </g>
   <g id="line2d_32">
    <path d="M 384.925489 244.945203
L 383.242425 262.202911
L 380.351086 269.464435
L 377.012351 275.590381
L 369.239215 284.42781
L 360.644329 294.72527
L 347.27417 311.318625
L 333.776182 327.996956
L 324.755205 338.727017
L 315.731184 348.931776
L 311.214608 353.813992
L 306.698033 358.510808
L 302.181457 363.045398
L 297.667925 367.379138
L 293.148305 371.488852
L 288.634773 375.428615
L 284.118198 379.136627
L 279.604665 382.620614
L 275.091133 385.90375
L 270.577601 389.001485
L 266.070156 391.85202
L 261.559667 394.532604
L 257.055266 396.989162
L 252.553907 399.29122
L 248.052549 401.438777
L 243.557278 403.393208
L 234.575867 406.938995
L 225.612716 410.052181
L 216.67087 412.77139
L 203.309841 416.402152
L 185.614847 420.573666
L 168.108551 424.312578
L 110.860041 435.961917
L 92.525909 440.766884
L 88.264988 442.072413
L 86.183224 442.945341
L 82.677095 444.359021
L 81.782302 444.953848
L 81.137077 445.054273
L 80.908813 445.525499
L 80.74142 445.309199
L 80.580114 445.479149
L 80.908813 445.262849
L 81.137077 445.370999
L 81.429254 444.884322
L 81.782302 444.861147
L 82.677095 444.443996
L 83.224928 444.12727
L 84.533639 443.609693
L 85.312779 443.200267
L 86.183224 443.053491
L 87.163236 442.489564
L 89.512829 441.732512
L 90.921976 441.20721
L 92.525909 440.836409
L 94.352017 440.179782
L 98.768157 438.943777
L 107.466522 436.757595
L 110.860041 436.116418
L 114.442257 435.15079
L 122.032783 433.64441
L 125.983265 432.717407
L 138.233411 430.384449
L 146.630468 428.654043
L 150.879214 427.74249
L 155.152309 427.008612
L 190.021856 419.623488
L 212.209078 413.991944
L 221.138749 411.43496
L 230.092769 408.538076
L 239.062007 405.231765
L 248.052549 401.438777
L 252.553907 399.283495
L 257.055266 397.004612
L 261.559667 394.501704
L 266.070156 391.85202
L 275.091133 385.880575
L 279.604665 382.589714
L 284.118198 379.098002
L 288.634773 375.382265
L 293.148305 371.450226
L 297.664881 367.332788
L 302.181457 362.983598
L 306.698033 358.449008
L 315.731184 348.862251
L 320.244716 343.825534
L 329.265693 333.304049
L 338.280584 322.365412
L 351.757267 305.594381
L 360.644329 294.570769
L 369.239215 284.25786
L 377.012351 275.412705
L 380.351086 269.286759
L 383.242425 262.025235
L 384.925489 244.759802
L 384.955924 42.48
L 386.657249 82.418384
L 388.626403 102.673402
L 390.909039 123.075195
L 393.550809 144.450341
L 400.155236 193.905957
L 404.260937 222.071401
L 409.017951 250.584472
L 414.523669 277.436662
L 420.902875 300.804865
L 428.289485 319.715728
L 436.844805 334.192427
L 446.754488 344.930213
L 458.231582 352.778839
L 471.525654 358.495358
L 486.919751 362.659147
L 504.751703 365.710532
L 525.40195 367.958515
L 549.320931 369.62712
L 577.023001 370.878575
L 609.107733 371.828753
L 646.269046 372.54718
L 689.307386 373.142007
L 689.307386 373.142007
" clip-path="url(#p2dd438812b)" style="fill: none; stroke: #ff7f0e; stroke-width: 1.5; stroke-linecap: square"/>
   </g>
   <g id="line2d_33">
    <path d="M 384.925489 351.859561
L 383.242425 363.748376
L 380.351086 368.854618
L 377.012351 373.057032
L 373.274915 376.680069
L 369.239215 379.92458
L 364.999599 382.821465
L 360.644329 385.424798
L 356.219059 387.765481
L 351.757267 389.874413
L 347.27417 391.80567
L 342.781942 393.582426
L 338.280584 395.204681
L 333.776182 396.703336
L 324.755205 399.376195
L 315.731184 401.662803
L 306.698033 403.617234
L 297.667925 405.25494
L 293.148305 405.911567
L 288.634773 406.452319
L 284.118198 406.86947
L 279.604665 407.108946
L 275.091133 407.178471
L 270.577601 407.008521
L 266.070156 406.537294
L 261.559667 405.710716
L 257.055266 404.412912
L 252.553907 402.597531
L 248.052549 400.133247
L 243.557278 397.143662
L 234.575867 390.34564
L 230.092769 387.51828
L 225.612716 385.764699
L 221.138749 385.069447
L 216.67087 385.154422
L 212.209078 385.749249
L 207.756416 386.792128
L 203.309841 388.259883
L 194.444083 391.736144
L 181.216968 398.325591
L 172.46382 402.929707
L 159.449752 409.689104
L 150.879214 413.968769
L 142.4152 417.846732
L 130.009835 423.061124
L 118.17665 427.63434
L 104.301267 433.003233
L 98.768157 435.28984
L 92.525909 438.171275
L 84.533639 442.644065
L 80.631853 445.60275
L 80.908813 445.386449
L 81.137077 445.525499
L 81.429254 445.123798
L 82.199263 445.123798
L 82.677095 444.706647
L 88.264988 443.038041
L 89.512829 442.644065
L 104.301267 439.314579
L 122.032783 436.131868
L 130.009835 434.826339
L 221.138749 420.836317
L 248.052549 416.185851
L 257.055266 414.44772
L 266.070156 412.539639
L 275.091133 410.407532
L 284.118198 407.950974
L 288.634773 406.568194
L 293.148305 405.023189
L 297.664881 403.339133
L 302.181457 401.438777
L 306.698033 399.32212
L 311.214608 396.927362
L 315.731184 394.254503
L 320.244716 391.234018
L 324.755205 387.811831
L 329.265693 383.980218
L 333.776182 379.716004
L 338.280584 374.965113
L 342.781942 369.742996
L 347.27417 363.995577
L 351.757267 357.730581
L 356.219059 350.940283
L 360.644329 343.640133
L 364.999599 335.891932
L 369.239215 327.734305
L 373.274915 319.329477
L 377.012351 310.847399
L 380.351086 302.357595
L 383.242425 293.682391
L 384.925489 281.191024
L 384.955924 185.82558
L 386.657249 210.522488
L 388.626403 223.446456
L 390.909039 236.045973
L 393.550809 248.70729
L 396.612585 261.700784
L 400.155236 274.995554
L 404.260937 288.375298
L 409.014907 301.515567
L 414.520625 314.045559
L 420.899832 325.602198
L 428.283398 335.915107
L 436.838718 344.883863
L 446.745358 352.516188
L 458.219408 358.904784
L 471.504349 364.211877
L 486.892359 368.591967
L 504.715181 372.176379
L 525.353254 375.088714
L 549.257017 377.429396
L 576.937783 379.298853
L 608.995122 380.782058
L 646.119914 381.948537
L 689.112601 382.929615
L 689.112601 382.929615
" clip-path="url(#p2dd438812b)" style="fill: none; stroke: #2ca02c; stroke-width: 1.5; stroke-linecap: square"/>
   </g>
   <g id="line2d_34">
    <path d="M 384.925489 281.770401
L 383.242425 293.713291
L 380.351086 302.36532
L 377.012351 310.445697
L 373.274915 318.101198
L 369.239215 325.246847
L 364.999599 331.797669
L 360.644329 337.745939
L 356.219059 343.114832
L 351.757267 347.950698
L 347.27417 352.330787
L 342.781942 356.324626
L 338.280584 359.963113
L 333.776182 363.300324
L 329.265693 366.374884
L 324.755205 369.271769
L 320.244716 371.952353
L 311.214608 376.834569
L 302.181457 381.214659
L 293.148305 385.216223
L 284.118198 388.91651
L 275.091133 392.338696
L 266.070156 395.575482
L 257.055266 398.634592
L 248.052549 401.546927
L 234.575867 405.664366
L 216.67087 410.677908
L 207.756416 413.003141
L 198.872396 415.127523
L 190.021856 416.973804
L 185.614847 417.808107
L 181.216968 418.480184
L 176.834307 419.005486
L 172.46382 419.283587
L 168.108551 419.175436
L 163.768499 418.526534
L 159.449752 417.074229
L 155.152309 414.33957
L 150.879214 410.314832
L 146.630468 405.39399
L 142.4152 401.299726
L 138.233411 399.584771
L 134.097275 399.746996
L 130.009835 401.075701
L 125.983265 403.269608
L 122.032783 406.120143
L 118.17665 409.426454
L 114.442257 412.987691
L 110.860041 416.564378
L 101.39471 426.591461
L 96.424651 431.643628
L 90.921976 436.78077
L 80.580114 445.525499
L 80.631853 445.533225
L 81.429254 445.340099
L 81.782302 445.162423
L 82.199263 445.146973
L 83.224928 444.567596
L 83.839718 444.567596
L 84.533639 444.405371
L 85.312779 443.980494
L 86.183224 443.864619
L 87.163236 443.516993
L 101.39471 440.295657
L 110.860041 438.572976
L 122.032783 436.711245
L 150.879214 432.477931
L 176.834307 428.916694
L 239.062007 420.612291
L 257.055266 418.063033
L 270.577601 416.062251
L 284.118198 413.899244
L 293.148305 412.269263
L 302.181457 410.469332
L 311.214608 408.352675
L 315.731184 407.163021
L 320.244716 405.842042
L 324.755205 404.351112
L 329.265693 402.659331
L 333.776182 400.774425
L 338.280584 398.580517
L 342.781942 396.077609
L 347.27417 393.188449
L 351.757267 389.843513
L 356.219059 386.0119
L 360.644329 381.639536
L 364.999599 376.734144
L 369.239215 371.272551
L 373.274915 365.339731
L 377.012351 359.06701
L 380.351086 352.485288
L 383.242425 345.50959
L 384.925489 335.428431
L 384.955924 169.973827
L 386.657249 190.051169
L 388.626403 200.294553
L 390.909039 210.167136
L 393.550809 220.008819
L 396.609542 230.089978
L 400.155236 240.487863
L 404.260937 251.148399
L 409.014907 261.97116
L 414.517582 272.793921
L 420.893745 283.415832
L 428.277311 293.643766
L 436.829587 303.284598
L 446.733184 312.207003
L 458.201147 320.326005
L 471.480001 327.60298
L 486.858881 334.037926
L 504.669528 339.677195
L 525.292383 344.574861
L 549.174843 348.777276
L 576.828216 352.361688
L 608.852077 355.366723
L 645.934259 357.854181
L 688.872164 360.117614
L 688.872164 360.117614
" clip-path="url(#p2dd438812b)" style="fill: none; stroke: #d62728; stroke-width: 1.5; stroke-linecap: square"/>
   </g>
   <g id="patch_3">
    <path d="M 50.14375 465.84
L 50.14375 22.32
" style="fill: none; stroke: #000000; stroke-width: 0.8; stroke-linejoin: miter; stroke-linecap: square"/>
   </g>
   <g id="patch_4">
    <path d="M 719.74375 465.84
L 719.74375 22.32
" style="fill: none; stroke: #000000; stroke-width: 0.8; stroke-linejoin: miter; stroke-linecap: square"/>
   </g>
   <g id="patch_5">
    <path d="M 50.14375 465.84
L 719.74375 465.84
" style="fill: none; stroke: #000000; stroke-width: 0.8; stroke-linejoin: miter; stroke-linecap: square"/>
   </g>
   <g id="patch_6">
    <path d="M 50.14375 22.32
L 719.74375 22.32
" style="fill: none; stroke: #000000; stroke-width: 0.8; stroke-linejoin: miter; stroke-linecap: square"/>
   </g>
   <g id="text_18">
    <!-- Result plot for $\alpha = -2$ and $Re = 100000$ and $M = 0.1$ -->
    <g transform="translate(227.68375 16.32) scale(0.12 -0.12)">
     <defs>
      <path id="DejaVuSans-52" d="M 2841 2188
Q 3044 2119 3236 1894
Q 3428 1669 3622 1275
L 4263 0
L 3584 0
L 2988 1197
Q 2756 1666 2539 1819
Q 2322 1972 1947 1972
L 1259 1972
L 1259 0
L 628 0
L 628 4666
L 2053 4666
Q 2853 4666 3247 4331
Q 3641 3997 3641 3322
Q 3641 2881 3436 2590
Q 3231 2300 2841 2188
z
M 1259 4147
L 1259 2491
L 2053 2491
Q 2509 2491 2742 2702
Q 2975 2913 2975 3322
Q 2975 3731 2742 3939
Q 2509 4147 2053 4147
L 1259 4147
z
" transform="scale(0.015625)"/>
      <path id="DejaVuSans-65" d="M 3597 1894
L 3597 1613
L 953 1613
Q 991 1019 1311 708
Q 1631 397 2203 397
Q 2534 397 2845 478
Q 3156 559 3463 722
L 3463 178
Q 3153 47 2828 -22
Q 2503 -91 2169 -91
Q 1331 -91 842 396
Q 353 884 353 1716
Q 353 2575 817 3079
Q 1281 3584 2069 3584
Q 2775 3584 3186 3129
Q 3597 2675 3597 1894
z
M 3022 2063
Q 3016 2534 2758 2815
Q 2500 3097 2075 3097
Q 1594 3097 1305 2825
Q 1016 2553 972 2059
L 3022 2063
z
" transform="scale(0.015625)"/>
      <path id="DejaVuSans-73" d="M 2834 3397
L 2834 2853
Q 2591 2978 2328 3040
Q 2066 3103 1784 3103
Q 1356 3103 1142 2972
Q 928 2841 928 2578
Q 928 2378 1081 2264
Q 1234 2150 1697 2047
L 1894 2003
Q 2506 1872 2764 1633
Q 3022 1394 3022 966
Q 3022 478 2636 193
Q 2250 -91 1575 -91
Q 1294 -91 989 -36
Q 684 19 347 128
L 347 722
Q 666 556 975 473
Q 1284 391 1588 391
Q 1994 391 2212 530
Q 2431 669 2431 922
Q 2431 1156 2273 1281
Q 2116 1406 1581 1522
L 1381 1569
Q 847 1681 609 1914
Q 372 2147 372 2553
Q 372 3047 722 3315
Q 1072 3584 1716 3584
Q 2034 3584 2315 3537
Q 2597 3491 2834 3397
z
" transform="scale(0.015625)"/>
      <path id="DejaVuSans-75" d="M 544 1381
L 544 3500
L 1119 3500
L 1119 1403
Q 1119 906 1312 657
Q 1506 409 1894 409
Q 2359 409 2629 706
Q 2900 1003 2900 1516
L 2900 3500
L 3475 3500
L 3475 0
L 2900 0
L 2900 538
Q 2691 219 2414 64
Q 2138 -91 1772 -91
Q 1169 -91 856 284
Q 544 659 544 1381
z
M 1991 3584
L 1991 3584
z
" transform="scale(0.015625)"/>
      <path id="DejaVuSans-6c" d="M 603 4863
L 1178 4863
L 1178 0
L 603 0
L 603 4863
z
" transform="scale(0.015625)"/>
      <path id="DejaVuSans-74" d="M 1172 4494
L 1172 3500
L 2356 3500
L 2356 3053
L 1172 3053
L 1172 1153
Q 1172 725 1289 603
Q 1406 481 1766 481
L 2356 481
L 2356 0
L 1766 0
Q 1100 0 847 248
Q 594 497 594 1153
L 594 3053
L 172 3053
L 172 3500
L 594 3500
L 594 4494
L 1172 4494
z
" transform="scale(0.015625)"/>
      <path id="DejaVuSans-20" transform="scale(0.015625)"/>
      <path id="DejaVuSans-70" d="M 1159 525
L 1159 -1331
L 581 -1331
L 581 3500
L 1159 3500
L 1159 2969
Q 1341 3281 1617 3432
Q 1894 3584 2278 3584
Q 2916 3584 3314 3078
Q 3713 2572 3713 1747
Q 3713 922 3314 415
Q 2916 -91 2278 -91
Q 1894 -91 1617 61
Q 1341 213 1159 525
z
M 3116 1747
Q 3116 2381 2855 2742
Q 2594 3103 2138 3103
Q 1681 3103 1420 2742
Q 1159 2381 1159 1747
Q 1159 1113 1420 752
Q 1681 391 2138 391
Q 2594 391 2855 752
Q 3116 1113 3116 1747
z
" transform="scale(0.015625)"/>
      <path id="DejaVuSans-6f" d="M 1959 3097
Q 1497 3097 1228 2736
Q 959 2375 959 1747
Q 959 1119 1226 758
Q 1494 397 1959 397
Q 2419 397 2687 759
Q 2956 1122 2956 1747
Q 2956 2369 2687 2733
Q 2419 3097 1959 3097
z
M 1959 3584
Q 2709 3584 3137 3096
Q 3566 2609 3566 1747
Q 3566 888 3137 398
Q 2709 -91 1959 -91
Q 1206 -91 779 398
Q 353 888 353 1747
Q 353 2609 779 3096
Q 1206 3584 1959 3584
z
" transform="scale(0.015625)"/>
      <path id="DejaVuSans-66" d="M 2375 4863
L 2375 4384
L 1825 4384
Q 1516 4384 1395 4259
Q 1275 4134 1275 3809
L 1275 3500
L 2222 3500
L 2222 3053
L 1275 3053
L 1275 0
L 697 0
L 697 3053
L 147 3053
L 147 3500
L 697 3500
L 697 3744
Q 697 4328 969 4595
Q 1241 4863 1831 4863
L 2375 4863
z
" transform="scale(0.015625)"/>
      <path id="DejaVuSans-72" d="M 2631 2963
Q 2534 3019 2420 3045
Q 2306 3072 2169 3072
Q 1681 3072 1420 2755
Q 1159 2438 1159 1844
L 1159 0
L 581 0
L 581 3500
L 1159 3500
L 1159 2956
Q 1341 3275 1631 3429
Q 1922 3584 2338 3584
Q 2397 3584 2469 3576
Q 2541 3569 2628 3553
L 2631 2963
z
" transform="scale(0.015625)"/>
      <path id="DejaVuSans-Oblique-3b1" d="M 2619 1628
L 2622 2350
Q 2625 3088 2069 3091
Q 1653 3094 1394 2747
Q 1069 2319 959 1747
Q 825 1059 994 731
Q 1169 397 1547 397
Q 1966 397 2319 1063
L 2619 1628
z
M 2166 3578
Q 3141 3594 3128 2584
Q 3128 2584 3616 3500
L 4128 3500
L 3119 1603
L 3109 919
Q 3109 766 3194 638
Q 3291 488 3391 488
L 3669 488
L 3575 0
L 3228 0
Q 2934 0 2722 263
Q 2622 394 2619 669
Q 2416 334 2066 50
Q 1900 -81 1453 -78
Q 722 -72 456 397
Q 184 884 353 1747
Q 534 2675 1009 3097
Q 1544 3569 2166 3578
z
" transform="scale(0.015625)"/>
      <path id="DejaVuSans-3d" d="M 678 2906
L 4684 2906
L 4684 2381
L 678 2381
L 678 2906
z
M 678 1631
L 4684 1631
L 4684 1100
L 678 1100
L 678 1631
z
" transform="scale(0.015625)"/>
      <path id="DejaVuSans-2212" d="M 678 2272
L 4684 2272
L 4684 1741
L 678 1741
L 678 2272
z
" transform="scale(0.015625)"/>
      <path id="DejaVuSans-61" d="M 2194 1759
Q 1497 1759 1228 1600
Q 959 1441 959 1056
Q 959 750 1161 570
Q 1363 391 1709 391
Q 2188 391 2477 730
Q 2766 1069 2766 1631
L 2766 1759
L 2194 1759
z
M 3341 1997
L 3341 0
L 2766 0
L 2766 531
Q 2569 213 2275 61
Q 1981 -91 1556 -91
Q 1019 -91 701 211
Q 384 513 384 1019
Q 384 1609 779 1909
Q 1175 2209 1959 2209
L 2766 2209
L 2766 2266
Q 2766 2663 2505 2880
Q 2244 3097 1772 3097
Q 1472 3097 1187 3025
Q 903 2953 641 2809
L 641 3341
Q 956 3463 1253 3523
Q 1550 3584 1831 3584
Q 2591 3584 2966 3190
Q 3341 2797 3341 1997
z
" transform="scale(0.015625)"/>
      <path id="DejaVuSans-6e" d="M 3513 2113
L 3513 0
L 2938 0
L 2938 2094
Q 2938 2591 2744 2837
Q 2550 3084 2163 3084
Q 1697 3084 1428 2787
Q 1159 2491 1159 1978
L 1159 0
L 581 0
L 581 3500
L 1159 3500
L 1159 2956
Q 1366 3272 1645 3428
Q 1925 3584 2291 3584
Q 2894 3584 3203 3211
Q 3513 2838 3513 2113
z
" transform="scale(0.015625)"/>
      <path id="DejaVuSans-64" d="M 2906 2969
L 2906 4863
L 3481 4863
L 3481 0
L 2906 0
L 2906 525
Q 2725 213 2448 61
Q 2172 -91 1784 -91
Q 1150 -91 751 415
Q 353 922 353 1747
Q 353 2572 751 3078
Q 1150 3584 1784 3584
Q 2172 3584 2448 3432
Q 2725 3281 2906 2969
z
M 947 1747
Q 947 1113 1208 752
Q 1469 391 1925 391
Q 2381 391 2643 752
Q 2906 1113 2906 1747
Q 2906 2381 2643 2742
Q 2381 3103 1925 3103
Q 1469 3103 1208 2742
Q 947 2381 947 1747
z
" transform="scale(0.015625)"/>
      <path id="DejaVuSans-Oblique-52" d="M 1613 4147
L 1294 2491
L 2106 2491
Q 2584 2491 2879 2755
Q 3175 3019 3175 3444
Q 3175 3784 2976 3965
Q 2778 4147 2406 4147
L 1613 4147
z
M 2772 2241
Q 2972 2194 3105 2009
Q 3238 1825 3413 1275
L 3809 0
L 3144 0
L 2778 1197
Q 2638 1659 2453 1815
Q 2269 1972 1888 1972
L 1191 1972
L 806 0
L 172 0
L 1081 4666
L 2503 4666
Q 3150 4666 3495 4373
Q 3841 4081 3841 3531
Q 3841 3044 3547 2687
Q 3253 2331 2772 2241
z
" transform="scale(0.015625)"/>
      <path id="DejaVuSans-Oblique-65" d="M 3078 2063
Q 3088 2113 3092 2166
Q 3097 2219 3097 2272
Q 3097 2653 2873 2875
Q 2650 3097 2266 3097
Q 1838 3097 1509 2826
Q 1181 2556 1013 2059
L 3078 2063
z
M 3578 1613
L 903 1613
Q 884 1494 878 1425
Q 872 1356 872 1306
Q 872 872 1139 634
Q 1406 397 1894 397
Q 2269 397 2603 481
Q 2938 566 3225 728
L 3116 159
Q 2806 34 2476 -28
Q 2147 -91 1806 -91
Q 1078 -91 686 257
Q 294 606 294 1247
Q 294 1794 489 2264
Q 684 2734 1063 3103
Q 1306 3334 1642 3459
Q 1978 3584 2356 3584
Q 2950 3584 3301 3228
Q 3653 2872 3653 2272
Q 3653 2128 3634 1964
Q 3616 1800 3578 1613
z
" transform="scale(0.015625)"/>
      <path id="DejaVuSans-Oblique-4d" d="M 1081 4666
L 2028 4666
L 2572 1522
L 4378 4666
L 5350 4666
L 4441 0
L 3828 0
L 4622 4091
L 2791 897
L 2175 897
L 1581 4103
L 788 0
L 172 0
L 1081 4666
z
" transform="scale(0.015625)"/>
     </defs>
     <use xlink:href="#DejaVuSans-52" transform="translate(0 0.015625)"/>
     <use xlink:href="#DejaVuSans-65" transform="translate(69.482422 0.015625)"/>
     <use xlink:href="#DejaVuSans-73" transform="translate(131.005859 0.015625)"/>
     <use xlink:href="#DejaVuSans-75" transform="translate(183.105469 0.015625)"/>
     <use xlink:href="#DejaVuSans-6c" transform="translate(246.484375 0.015625)"/>
     <use xlink:href="#DejaVuSans-74" transform="translate(274.267578 0.015625)"/>
     <use xlink:href="#DejaVuSans-20" transform="translate(313.476562 0.015625)"/>
     <use xlink:href="#DejaVuSans-70" transform="translate(345.263672 0.015625)"/>
     <use xlink:href="#DejaVuSans-6c" transform="translate(408.740234 0.015625)"/>
     <use xlink:href="#DejaVuSans-6f" transform="translate(436.523438 0.015625)"/>
     <use xlink:href="#DejaVuSans-74" transform="translate(497.705078 0.015625)"/>
     <use xlink:href="#DejaVuSans-20" transform="translate(536.914062 0.015625)"/>
     <use xlink:href="#DejaVuSans-66" transform="translate(568.701172 0.015625)"/>
     <use xlink:href="#DejaVuSans-6f" transform="translate(603.90625 0.015625)"/>
     <use xlink:href="#DejaVuSans-72" transform="translate(665.087891 0.015625)"/>
     <use xlink:href="#DejaVuSans-20" transform="translate(706.201172 0.015625)"/>
     <use xlink:href="#DejaVuSans-Oblique-3b1" transform="translate(737.988281 0.015625)"/>
     <use xlink:href="#DejaVuSans-3d" transform="translate(823.388672 0.015625)"/>
     <use xlink:href="#DejaVuSans-2212" transform="translate(946.142578 0.015625)"/>
     <use xlink:href="#DejaVuSans-32" transform="translate(1049.414062 0.015625)"/>
     <use xlink:href="#DejaVuSans-20" transform="translate(1113.037109 0.015625)"/>
     <use xlink:href="#DejaVuSans-61" transform="translate(1144.824219 0.015625)"/>
     <use xlink:href="#DejaVuSans-6e" transform="translate(1206.103516 0.015625)"/>
     <use xlink:href="#DejaVuSans-64" transform="translate(1269.482422 0.015625)"/>
     <use xlink:href="#DejaVuSans-20" transform="translate(1332.958984 0.015625)"/>
     <use xlink:href="#DejaVuSans-Oblique-52" transform="translate(1364.746094 0.015625)"/>
     <use xlink:href="#DejaVuSans-Oblique-65" transform="translate(1434.228516 0.015625)"/>
     <use xlink:href="#DejaVuSans-3d" transform="translate(1515.234375 0.015625)"/>
     <use xlink:href="#DejaVuSans-31" transform="translate(1618.505859 0.015625)"/>
     <use xlink:href="#DejaVuSans-30" transform="translate(1682.128906 0.015625)"/>
     <use xlink:href="#DejaVuSans-30" transform="translate(1745.751953 0.015625)"/>
     <use xlink:href="#DejaVuSans-30" transform="translate(1809.375 0.015625)"/>
     <use xlink:href="#DejaVuSans-30" transform="translate(1872.998047 0.015625)"/>
     <use xlink:href="#DejaVuSans-30" transform="translate(1936.621094 0.015625)"/>
     <use xlink:href="#DejaVuSans-20" transform="translate(2000.244141 0.015625)"/>
     <use xlink:href="#DejaVuSans-61" transform="translate(2032.03125 0.015625)"/>
     <use xlink:href="#DejaVuSans-6e" transform="translate(2093.310547 0.015625)"/>
     <use xlink:href="#DejaVuSans-64" transform="translate(2156.689453 0.015625)"/>
     <use xlink:href="#DejaVuSans-20" transform="translate(2220.166016 0.015625)"/>
     <use xlink:href="#DejaVuSans-Oblique-4d" transform="translate(2251.953125 0.015625)"/>
     <use xlink:href="#DejaVuSans-3d" transform="translate(2357.714844 0.015625)"/>
     <use xlink:href="#DejaVuSans-30" transform="translate(2460.986328 0.015625)"/>
     <use xlink:href="#DejaVuSans-2e" transform="translate(2524.609375 0.015625)"/>
     <use xlink:href="#DejaVuSans-31" transform="translate(2556.396484 0.015625)"/>
    </g>
   </g>
   <g id="legend_1">
    <g id="patch_7">
     <path d="M 529.74375 89.0325
L 712.74375 89.0325
Q 714.74375 89.0325 714.74375 87.0325
L 714.74375 29.32
Q 714.74375 27.32 712.74375 27.32
L 529.74375 27.32
Q 527.74375 27.32 527.74375 29.32
L 527.74375 87.0325
Q 527.74375 89.0325 529.74375 89.0325
z
" style="fill: #ffffff; opacity: 0.8; stroke: #cccccc; stroke-linejoin: miter"/>
    </g>
    <g id="line2d_35">
     <path d="M 531.74375 35.418437
L 541.74375 35.418437
L 551.74375 35.418437
" style="fill: none; stroke: #1f77b4; stroke-width: 1.5; stroke-linecap: square"/>
    </g>
    <g id="text_19">
     <!-- $\alpha = -2$; $Re = 100000$; $M = 0.1$ -->
     <g transform="translate(559.74375 38.918437) scale(0.1 -0.1)">
      <defs>
       <path id="DejaVuSans-3b" d="M 750 3309
L 1409 3309
L 1409 2516
L 750 2516
L 750 3309
z
M 750 794
L 1409 794
L 1409 256
L 897 -744
L 494 -744
L 750 256
L 750 794
z
" transform="scale(0.015625)"/>
      </defs>
      <use xlink:href="#DejaVuSans-Oblique-3b1" transform="translate(0 0.78125)"/>
      <use xlink:href="#DejaVuSans-3d" transform="translate(85.400391 0.78125)"/>
      <use xlink:href="#DejaVuSans-2212" transform="translate(208.154297 0.78125)"/>
      <use xlink:href="#DejaVuSans-32" transform="translate(311.425781 0.78125)"/>
      <use xlink:href="#DejaVuSans-3b" transform="translate(375.048828 0.78125)"/>
      <use xlink:href="#DejaVuSans-20" transform="translate(408.740234 0.78125)"/>
      <use xlink:href="#DejaVuSans-Oblique-52" transform="translate(440.527344 0.78125)"/>
      <use xlink:href="#DejaVuSans-Oblique-65" transform="translate(510.009766 0.78125)"/>
      <use xlink:href="#DejaVuSans-3d" transform="translate(591.015625 0.78125)"/>
      <use xlink:href="#DejaVuSans-31" transform="translate(694.287109 0.78125)"/>
      <use xlink:href="#DejaVuSans-30" transform="translate(757.910156 0.78125)"/>
      <use xlink:href="#DejaVuSans-30" transform="translate(821.533203 0.78125)"/>
      <use xlink:href="#DejaVuSans-30" transform="translate(885.15625 0.78125)"/>
      <use xlink:href="#DejaVuSans-30" transform="translate(948.779297 0.78125)"/>
      <use xlink:href="#DejaVuSans-30" transform="translate(1012.402344 0.78125)"/>
      <use xlink:href="#DejaVuSans-3b" transform="translate(1076.025391 0.78125)"/>
      <use xlink:href="#DejaVuSans-20" transform="translate(1109.716797 0.78125)"/>
      <use xlink:href="#DejaVuSans-Oblique-4d" transform="translate(1141.503906 0.78125)"/>
      <use xlink:href="#DejaVuSans-3d" transform="translate(1247.265625 0.78125)"/>
      <use xlink:href="#DejaVuSans-30" transform="translate(1350.537109 0.78125)"/>
      <use xlink:href="#DejaVuSans-2e" transform="translate(1414.160156 0.78125)"/>
      <use xlink:href="#DejaVuSans-31" transform="translate(1445.947266 0.78125)"/>
     </g>
    </g>
    <g id="line2d_36">
     <path d="M 531.74375 50.096563
L 541.74375 50.096563
L 551.74375 50.096563
" style="fill: none; stroke: #ff7f0e; stroke-width: 1.5; stroke-linecap: square"/>
    </g>
    <g id="text_20">
     <!-- $\alpha = 0$; $Re = 100000$; $M = 0.1$ -->
     <g transform="translate(559.74375 53.596563) scale(0.1 -0.1)">
      <use xlink:href="#DejaVuSans-Oblique-3b1" transform="translate(0 0.78125)"/>
      <use xlink:href="#DejaVuSans-3d" transform="translate(85.400391 0.78125)"/>
      <use xlink:href="#DejaVuSans-30" transform="translate(188.671875 0.78125)"/>
      <use xlink:href="#DejaVuSans-3b" transform="translate(252.294922 0.78125)"/>
      <use xlink:href="#DejaVuSans-20" transform="translate(285.986328 0.78125)"/>
      <use xlink:href="#DejaVuSans-Oblique-52" transform="translate(317.773438 0.78125)"/>
      <use xlink:href="#DejaVuSans-Oblique-65" transform="translate(387.255859 0.78125)"/>
      <use xlink:href="#DejaVuSans-3d" transform="translate(468.261719 0.78125)"/>
      <use xlink:href="#DejaVuSans-31" transform="translate(571.533203 0.78125)"/>
      <use xlink:href="#DejaVuSans-30" transform="translate(635.15625 0.78125)"/>
      <use xlink:href="#DejaVuSans-30" transform="translate(698.779297 0.78125)"/>
      <use xlink:href="#DejaVuSans-30" transform="translate(762.402344 0.78125)"/>
      <use xlink:href="#DejaVuSans-30" transform="translate(826.025391 0.78125)"/>
      <use xlink:href="#DejaVuSans-30" transform="translate(889.648438 0.78125)"/>
      <use xlink:href="#DejaVuSans-3b" transform="translate(953.271484 0.78125)"/>
      <use xlink:href="#DejaVuSans-20" transform="translate(986.962891 0.78125)"/>
      <use xlink:href="#DejaVuSans-Oblique-4d" transform="translate(1018.75 0.78125)"/>
      <use xlink:href="#DejaVuSans-3d" transform="translate(1124.511719 0.78125)"/>
      <use xlink:href="#DejaVuSans-30" transform="translate(1227.783203 0.78125)"/>
      <use xlink:href="#DejaVuSans-2e" transform="translate(1291.40625 0.78125)"/>
      <use xlink:href="#DejaVuSans-31" transform="translate(1323.193359 0.78125)"/>
     </g>
    </g>
    <g id="line2d_37">
     <path d="M 531.74375 64.774687
L 541.74375 64.774687
L 551.74375 64.774687
" style="fill: none; stroke: #2ca02c; stroke-width: 1.5; stroke-linecap: square"/>
    </g>
    <g id="text_21">
     <!-- $\alpha = 4$; $Re = 100000$; $M = 0.1$ -->
     <g transform="translate(559.74375 68.274687) scale(0.1 -0.1)">
      <use xlink:href="#DejaVuSans-Oblique-3b1" transform="translate(0 0.78125)"/>
      <use xlink:href="#DejaVuSans-3d" transform="translate(85.400391 0.78125)"/>
      <use xlink:href="#DejaVuSans-34" transform="translate(188.671875 0.78125)"/>
      <use xlink:href="#DejaVuSans-3b" transform="translate(252.294922 0.78125)"/>
      <use xlink:href="#DejaVuSans-20" transform="translate(285.986328 0.78125)"/>
      <use xlink:href="#DejaVuSans-Oblique-52" transform="translate(317.773438 0.78125)"/>
      <use xlink:href="#DejaVuSans-Oblique-65" transform="translate(387.255859 0.78125)"/>
      <use xlink:href="#DejaVuSans-3d" transform="translate(468.261719 0.78125)"/>
      <use xlink:href="#DejaVuSans-31" transform="translate(571.533203 0.78125)"/>
      <use xlink:href="#DejaVuSans-30" transform="translate(635.15625 0.78125)"/>
      <use xlink:href="#DejaVuSans-30" transform="translate(698.779297 0.78125)"/>
      <use xlink:href="#DejaVuSans-30" transform="translate(762.402344 0.78125)"/>
      <use xlink:href="#DejaVuSans-30" transform="translate(826.025391 0.78125)"/>
      <use xlink:href="#DejaVuSans-30" transform="translate(889.648438 0.78125)"/>
      <use xlink:href="#DejaVuSans-3b" transform="translate(953.271484 0.78125)"/>
      <use xlink:href="#DejaVuSans-20" transform="translate(986.962891 0.78125)"/>
      <use xlink:href="#DejaVuSans-Oblique-4d" transform="translate(1018.75 0.78125)"/>
      <use xlink:href="#DejaVuSans-3d" transform="translate(1124.511719 0.78125)"/>
      <use xlink:href="#DejaVuSans-30" transform="translate(1227.783203 0.78125)"/>
      <use xlink:href="#DejaVuSans-2e" transform="translate(1291.40625 0.78125)"/>
      <use xlink:href="#DejaVuSans-31" transform="translate(1323.193359 0.78125)"/>
     </g>
    </g>
    <g id="line2d_38">
     <path d="M 531.74375 79.452812
L 541.74375 79.452812
L 551.74375 79.452812
" style="fill: none; stroke: #d62728; stroke-width: 1.5; stroke-linecap: square"/>
    </g>
    <g id="text_22">
     <!-- $\alpha = 6$; $Re = 100000$; $M = 0.1$ -->
     <g transform="translate(559.74375 82.952812) scale(0.1 -0.1)">
      <defs>
       <path id="DejaVuSans-36" d="M 2113 2584
Q 1688 2584 1439 2293
Q 1191 2003 1191 1497
Q 1191 994 1439 701
Q 1688 409 2113 409
Q 2538 409 2786 701
Q 3034 994 3034 1497
Q 3034 2003 2786 2293
Q 2538 2584 2113 2584
z
M 3366 4563
L 3366 3988
Q 3128 4100 2886 4159
Q 2644 4219 2406 4219
Q 1781 4219 1451 3797
Q 1122 3375 1075 2522
Q 1259 2794 1537 2939
Q 1816 3084 2150 3084
Q 2853 3084 3261 2657
Q 3669 2231 3669 1497
Q 3669 778 3244 343
Q 2819 -91 2113 -91
Q 1303 -91 875 529
Q 447 1150 447 2328
Q 447 3434 972 4092
Q 1497 4750 2381 4750
Q 2619 4750 2861 4703
Q 3103 4656 3366 4563
z
" transform="scale(0.015625)"/>
      </defs>
      <use xlink:href="#DejaVuSans-Oblique-3b1" transform="translate(0 0.78125)"/>
      <use xlink:href="#DejaVuSans-3d" transform="translate(85.400391 0.78125)"/>
      <use xlink:href="#DejaVuSans-36" transform="translate(188.671875 0.78125)"/>
      <use xlink:href="#DejaVuSans-3b" transform="translate(252.294922 0.78125)"/>
      <use xlink:href="#DejaVuSans-20" transform="translate(285.986328 0.78125)"/>
      <use xlink:href="#DejaVuSans-Oblique-52" transform="translate(317.773438 0.78125)"/>
      <use xlink:href="#DejaVuSans-Oblique-65" transform="translate(387.255859 0.78125)"/>
      <use xlink:href="#DejaVuSans-3d" transform="translate(468.261719 0.78125)"/>
      <use xlink:href="#DejaVuSans-31" transform="translate(571.533203 0.78125)"/>
      <use xlink:href="#DejaVuSans-30" transform="translate(635.15625 0.78125)"/>
      <use xlink:href="#DejaVuSans-30" transform="translate(698.779297 0.78125)"/>
      <use xlink:href="#DejaVuSans-30" transform="translate(762.402344 0.78125)"/>
      <use xlink:href="#DejaVuSans-30" transform="translate(826.025391 0.78125)"/>
      <use xlink:href="#DejaVuSans-30" transform="translate(889.648438 0.78125)"/>
      <use xlink:href="#DejaVuSans-3b" transform="translate(953.271484 0.78125)"/>
      <use xlink:href="#DejaVuSans-20" transform="translate(986.962891 0.78125)"/>
      <use xlink:href="#DejaVuSans-Oblique-4d" transform="translate(1018.75 0.78125)"/>
      <use xlink:href="#DejaVuSans-3d" transform="translate(1124.511719 0.78125)"/>
      <use xlink:href="#DejaVuSans-30" transform="translate(1227.783203 0.78125)"/>
      <use xlink:href="#DejaVuSans-2e" transform="translate(1291.40625 0.78125)"/>
      <use xlink:href="#DejaVuSans-31" transform="translate(1323.193359 0.78125)"/>
     </g>
    </g>
   </g>
  </g>
 </g>
 <defs>
  <clipPath id="p2dd438812b">
   <rect x="50.14375" y="22.32" width="669.6" height="443.52"/>
  </clipPath>
 </defs>
</svg>


#
``` python
# Run the xfoil in polar mode from alpha min to alpha max with interval
re = 100000.0
almin = -10.0
almax = 10.0
alint = 0.5
polar1 = xfoil.run_polar(almin, almax, alint, mach=mach, re=re)
```

#
``` python
# Run the xfoil in polar mode from alpha min to alpha max with interval
re = 200000.0
almin = -10.0
almax = 10.0
alint = 0.5
polar2 = xfoil.run_polar(almin, almax, alint, mach=mach, re=re)
```

#
``` python
# Plot two polars created above
axp1 = None
axp1 = polar1.plot_polar(ax=axp1)
axp1 = polar2.plot_polar(ax=axp1)
_ = axp1.legend()
```

<svg xmlns:xlink="http://www.w3.org/1999/xlink" width="735.323438pt" height="503.39625pt" viewBox="0 0 735.323438 503.39625" xmlns="http://www.w3.org/2000/svg" version="1.1">
 <metadata>
  <rdf:RDF xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:cc="http://creativecommons.org/ns#" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
   <cc:Work>
    <dc:type rdf:resource="http://purl.org/dc/dcmitype/StillImage"/>
    <dc:date>2023-02-24T16:11:45.125820</dc:date>
    <dc:format>image/svg+xml</dc:format>
    <dc:creator>
     <cc:Agent>
      <dc:title>Matplotlib v3.6.2, https://matplotlib.org/</dc:title>
     </cc:Agent>
    </dc:creator>
   </cc:Work>
  </rdf:RDF>
 </metadata>
 <defs>
  <style type="text/css">*{stroke-linejoin: round; stroke-linecap: butt}</style>
 </defs>
 <g id="figure_1">
  <g id="patch_1">
   <path d="M 0 503.39625
L 735.323438 503.39625
L 735.323438 0
L 0 0
z
" style="fill: #ffffff"/>
  </g>
  <g id="axes_1">
   <g id="patch_2">
    <path d="M 58.523438 465.84
L 728.123438 465.84
L 728.123438 22.32
L 58.523438 22.32
z
" style="fill: #ffffff"/>
   </g>
   <g id="matplotlib.axis_1">
    <g id="xtick_1">
     <g id="line2d_1">
      <path d="M 81.031371 465.84
L 81.031371 22.32
" clip-path="url(#pd13b6a2ddb)" style="fill: none; stroke: #b0b0b0; stroke-width: 0.8; stroke-linecap: square"/>
     </g>
     <g id="line2d_2">
      <defs>
       <path id="m52a023c4bc" d="M 0 0
L 0 3.5
" style="stroke: #000000; stroke-width: 0.8"/>
      </defs>
      <g>
       <use xlink:href="#m52a023c4bc" x="81.031371" y="465.84" style="stroke: #000000; stroke-width: 0.8"/>
      </g>
     </g>
     <g id="text_1">
      <!-- 0.010 -->
      <g transform="translate(66.717308 480.438437) scale(0.1 -0.1)">
       <defs>
        <path id="DejaVuSans-30" d="M 2034 4250
Q 1547 4250 1301 3770
Q 1056 3291 1056 2328
Q 1056 1369 1301 889
Q 1547 409 2034 409
Q 2525 409 2770 889
Q 3016 1369 3016 2328
Q 3016 3291 2770 3770
Q 2525 4250 2034 4250
z
M 2034 4750
Q 2819 4750 3233 4129
Q 3647 3509 3647 2328
Q 3647 1150 3233 529
Q 2819 -91 2034 -91
Q 1250 -91 836 529
Q 422 1150 422 2328
Q 422 3509 836 4129
Q 1250 4750 2034 4750
z
" transform="scale(0.015625)"/>
        <path id="DejaVuSans-2e" d="M 684 794
L 1344 794
L 1344 0
L 684 0
L 684 794
z
" transform="scale(0.015625)"/>
        <path id="DejaVuSans-31" d="M 794 531
L 1825 531
L 1825 4091
L 703 3866
L 703 4441
L 1819 4666
L 2450 4666
L 2450 531
L 3481 531
L 3481 0
L 794 0
L 794 531
z
" transform="scale(0.015625)"/>
       </defs>
       <use xlink:href="#DejaVuSans-30"/>
       <use xlink:href="#DejaVuSans-2e" x="63.623047"/>
       <use xlink:href="#DejaVuSans-30" x="95.410156"/>
       <use xlink:href="#DejaVuSans-31" x="159.033203"/>
       <use xlink:href="#DejaVuSans-30" x="222.65625"/>
      </g>
     </g>
    </g>
    <g id="xtick_2">
     <g id="line2d_3">
      <path d="M 169.125043 465.84
L 169.125043 22.32
" clip-path="url(#pd13b6a2ddb)" style="fill: none; stroke: #b0b0b0; stroke-width: 0.8; stroke-linecap: square"/>
     </g>
     <g id="line2d_4">
      <g>
       <use xlink:href="#m52a023c4bc" x="169.125043" y="465.84" style="stroke: #000000; stroke-width: 0.8"/>
      </g>
     </g>
     <g id="text_2">
      <!-- 0.015 -->
      <g transform="translate(154.81098 480.438437) scale(0.1 -0.1)">
       <defs>
        <path id="DejaVuSans-35" d="M 691 4666
L 3169 4666
L 3169 4134
L 1269 4134
L 1269 2991
Q 1406 3038 1543 3061
Q 1681 3084 1819 3084
Q 2600 3084 3056 2656
Q 3513 2228 3513 1497
Q 3513 744 3044 326
Q 2575 -91 1722 -91
Q 1428 -91 1123 -41
Q 819 9 494 109
L 494 744
Q 775 591 1075 516
Q 1375 441 1709 441
Q 2250 441 2565 725
Q 2881 1009 2881 1497
Q 2881 1984 2565 2268
Q 2250 2553 1709 2553
Q 1456 2553 1204 2497
Q 953 2441 691 2322
L 691 4666
z
" transform="scale(0.015625)"/>
       </defs>
       <use xlink:href="#DejaVuSans-30"/>
       <use xlink:href="#DejaVuSans-2e" x="63.623047"/>
       <use xlink:href="#DejaVuSans-30" x="95.410156"/>
       <use xlink:href="#DejaVuSans-31" x="159.033203"/>
       <use xlink:href="#DejaVuSans-35" x="222.65625"/>
      </g>
     </g>
    </g>
    <g id="xtick_3">
     <g id="line2d_5">
      <path d="M 257.218714 465.84
L 257.218714 22.32
" clip-path="url(#pd13b6a2ddb)" style="fill: none; stroke: #b0b0b0; stroke-width: 0.8; stroke-linecap: square"/>
     </g>
     <g id="line2d_6">
      <g>
       <use xlink:href="#m52a023c4bc" x="257.218714" y="465.84" style="stroke: #000000; stroke-width: 0.8"/>
      </g>
     </g>
     <g id="text_3">
      <!-- 0.020 -->
      <g transform="translate(242.904652 480.438437) scale(0.1 -0.1)">
       <defs>
        <path id="DejaVuSans-32" d="M 1228 531
L 3431 531
L 3431 0
L 469 0
L 469 531
Q 828 903 1448 1529
Q 2069 2156 2228 2338
Q 2531 2678 2651 2914
Q 2772 3150 2772 3378
Q 2772 3750 2511 3984
Q 2250 4219 1831 4219
Q 1534 4219 1204 4116
Q 875 4013 500 3803
L 500 4441
Q 881 4594 1212 4672
Q 1544 4750 1819 4750
Q 2544 4750 2975 4387
Q 3406 4025 3406 3419
Q 3406 3131 3298 2873
Q 3191 2616 2906 2266
Q 2828 2175 2409 1742
Q 1991 1309 1228 531
z
" transform="scale(0.015625)"/>
       </defs>
       <use xlink:href="#DejaVuSans-30"/>
       <use xlink:href="#DejaVuSans-2e" x="63.623047"/>
       <use xlink:href="#DejaVuSans-30" x="95.410156"/>
       <use xlink:href="#DejaVuSans-32" x="159.033203"/>
       <use xlink:href="#DejaVuSans-30" x="222.65625"/>
      </g>
     </g>
    </g>
    <g id="xtick_4">
     <g id="line2d_7">
      <path d="M 345.312386 465.84
L 345.312386 22.32
" clip-path="url(#pd13b6a2ddb)" style="fill: none; stroke: #b0b0b0; stroke-width: 0.8; stroke-linecap: square"/>
     </g>
     <g id="line2d_8">
      <g>
       <use xlink:href="#m52a023c4bc" x="345.312386" y="465.84" style="stroke: #000000; stroke-width: 0.8"/>
      </g>
     </g>
     <g id="text_4">
      <!-- 0.025 -->
      <g transform="translate(330.998324 480.438437) scale(0.1 -0.1)">
       <use xlink:href="#DejaVuSans-30"/>
       <use xlink:href="#DejaVuSans-2e" x="63.623047"/>
       <use xlink:href="#DejaVuSans-30" x="95.410156"/>
       <use xlink:href="#DejaVuSans-32" x="159.033203"/>
       <use xlink:href="#DejaVuSans-35" x="222.65625"/>
      </g>
     </g>
    </g>
    <g id="xtick_5">
     <g id="line2d_9">
      <path d="M 433.406058 465.84
L 433.406058 22.32
" clip-path="url(#pd13b6a2ddb)" style="fill: none; stroke: #b0b0b0; stroke-width: 0.8; stroke-linecap: square"/>
     </g>
     <g id="line2d_10">
      <g>
       <use xlink:href="#m52a023c4bc" x="433.406058" y="465.84" style="stroke: #000000; stroke-width: 0.8"/>
      </g>
     </g>
     <g id="text_5">
      <!-- 0.030 -->
      <g transform="translate(419.091996 480.438437) scale(0.1 -0.1)">
       <defs>
        <path id="DejaVuSans-33" d="M 2597 2516
Q 3050 2419 3304 2112
Q 3559 1806 3559 1356
Q 3559 666 3084 287
Q 2609 -91 1734 -91
Q 1441 -91 1130 -33
Q 819 25 488 141
L 488 750
Q 750 597 1062 519
Q 1375 441 1716 441
Q 2309 441 2620 675
Q 2931 909 2931 1356
Q 2931 1769 2642 2001
Q 2353 2234 1838 2234
L 1294 2234
L 1294 2753
L 1863 2753
Q 2328 2753 2575 2939
Q 2822 3125 2822 3475
Q 2822 3834 2567 4026
Q 2313 4219 1838 4219
Q 1578 4219 1281 4162
Q 984 4106 628 3988
L 628 4550
Q 988 4650 1302 4700
Q 1616 4750 1894 4750
Q 2613 4750 3031 4423
Q 3450 4097 3450 3541
Q 3450 3153 3228 2886
Q 3006 2619 2597 2516
z
" transform="scale(0.015625)"/>
       </defs>
       <use xlink:href="#DejaVuSans-30"/>
       <use xlink:href="#DejaVuSans-2e" x="63.623047"/>
       <use xlink:href="#DejaVuSans-30" x="95.410156"/>
       <use xlink:href="#DejaVuSans-33" x="159.033203"/>
       <use xlink:href="#DejaVuSans-30" x="222.65625"/>
      </g>
     </g>
    </g>
    <g id="xtick_6">
     <g id="line2d_11">
      <path d="M 521.49973 465.84
L 521.49973 22.32
" clip-path="url(#pd13b6a2ddb)" style="fill: none; stroke: #b0b0b0; stroke-width: 0.8; stroke-linecap: square"/>
     </g>
     <g id="line2d_12">
      <g>
       <use xlink:href="#m52a023c4bc" x="521.49973" y="465.84" style="stroke: #000000; stroke-width: 0.8"/>
      </g>
     </g>
     <g id="text_6">
      <!-- 0.035 -->
      <g transform="translate(507.185668 480.438437) scale(0.1 -0.1)">
       <use xlink:href="#DejaVuSans-30"/>
       <use xlink:href="#DejaVuSans-2e" x="63.623047"/>
       <use xlink:href="#DejaVuSans-30" x="95.410156"/>
       <use xlink:href="#DejaVuSans-33" x="159.033203"/>
       <use xlink:href="#DejaVuSans-35" x="222.65625"/>
      </g>
     </g>
    </g>
    <g id="xtick_7">
     <g id="line2d_13">
      <path d="M 609.593402 465.84
L 609.593402 22.32
" clip-path="url(#pd13b6a2ddb)" style="fill: none; stroke: #b0b0b0; stroke-width: 0.8; stroke-linecap: square"/>
     </g>
     <g id="line2d_14">
      <g>
       <use xlink:href="#m52a023c4bc" x="609.593402" y="465.84" style="stroke: #000000; stroke-width: 0.8"/>
      </g>
     </g>
     <g id="text_7">
      <!-- 0.040 -->
      <g transform="translate(595.279339 480.438437) scale(0.1 -0.1)">
       <defs>
        <path id="DejaVuSans-34" d="M 2419 4116
L 825 1625
L 2419 1625
L 2419 4116
z
M 2253 4666
L 3047 4666
L 3047 1625
L 3713 1625
L 3713 1100
L 3047 1100
L 3047 0
L 2419 0
L 2419 1100
L 313 1100
L 313 1709
L 2253 4666
z
" transform="scale(0.015625)"/>
       </defs>
       <use xlink:href="#DejaVuSans-30"/>
       <use xlink:href="#DejaVuSans-2e" x="63.623047"/>
       <use xlink:href="#DejaVuSans-30" x="95.410156"/>
       <use xlink:href="#DejaVuSans-34" x="159.033203"/>
       <use xlink:href="#DejaVuSans-30" x="222.65625"/>
      </g>
     </g>
    </g>
    <g id="xtick_8">
     <g id="line2d_15">
      <path d="M 697.687074 465.84
L 697.687074 22.32
" clip-path="url(#pd13b6a2ddb)" style="fill: none; stroke: #b0b0b0; stroke-width: 0.8; stroke-linecap: square"/>
     </g>
     <g id="line2d_16">
      <g>
       <use xlink:href="#m52a023c4bc" x="697.687074" y="465.84" style="stroke: #000000; stroke-width: 0.8"/>
      </g>
     </g>
     <g id="text_8">
      <!-- 0.045 -->
      <g transform="translate(683.373011 480.438437) scale(0.1 -0.1)">
       <use xlink:href="#DejaVuSans-30"/>
       <use xlink:href="#DejaVuSans-2e" x="63.623047"/>
       <use xlink:href="#DejaVuSans-30" x="95.410156"/>
       <use xlink:href="#DejaVuSans-34" x="159.033203"/>
       <use xlink:href="#DejaVuSans-35" x="222.65625"/>
      </g>
     </g>
    </g>
    <g id="text_9">
     <!-- $C_d$ -->
     <g transform="translate(387.473437 494.116562) scale(0.1 -0.1)">
      <defs>
       <path id="DejaVuSans-Oblique-43" d="M 4447 4306
L 4319 3641
Q 4019 3944 3683 4091
Q 3347 4238 2956 4238
Q 2422 4238 2017 3981
Q 1613 3725 1319 3200
Q 1131 2863 1032 2486
Q 934 2109 934 1728
Q 934 1091 1264 756
Q 1594 422 2222 422
Q 2656 422 3056 561
Q 3456 700 3834 978
L 3688 231
Q 3316 72 2936 -9
Q 2556 -91 2175 -91
Q 1278 -91 773 396
Q 269 884 269 1753
Q 269 2309 461 2846
Q 653 3384 1013 3828
Q 1394 4300 1883 4525
Q 2372 4750 3022 4750
Q 3422 4750 3780 4639
Q 4138 4528 4447 4306
z
" transform="scale(0.015625)"/>
       <path id="DejaVuSans-Oblique-64" d="M 2675 525
Q 2444 222 2128 65
Q 1813 -91 1428 -91
Q 903 -91 598 267
Q 294 625 294 1247
Q 294 1766 478 2236
Q 663 2706 1013 3078
Q 1244 3325 1534 3454
Q 1825 3584 2144 3584
Q 2481 3584 2739 3421
Q 2997 3259 3138 2956
L 3513 4863
L 4091 4863
L 3144 0
L 2566 0
L 2675 525
z
M 891 1350
Q 891 897 1095 644
Q 1300 391 1663 391
Q 1931 391 2161 520
Q 2391 650 2566 903
Q 2750 1166 2856 1509
Q 2963 1853 2963 2188
Q 2963 2622 2758 2865
Q 2553 3109 2194 3109
Q 1922 3109 1687 2981
Q 1453 2853 1288 2613
Q 1106 2353 998 2009
Q 891 1666 891 1350
z
" transform="scale(0.015625)"/>
      </defs>
      <use xlink:href="#DejaVuSans-Oblique-43" transform="translate(0 0.78125)"/>
      <use xlink:href="#DejaVuSans-Oblique-64" transform="translate(69.824219 -15.625) scale(0.7)"/>
     </g>
    </g>
   </g>
   <g id="matplotlib.axis_2">
    <g id="ytick_1">
     <g id="line2d_17">
      <path d="M 58.523438 447.019265
L 728.123438 447.019265
" clip-path="url(#pd13b6a2ddb)" style="fill: none; stroke: #b0b0b0; stroke-width: 0.8; stroke-linecap: square"/>
     </g>
     <g id="line2d_18">
      <defs>
       <path id="m625aec2627" d="M 0 0
L -3.5 0
" style="stroke: #000000; stroke-width: 0.8"/>
      </defs>
      <g>
       <use xlink:href="#m625aec2627" x="58.523438" y="447.019265" style="stroke: #000000; stroke-width: 0.8"/>
      </g>
     </g>
     <g id="text_10">
      <!-- −1.00 -->
      <g transform="translate(20.878125 450.818484) scale(0.1 -0.1)">
       <defs>
        <path id="DejaVuSans-2212" d="M 678 2272
L 4684 2272
L 4684 1741
L 678 1741
L 678 2272
z
" transform="scale(0.015625)"/>
       </defs>
       <use xlink:href="#DejaVuSans-2212"/>
       <use xlink:href="#DejaVuSans-31" x="83.789062"/>
       <use xlink:href="#DejaVuSans-2e" x="147.412109"/>
       <use xlink:href="#DejaVuSans-30" x="179.199219"/>
       <use xlink:href="#DejaVuSans-30" x="242.822266"/>
      </g>
     </g>
    </g>
    <g id="ytick_2">
     <g id="line2d_19">
      <path d="M 58.523438 396.289522
L 728.123438 396.289522
" clip-path="url(#pd13b6a2ddb)" style="fill: none; stroke: #b0b0b0; stroke-width: 0.8; stroke-linecap: square"/>
     </g>
     <g id="line2d_20">
      <g>
       <use xlink:href="#m625aec2627" x="58.523438" y="396.289522" style="stroke: #000000; stroke-width: 0.8"/>
      </g>
     </g>
     <g id="text_11">
      <!-- −0.75 -->
      <g transform="translate(20.878125 400.088741) scale(0.1 -0.1)">
       <defs>
        <path id="DejaVuSans-37" d="M 525 4666
L 3525 4666
L 3525 4397
L 1831 0
L 1172 0
L 2766 4134
L 525 4134
L 525 4666
z
" transform="scale(0.015625)"/>
       </defs>
       <use xlink:href="#DejaVuSans-2212"/>
       <use xlink:href="#DejaVuSans-30" x="83.789062"/>
       <use xlink:href="#DejaVuSans-2e" x="147.412109"/>
       <use xlink:href="#DejaVuSans-37" x="179.199219"/>
       <use xlink:href="#DejaVuSans-35" x="242.822266"/>
      </g>
     </g>
    </g>
    <g id="ytick_3">
     <g id="line2d_21">
      <path d="M 58.523438 345.559779
L 728.123438 345.559779
" clip-path="url(#pd13b6a2ddb)" style="fill: none; stroke: #b0b0b0; stroke-width: 0.8; stroke-linecap: square"/>
     </g>
     <g id="line2d_22">
      <g>
       <use xlink:href="#m625aec2627" x="58.523438" y="345.559779" style="stroke: #000000; stroke-width: 0.8"/>
      </g>
     </g>
     <g id="text_12">
      <!-- −0.50 -->
      <g transform="translate(20.878125 349.358997) scale(0.1 -0.1)">
       <use xlink:href="#DejaVuSans-2212"/>
       <use xlink:href="#DejaVuSans-30" x="83.789062"/>
       <use xlink:href="#DejaVuSans-2e" x="147.412109"/>
       <use xlink:href="#DejaVuSans-35" x="179.199219"/>
       <use xlink:href="#DejaVuSans-30" x="242.822266"/>
      </g>
     </g>
    </g>
    <g id="ytick_4">
     <g id="line2d_23">
      <path d="M 58.523438 294.830035
L 728.123438 294.830035
" clip-path="url(#pd13b6a2ddb)" style="fill: none; stroke: #b0b0b0; stroke-width: 0.8; stroke-linecap: square"/>
     </g>
     <g id="line2d_24">
      <g>
       <use xlink:href="#m625aec2627" x="58.523438" y="294.830035" style="stroke: #000000; stroke-width: 0.8"/>
      </g>
     </g>
     <g id="text_13">
      <!-- −0.25 -->
      <g transform="translate(20.878125 298.629254) scale(0.1 -0.1)">
       <use xlink:href="#DejaVuSans-2212"/>
       <use xlink:href="#DejaVuSans-30" x="83.789062"/>
       <use xlink:href="#DejaVuSans-2e" x="147.412109"/>
       <use xlink:href="#DejaVuSans-32" x="179.199219"/>
       <use xlink:href="#DejaVuSans-35" x="242.822266"/>
      </g>
     </g>
    </g>
    <g id="ytick_5">
     <g id="line2d_25">
      <path d="M 58.523438 244.100292
L 728.123438 244.100292
" clip-path="url(#pd13b6a2ddb)" style="fill: none; stroke: #b0b0b0; stroke-width: 0.8; stroke-linecap: square"/>
     </g>
     <g id="line2d_26">
      <g>
       <use xlink:href="#m625aec2627" x="58.523438" y="244.100292" style="stroke: #000000; stroke-width: 0.8"/>
      </g>
     </g>
     <g id="text_14">
      <!-- 0.00 -->
      <g transform="translate(29.257812 247.899511) scale(0.1 -0.1)">
       <use xlink:href="#DejaVuSans-30"/>
       <use xlink:href="#DejaVuSans-2e" x="63.623047"/>
       <use xlink:href="#DejaVuSans-30" x="95.410156"/>
       <use xlink:href="#DejaVuSans-30" x="159.033203"/>
      </g>
     </g>
    </g>
    <g id="ytick_6">
     <g id="line2d_27">
      <path d="M 58.523438 193.370549
L 728.123438 193.370549
" clip-path="url(#pd13b6a2ddb)" style="fill: none; stroke: #b0b0b0; stroke-width: 0.8; stroke-linecap: square"/>
     </g>
     <g id="line2d_28">
      <g>
       <use xlink:href="#m625aec2627" x="58.523438" y="193.370549" style="stroke: #000000; stroke-width: 0.8"/>
      </g>
     </g>
     <g id="text_15">
      <!-- 0.25 -->
      <g transform="translate(29.257812 197.169767) scale(0.1 -0.1)">
       <use xlink:href="#DejaVuSans-30"/>
       <use xlink:href="#DejaVuSans-2e" x="63.623047"/>
       <use xlink:href="#DejaVuSans-32" x="95.410156"/>
       <use xlink:href="#DejaVuSans-35" x="159.033203"/>
      </g>
     </g>
    </g>
    <g id="ytick_7">
     <g id="line2d_29">
      <path d="M 58.523438 142.640805
L 728.123438 142.640805
" clip-path="url(#pd13b6a2ddb)" style="fill: none; stroke: #b0b0b0; stroke-width: 0.8; stroke-linecap: square"/>
     </g>
     <g id="line2d_30">
      <g>
       <use xlink:href="#m625aec2627" x="58.523438" y="142.640805" style="stroke: #000000; stroke-width: 0.8"/>
      </g>
     </g>
     <g id="text_16">
      <!-- 0.50 -->
      <g transform="translate(29.257812 146.440024) scale(0.1 -0.1)">
       <use xlink:href="#DejaVuSans-30"/>
       <use xlink:href="#DejaVuSans-2e" x="63.623047"/>
       <use xlink:href="#DejaVuSans-35" x="95.410156"/>
       <use xlink:href="#DejaVuSans-30" x="159.033203"/>
      </g>
     </g>
    </g>
    <g id="ytick_8">
     <g id="line2d_31">
      <path d="M 58.523438 91.911062
L 728.123438 91.911062
" clip-path="url(#pd13b6a2ddb)" style="fill: none; stroke: #b0b0b0; stroke-width: 0.8; stroke-linecap: square"/>
     </g>
     <g id="line2d_32">
      <g>
       <use xlink:href="#m625aec2627" x="58.523438" y="91.911062" style="stroke: #000000; stroke-width: 0.8"/>
      </g>
     </g>
     <g id="text_17">
      <!-- 0.75 -->
      <g transform="translate(29.257812 95.710281) scale(0.1 -0.1)">
       <use xlink:href="#DejaVuSans-30"/>
       <use xlink:href="#DejaVuSans-2e" x="63.623047"/>
       <use xlink:href="#DejaVuSans-37" x="95.410156"/>
       <use xlink:href="#DejaVuSans-35" x="159.033203"/>
      </g>
     </g>
    </g>
    <g id="ytick_9">
     <g id="line2d_33">
      <path d="M 58.523438 41.181319
L 728.123438 41.181319
" clip-path="url(#pd13b6a2ddb)" style="fill: none; stroke: #b0b0b0; stroke-width: 0.8; stroke-linecap: square"/>
     </g>
     <g id="line2d_34">
      <g>
       <use xlink:href="#m625aec2627" x="58.523438" y="41.181319" style="stroke: #000000; stroke-width: 0.8"/>
      </g>
     </g>
     <g id="text_18">
      <!-- 1.00 -->
      <g transform="translate(29.257812 44.980537) scale(0.1 -0.1)">
       <use xlink:href="#DejaVuSans-31"/>
       <use xlink:href="#DejaVuSans-2e" x="63.623047"/>
       <use xlink:href="#DejaVuSans-30" x="95.410156"/>
       <use xlink:href="#DejaVuSans-30" x="159.033203"/>
      </g>
     </g>
    </g>
    <g id="text_19">
     <!-- $C_l$ -->
     <g transform="translate(14.798437 248.73) rotate(-90) scale(0.1 -0.1)">
      <defs>
       <path id="DejaVuSans-Oblique-6c" d="M 1172 4863
L 1747 4863
L 800 0
L 225 0
L 1172 4863
z
" transform="scale(0.015625)"/>
      </defs>
      <use xlink:href="#DejaVuSans-Oblique-43" transform="translate(0 0.78125)"/>
      <use xlink:href="#DejaVuSans-Oblique-6c" transform="translate(69.824219 -15.625) scale(0.7)"/>
     </g>
    </g>
   </g>
   <g id="line2d_35">
    <path d="M 697.158512 437.035652
L 612.764774 434.6615
L 532.423345 431.942386
L 473.576773 425.266351
L 418.253947 418.164187
L 371.388113 410.656185
L 328.926963 402.985848
L 293.33712 395.802516
L 262.15196 389.187358
L 233.60961 383.140372
L 210.352881 377.296306
L 193.086521 371.229029
L 180.929595 364.776205
L 172.296415 358.059587
L 166.482232 351.200926
L 163.663235 344.200221
L 165.248921 336.712511
L 174.939225 326.485395
L 196.786456 307.755974
L 221.981246 277.196376
L 232.023924 244.059708
L 221.981246 210.963624
L 196.786456 180.44461
L 174.939225 161.735481
L 165.248921 151.488072
L 163.663235 144.020654
L 166.482232 137.01995
L 172.296415 130.161288
L 180.753407 123.44467
L 192.910334 116.991847
L 210.176694 110.92457
L 233.60961 105.080503
L 262.15196 99.013226
L 293.33712 92.398067
L 328.926963 85.214736
L 418.077759 70.036397
L 473.400585 62.934233
L 532.423345 56.27849
L 697.687074 51.205516
" clip-path="url(#pd13b6a2ddb)" style="fill: none; stroke: #1f77b4; stroke-width: 1.5; stroke-linecap: square"/>
   </g>
   <g id="line2d_36">
    <path d="M 430.587061 445.68
L 380.90223 438.801047
L 346.36951 432.30764
L 310.60348 425.225767
L 279.065945 418.570025
L 251.404532 412.09691
L 226.914491 405.765838
L 204.186324 399.556517
L 183.043843 393.347197
L 163.663235 387.016125
L 147.277812 380.461842
L 134.592323 373.684348
L 124.725832 366.785103
L 117.325963 359.90615
L 113.097467 344.666935
L 108.868971 328.392833
L 103.054789 312.889824
L 97.416794 297.34623
L 92.835923 280.382204
L 90.016925 262.403583
L 88.959801 244.08
L 90.193113 225.817292
L 92.835923 207.818379
L 97.416794 190.854353
L 103.054789 175.31076
L 108.692784 159.848334
L 113.097467 143.493065
L 117.325963 128.314726
L 124.725832 121.435773
L 134.416136 114.516236
L 147.277812 107.738742
L 163.663235 101.204751
L 183.043843 94.873679
L 204.010137 88.664358
L 227.266866 82.455038
L 251.404532 76.103674
L 310.955854 62.934233
L 345.840948 55.872652
L 430.587061 42.48
" clip-path="url(#pd13b6a2ddb)" style="fill: none; stroke: #ff7f0e; stroke-width: 1.5; stroke-linecap: square"/>
   </g>
   <g id="patch_3">
    <path d="M 58.523438 465.84
L 58.523438 22.32
" style="fill: none; stroke: #000000; stroke-width: 0.8; stroke-linejoin: miter; stroke-linecap: square"/>
   </g>
   <g id="patch_4">
    <path d="M 728.123438 465.84
L 728.123438 22.32
" style="fill: none; stroke: #000000; stroke-width: 0.8; stroke-linejoin: miter; stroke-linecap: square"/>
   </g>
   <g id="patch_5">
    <path d="M 58.523438 465.84
L 728.123438 465.84
" style="fill: none; stroke: #000000; stroke-width: 0.8; stroke-linejoin: miter; stroke-linecap: square"/>
   </g>
   <g id="patch_6">
    <path d="M 58.523438 22.32
L 728.123438 22.32
" style="fill: none; stroke: #000000; stroke-width: 0.8; stroke-linejoin: miter; stroke-linecap: square"/>
   </g>
   <g id="text_20">
    <!-- Polar plot for $M = 0.1$ and $Re = 100000$ -->
    <g transform="translate(277.403437 16.32) scale(0.12 -0.12)">
     <defs>
      <path id="DejaVuSans-50" d="M 1259 4147
L 1259 2394
L 2053 2394
Q 2494 2394 2734 2622
Q 2975 2850 2975 3272
Q 2975 3691 2734 3919
Q 2494 4147 2053 4147
L 1259 4147
z
M 628 4666
L 2053 4666
Q 2838 4666 3239 4311
Q 3641 3956 3641 3272
Q 3641 2581 3239 2228
Q 2838 1875 2053 1875
L 1259 1875
L 1259 0
L 628 0
L 628 4666
z
" transform="scale(0.015625)"/>
      <path id="DejaVuSans-6f" d="M 1959 3097
Q 1497 3097 1228 2736
Q 959 2375 959 1747
Q 959 1119 1226 758
Q 1494 397 1959 397
Q 2419 397 2687 759
Q 2956 1122 2956 1747
Q 2956 2369 2687 2733
Q 2419 3097 1959 3097
z
M 1959 3584
Q 2709 3584 3137 3096
Q 3566 2609 3566 1747
Q 3566 888 3137 398
Q 2709 -91 1959 -91
Q 1206 -91 779 398
Q 353 888 353 1747
Q 353 2609 779 3096
Q 1206 3584 1959 3584
z
" transform="scale(0.015625)"/>
      <path id="DejaVuSans-6c" d="M 603 4863
L 1178 4863
L 1178 0
L 603 0
L 603 4863
z
" transform="scale(0.015625)"/>
      <path id="DejaVuSans-61" d="M 2194 1759
Q 1497 1759 1228 1600
Q 959 1441 959 1056
Q 959 750 1161 570
Q 1363 391 1709 391
Q 2188 391 2477 730
Q 2766 1069 2766 1631
L 2766 1759
L 2194 1759
z
M 3341 1997
L 3341 0
L 2766 0
L 2766 531
Q 2569 213 2275 61
Q 1981 -91 1556 -91
Q 1019 -91 701 211
Q 384 513 384 1019
Q 384 1609 779 1909
Q 1175 2209 1959 2209
L 2766 2209
L 2766 2266
Q 2766 2663 2505 2880
Q 2244 3097 1772 3097
Q 1472 3097 1187 3025
Q 903 2953 641 2809
L 641 3341
Q 956 3463 1253 3523
Q 1550 3584 1831 3584
Q 2591 3584 2966 3190
Q 3341 2797 3341 1997
z
" transform="scale(0.015625)"/>
      <path id="DejaVuSans-72" d="M 2631 2963
Q 2534 3019 2420 3045
Q 2306 3072 2169 3072
Q 1681 3072 1420 2755
Q 1159 2438 1159 1844
L 1159 0
L 581 0
L 581 3500
L 1159 3500
L 1159 2956
Q 1341 3275 1631 3429
Q 1922 3584 2338 3584
Q 2397 3584 2469 3576
Q 2541 3569 2628 3553
L 2631 2963
z
" transform="scale(0.015625)"/>
      <path id="DejaVuSans-20" transform="scale(0.015625)"/>
      <path id="DejaVuSans-70" d="M 1159 525
L 1159 -1331
L 581 -1331
L 581 3500
L 1159 3500
L 1159 2969
Q 1341 3281 1617 3432
Q 1894 3584 2278 3584
Q 2916 3584 3314 3078
Q 3713 2572 3713 1747
Q 3713 922 3314 415
Q 2916 -91 2278 -91
Q 1894 -91 1617 61
Q 1341 213 1159 525
z
M 3116 1747
Q 3116 2381 2855 2742
Q 2594 3103 2138 3103
Q 1681 3103 1420 2742
Q 1159 2381 1159 1747
Q 1159 1113 1420 752
Q 1681 391 2138 391
Q 2594 391 2855 752
Q 3116 1113 3116 1747
z
" transform="scale(0.015625)"/>
      <path id="DejaVuSans-74" d="M 1172 4494
L 1172 3500
L 2356 3500
L 2356 3053
L 1172 3053
L 1172 1153
Q 1172 725 1289 603
Q 1406 481 1766 481
L 2356 481
L 2356 0
L 1766 0
Q 1100 0 847 248
Q 594 497 594 1153
L 594 3053
L 172 3053
L 172 3500
L 594 3500
L 594 4494
L 1172 4494
z
" transform="scale(0.015625)"/>
      <path id="DejaVuSans-66" d="M 2375 4863
L 2375 4384
L 1825 4384
Q 1516 4384 1395 4259
Q 1275 4134 1275 3809
L 1275 3500
L 2222 3500
L 2222 3053
L 1275 3053
L 1275 0
L 697 0
L 697 3053
L 147 3053
L 147 3500
L 697 3500
L 697 3744
Q 697 4328 969 4595
Q 1241 4863 1831 4863
L 2375 4863
z
" transform="scale(0.015625)"/>
      <path id="DejaVuSans-Oblique-4d" d="M 1081 4666
L 2028 4666
L 2572 1522
L 4378 4666
L 5350 4666
L 4441 0
L 3828 0
L 4622 4091
L 2791 897
L 2175 897
L 1581 4103
L 788 0
L 172 0
L 1081 4666
z
" transform="scale(0.015625)"/>
      <path id="DejaVuSans-3d" d="M 678 2906
L 4684 2906
L 4684 2381
L 678 2381
L 678 2906
z
M 678 1631
L 4684 1631
L 4684 1100
L 678 1100
L 678 1631
z
" transform="scale(0.015625)"/>
      <path id="DejaVuSans-6e" d="M 3513 2113
L 3513 0
L 2938 0
L 2938 2094
Q 2938 2591 2744 2837
Q 2550 3084 2163 3084
Q 1697 3084 1428 2787
Q 1159 2491 1159 1978
L 1159 0
L 581 0
L 581 3500
L 1159 3500
L 1159 2956
Q 1366 3272 1645 3428
Q 1925 3584 2291 3584
Q 2894 3584 3203 3211
Q 3513 2838 3513 2113
z
" transform="scale(0.015625)"/>
      <path id="DejaVuSans-64" d="M 2906 2969
L 2906 4863
L 3481 4863
L 3481 0
L 2906 0
L 2906 525
Q 2725 213 2448 61
Q 2172 -91 1784 -91
Q 1150 -91 751 415
Q 353 922 353 1747
Q 353 2572 751 3078
Q 1150 3584 1784 3584
Q 2172 3584 2448 3432
Q 2725 3281 2906 2969
z
M 947 1747
Q 947 1113 1208 752
Q 1469 391 1925 391
Q 2381 391 2643 752
Q 2906 1113 2906 1747
Q 2906 2381 2643 2742
Q 2381 3103 1925 3103
Q 1469 3103 1208 2742
Q 947 2381 947 1747
z
" transform="scale(0.015625)"/>
      <path id="DejaVuSans-Oblique-52" d="M 1613 4147
L 1294 2491
L 2106 2491
Q 2584 2491 2879 2755
Q 3175 3019 3175 3444
Q 3175 3784 2976 3965
Q 2778 4147 2406 4147
L 1613 4147
z
M 2772 2241
Q 2972 2194 3105 2009
Q 3238 1825 3413 1275
L 3809 0
L 3144 0
L 2778 1197
Q 2638 1659 2453 1815
Q 2269 1972 1888 1972
L 1191 1972
L 806 0
L 172 0
L 1081 4666
L 2503 4666
Q 3150 4666 3495 4373
Q 3841 4081 3841 3531
Q 3841 3044 3547 2687
Q 3253 2331 2772 2241
z
" transform="scale(0.015625)"/>
      <path id="DejaVuSans-Oblique-65" d="M 3078 2063
Q 3088 2113 3092 2166
Q 3097 2219 3097 2272
Q 3097 2653 2873 2875
Q 2650 3097 2266 3097
Q 1838 3097 1509 2826
Q 1181 2556 1013 2059
L 3078 2063
z
M 3578 1613
L 903 1613
Q 884 1494 878 1425
Q 872 1356 872 1306
Q 872 872 1139 634
Q 1406 397 1894 397
Q 2269 397 2603 481
Q 2938 566 3225 728
L 3116 159
Q 2806 34 2476 -28
Q 2147 -91 1806 -91
Q 1078 -91 686 257
Q 294 606 294 1247
Q 294 1794 489 2264
Q 684 2734 1063 3103
Q 1306 3334 1642 3459
Q 1978 3584 2356 3584
Q 2950 3584 3301 3228
Q 3653 2872 3653 2272
Q 3653 2128 3634 1964
Q 3616 1800 3578 1613
z
" transform="scale(0.015625)"/>
     </defs>
     <use xlink:href="#DejaVuSans-50" transform="translate(0 0.015625)"/>
     <use xlink:href="#DejaVuSans-6f" transform="translate(60.302734 0.015625)"/>
     <use xlink:href="#DejaVuSans-6c" transform="translate(121.484375 0.015625)"/>
     <use xlink:href="#DejaVuSans-61" transform="translate(149.267578 0.015625)"/>
     <use xlink:href="#DejaVuSans-72" transform="translate(210.546875 0.015625)"/>
     <use xlink:href="#DejaVuSans-20" transform="translate(251.660156 0.015625)"/>
     <use xlink:href="#DejaVuSans-70" transform="translate(283.447266 0.015625)"/>
     <use xlink:href="#DejaVuSans-6c" transform="translate(346.923828 0.015625)"/>
     <use xlink:href="#DejaVuSans-6f" transform="translate(374.707031 0.015625)"/>
     <use xlink:href="#DejaVuSans-74" transform="translate(435.888672 0.015625)"/>
     <use xlink:href="#DejaVuSans-20" transform="translate(475.097656 0.015625)"/>
     <use xlink:href="#DejaVuSans-66" transform="translate(506.884766 0.015625)"/>
     <use xlink:href="#DejaVuSans-6f" transform="translate(542.089844 0.015625)"/>
     <use xlink:href="#DejaVuSans-72" transform="translate(603.271484 0.015625)"/>
     <use xlink:href="#DejaVuSans-20" transform="translate(644.384766 0.015625)"/>
     <use xlink:href="#DejaVuSans-Oblique-4d" transform="translate(676.171875 0.015625)"/>
     <use xlink:href="#DejaVuSans-3d" transform="translate(781.933594 0.015625)"/>
     <use xlink:href="#DejaVuSans-30" transform="translate(885.205078 0.015625)"/>
     <use xlink:href="#DejaVuSans-2e" transform="translate(948.828125 0.015625)"/>
     <use xlink:href="#DejaVuSans-31" transform="translate(980.615234 0.015625)"/>
     <use xlink:href="#DejaVuSans-20" transform="translate(1044.238281 0.015625)"/>
     <use xlink:href="#DejaVuSans-61" transform="translate(1076.025391 0.015625)"/>
     <use xlink:href="#DejaVuSans-6e" transform="translate(1137.304688 0.015625)"/>
     <use xlink:href="#DejaVuSans-64" transform="translate(1200.683594 0.015625)"/>
     <use xlink:href="#DejaVuSans-20" transform="translate(1264.160156 0.015625)"/>
     <use xlink:href="#DejaVuSans-Oblique-52" transform="translate(1295.947266 0.015625)"/>
     <use xlink:href="#DejaVuSans-Oblique-65" transform="translate(1365.429688 0.015625)"/>
     <use xlink:href="#DejaVuSans-3d" transform="translate(1446.435547 0.015625)"/>
     <use xlink:href="#DejaVuSans-31" transform="translate(1549.707031 0.015625)"/>
     <use xlink:href="#DejaVuSans-30" transform="translate(1613.330078 0.015625)"/>
     <use xlink:href="#DejaVuSans-30" transform="translate(1676.953125 0.015625)"/>
     <use xlink:href="#DejaVuSans-30" transform="translate(1740.576172 0.015625)"/>
     <use xlink:href="#DejaVuSans-30" transform="translate(1804.199219 0.015625)"/>
     <use xlink:href="#DejaVuSans-30" transform="translate(1867.822266 0.015625)"/>
    </g>
   </g>
   <g id="legend_1">
    <g id="patch_7">
     <path d="M 65.523438 59.67625
L 204.523438 59.67625
Q 206.523438 59.67625 206.523438 57.67625
L 206.523438 29.32
Q 206.523438 27.32 204.523438 27.32
L 65.523438 27.32
Q 63.523438 27.32 63.523438 29.32
L 63.523438 57.67625
Q 63.523438 59.67625 65.523438 59.67625
z
" style="fill: #ffffff; opacity: 0.8; stroke: #cccccc; stroke-linejoin: miter"/>
    </g>
    <g id="line2d_37">
     <path d="M 67.523438 35.418437
L 77.523438 35.418437
L 87.523438 35.418437
" style="fill: none; stroke: #1f77b4; stroke-width: 1.5; stroke-linecap: square"/>
    </g>
    <g id="text_21">
     <!-- $Re = 100000$; $M = 0.1$ -->
     <g transform="translate(95.523438 38.918437) scale(0.1 -0.1)">
      <defs>
       <path id="DejaVuSans-3b" d="M 750 3309
L 1409 3309
L 1409 2516
L 750 2516
L 750 3309
z
M 750 794
L 1409 794
L 1409 256
L 897 -744
L 494 -744
L 750 256
L 750 794
z
" transform="scale(0.015625)"/>
      </defs>
      <use xlink:href="#DejaVuSans-Oblique-52" transform="translate(0 0.78125)"/>
      <use xlink:href="#DejaVuSans-Oblique-65" transform="translate(69.482422 0.78125)"/>
      <use xlink:href="#DejaVuSans-3d" transform="translate(150.488281 0.78125)"/>
      <use xlink:href="#DejaVuSans-31" transform="translate(253.759766 0.78125)"/>
      <use xlink:href="#DejaVuSans-30" transform="translate(317.382812 0.78125)"/>
      <use xlink:href="#DejaVuSans-30" transform="translate(381.005859 0.78125)"/>
      <use xlink:href="#DejaVuSans-30" transform="translate(444.628906 0.78125)"/>
      <use xlink:href="#DejaVuSans-30" transform="translate(508.251953 0.78125)"/>
      <use xlink:href="#DejaVuSans-30" transform="translate(571.875 0.78125)"/>
      <use xlink:href="#DejaVuSans-3b" transform="translate(635.498047 0.78125)"/>
      <use xlink:href="#DejaVuSans-20" transform="translate(669.189453 0.78125)"/>
      <use xlink:href="#DejaVuSans-Oblique-4d" transform="translate(700.976562 0.78125)"/>
      <use xlink:href="#DejaVuSans-3d" transform="translate(806.738281 0.78125)"/>
      <use xlink:href="#DejaVuSans-30" transform="translate(910.009766 0.78125)"/>
      <use xlink:href="#DejaVuSans-2e" transform="translate(973.632812 0.78125)"/>
      <use xlink:href="#DejaVuSans-31" transform="translate(1005.419922 0.78125)"/>
     </g>
    </g>
    <g id="line2d_38">
     <path d="M 67.523438 50.096562
L 77.523438 50.096562
L 87.523438 50.096562
" style="fill: none; stroke: #ff7f0e; stroke-width: 1.5; stroke-linecap: square"/>
    </g>
    <g id="text_22">
     <!-- $Re = 200000$; $M = 0.1$ -->
     <g transform="translate(95.523438 53.596562) scale(0.1 -0.1)">
      <use xlink:href="#DejaVuSans-Oblique-52" transform="translate(0 0.78125)"/>
      <use xlink:href="#DejaVuSans-Oblique-65" transform="translate(69.482422 0.78125)"/>
      <use xlink:href="#DejaVuSans-3d" transform="translate(150.488281 0.78125)"/>
      <use xlink:href="#DejaVuSans-32" transform="translate(253.759766 0.78125)"/>
      <use xlink:href="#DejaVuSans-30" transform="translate(317.382812 0.78125)"/>
      <use xlink:href="#DejaVuSans-30" transform="translate(381.005859 0.78125)"/>
      <use xlink:href="#DejaVuSans-30" transform="translate(444.628906 0.78125)"/>
      <use xlink:href="#DejaVuSans-30" transform="translate(508.251953 0.78125)"/>
      <use xlink:href="#DejaVuSans-30" transform="translate(571.875 0.78125)"/>
      <use xlink:href="#DejaVuSans-3b" transform="translate(635.498047 0.78125)"/>
      <use xlink:href="#DejaVuSans-20" transform="translate(669.189453 0.78125)"/>
      <use xlink:href="#DejaVuSans-Oblique-4d" transform="translate(700.976562 0.78125)"/>
      <use xlink:href="#DejaVuSans-3d" transform="translate(806.738281 0.78125)"/>
      <use xlink:href="#DejaVuSans-30" transform="translate(910.009766 0.78125)"/>
      <use xlink:href="#DejaVuSans-2e" transform="translate(973.632812 0.78125)"/>
      <use xlink:href="#DejaVuSans-31" transform="translate(1005.419922 0.78125)"/>
     </g>
    </g>
   </g>
  </g>
 </g>
 <defs>
  <clipPath id="pd13b6a2ddb">
   <rect x="58.523438" y="22.32" width="669.6" height="443.52"/>
  </clipPath>
 </defs>
</svg>


#
``` python
# Plot two lift to drag ratios created above
axp2 = None
axp2 = polar1.plot_polar(ax=axp2, xaxis='alpha', yaxis='clocd', ls='-o')
axp2 = polar2.plot_polar(ax=axp2, xaxis='alpha', yaxis='clocd', ls='-x')
_ = axp2.legend()
```

<svg xmlns:xlink="http://www.w3.org/1999/xlink" width="729.504687pt" height="503.39625pt" viewBox="0 0 729.504687 503.39625" xmlns="http://www.w3.org/2000/svg" version="1.1">
 <metadata>
  <rdf:RDF xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:cc="http://creativecommons.org/ns#" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
   <cc:Work>
    <dc:type rdf:resource="http://purl.org/dc/dcmitype/StillImage"/>
    <dc:date>2023-02-24T16:11:45.293071</dc:date>
    <dc:format>image/svg+xml</dc:format>
    <dc:creator>
     <cc:Agent>
      <dc:title>Matplotlib v3.6.2, https://matplotlib.org/</dc:title>
     </cc:Agent>
    </dc:creator>
   </cc:Work>
  </rdf:RDF>
 </metadata>
 <defs>
  <style type="text/css">*{stroke-linejoin: round; stroke-linecap: butt}</style>
 </defs>
 <g id="figure_1">
  <g id="patch_1">
   <path d="M 0 503.39625
L 729.504687 503.39625
L 729.504687 0
L 0 0
z
" style="fill: #ffffff"/>
  </g>
  <g id="axes_1">
   <g id="patch_2">
    <path d="M 52.704687 465.84
L 722.304688 465.84
L 722.304688 22.32
L 52.704687 22.32
z
" style="fill: #ffffff"/>
   </g>
   <g id="matplotlib.axis_1">
    <g id="xtick_1">
     <g id="line2d_1">
      <path d="M 83.141051 465.84
L 83.141051 22.32
" clip-path="url(#p18e5c327e8)" style="fill: none; stroke: #b0b0b0; stroke-width: 0.8; stroke-linecap: square"/>
     </g>
     <g id="line2d_2">
      <defs>
       <path id="mcdf076411a" d="M 0 0
L 0 3.5
" style="stroke: #000000; stroke-width: 0.8"/>
      </defs>
      <g>
       <use xlink:href="#mcdf076411a" x="83.141051" y="465.84" style="stroke: #000000; stroke-width: 0.8"/>
      </g>
     </g>
     <g id="text_1">
      <!-- −10.0 -->
      <g transform="translate(67.818395 480.438437) scale(0.1 -0.1)">
       <defs>
        <path id="DejaVuSans-2212" d="M 678 2272
L 4684 2272
L 4684 1741
L 678 1741
L 678 2272
z
" transform="scale(0.015625)"/>
        <path id="DejaVuSans-31" d="M 794 531
L 1825 531
L 1825 4091
L 703 3866
L 703 4441
L 1819 4666
L 2450 4666
L 2450 531
L 3481 531
L 3481 0
L 794 0
L 794 531
z
" transform="scale(0.015625)"/>
        <path id="DejaVuSans-30" d="M 2034 4250
Q 1547 4250 1301 3770
Q 1056 3291 1056 2328
Q 1056 1369 1301 889
Q 1547 409 2034 409
Q 2525 409 2770 889
Q 3016 1369 3016 2328
Q 3016 3291 2770 3770
Q 2525 4250 2034 4250
z
M 2034 4750
Q 2819 4750 3233 4129
Q 3647 3509 3647 2328
Q 3647 1150 3233 529
Q 2819 -91 2034 -91
Q 1250 -91 836 529
Q 422 1150 422 2328
Q 422 3509 836 4129
Q 1250 4750 2034 4750
z
" transform="scale(0.015625)"/>
        <path id="DejaVuSans-2e" d="M 684 794
L 1344 794
L 1344 0
L 684 0
L 684 794
z
" transform="scale(0.015625)"/>
       </defs>
       <use xlink:href="#DejaVuSans-2212"/>
       <use xlink:href="#DejaVuSans-31" x="83.789062"/>
       <use xlink:href="#DejaVuSans-30" x="147.412109"/>
       <use xlink:href="#DejaVuSans-2e" x="211.035156"/>
       <use xlink:href="#DejaVuSans-30" x="242.822266"/>
      </g>
     </g>
    </g>
    <g id="xtick_2">
     <g id="line2d_3">
      <path d="M 159.23196 465.84
L 159.23196 22.32
" clip-path="url(#p18e5c327e8)" style="fill: none; stroke: #b0b0b0; stroke-width: 0.8; stroke-linecap: square"/>
     </g>
     <g id="line2d_4">
      <g>
       <use xlink:href="#mcdf076411a" x="159.23196" y="465.84" style="stroke: #000000; stroke-width: 0.8"/>
      </g>
     </g>
     <g id="text_2">
      <!-- −7.5 -->
      <g transform="translate(147.090554 480.438437) scale(0.1 -0.1)">
       <defs>
        <path id="DejaVuSans-37" d="M 525 4666
L 3525 4666
L 3525 4397
L 1831 0
L 1172 0
L 2766 4134
L 525 4134
L 525 4666
z
" transform="scale(0.015625)"/>
        <path id="DejaVuSans-35" d="M 691 4666
L 3169 4666
L 3169 4134
L 1269 4134
L 1269 2991
Q 1406 3038 1543 3061
Q 1681 3084 1819 3084
Q 2600 3084 3056 2656
Q 3513 2228 3513 1497
Q 3513 744 3044 326
Q 2575 -91 1722 -91
Q 1428 -91 1123 -41
Q 819 9 494 109
L 494 744
Q 775 591 1075 516
Q 1375 441 1709 441
Q 2250 441 2565 725
Q 2881 1009 2881 1497
Q 2881 1984 2565 2268
Q 2250 2553 1709 2553
Q 1456 2553 1204 2497
Q 953 2441 691 2322
L 691 4666
z
" transform="scale(0.015625)"/>
       </defs>
       <use xlink:href="#DejaVuSans-2212"/>
       <use xlink:href="#DejaVuSans-37" x="83.789062"/>
       <use xlink:href="#DejaVuSans-2e" x="147.412109"/>
       <use xlink:href="#DejaVuSans-35" x="179.199219"/>
      </g>
     </g>
    </g>
    <g id="xtick_3">
     <g id="line2d_5">
      <path d="M 235.322869 465.84
L 235.322869 22.32
" clip-path="url(#p18e5c327e8)" style="fill: none; stroke: #b0b0b0; stroke-width: 0.8; stroke-linecap: square"/>
     </g>
     <g id="line2d_6">
      <g>
       <use xlink:href="#mcdf076411a" x="235.322869" y="465.84" style="stroke: #000000; stroke-width: 0.8"/>
      </g>
     </g>
     <g id="text_3">
      <!-- −5.0 -->
      <g transform="translate(223.181463 480.438437) scale(0.1 -0.1)">
       <use xlink:href="#DejaVuSans-2212"/>
       <use xlink:href="#DejaVuSans-35" x="83.789062"/>
       <use xlink:href="#DejaVuSans-2e" x="147.412109"/>
       <use xlink:href="#DejaVuSans-30" x="179.199219"/>
      </g>
     </g>
    </g>
    <g id="xtick_4">
     <g id="line2d_7">
      <path d="M 311.413778 465.84
L 311.413778 22.32
" clip-path="url(#p18e5c327e8)" style="fill: none; stroke: #b0b0b0; stroke-width: 0.8; stroke-linecap: square"/>
     </g>
     <g id="line2d_8">
      <g>
       <use xlink:href="#mcdf076411a" x="311.413778" y="465.84" style="stroke: #000000; stroke-width: 0.8"/>
      </g>
     </g>
     <g id="text_4">
      <!-- −2.5 -->
      <g transform="translate(299.272372 480.438437) scale(0.1 -0.1)">
       <defs>
        <path id="DejaVuSans-32" d="M 1228 531
L 3431 531
L 3431 0
L 469 0
L 469 531
Q 828 903 1448 1529
Q 2069 2156 2228 2338
Q 2531 2678 2651 2914
Q 2772 3150 2772 3378
Q 2772 3750 2511 3984
Q 2250 4219 1831 4219
Q 1534 4219 1204 4116
Q 875 4013 500 3803
L 500 4441
Q 881 4594 1212 4672
Q 1544 4750 1819 4750
Q 2544 4750 2975 4387
Q 3406 4025 3406 3419
Q 3406 3131 3298 2873
Q 3191 2616 2906 2266
Q 2828 2175 2409 1742
Q 1991 1309 1228 531
z
" transform="scale(0.015625)"/>
       </defs>
       <use xlink:href="#DejaVuSans-2212"/>
       <use xlink:href="#DejaVuSans-32" x="83.789062"/>
       <use xlink:href="#DejaVuSans-2e" x="147.412109"/>
       <use xlink:href="#DejaVuSans-35" x="179.199219"/>
      </g>
     </g>
    </g>
    <g id="xtick_5">
     <g id="line2d_9">
      <path d="M 387.504687 465.84
L 387.504687 22.32
" clip-path="url(#p18e5c327e8)" style="fill: none; stroke: #b0b0b0; stroke-width: 0.8; stroke-linecap: square"/>
     </g>
     <g id="line2d_10">
      <g>
       <use xlink:href="#mcdf076411a" x="387.504687" y="465.84" style="stroke: #000000; stroke-width: 0.8"/>
      </g>
     </g>
     <g id="text_5">
      <!-- 0.0 -->
      <g transform="translate(379.553125 480.438437) scale(0.1 -0.1)">
       <use xlink:href="#DejaVuSans-30"/>
       <use xlink:href="#DejaVuSans-2e" x="63.623047"/>
       <use xlink:href="#DejaVuSans-30" x="95.410156"/>
      </g>
     </g>
    </g>
    <g id="xtick_6">
     <g id="line2d_11">
      <path d="M 463.595597 465.84
L 463.595597 22.32
" clip-path="url(#p18e5c327e8)" style="fill: none; stroke: #b0b0b0; stroke-width: 0.8; stroke-linecap: square"/>
     </g>
     <g id="line2d_12">
      <g>
       <use xlink:href="#mcdf076411a" x="463.595597" y="465.84" style="stroke: #000000; stroke-width: 0.8"/>
      </g>
     </g>
     <g id="text_6">
      <!-- 2.5 -->
      <g transform="translate(455.644034 480.438437) scale(0.1 -0.1)">
       <use xlink:href="#DejaVuSans-32"/>
       <use xlink:href="#DejaVuSans-2e" x="63.623047"/>
       <use xlink:href="#DejaVuSans-35" x="95.410156"/>
      </g>
     </g>
    </g>
    <g id="xtick_7">
     <g id="line2d_13">
      <path d="M 539.686506 465.84
L 539.686506 22.32
" clip-path="url(#p18e5c327e8)" style="fill: none; stroke: #b0b0b0; stroke-width: 0.8; stroke-linecap: square"/>
     </g>
     <g id="line2d_14">
      <g>
       <use xlink:href="#mcdf076411a" x="539.686506" y="465.84" style="stroke: #000000; stroke-width: 0.8"/>
      </g>
     </g>
     <g id="text_7">
      <!-- 5.0 -->
      <g transform="translate(531.734943 480.438437) scale(0.1 -0.1)">
       <use xlink:href="#DejaVuSans-35"/>
       <use xlink:href="#DejaVuSans-2e" x="63.623047"/>
       <use xlink:href="#DejaVuSans-30" x="95.410156"/>
      </g>
     </g>
    </g>
    <g id="xtick_8">
     <g id="line2d_15">
      <path d="M 615.777415 465.84
L 615.777415 22.32
" clip-path="url(#p18e5c327e8)" style="fill: none; stroke: #b0b0b0; stroke-width: 0.8; stroke-linecap: square"/>
     </g>
     <g id="line2d_16">
      <g>
       <use xlink:href="#mcdf076411a" x="615.777415" y="465.84" style="stroke: #000000; stroke-width: 0.8"/>
      </g>
     </g>
     <g id="text_8">
      <!-- 7.5 -->
      <g transform="translate(607.825852 480.438437) scale(0.1 -0.1)">
       <use xlink:href="#DejaVuSans-37"/>
       <use xlink:href="#DejaVuSans-2e" x="63.623047"/>
       <use xlink:href="#DejaVuSans-35" x="95.410156"/>
      </g>
     </g>
    </g>
    <g id="xtick_9">
     <g id="line2d_17">
      <path d="M 691.868324 465.84
L 691.868324 22.32
" clip-path="url(#p18e5c327e8)" style="fill: none; stroke: #b0b0b0; stroke-width: 0.8; stroke-linecap: square"/>
     </g>
     <g id="line2d_18">
      <g>
       <use xlink:href="#mcdf076411a" x="691.868324" y="465.84" style="stroke: #000000; stroke-width: 0.8"/>
      </g>
     </g>
     <g id="text_9">
      <!-- 10.0 -->
      <g transform="translate(680.735511 480.438437) scale(0.1 -0.1)">
       <use xlink:href="#DejaVuSans-31"/>
       <use xlink:href="#DejaVuSans-30" x="63.623047"/>
       <use xlink:href="#DejaVuSans-2e" x="127.246094"/>
       <use xlink:href="#DejaVuSans-30" x="159.033203"/>
      </g>
     </g>
    </g>
    <g id="text_10">
     <!-- $\alpha$ -->
     <g transform="translate(384.204687 494.116562) scale(0.1 -0.1)">
      <defs>
       <path id="DejaVuSans-Oblique-3b1" d="M 2619 1628
L 2622 2350
Q 2625 3088 2069 3091
Q 1653 3094 1394 2747
Q 1069 2319 959 1747
Q 825 1059 994 731
Q 1169 397 1547 397
Q 1966 397 2319 1063
L 2619 1628
z
M 2166 3578
Q 3141 3594 3128 2584
Q 3128 2584 3616 3500
L 4128 3500
L 3119 1603
L 3109 919
Q 3109 766 3194 638
Q 3291 488 3391 488
L 3669 488
L 3575 0
L 3228 0
Q 2934 0 2722 263
Q 2622 394 2619 669
Q 2416 334 2066 50
Q 1900 -81 1453 -78
Q 722 -72 456 397
Q 184 884 353 1747
Q 534 2675 1009 3097
Q 1544 3569 2166 3578
z
" transform="scale(0.015625)"/>
      </defs>
      <use xlink:href="#DejaVuSans-Oblique-3b1" transform="translate(0 0.84375)"/>
     </g>
    </g>
   </g>
   <g id="matplotlib.axis_2">
    <g id="ytick_1">
     <g id="line2d_19">
      <path d="M 52.704687 408.758371
L 722.304688 408.758371
" clip-path="url(#p18e5c327e8)" style="fill: none; stroke: #b0b0b0; stroke-width: 0.8; stroke-linecap: square"/>
     </g>
     <g id="line2d_20">
      <defs>
       <path id="m7bdf033589" d="M 0 0
L -3.5 0
" style="stroke: #000000; stroke-width: 0.8"/>
      </defs>
      <g>
       <use xlink:href="#m7bdf033589" x="52.704687" y="408.758371" style="stroke: #000000; stroke-width: 0.8"/>
      </g>
     </g>
     <g id="text_11">
      <!-- −40 -->
      <g transform="translate(24.6 412.55759) scale(0.1 -0.1)">
       <defs>
        <path id="DejaVuSans-34" d="M 2419 4116
L 825 1625
L 2419 1625
L 2419 4116
z
M 2253 4666
L 3047 4666
L 3047 1625
L 3713 1625
L 3713 1100
L 3047 1100
L 3047 0
L 2419 0
L 2419 1100
L 313 1100
L 313 1709
L 2253 4666
z
" transform="scale(0.015625)"/>
       </defs>
       <use xlink:href="#DejaVuSans-2212"/>
       <use xlink:href="#DejaVuSans-34" x="83.789062"/>
       <use xlink:href="#DejaVuSans-30" x="147.412109"/>
      </g>
     </g>
    </g>
    <g id="ytick_2">
     <g id="line2d_21">
      <path d="M 52.704687 326.457851
L 722.304688 326.457851
" clip-path="url(#p18e5c327e8)" style="fill: none; stroke: #b0b0b0; stroke-width: 0.8; stroke-linecap: square"/>
     </g>
     <g id="line2d_22">
      <g>
       <use xlink:href="#m7bdf033589" x="52.704687" y="326.457851" style="stroke: #000000; stroke-width: 0.8"/>
      </g>
     </g>
     <g id="text_12">
      <!-- −20 -->
      <g transform="translate(24.6 330.257069) scale(0.1 -0.1)">
       <use xlink:href="#DejaVuSans-2212"/>
       <use xlink:href="#DejaVuSans-32" x="83.789062"/>
       <use xlink:href="#DejaVuSans-30" x="147.412109"/>
      </g>
     </g>
    </g>
    <g id="ytick_3">
     <g id="line2d_23">
      <path d="M 52.704687 244.15733
L 722.304688 244.15733
" clip-path="url(#p18e5c327e8)" style="fill: none; stroke: #b0b0b0; stroke-width: 0.8; stroke-linecap: square"/>
     </g>
     <g id="line2d_24">
      <g>
       <use xlink:href="#m7bdf033589" x="52.704687" y="244.15733" style="stroke: #000000; stroke-width: 0.8"/>
      </g>
     </g>
     <g id="text_13">
      <!-- 0 -->
      <g transform="translate(39.342187 247.956549) scale(0.1 -0.1)">
       <use xlink:href="#DejaVuSans-30"/>
      </g>
     </g>
    </g>
    <g id="ytick_4">
     <g id="line2d_25">
      <path d="M 52.704687 161.85681
L 722.304688 161.85681
" clip-path="url(#p18e5c327e8)" style="fill: none; stroke: #b0b0b0; stroke-width: 0.8; stroke-linecap: square"/>
     </g>
     <g id="line2d_26">
      <g>
       <use xlink:href="#m7bdf033589" x="52.704687" y="161.85681" style="stroke: #000000; stroke-width: 0.8"/>
      </g>
     </g>
     <g id="text_14">
      <!-- 20 -->
      <g transform="translate(32.979687 165.656029) scale(0.1 -0.1)">
       <use xlink:href="#DejaVuSans-32"/>
       <use xlink:href="#DejaVuSans-30" x="63.623047"/>
      </g>
     </g>
    </g>
    <g id="ytick_5">
     <g id="line2d_27">
      <path d="M 52.704687 79.55629
L 722.304688 79.55629
" clip-path="url(#p18e5c327e8)" style="fill: none; stroke: #b0b0b0; stroke-width: 0.8; stroke-linecap: square"/>
     </g>
     <g id="line2d_28">
      <g>
       <use xlink:href="#m7bdf033589" x="52.704687" y="79.55629" style="stroke: #000000; stroke-width: 0.8"/>
      </g>
     </g>
     <g id="text_15">
      <!-- 40 -->
      <g transform="translate(32.979687 83.355508) scale(0.1 -0.1)">
       <use xlink:href="#DejaVuSans-34"/>
       <use xlink:href="#DejaVuSans-30" x="63.623047"/>
      </g>
     </g>
    </g>
    <g id="text_16">
     <!-- $\frac{c_l}{c_d}$ -->
     <g transform="translate(16.7 248.33) rotate(-90) scale(0.1 -0.1)">
      <defs>
       <path id="DejaVuSans-Oblique-63" d="M 3431 3366
L 3316 2797
Q 3109 2947 2876 3022
Q 2644 3097 2394 3097
Q 2119 3097 1870 3000
Q 1622 2903 1453 2725
Q 1184 2453 1037 2087
Q 891 1722 891 1331
Q 891 859 1127 628
Q 1363 397 1844 397
Q 2081 397 2348 469
Q 2616 541 2906 684
L 2797 116
Q 2547 13 2283 -39
Q 2019 -91 1741 -91
Q 1044 -91 669 257
Q 294 606 294 1253
Q 294 1797 489 2255
Q 684 2713 1069 3078
Q 1331 3328 1684 3456
Q 2038 3584 2456 3584
Q 2700 3584 2940 3529
Q 3181 3475 3431 3366
z
" transform="scale(0.015625)"/>
       <path id="DejaVuSans-Oblique-6c" d="M 1172 4863
L 1747 4863
L 800 0
L 225 0
L 1172 4863
z
" transform="scale(0.015625)"/>
       <path id="DejaVuSans-Oblique-64" d="M 2675 525
Q 2444 222 2128 65
Q 1813 -91 1428 -91
Q 903 -91 598 267
Q 294 625 294 1247
Q 294 1766 478 2236
Q 663 2706 1013 3078
Q 1244 3325 1534 3454
Q 1825 3584 2144 3584
Q 2481 3584 2739 3421
Q 2997 3259 3138 2956
L 3513 4863
L 4091 4863
L 3144 0
L 2566 0
L 2675 525
z
M 891 1350
Q 891 897 1095 644
Q 1300 391 1663 391
Q 1931 391 2161 520
Q 2391 650 2566 903
Q 2750 1166 2856 1509
Q 2963 1853 2963 2188
Q 2963 2622 2758 2865
Q 2553 3109 2194 3109
Q 1922 3109 1687 2981
Q 1453 2853 1288 2613
Q 1106 2353 998 2009
Q 891 1666 891 1350
z
" transform="scale(0.015625)"/>
      </defs>
      <use xlink:href="#DejaVuSans-Oblique-63" transform="translate(9 55.8) scale(0.7)"/>
      <use xlink:href="#DejaVuSans-Oblique-6c" transform="translate(47.486328 44.315625) scale(0.49)"/>
      <use xlink:href="#DejaVuSans-Oblique-63" transform="translate(0 -26.134375) scale(0.7)"/>
      <use xlink:href="#DejaVuSans-Oblique-64" transform="translate(38.486328 -37.61875) scale(0.49)"/>
      <path d="M 0 19.315625
L 0 25.565625
L 71.503906 25.565625
L 71.503906 19.315625
L 0 19.315625
z
"/>
     </g>
    </g>
   </g>
   <g id="line2d_29">
    <path d="M 83.141051 331.16126
L 98.359233 340.335054
L 113.577415 351.099486
L 128.795597 357.970689
L 144.013778 365.292173
L 159.23196 371.710705
L 174.450142 378.019622
L 189.668324 383.676308
L 204.886506 389.238376
L 220.104687 395.262144
L 235.322869 399.930287
L 250.541051 401.740692
L 265.759233 400.328739
L 280.977415 396.397028
L 296.195597 390.413945
L 311.413778 382.342649
L 326.63196 371.227552
L 341.850142 353.139754
L 357.068324 322.062198
L 372.286506 281.444038
L 387.504687 244.113011
L 402.722869 206.8249
L 417.941051 166.252462
L 433.159233 135.201749
L 448.377415 117.087109
L 463.595597 106.000024
L 478.813778 97.928426
L 494.03196 91.944741
L 509.250142 87.912473
L 524.468324 86.502756
L 539.686506 88.318232
L 554.904688 93.074569
L 570.122869 99.076285
L 585.341051 104.638353
L 600.559233 110.295038
L 630.995597 122.980903
L 646.213778 130.308702
L 661.43196 137.226727
L 691.868324 157.229692
" clip-path="url(#p18e5c327e8)" style="fill: none; stroke: #1f77b4; stroke-width: 1.5; stroke-linecap: square"/>
   </g>
   <g id="line2d_30">
    <path d="M 83.141051 381.150187
L 98.359233 390.28492
L 113.577415 396.459271
L 128.795597 403.648091
L 144.013778 410.734513
L 159.23196 417.35662
L 174.450142 423.50313
L 189.668324 429.708915
L 204.886506 435.835711
L 220.104687 441.448877
L 235.322869 445.123717
L 250.541051 445.68
L 265.759233 443.511876
L 280.977415 438.887459
L 296.195597 416.695985
L 311.413778 391.772339
L 326.63196 368.156781
L 341.850142 342.948074
L 357.068324 313.113905
L 372.286506 279.473729
L 387.504687 244.117952
L 402.722869 208.913619
L 417.941051 175.200756
L 433.159233 145.366587
L 448.377415 120.15788
L 463.595597 96.485869
L 478.813778 71.549048
L 494.03196 49.461323
L 509.250142 44.835758
L 524.468324 42.48
L 539.686506 43.190943
L 554.904688 46.893796
L 570.122869 52.50501
L 585.341051 58.520703
L 600.559233 65.030023
L 615.777415 70.95804
L 646.213778 84.769251
L 661.43196 91.656406
L 691.868324 107.136893
" clip-path="url(#p18e5c327e8)" style="fill: none; stroke: #ff7f0e; stroke-width: 1.5; stroke-linecap: square"/>
   </g>
   <g id="patch_3">
    <path d="M 52.704687 465.84
L 52.704687 22.32
" style="fill: none; stroke: #000000; stroke-width: 0.8; stroke-linejoin: miter; stroke-linecap: square"/>
   </g>
   <g id="patch_4">
    <path d="M 722.304688 465.84
L 722.304688 22.32
" style="fill: none; stroke: #000000; stroke-width: 0.8; stroke-linejoin: miter; stroke-linecap: square"/>
   </g>
   <g id="patch_5">
    <path d="M 52.704687 465.84
L 722.304688 465.84
" style="fill: none; stroke: #000000; stroke-width: 0.8; stroke-linejoin: miter; stroke-linecap: square"/>
   </g>
   <g id="patch_6">
    <path d="M 52.704687 22.32
L 722.304688 22.32
" style="fill: none; stroke: #000000; stroke-width: 0.8; stroke-linejoin: miter; stroke-linecap: square"/>
   </g>
   <g id="text_17">
    <!-- Polar plot for $M = 0.1$ and $Re = 100000$ -->
    <g transform="translate(271.584687 16.32) scale(0.12 -0.12)">
     <defs>
      <path id="DejaVuSans-50" d="M 1259 4147
L 1259 2394
L 2053 2394
Q 2494 2394 2734 2622
Q 2975 2850 2975 3272
Q 2975 3691 2734 3919
Q 2494 4147 2053 4147
L 1259 4147
z
M 628 4666
L 2053 4666
Q 2838 4666 3239 4311
Q 3641 3956 3641 3272
Q 3641 2581 3239 2228
Q 2838 1875 2053 1875
L 1259 1875
L 1259 0
L 628 0
L 628 4666
z
" transform="scale(0.015625)"/>
      <path id="DejaVuSans-6f" d="M 1959 3097
Q 1497 3097 1228 2736
Q 959 2375 959 1747
Q 959 1119 1226 758
Q 1494 397 1959 397
Q 2419 397 2687 759
Q 2956 1122 2956 1747
Q 2956 2369 2687 2733
Q 2419 3097 1959 3097
z
M 1959 3584
Q 2709 3584 3137 3096
Q 3566 2609 3566 1747
Q 3566 888 3137 398
Q 2709 -91 1959 -91
Q 1206 -91 779 398
Q 353 888 353 1747
Q 353 2609 779 3096
Q 1206 3584 1959 3584
z
" transform="scale(0.015625)"/>
      <path id="DejaVuSans-6c" d="M 603 4863
L 1178 4863
L 1178 0
L 603 0
L 603 4863
z
" transform="scale(0.015625)"/>
      <path id="DejaVuSans-61" d="M 2194 1759
Q 1497 1759 1228 1600
Q 959 1441 959 1056
Q 959 750 1161 570
Q 1363 391 1709 391
Q 2188 391 2477 730
Q 2766 1069 2766 1631
L 2766 1759
L 2194 1759
z
M 3341 1997
L 3341 0
L 2766 0
L 2766 531
Q 2569 213 2275 61
Q 1981 -91 1556 -91
Q 1019 -91 701 211
Q 384 513 384 1019
Q 384 1609 779 1909
Q 1175 2209 1959 2209
L 2766 2209
L 2766 2266
Q 2766 2663 2505 2880
Q 2244 3097 1772 3097
Q 1472 3097 1187 3025
Q 903 2953 641 2809
L 641 3341
Q 956 3463 1253 3523
Q 1550 3584 1831 3584
Q 2591 3584 2966 3190
Q 3341 2797 3341 1997
z
" transform="scale(0.015625)"/>
      <path id="DejaVuSans-72" d="M 2631 2963
Q 2534 3019 2420 3045
Q 2306 3072 2169 3072
Q 1681 3072 1420 2755
Q 1159 2438 1159 1844
L 1159 0
L 581 0
L 581 3500
L 1159 3500
L 1159 2956
Q 1341 3275 1631 3429
Q 1922 3584 2338 3584
Q 2397 3584 2469 3576
Q 2541 3569 2628 3553
L 2631 2963
z
" transform="scale(0.015625)"/>
      <path id="DejaVuSans-20" transform="scale(0.015625)"/>
      <path id="DejaVuSans-70" d="M 1159 525
L 1159 -1331
L 581 -1331
L 581 3500
L 1159 3500
L 1159 2969
Q 1341 3281 1617 3432
Q 1894 3584 2278 3584
Q 2916 3584 3314 3078
Q 3713 2572 3713 1747
Q 3713 922 3314 415
Q 2916 -91 2278 -91
Q 1894 -91 1617 61
Q 1341 213 1159 525
z
M 3116 1747
Q 3116 2381 2855 2742
Q 2594 3103 2138 3103
Q 1681 3103 1420 2742
Q 1159 2381 1159 1747
Q 1159 1113 1420 752
Q 1681 391 2138 391
Q 2594 391 2855 752
Q 3116 1113 3116 1747
z
" transform="scale(0.015625)"/>
      <path id="DejaVuSans-74" d="M 1172 4494
L 1172 3500
L 2356 3500
L 2356 3053
L 1172 3053
L 1172 1153
Q 1172 725 1289 603
Q 1406 481 1766 481
L 2356 481
L 2356 0
L 1766 0
Q 1100 0 847 248
Q 594 497 594 1153
L 594 3053
L 172 3053
L 172 3500
L 594 3500
L 594 4494
L 1172 4494
z
" transform="scale(0.015625)"/>
      <path id="DejaVuSans-66" d="M 2375 4863
L 2375 4384
L 1825 4384
Q 1516 4384 1395 4259
Q 1275 4134 1275 3809
L 1275 3500
L 2222 3500
L 2222 3053
L 1275 3053
L 1275 0
L 697 0
L 697 3053
L 147 3053
L 147 3500
L 697 3500
L 697 3744
Q 697 4328 969 4595
Q 1241 4863 1831 4863
L 2375 4863
z
" transform="scale(0.015625)"/>
      <path id="DejaVuSans-Oblique-4d" d="M 1081 4666
L 2028 4666
L 2572 1522
L 4378 4666
L 5350 4666
L 4441 0
L 3828 0
L 4622 4091
L 2791 897
L 2175 897
L 1581 4103
L 788 0
L 172 0
L 1081 4666
z
" transform="scale(0.015625)"/>
      <path id="DejaVuSans-3d" d="M 678 2906
L 4684 2906
L 4684 2381
L 678 2381
L 678 2906
z
M 678 1631
L 4684 1631
L 4684 1100
L 678 1100
L 678 1631
z
" transform="scale(0.015625)"/>
      <path id="DejaVuSans-6e" d="M 3513 2113
L 3513 0
L 2938 0
L 2938 2094
Q 2938 2591 2744 2837
Q 2550 3084 2163 3084
Q 1697 3084 1428 2787
Q 1159 2491 1159 1978
L 1159 0
L 581 0
L 581 3500
L 1159 3500
L 1159 2956
Q 1366 3272 1645 3428
Q 1925 3584 2291 3584
Q 2894 3584 3203 3211
Q 3513 2838 3513 2113
z
" transform="scale(0.015625)"/>
      <path id="DejaVuSans-64" d="M 2906 2969
L 2906 4863
L 3481 4863
L 3481 0
L 2906 0
L 2906 525
Q 2725 213 2448 61
Q 2172 -91 1784 -91
Q 1150 -91 751 415
Q 353 922 353 1747
Q 353 2572 751 3078
Q 1150 3584 1784 3584
Q 2172 3584 2448 3432
Q 2725 3281 2906 2969
z
M 947 1747
Q 947 1113 1208 752
Q 1469 391 1925 391
Q 2381 391 2643 752
Q 2906 1113 2906 1747
Q 2906 2381 2643 2742
Q 2381 3103 1925 3103
Q 1469 3103 1208 2742
Q 947 2381 947 1747
z
" transform="scale(0.015625)"/>
      <path id="DejaVuSans-Oblique-52" d="M 1613 4147
L 1294 2491
L 2106 2491
Q 2584 2491 2879 2755
Q 3175 3019 3175 3444
Q 3175 3784 2976 3965
Q 2778 4147 2406 4147
L 1613 4147
z
M 2772 2241
Q 2972 2194 3105 2009
Q 3238 1825 3413 1275
L 3809 0
L 3144 0
L 2778 1197
Q 2638 1659 2453 1815
Q 2269 1972 1888 1972
L 1191 1972
L 806 0
L 172 0
L 1081 4666
L 2503 4666
Q 3150 4666 3495 4373
Q 3841 4081 3841 3531
Q 3841 3044 3547 2687
Q 3253 2331 2772 2241
z
" transform="scale(0.015625)"/>
      <path id="DejaVuSans-Oblique-65" d="M 3078 2063
Q 3088 2113 3092 2166
Q 3097 2219 3097 2272
Q 3097 2653 2873 2875
Q 2650 3097 2266 3097
Q 1838 3097 1509 2826
Q 1181 2556 1013 2059
L 3078 2063
z
M 3578 1613
L 903 1613
Q 884 1494 878 1425
Q 872 1356 872 1306
Q 872 872 1139 634
Q 1406 397 1894 397
Q 2269 397 2603 481
Q 2938 566 3225 728
L 3116 159
Q 2806 34 2476 -28
Q 2147 -91 1806 -91
Q 1078 -91 686 257
Q 294 606 294 1247
Q 294 1794 489 2264
Q 684 2734 1063 3103
Q 1306 3334 1642 3459
Q 1978 3584 2356 3584
Q 2950 3584 3301 3228
Q 3653 2872 3653 2272
Q 3653 2128 3634 1964
Q 3616 1800 3578 1613
z
" transform="scale(0.015625)"/>
     </defs>
     <use xlink:href="#DejaVuSans-50" transform="translate(0 0.015625)"/>
     <use xlink:href="#DejaVuSans-6f" transform="translate(60.302734 0.015625)"/>
     <use xlink:href="#DejaVuSans-6c" transform="translate(121.484375 0.015625)"/>
     <use xlink:href="#DejaVuSans-61" transform="translate(149.267578 0.015625)"/>
     <use xlink:href="#DejaVuSans-72" transform="translate(210.546875 0.015625)"/>
     <use xlink:href="#DejaVuSans-20" transform="translate(251.660156 0.015625)"/>
     <use xlink:href="#DejaVuSans-70" transform="translate(283.447266 0.015625)"/>
     <use xlink:href="#DejaVuSans-6c" transform="translate(346.923828 0.015625)"/>
     <use xlink:href="#DejaVuSans-6f" transform="translate(374.707031 0.015625)"/>
     <use xlink:href="#DejaVuSans-74" transform="translate(435.888672 0.015625)"/>
     <use xlink:href="#DejaVuSans-20" transform="translate(475.097656 0.015625)"/>
     <use xlink:href="#DejaVuSans-66" transform="translate(506.884766 0.015625)"/>
     <use xlink:href="#DejaVuSans-6f" transform="translate(542.089844 0.015625)"/>
     <use xlink:href="#DejaVuSans-72" transform="translate(603.271484 0.015625)"/>
     <use xlink:href="#DejaVuSans-20" transform="translate(644.384766 0.015625)"/>
     <use xlink:href="#DejaVuSans-Oblique-4d" transform="translate(676.171875 0.015625)"/>
     <use xlink:href="#DejaVuSans-3d" transform="translate(781.933594 0.015625)"/>
     <use xlink:href="#DejaVuSans-30" transform="translate(885.205078 0.015625)"/>
     <use xlink:href="#DejaVuSans-2e" transform="translate(948.828125 0.015625)"/>
     <use xlink:href="#DejaVuSans-31" transform="translate(980.615234 0.015625)"/>
     <use xlink:href="#DejaVuSans-20" transform="translate(1044.238281 0.015625)"/>
     <use xlink:href="#DejaVuSans-61" transform="translate(1076.025391 0.015625)"/>
     <use xlink:href="#DejaVuSans-6e" transform="translate(1137.304688 0.015625)"/>
     <use xlink:href="#DejaVuSans-64" transform="translate(1200.683594 0.015625)"/>
     <use xlink:href="#DejaVuSans-20" transform="translate(1264.160156 0.015625)"/>
     <use xlink:href="#DejaVuSans-Oblique-52" transform="translate(1295.947266 0.015625)"/>
     <use xlink:href="#DejaVuSans-Oblique-65" transform="translate(1365.429688 0.015625)"/>
     <use xlink:href="#DejaVuSans-3d" transform="translate(1446.435547 0.015625)"/>
     <use xlink:href="#DejaVuSans-31" transform="translate(1549.707031 0.015625)"/>
     <use xlink:href="#DejaVuSans-30" transform="translate(1613.330078 0.015625)"/>
     <use xlink:href="#DejaVuSans-30" transform="translate(1676.953125 0.015625)"/>
     <use xlink:href="#DejaVuSans-30" transform="translate(1740.576172 0.015625)"/>
     <use xlink:href="#DejaVuSans-30" transform="translate(1804.199219 0.015625)"/>
     <use xlink:href="#DejaVuSans-30" transform="translate(1867.822266 0.015625)"/>
    </g>
   </g>
   <g id="legend_1">
    <g id="patch_7">
     <path d="M 59.704687 59.67625
L 198.704688 59.67625
Q 200.704688 59.67625 200.704688 57.67625
L 200.704688 29.32
Q 200.704688 27.32 198.704688 27.32
L 59.704687 27.32
Q 57.704687 27.32 57.704687 29.32
L 57.704687 57.67625
Q 57.704687 59.67625 59.704687 59.67625
z
" style="fill: #ffffff; opacity: 0.8; stroke: #cccccc; stroke-linejoin: miter"/>
    </g>
    <g id="line2d_31">
     <path d="M 61.704687 35.418437
L 71.704688 35.418437
L 81.704688 35.418437
" style="fill: none; stroke: #1f77b4; stroke-width: 1.5; stroke-linecap: square"/>
    </g>
    <g id="text_18">
     <!-- $Re = 100000$; $M = 0.1$ -->
     <g transform="translate(89.704688 38.918437) scale(0.1 -0.1)">
      <defs>
       <path id="DejaVuSans-3b" d="M 750 3309
L 1409 3309
L 1409 2516
L 750 2516
L 750 3309
z
M 750 794
L 1409 794
L 1409 256
L 897 -744
L 494 -744
L 750 256
L 750 794
z
" transform="scale(0.015625)"/>
      </defs>
      <use xlink:href="#DejaVuSans-Oblique-52" transform="translate(0 0.78125)"/>
      <use xlink:href="#DejaVuSans-Oblique-65" transform="translate(69.482422 0.78125)"/>
      <use xlink:href="#DejaVuSans-3d" transform="translate(150.488281 0.78125)"/>
      <use xlink:href="#DejaVuSans-31" transform="translate(253.759766 0.78125)"/>
      <use xlink:href="#DejaVuSans-30" transform="translate(317.382812 0.78125)"/>
      <use xlink:href="#DejaVuSans-30" transform="translate(381.005859 0.78125)"/>
      <use xlink:href="#DejaVuSans-30" transform="translate(444.628906 0.78125)"/>
      <use xlink:href="#DejaVuSans-30" transform="translate(508.251953 0.78125)"/>
      <use xlink:href="#DejaVuSans-30" transform="translate(571.875 0.78125)"/>
      <use xlink:href="#DejaVuSans-3b" transform="translate(635.498047 0.78125)"/>
      <use xlink:href="#DejaVuSans-20" transform="translate(669.189453 0.78125)"/>
      <use xlink:href="#DejaVuSans-Oblique-4d" transform="translate(700.976562 0.78125)"/>
      <use xlink:href="#DejaVuSans-3d" transform="translate(806.738281 0.78125)"/>
      <use xlink:href="#DejaVuSans-30" transform="translate(910.009766 0.78125)"/>
      <use xlink:href="#DejaVuSans-2e" transform="translate(973.632812 0.78125)"/>
      <use xlink:href="#DejaVuSans-31" transform="translate(1005.419922 0.78125)"/>
     </g>
    </g>
    <g id="line2d_32">
     <path d="M 61.704687 50.096562
L 71.704688 50.096562
L 81.704688 50.096562
" style="fill: none; stroke: #ff7f0e; stroke-width: 1.5; stroke-linecap: square"/>
    </g>
    <g id="text_19">
     <!-- $Re = 200000$; $M = 0.1$ -->
     <g transform="translate(89.704688 53.596562) scale(0.1 -0.1)">
      <use xlink:href="#DejaVuSans-Oblique-52" transform="translate(0 0.78125)"/>
      <use xlink:href="#DejaVuSans-Oblique-65" transform="translate(69.482422 0.78125)"/>
      <use xlink:href="#DejaVuSans-3d" transform="translate(150.488281 0.78125)"/>
      <use xlink:href="#DejaVuSans-32" transform="translate(253.759766 0.78125)"/>
      <use xlink:href="#DejaVuSans-30" transform="translate(317.382812 0.78125)"/>
      <use xlink:href="#DejaVuSans-30" transform="translate(381.005859 0.78125)"/>
      <use xlink:href="#DejaVuSans-30" transform="translate(444.628906 0.78125)"/>
      <use xlink:href="#DejaVuSans-30" transform="translate(508.251953 0.78125)"/>
      <use xlink:href="#DejaVuSans-30" transform="translate(571.875 0.78125)"/>
      <use xlink:href="#DejaVuSans-3b" transform="translate(635.498047 0.78125)"/>
      <use xlink:href="#DejaVuSans-20" transform="translate(669.189453 0.78125)"/>
      <use xlink:href="#DejaVuSans-Oblique-4d" transform="translate(700.976562 0.78125)"/>
      <use xlink:href="#DejaVuSans-3d" transform="translate(806.738281 0.78125)"/>
      <use xlink:href="#DejaVuSans-30" transform="translate(910.009766 0.78125)"/>
      <use xlink:href="#DejaVuSans-2e" transform="translate(973.632812 0.78125)"/>
      <use xlink:href="#DejaVuSans-31" transform="translate(1005.419922 0.78125)"/>
     </g>
    </g>
   </g>
  </g>
 </g>
 <defs>
  <clipPath id="p18e5c327e8">
   <rect x="52.704687" y="22.32" width="669.6" height="443.52"/>
  </clipPath>
 </defs>
</svg>


#
``` python
# Plot two lift curves created above
axp3 = None
axp3 = polar1.plot_polar(ax=axp3, xaxis='alpha', yaxis='cl', ls='-o')
axp3 = polar2.plot_polar(ax=axp3, xaxis='alpha', yaxis='cl', ls='-x')
_ = axp3.legend()
```

<svg xmlns:xlink="http://www.w3.org/1999/xlink" width="735.323437pt" height="503.39625pt" viewBox="0 0 735.323437 503.39625" xmlns="http://www.w3.org/2000/svg" version="1.1">
 <metadata>
  <rdf:RDF xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:cc="http://creativecommons.org/ns#" xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#">
   <cc:Work>
    <dc:type rdf:resource="http://purl.org/dc/dcmitype/StillImage"/>
    <dc:date>2023-02-24T16:11:45.457855</dc:date>
    <dc:format>image/svg+xml</dc:format>
    <dc:creator>
     <cc:Agent>
      <dc:title>Matplotlib v3.6.2, https://matplotlib.org/</dc:title>
     </cc:Agent>
    </dc:creator>
   </cc:Work>
  </rdf:RDF>
 </metadata>
 <defs>
  <style type="text/css">*{stroke-linejoin: round; stroke-linecap: butt}</style>
 </defs>
 <g id="figure_1">
  <g id="patch_1">
   <path d="M 0 503.39625
L 735.323437 503.39625
L 735.323437 0
L 0 0
z
" style="fill: #ffffff"/>
  </g>
  <g id="axes_1">
   <g id="patch_2">
    <path d="M 58.523438 465.84
L 728.123438 465.84
L 728.123438 22.32
L 58.523438 22.32
z
" style="fill: #ffffff"/>
   </g>
   <g id="matplotlib.axis_1">
    <g id="xtick_1">
     <g id="line2d_1">
      <path d="M 88.959801 465.84
L 88.959801 22.32
" clip-path="url(#p9e8d1be128)" style="fill: none; stroke: #b0b0b0; stroke-width: 0.8; stroke-linecap: square"/>
     </g>
     <g id="line2d_2">
      <defs>
       <path id="m9aba552471" d="M 0 0
L 0 3.5
" style="stroke: #000000; stroke-width: 0.8"/>
      </defs>
      <g>
       <use xlink:href="#m9aba552471" x="88.959801" y="465.84" style="stroke: #000000; stroke-width: 0.8"/>
      </g>
     </g>
     <g id="text_1">
      <!-- −10.0 -->
      <g transform="translate(73.637145 480.438437) scale(0.1 -0.1)">
       <defs>
        <path id="DejaVuSans-2212" d="M 678 2272
L 4684 2272
L 4684 1741
L 678 1741
L 678 2272
z
" transform="scale(0.015625)"/>
        <path id="DejaVuSans-31" d="M 794 531
L 1825 531
L 1825 4091
L 703 3866
L 703 4441
L 1819 4666
L 2450 4666
L 2450 531
L 3481 531
L 3481 0
L 794 0
L 794 531
z
" transform="scale(0.015625)"/>
        <path id="DejaVuSans-30" d="M 2034 4250
Q 1547 4250 1301 3770
Q 1056 3291 1056 2328
Q 1056 1369 1301 889
Q 1547 409 2034 409
Q 2525 409 2770 889
Q 3016 1369 3016 2328
Q 3016 3291 2770 3770
Q 2525 4250 2034 4250
z
M 2034 4750
Q 2819 4750 3233 4129
Q 3647 3509 3647 2328
Q 3647 1150 3233 529
Q 2819 -91 2034 -91
Q 1250 -91 836 529
Q 422 1150 422 2328
Q 422 3509 836 4129
Q 1250 4750 2034 4750
z
" transform="scale(0.015625)"/>
        <path id="DejaVuSans-2e" d="M 684 794
L 1344 794
L 1344 0
L 684 0
L 684 794
z
" transform="scale(0.015625)"/>
       </defs>
       <use xlink:href="#DejaVuSans-2212"/>
       <use xlink:href="#DejaVuSans-31" x="83.789062"/>
       <use xlink:href="#DejaVuSans-30" x="147.412109"/>
       <use xlink:href="#DejaVuSans-2e" x="211.035156"/>
       <use xlink:href="#DejaVuSans-30" x="242.822266"/>
      </g>
     </g>
    </g>
    <g id="xtick_2">
     <g id="line2d_3">
      <path d="M 165.05071 465.84
L 165.05071 22.32
" clip-path="url(#p9e8d1be128)" style="fill: none; stroke: #b0b0b0; stroke-width: 0.8; stroke-linecap: square"/>
     </g>
     <g id="line2d_4">
      <g>
       <use xlink:href="#m9aba552471" x="165.05071" y="465.84" style="stroke: #000000; stroke-width: 0.8"/>
      </g>
     </g>
     <g id="text_2">
      <!-- −7.5 -->
      <g transform="translate(152.909304 480.438437) scale(0.1 -0.1)">
       <defs>
        <path id="DejaVuSans-37" d="M 525 4666
L 3525 4666
L 3525 4397
L 1831 0
L 1172 0
L 2766 4134
L 525 4134
L 525 4666
z
" transform="scale(0.015625)"/>
        <path id="DejaVuSans-35" d="M 691 4666
L 3169 4666
L 3169 4134
L 1269 4134
L 1269 2991
Q 1406 3038 1543 3061
Q 1681 3084 1819 3084
Q 2600 3084 3056 2656
Q 3513 2228 3513 1497
Q 3513 744 3044 326
Q 2575 -91 1722 -91
Q 1428 -91 1123 -41
Q 819 9 494 109
L 494 744
Q 775 591 1075 516
Q 1375 441 1709 441
Q 2250 441 2565 725
Q 2881 1009 2881 1497
Q 2881 1984 2565 2268
Q 2250 2553 1709 2553
Q 1456 2553 1204 2497
Q 953 2441 691 2322
L 691 4666
z
" transform="scale(0.015625)"/>
       </defs>
       <use xlink:href="#DejaVuSans-2212"/>
       <use xlink:href="#DejaVuSans-37" x="83.789062"/>
       <use xlink:href="#DejaVuSans-2e" x="147.412109"/>
       <use xlink:href="#DejaVuSans-35" x="179.199219"/>
      </g>
     </g>
    </g>
    <g id="xtick_3">
     <g id="line2d_5">
      <path d="M 241.141619 465.84
L 241.141619 22.32
" clip-path="url(#p9e8d1be128)" style="fill: none; stroke: #b0b0b0; stroke-width: 0.8; stroke-linecap: square"/>
     </g>
     <g id="line2d_6">
      <g>
       <use xlink:href="#m9aba552471" x="241.141619" y="465.84" style="stroke: #000000; stroke-width: 0.8"/>
      </g>
     </g>
     <g id="text_3">
      <!-- −5.0 -->
      <g transform="translate(229.000213 480.438437) scale(0.1 -0.1)">
       <use xlink:href="#DejaVuSans-2212"/>
       <use xlink:href="#DejaVuSans-35" x="83.789062"/>
       <use xlink:href="#DejaVuSans-2e" x="147.412109"/>
       <use xlink:href="#DejaVuSans-30" x="179.199219"/>
      </g>
     </g>
    </g>
    <g id="xtick_4">
     <g id="line2d_7">
      <path d="M 317.232528 465.84
L 317.232528 22.32
" clip-path="url(#p9e8d1be128)" style="fill: none; stroke: #b0b0b0; stroke-width: 0.8; stroke-linecap: square"/>
     </g>
     <g id="line2d_8">
      <g>
       <use xlink:href="#m9aba552471" x="317.232528" y="465.84" style="stroke: #000000; stroke-width: 0.8"/>
      </g>
     </g>
     <g id="text_4">
      <!-- −2.5 -->
      <g transform="translate(305.091122 480.438437) scale(0.1 -0.1)">
       <defs>
        <path id="DejaVuSans-32" d="M 1228 531
L 3431 531
L 3431 0
L 469 0
L 469 531
Q 828 903 1448 1529
Q 2069 2156 2228 2338
Q 2531 2678 2651 2914
Q 2772 3150 2772 3378
Q 2772 3750 2511 3984
Q 2250 4219 1831 4219
Q 1534 4219 1204 4116
Q 875 4013 500 3803
L 500 4441
Q 881 4594 1212 4672
Q 1544 4750 1819 4750
Q 2544 4750 2975 4387
Q 3406 4025 3406 3419
Q 3406 3131 3298 2873
Q 3191 2616 2906 2266
Q 2828 2175 2409 1742
Q 1991 1309 1228 531
z
" transform="scale(0.015625)"/>
       </defs>
       <use xlink:href="#DejaVuSans-2212"/>
       <use xlink:href="#DejaVuSans-32" x="83.789062"/>
       <use xlink:href="#DejaVuSans-2e" x="147.412109"/>
       <use xlink:href="#DejaVuSans-35" x="179.199219"/>
      </g>
     </g>
    </g>
    <g id="xtick_5">
     <g id="line2d_9">
      <path d="M 393.323438 465.84
L 393.323438 22.32
" clip-path="url(#p9e8d1be128)" style="fill: none; stroke: #b0b0b0; stroke-width: 0.8; stroke-linecap: square"/>
     </g>
     <g id="line2d_10">
      <g>
       <use xlink:href="#m9aba552471" x="393.323438" y="465.84" style="stroke: #000000; stroke-width: 0.8"/>
      </g>
     </g>
     <g id="text_5">
      <!-- 0.0 -->
      <g transform="translate(385.371875 480.438437) scale(0.1 -0.1)">
       <use xlink:href="#DejaVuSans-30"/>
       <use xlink:href="#DejaVuSans-2e" x="63.623047"/>
       <use xlink:href="#DejaVuSans-30" x="95.410156"/>
      </g>
     </g>
    </g>
    <g id="xtick_6">
     <g id="line2d_11">
      <path d="M 469.414347 465.84
L 469.414347 22.32
" clip-path="url(#p9e8d1be128)" style="fill: none; stroke: #b0b0b0; stroke-width: 0.8; stroke-linecap: square"/>
     </g>
     <g id="line2d_12">
      <g>
       <use xlink:href="#m9aba552471" x="469.414347" y="465.84" style="stroke: #000000; stroke-width: 0.8"/>
      </g>
     </g>
     <g id="text_6">
      <!-- 2.5 -->
      <g transform="translate(461.462784 480.438437) scale(0.1 -0.1)">
       <use xlink:href="#DejaVuSans-32"/>
       <use xlink:href="#DejaVuSans-2e" x="63.623047"/>
       <use xlink:href="#DejaVuSans-35" x="95.410156"/>
      </g>
     </g>
    </g>
    <g id="xtick_7">
     <g id="line2d_13">
      <path d="M 545.505256 465.84
L 545.505256 22.32
" clip-path="url(#p9e8d1be128)" style="fill: none; stroke: #b0b0b0; stroke-width: 0.8; stroke-linecap: square"/>
     </g>
     <g id="line2d_14">
      <g>
       <use xlink:href="#m9aba552471" x="545.505256" y="465.84" style="stroke: #000000; stroke-width: 0.8"/>
      </g>
     </g>
     <g id="text_7">
      <!-- 5.0 -->
      <g transform="translate(537.553693 480.438437) scale(0.1 -0.1)">
       <use xlink:href="#DejaVuSans-35"/>
       <use xlink:href="#DejaVuSans-2e" x="63.623047"/>
       <use xlink:href="#DejaVuSans-30" x="95.410156"/>
      </g>
     </g>
    </g>
    <g id="xtick_8">
     <g id="line2d_15">
      <path d="M 621.596165 465.84
L 621.596165 22.32
" clip-path="url(#p9e8d1be128)" style="fill: none; stroke: #b0b0b0; stroke-width: 0.8; stroke-linecap: square"/>
     </g>
     <g id="line2d_16">
      <g>
       <use xlink:href="#m9aba552471" x="621.596165" y="465.84" style="stroke: #000000; stroke-width: 0.8"/>
      </g>
     </g>
     <g id="text_8">
      <!-- 7.5 -->
      <g transform="translate(613.644602 480.438437) scale(0.1 -0.1)">
       <use xlink:href="#DejaVuSans-37"/>
       <use xlink:href="#DejaVuSans-2e" x="63.623047"/>
       <use xlink:href="#DejaVuSans-35" x="95.410156"/>
      </g>
     </g>
    </g>
    <g id="xtick_9">
     <g id="line2d_17">
      <path d="M 697.687074 465.84
L 697.687074 22.32
" clip-path="url(#p9e8d1be128)" style="fill: none; stroke: #b0b0b0; stroke-width: 0.8; stroke-linecap: square"/>
     </g>
     <g id="line2d_18">
      <g>
       <use xlink:href="#m9aba552471" x="697.687074" y="465.84" style="stroke: #000000; stroke-width: 0.8"/>
      </g>
     </g>
     <g id="text_9">
      <!-- 10.0 -->
      <g transform="translate(686.554261 480.438437) scale(0.1 -0.1)">
       <use xlink:href="#DejaVuSans-31"/>
       <use xlink:href="#DejaVuSans-30" x="63.623047"/>
       <use xlink:href="#DejaVuSans-2e" x="127.246094"/>
       <use xlink:href="#DejaVuSans-30" x="159.033203"/>
      </g>
     </g>
    </g>
    <g id="text_10">
     <!-- $\alpha$ -->
     <g transform="translate(390.023438 494.116562) scale(0.1 -0.1)">
      <defs>
       <path id="DejaVuSans-Oblique-3b1" d="M 2619 1628
L 2622 2350
Q 2625 3088 2069 3091
Q 1653 3094 1394 2747
Q 1069 2319 959 1747
Q 825 1059 994 731
Q 1169 397 1547 397
Q 1966 397 2319 1063
L 2619 1628
z
M 2166 3578
Q 3141 3594 3128 2584
Q 3128 2584 3616 3500
L 4128 3500
L 3119 1603
L 3109 919
Q 3109 766 3194 638
Q 3291 488 3391 488
L 3669 488
L 3575 0
L 3228 0
Q 2934 0 2722 263
Q 2622 394 2619 669
Q 2416 334 2066 50
Q 1900 -81 1453 -78
Q 722 -72 456 397
Q 184 884 353 1747
Q 534 2675 1009 3097
Q 1544 3569 2166 3578
z
" transform="scale(0.015625)"/>
      </defs>
      <use xlink:href="#DejaVuSans-Oblique-3b1" transform="translate(0 0.84375)"/>
     </g>
    </g>
   </g>
   <g id="matplotlib.axis_2">
    <g id="ytick_1">
     <g id="line2d_19">
      <path d="M 58.523438 447.019265
L 728.123438 447.019265
" clip-path="url(#p9e8d1be128)" style="fill: none; stroke: #b0b0b0; stroke-width: 0.8; stroke-linecap: square"/>
     </g>
     <g id="line2d_20">
      <defs>
       <path id="m0256a65149" d="M 0 0
L -3.5 0
" style="stroke: #000000; stroke-width: 0.8"/>
      </defs>
      <g>
       <use xlink:href="#m0256a65149" x="58.523438" y="447.019265" style="stroke: #000000; stroke-width: 0.8"/>
      </g>
     </g>
     <g id="text_11">
      <!-- −1.00 -->
      <g transform="translate(20.878125 450.818484) scale(0.1 -0.1)">
       <use xlink:href="#DejaVuSans-2212"/>
       <use xlink:href="#DejaVuSans-31" x="83.789062"/>
       <use xlink:href="#DejaVuSans-2e" x="147.412109"/>
       <use xlink:href="#DejaVuSans-30" x="179.199219"/>
       <use xlink:href="#DejaVuSans-30" x="242.822266"/>
      </g>
     </g>
    </g>
    <g id="ytick_2">
     <g id="line2d_21">
      <path d="M 58.523438 396.289522
L 728.123438 396.289522
" clip-path="url(#p9e8d1be128)" style="fill: none; stroke: #b0b0b0; stroke-width: 0.8; stroke-linecap: square"/>
     </g>
     <g id="line2d_22">
      <g>
       <use xlink:href="#m0256a65149" x="58.523438" y="396.289522" style="stroke: #000000; stroke-width: 0.8"/>
      </g>
     </g>
     <g id="text_12">
      <!-- −0.75 -->
      <g transform="translate(20.878125 400.088741) scale(0.1 -0.1)">
       <use xlink:href="#DejaVuSans-2212"/>
       <use xlink:href="#DejaVuSans-30" x="83.789062"/>
       <use xlink:href="#DejaVuSans-2e" x="147.412109"/>
       <use xlink:href="#DejaVuSans-37" x="179.199219"/>
       <use xlink:href="#DejaVuSans-35" x="242.822266"/>
      </g>
     </g>
    </g>
    <g id="ytick_3">
     <g id="line2d_23">
      <path d="M 58.523438 345.559779
L 728.123438 345.559779
" clip-path="url(#p9e8d1be128)" style="fill: none; stroke: #b0b0b0; stroke-width: 0.8; stroke-linecap: square"/>
     </g>
     <g id="line2d_24">
      <g>
       <use xlink:href="#m0256a65149" x="58.523438" y="345.559779" style="stroke: #000000; stroke-width: 0.8"/>
      </g>
     </g>
     <g id="text_13">
      <!-- −0.50 -->
      <g transform="translate(20.878125 349.358997) scale(0.1 -0.1)">
       <use xlink:href="#DejaVuSans-2212"/>
       <use xlink:href="#DejaVuSans-30" x="83.789062"/>
       <use xlink:href="#DejaVuSans-2e" x="147.412109"/>
       <use xlink:href="#DejaVuSans-35" x="179.199219"/>
       <use xlink:href="#DejaVuSans-30" x="242.822266"/>
      </g>
     </g>
    </g>
    <g id="ytick_4">
     <g id="line2d_25">
      <path d="M 58.523438 294.830035
L 728.123438 294.830035
" clip-path="url(#p9e8d1be128)" style="fill: none; stroke: #b0b0b0; stroke-width: 0.8; stroke-linecap: square"/>
     </g>
     <g id="line2d_26">
      <g>
       <use xlink:href="#m0256a65149" x="58.523438" y="294.830035" style="stroke: #000000; stroke-width: 0.8"/>
      </g>
     </g>
     <g id="text_14">
      <!-- −0.25 -->
      <g transform="translate(20.878125 298.629254) scale(0.1 -0.1)">
       <use xlink:href="#DejaVuSans-2212"/>
       <use xlink:href="#DejaVuSans-30" x="83.789062"/>
       <use xlink:href="#DejaVuSans-2e" x="147.412109"/>
       <use xlink:href="#DejaVuSans-32" x="179.199219"/>
       <use xlink:href="#DejaVuSans-35" x="242.822266"/>
      </g>
     </g>
    </g>
    <g id="ytick_5">
     <g id="line2d_27">
      <path d="M 58.523438 244.100292
L 728.123438 244.100292
" clip-path="url(#p9e8d1be128)" style="fill: none; stroke: #b0b0b0; stroke-width: 0.8; stroke-linecap: square"/>
     </g>
     <g id="line2d_28">
      <g>
       <use xlink:href="#m0256a65149" x="58.523438" y="244.100292" style="stroke: #000000; stroke-width: 0.8"/>
      </g>
     </g>
     <g id="text_15">
      <!-- 0.00 -->
      <g transform="translate(29.257812 247.899511) scale(0.1 -0.1)">
       <use xlink:href="#DejaVuSans-30"/>
       <use xlink:href="#DejaVuSans-2e" x="63.623047"/>
       <use xlink:href="#DejaVuSans-30" x="95.410156"/>
       <use xlink:href="#DejaVuSans-30" x="159.033203"/>
      </g>
     </g>
    </g>
    <g id="ytick_6">
     <g id="line2d_29">
      <path d="M 58.523438 193.370549
L 728.123438 193.370549
" clip-path="url(#p9e8d1be128)" style="fill: none; stroke: #b0b0b0; stroke-width: 0.8; stroke-linecap: square"/>
     </g>
     <g id="line2d_30">
      <g>
       <use xlink:href="#m0256a65149" x="58.523438" y="193.370549" style="stroke: #000000; stroke-width: 0.8"/>
      </g>
     </g>
     <g id="text_16">
      <!-- 0.25 -->
      <g transform="translate(29.257812 197.169767) scale(0.1 -0.1)">
       <use xlink:href="#DejaVuSans-30"/>
       <use xlink:href="#DejaVuSans-2e" x="63.623047"/>
       <use xlink:href="#DejaVuSans-32" x="95.410156"/>
       <use xlink:href="#DejaVuSans-35" x="159.033203"/>
      </g>
     </g>
    </g>
    <g id="ytick_7">
     <g id="line2d_31">
      <path d="M 58.523438 142.640805
L 728.123438 142.640805
" clip-path="url(#p9e8d1be128)" style="fill: none; stroke: #b0b0b0; stroke-width: 0.8; stroke-linecap: square"/>
     </g>
     <g id="line2d_32">
      <g>
       <use xlink:href="#m0256a65149" x="58.523438" y="142.640805" style="stroke: #000000; stroke-width: 0.8"/>
      </g>
     </g>
     <g id="text_17">
      <!-- 0.50 -->
      <g transform="translate(29.257812 146.440024) scale(0.1 -0.1)">
       <use xlink:href="#DejaVuSans-30"/>
       <use xlink:href="#DejaVuSans-2e" x="63.623047"/>
       <use xlink:href="#DejaVuSans-35" x="95.410156"/>
       <use xlink:href="#DejaVuSans-30" x="159.033203"/>
      </g>
     </g>
    </g>
    <g id="ytick_8">
     <g id="line2d_33">
      <path d="M 58.523438 91.911062
L 728.123438 91.911062
" clip-path="url(#p9e8d1be128)" style="fill: none; stroke: #b0b0b0; stroke-width: 0.8; stroke-linecap: square"/>
     </g>
     <g id="line2d_34">
      <g>
       <use xlink:href="#m0256a65149" x="58.523438" y="91.911062" style="stroke: #000000; stroke-width: 0.8"/>
      </g>
     </g>
     <g id="text_18">
      <!-- 0.75 -->
      <g transform="translate(29.257812 95.710281) scale(0.1 -0.1)">
       <use xlink:href="#DejaVuSans-30"/>
       <use xlink:href="#DejaVuSans-2e" x="63.623047"/>
       <use xlink:href="#DejaVuSans-37" x="95.410156"/>
       <use xlink:href="#DejaVuSans-35" x="159.033203"/>
      </g>
     </g>
    </g>
    <g id="ytick_9">
     <g id="line2d_35">
      <path d="M 58.523438 41.181319
L 728.123438 41.181319
" clip-path="url(#p9e8d1be128)" style="fill: none; stroke: #b0b0b0; stroke-width: 0.8; stroke-linecap: square"/>
     </g>
     <g id="line2d_36">
      <g>
       <use xlink:href="#m0256a65149" x="58.523438" y="41.181319" style="stroke: #000000; stroke-width: 0.8"/>
      </g>
     </g>
     <g id="text_19">
      <!-- 1.00 -->
      <g transform="translate(29.257812 44.980537) scale(0.1 -0.1)">
       <use xlink:href="#DejaVuSans-31"/>
       <use xlink:href="#DejaVuSans-2e" x="63.623047"/>
       <use xlink:href="#DejaVuSans-30" x="95.410156"/>
       <use xlink:href="#DejaVuSans-30" x="159.033203"/>
      </g>
     </g>
    </g>
    <g id="text_20">
     <!-- $C_l$ -->
     <g transform="translate(14.798437 248.73) rotate(-90) scale(0.1 -0.1)">
      <defs>
       <path id="DejaVuSans-Oblique-43" d="M 4447 4306
L 4319 3641
Q 4019 3944 3683 4091
Q 3347 4238 2956 4238
Q 2422 4238 2017 3981
Q 1613 3725 1319 3200
Q 1131 2863 1032 2486
Q 934 2109 934 1728
Q 934 1091 1264 756
Q 1594 422 2222 422
Q 2656 422 3056 561
Q 3456 700 3834 978
L 3688 231
Q 3316 72 2936 -9
Q 2556 -91 2175 -91
Q 1278 -91 773 396
Q 269 884 269 1753
Q 269 2309 461 2846
Q 653 3384 1013 3828
Q 1394 4300 1883 4525
Q 2372 4750 3022 4750
Q 3422 4750 3780 4639
Q 4138 4528 4447 4306
z
" transform="scale(0.015625)"/>
       <path id="DejaVuSans-Oblique-6c" d="M 1172 4863
L 1747 4863
L 800 0
L 225 0
L 1172 4863
z
" transform="scale(0.015625)"/>
      </defs>
      <use xlink:href="#DejaVuSans-Oblique-43" transform="translate(0 0.78125)"/>
      <use xlink:href="#DejaVuSans-Oblique-6c" transform="translate(69.824219 -15.625) scale(0.7)"/>
     </g>
    </g>
   </g>
   <g id="line2d_37">
    <path d="M 88.959801 437.035652
L 104.177983 434.6615
L 119.396165 431.942386
L 134.614347 425.266351
L 149.832528 418.164187
L 165.05071 410.656185
L 180.268892 402.985848
L 195.487074 395.802516
L 210.705256 389.187358
L 225.923438 383.140372
L 241.141619 377.296306
L 256.359801 371.229029
L 271.577983 364.776205
L 286.796165 358.059587
L 302.014347 351.200926
L 317.232528 344.200221
L 332.45071 336.712511
L 347.668892 326.485395
L 362.887074 307.755974
L 378.105256 277.196376
L 393.323438 244.059708
L 408.541619 210.963624
L 423.759801 180.44461
L 438.977983 161.735481
L 454.196165 151.488072
L 469.414347 144.020654
L 484.632528 137.01995
L 499.85071 130.161288
L 515.068892 123.44467
L 530.287074 116.991847
L 545.505256 110.92457
L 560.723438 105.080503
L 575.941619 99.013226
L 591.159801 92.398067
L 606.377983 85.214736
L 636.814347 70.036397
L 652.032528 62.934233
L 667.25071 56.27849
L 697.687074 51.205516
" clip-path="url(#p9e8d1be128)" style="fill: none; stroke: #1f77b4; stroke-width: 1.5; stroke-linecap: square"/>
   </g>
   <g id="line2d_38">
    <path d="M 88.959801 445.68
L 104.177983 438.801047
L 119.396165 432.30764
L 134.614347 425.225767
L 149.832528 418.570025
L 165.05071 412.09691
L 180.268892 405.765838
L 195.487074 399.556517
L 210.705256 393.347197
L 225.923438 387.016125
L 241.141619 380.461842
L 256.359801 373.684348
L 271.577983 366.785103
L 286.796165 359.90615
L 302.014347 344.666935
L 317.232528 328.392833
L 332.45071 312.889824
L 347.668892 297.34623
L 362.887074 280.382204
L 378.105256 262.403583
L 393.323438 244.08
L 408.541619 225.817292
L 423.759801 207.818379
L 438.977983 190.854353
L 454.196165 175.31076
L 469.414347 159.848334
L 484.632528 143.493065
L 499.85071 128.314726
L 515.068892 121.435773
L 530.287074 114.516236
L 545.505256 107.738742
L 560.723438 101.204751
L 575.941619 94.873679
L 591.159801 88.664358
L 606.377983 82.455038
L 621.596165 76.103674
L 652.032528 62.934233
L 667.25071 55.872652
L 697.687074 42.48
" clip-path="url(#p9e8d1be128)" style="fill: none; stroke: #ff7f0e; stroke-width: 1.5; stroke-linecap: square"/>
   </g>
   <g id="patch_3">
    <path d="M 58.523438 465.84
L 58.523438 22.32
" style="fill: none; stroke: #000000; stroke-width: 0.8; stroke-linejoin: miter; stroke-linecap: square"/>
   </g>
   <g id="patch_4">
    <path d="M 728.123438 465.84
L 728.123438 22.32
" style="fill: none; stroke: #000000; stroke-width: 0.8; stroke-linejoin: miter; stroke-linecap: square"/>
   </g>
   <g id="patch_5">
    <path d="M 58.523438 465.84
L 728.123438 465.84
" style="fill: none; stroke: #000000; stroke-width: 0.8; stroke-linejoin: miter; stroke-linecap: square"/>
   </g>
   <g id="patch_6">
    <path d="M 58.523438 22.32
L 728.123438 22.32
" style="fill: none; stroke: #000000; stroke-width: 0.8; stroke-linejoin: miter; stroke-linecap: square"/>
   </g>
   <g id="text_21">
    <!-- Polar plot for $M = 0.1$ and $Re = 100000$ -->
    <g transform="translate(277.403437 16.32) scale(0.12 -0.12)">
     <defs>
      <path id="DejaVuSans-50" d="M 1259 4147
L 1259 2394
L 2053 2394
Q 2494 2394 2734 2622
Q 2975 2850 2975 3272
Q 2975 3691 2734 3919
Q 2494 4147 2053 4147
L 1259 4147
z
M 628 4666
L 2053 4666
Q 2838 4666 3239 4311
Q 3641 3956 3641 3272
Q 3641 2581 3239 2228
Q 2838 1875 2053 1875
L 1259 1875
L 1259 0
L 628 0
L 628 4666
z
" transform="scale(0.015625)"/>
      <path id="DejaVuSans-6f" d="M 1959 3097
Q 1497 3097 1228 2736
Q 959 2375 959 1747
Q 959 1119 1226 758
Q 1494 397 1959 397
Q 2419 397 2687 759
Q 2956 1122 2956 1747
Q 2956 2369 2687 2733
Q 2419 3097 1959 3097
z
M 1959 3584
Q 2709 3584 3137 3096
Q 3566 2609 3566 1747
Q 3566 888 3137 398
Q 2709 -91 1959 -91
Q 1206 -91 779 398
Q 353 888 353 1747
Q 353 2609 779 3096
Q 1206 3584 1959 3584
z
" transform="scale(0.015625)"/>
      <path id="DejaVuSans-6c" d="M 603 4863
L 1178 4863
L 1178 0
L 603 0
L 603 4863
z
" transform="scale(0.015625)"/>
      <path id="DejaVuSans-61" d="M 2194 1759
Q 1497 1759 1228 1600
Q 959 1441 959 1056
Q 959 750 1161 570
Q 1363 391 1709 391
Q 2188 391 2477 730
Q 2766 1069 2766 1631
L 2766 1759
L 2194 1759
z
M 3341 1997
L 3341 0
L 2766 0
L 2766 531
Q 2569 213 2275 61
Q 1981 -91 1556 -91
Q 1019 -91 701 211
Q 384 513 384 1019
Q 384 1609 779 1909
Q 1175 2209 1959 2209
L 2766 2209
L 2766 2266
Q 2766 2663 2505 2880
Q 2244 3097 1772 3097
Q 1472 3097 1187 3025
Q 903 2953 641 2809
L 641 3341
Q 956 3463 1253 3523
Q 1550 3584 1831 3584
Q 2591 3584 2966 3190
Q 3341 2797 3341 1997
z
" transform="scale(0.015625)"/>
      <path id="DejaVuSans-72" d="M 2631 2963
Q 2534 3019 2420 3045
Q 2306 3072 2169 3072
Q 1681 3072 1420 2755
Q 1159 2438 1159 1844
L 1159 0
L 581 0
L 581 3500
L 1159 3500
L 1159 2956
Q 1341 3275 1631 3429
Q 1922 3584 2338 3584
Q 2397 3584 2469 3576
Q 2541 3569 2628 3553
L 2631 2963
z
" transform="scale(0.015625)"/>
      <path id="DejaVuSans-20" transform="scale(0.015625)"/>
      <path id="DejaVuSans-70" d="M 1159 525
L 1159 -1331
L 581 -1331
L 581 3500
L 1159 3500
L 1159 2969
Q 1341 3281 1617 3432
Q 1894 3584 2278 3584
Q 2916 3584 3314 3078
Q 3713 2572 3713 1747
Q 3713 922 3314 415
Q 2916 -91 2278 -91
Q 1894 -91 1617 61
Q 1341 213 1159 525
z
M 3116 1747
Q 3116 2381 2855 2742
Q 2594 3103 2138 3103
Q 1681 3103 1420 2742
Q 1159 2381 1159 1747
Q 1159 1113 1420 752
Q 1681 391 2138 391
Q 2594 391 2855 752
Q 3116 1113 3116 1747
z
" transform="scale(0.015625)"/>
      <path id="DejaVuSans-74" d="M 1172 4494
L 1172 3500
L 2356 3500
L 2356 3053
L 1172 3053
L 1172 1153
Q 1172 725 1289 603
Q 1406 481 1766 481
L 2356 481
L 2356 0
L 1766 0
Q 1100 0 847 248
Q 594 497 594 1153
L 594 3053
L 172 3053
L 172 3500
L 594 3500
L 594 4494
L 1172 4494
z
" transform="scale(0.015625)"/>
      <path id="DejaVuSans-66" d="M 2375 4863
L 2375 4384
L 1825 4384
Q 1516 4384 1395 4259
Q 1275 4134 1275 3809
L 1275 3500
L 2222 3500
L 2222 3053
L 1275 3053
L 1275 0
L 697 0
L 697 3053
L 147 3053
L 147 3500
L 697 3500
L 697 3744
Q 697 4328 969 4595
Q 1241 4863 1831 4863
L 2375 4863
z
" transform="scale(0.015625)"/>
      <path id="DejaVuSans-Oblique-4d" d="M 1081 4666
L 2028 4666
L 2572 1522
L 4378 4666
L 5350 4666
L 4441 0
L 3828 0
L 4622 4091
L 2791 897
L 2175 897
L 1581 4103
L 788 0
L 172 0
L 1081 4666
z
" transform="scale(0.015625)"/>
      <path id="DejaVuSans-3d" d="M 678 2906
L 4684 2906
L 4684 2381
L 678 2381
L 678 2906
z
M 678 1631
L 4684 1631
L 4684 1100
L 678 1100
L 678 1631
z
" transform="scale(0.015625)"/>
      <path id="DejaVuSans-6e" d="M 3513 2113
L 3513 0
L 2938 0
L 2938 2094
Q 2938 2591 2744 2837
Q 2550 3084 2163 3084
Q 1697 3084 1428 2787
Q 1159 2491 1159 1978
L 1159 0
L 581 0
L 581 3500
L 1159 3500
L 1159 2956
Q 1366 3272 1645 3428
Q 1925 3584 2291 3584
Q 2894 3584 3203 3211
Q 3513 2838 3513 2113
z
" transform="scale(0.015625)"/>
      <path id="DejaVuSans-64" d="M 2906 2969
L 2906 4863
L 3481 4863
L 3481 0
L 2906 0
L 2906 525
Q 2725 213 2448 61
Q 2172 -91 1784 -91
Q 1150 -91 751 415
Q 353 922 353 1747
Q 353 2572 751 3078
Q 1150 3584 1784 3584
Q 2172 3584 2448 3432
Q 2725 3281 2906 2969
z
M 947 1747
Q 947 1113 1208 752
Q 1469 391 1925 391
Q 2381 391 2643 752
Q 2906 1113 2906 1747
Q 2906 2381 2643 2742
Q 2381 3103 1925 3103
Q 1469 3103 1208 2742
Q 947 2381 947 1747
z
" transform="scale(0.015625)"/>
      <path id="DejaVuSans-Oblique-52" d="M 1613 4147
L 1294 2491
L 2106 2491
Q 2584 2491 2879 2755
Q 3175 3019 3175 3444
Q 3175 3784 2976 3965
Q 2778 4147 2406 4147
L 1613 4147
z
M 2772 2241
Q 2972 2194 3105 2009
Q 3238 1825 3413 1275
L 3809 0
L 3144 0
L 2778 1197
Q 2638 1659 2453 1815
Q 2269 1972 1888 1972
L 1191 1972
L 806 0
L 172 0
L 1081 4666
L 2503 4666
Q 3150 4666 3495 4373
Q 3841 4081 3841 3531
Q 3841 3044 3547 2687
Q 3253 2331 2772 2241
z
" transform="scale(0.015625)"/>
      <path id="DejaVuSans-Oblique-65" d="M 3078 2063
Q 3088 2113 3092 2166
Q 3097 2219 3097 2272
Q 3097 2653 2873 2875
Q 2650 3097 2266 3097
Q 1838 3097 1509 2826
Q 1181 2556 1013 2059
L 3078 2063
z
M 3578 1613
L 903 1613
Q 884 1494 878 1425
Q 872 1356 872 1306
Q 872 872 1139 634
Q 1406 397 1894 397
Q 2269 397 2603 481
Q 2938 566 3225 728
L 3116 159
Q 2806 34 2476 -28
Q 2147 -91 1806 -91
Q 1078 -91 686 257
Q 294 606 294 1247
Q 294 1794 489 2264
Q 684 2734 1063 3103
Q 1306 3334 1642 3459
Q 1978 3584 2356 3584
Q 2950 3584 3301 3228
Q 3653 2872 3653 2272
Q 3653 2128 3634 1964
Q 3616 1800 3578 1613
z
" transform="scale(0.015625)"/>
     </defs>
     <use xlink:href="#DejaVuSans-50" transform="translate(0 0.015625)"/>
     <use xlink:href="#DejaVuSans-6f" transform="translate(60.302734 0.015625)"/>
     <use xlink:href="#DejaVuSans-6c" transform="translate(121.484375 0.015625)"/>
     <use xlink:href="#DejaVuSans-61" transform="translate(149.267578 0.015625)"/>
     <use xlink:href="#DejaVuSans-72" transform="translate(210.546875 0.015625)"/>
     <use xlink:href="#DejaVuSans-20" transform="translate(251.660156 0.015625)"/>
     <use xlink:href="#DejaVuSans-70" transform="translate(283.447266 0.015625)"/>
     <use xlink:href="#DejaVuSans-6c" transform="translate(346.923828 0.015625)"/>
     <use xlink:href="#DejaVuSans-6f" transform="translate(374.707031 0.015625)"/>
     <use xlink:href="#DejaVuSans-74" transform="translate(435.888672 0.015625)"/>
     <use xlink:href="#DejaVuSans-20" transform="translate(475.097656 0.015625)"/>
     <use xlink:href="#DejaVuSans-66" transform="translate(506.884766 0.015625)"/>
     <use xlink:href="#DejaVuSans-6f" transform="translate(542.089844 0.015625)"/>
     <use xlink:href="#DejaVuSans-72" transform="translate(603.271484 0.015625)"/>
     <use xlink:href="#DejaVuSans-20" transform="translate(644.384766 0.015625)"/>
     <use xlink:href="#DejaVuSans-Oblique-4d" transform="translate(676.171875 0.015625)"/>
     <use xlink:href="#DejaVuSans-3d" transform="translate(781.933594 0.015625)"/>
     <use xlink:href="#DejaVuSans-30" transform="translate(885.205078 0.015625)"/>
     <use xlink:href="#DejaVuSans-2e" transform="translate(948.828125 0.015625)"/>
     <use xlink:href="#DejaVuSans-31" transform="translate(980.615234 0.015625)"/>
     <use xlink:href="#DejaVuSans-20" transform="translate(1044.238281 0.015625)"/>
     <use xlink:href="#DejaVuSans-61" transform="translate(1076.025391 0.015625)"/>
     <use xlink:href="#DejaVuSans-6e" transform="translate(1137.304688 0.015625)"/>
     <use xlink:href="#DejaVuSans-64" transform="translate(1200.683594 0.015625)"/>
     <use xlink:href="#DejaVuSans-20" transform="translate(1264.160156 0.015625)"/>
     <use xlink:href="#DejaVuSans-Oblique-52" transform="translate(1295.947266 0.015625)"/>
     <use xlink:href="#DejaVuSans-Oblique-65" transform="translate(1365.429688 0.015625)"/>
     <use xlink:href="#DejaVuSans-3d" transform="translate(1446.435547 0.015625)"/>
     <use xlink:href="#DejaVuSans-31" transform="translate(1549.707031 0.015625)"/>
     <use xlink:href="#DejaVuSans-30" transform="translate(1613.330078 0.015625)"/>
     <use xlink:href="#DejaVuSans-30" transform="translate(1676.953125 0.015625)"/>
     <use xlink:href="#DejaVuSans-30" transform="translate(1740.576172 0.015625)"/>
     <use xlink:href="#DejaVuSans-30" transform="translate(1804.199219 0.015625)"/>
     <use xlink:href="#DejaVuSans-30" transform="translate(1867.822266 0.015625)"/>
    </g>
   </g>
   <g id="legend_1">
    <g id="patch_7">
     <path d="M 65.523438 59.67625
L 204.523438 59.67625
Q 206.523438 59.67625 206.523438 57.67625
L 206.523438 29.32
Q 206.523438 27.32 204.523438 27.32
L 65.523438 27.32
Q 63.523438 27.32 63.523438 29.32
L 63.523438 57.67625
Q 63.523438 59.67625 65.523438 59.67625
z
" style="fill: #ffffff; opacity: 0.8; stroke: #cccccc; stroke-linejoin: miter"/>
    </g>
    <g id="line2d_39">
     <path d="M 67.523438 35.418437
L 77.523438 35.418437
L 87.523438 35.418437
" style="fill: none; stroke: #1f77b4; stroke-width: 1.5; stroke-linecap: square"/>
    </g>
    <g id="text_22">
     <!-- $Re = 100000$; $M = 0.1$ -->
     <g transform="translate(95.523438 38.918437) scale(0.1 -0.1)">
      <defs>
       <path id="DejaVuSans-3b" d="M 750 3309
L 1409 3309
L 1409 2516
L 750 2516
L 750 3309
z
M 750 794
L 1409 794
L 1409 256
L 897 -744
L 494 -744
L 750 256
L 750 794
z
" transform="scale(0.015625)"/>
      </defs>
      <use xlink:href="#DejaVuSans-Oblique-52" transform="translate(0 0.78125)"/>
      <use xlink:href="#DejaVuSans-Oblique-65" transform="translate(69.482422 0.78125)"/>
      <use xlink:href="#DejaVuSans-3d" transform="translate(150.488281 0.78125)"/>
      <use xlink:href="#DejaVuSans-31" transform="translate(253.759766 0.78125)"/>
      <use xlink:href="#DejaVuSans-30" transform="translate(317.382812 0.78125)"/>
      <use xlink:href="#DejaVuSans-30" transform="translate(381.005859 0.78125)"/>
      <use xlink:href="#DejaVuSans-30" transform="translate(444.628906 0.78125)"/>
      <use xlink:href="#DejaVuSans-30" transform="translate(508.251953 0.78125)"/>
      <use xlink:href="#DejaVuSans-30" transform="translate(571.875 0.78125)"/>
      <use xlink:href="#DejaVuSans-3b" transform="translate(635.498047 0.78125)"/>
      <use xlink:href="#DejaVuSans-20" transform="translate(669.189453 0.78125)"/>
      <use xlink:href="#DejaVuSans-Oblique-4d" transform="translate(700.976562 0.78125)"/>
      <use xlink:href="#DejaVuSans-3d" transform="translate(806.738281 0.78125)"/>
      <use xlink:href="#DejaVuSans-30" transform="translate(910.009766 0.78125)"/>
      <use xlink:href="#DejaVuSans-2e" transform="translate(973.632812 0.78125)"/>
      <use xlink:href="#DejaVuSans-31" transform="translate(1005.419922 0.78125)"/>
     </g>
    </g>
    <g id="line2d_40">
     <path d="M 67.523438 50.096562
L 77.523438 50.096562
L 87.523438 50.096562
" style="fill: none; stroke: #ff7f0e; stroke-width: 1.5; stroke-linecap: square"/>
    </g>
    <g id="text_23">
     <!-- $Re = 200000$; $M = 0.1$ -->
     <g transform="translate(95.523438 53.596562) scale(0.1 -0.1)">
      <use xlink:href="#DejaVuSans-Oblique-52" transform="translate(0 0.78125)"/>
      <use xlink:href="#DejaVuSans-Oblique-65" transform="translate(69.482422 0.78125)"/>
      <use xlink:href="#DejaVuSans-3d" transform="translate(150.488281 0.78125)"/>
      <use xlink:href="#DejaVuSans-32" transform="translate(253.759766 0.78125)"/>
      <use xlink:href="#DejaVuSans-30" transform="translate(317.382812 0.78125)"/>
      <use xlink:href="#DejaVuSans-30" transform="translate(381.005859 0.78125)"/>
      <use xlink:href="#DejaVuSans-30" transform="translate(444.628906 0.78125)"/>
      <use xlink:href="#DejaVuSans-30" transform="translate(508.251953 0.78125)"/>
      <use xlink:href="#DejaVuSans-30" transform="translate(571.875 0.78125)"/>
      <use xlink:href="#DejaVuSans-3b" transform="translate(635.498047 0.78125)"/>
      <use xlink:href="#DejaVuSans-20" transform="translate(669.189453 0.78125)"/>
      <use xlink:href="#DejaVuSans-Oblique-4d" transform="translate(700.976562 0.78125)"/>
      <use xlink:href="#DejaVuSans-3d" transform="translate(806.738281 0.78125)"/>
      <use xlink:href="#DejaVuSans-30" transform="translate(910.009766 0.78125)"/>
      <use xlink:href="#DejaVuSans-2e" transform="translate(973.632812 0.78125)"/>
      <use xlink:href="#DejaVuSans-31" transform="translate(1005.419922 0.78125)"/>
     </g>
    </g>
   </g>
  </g>
 </g>
 <defs>
  <clipPath id="p9e8d1be128">
   <rect x="58.523438" y="22.32" width="669.6" height="443.52"/>
  </clipPath>
 </defs>
</svg>
