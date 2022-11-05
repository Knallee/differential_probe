import pandas as pd
import matplotlib.pyplot as mp

ch_a    = pd.read_excel(r'..\data\031122\dc_perfomance.xlsx', sheet_name='channel_a')
#print(ch_a)

ch_b = pd.read_excel(r'C:..\data\031122\dc_perfomance.xlsx', sheet_name='channel_b')
#print(ch_b)

ch_c = pd.read_excel(r'C:..\data\031122\dc_perfomance.xlsx', sheet_name='channel_c')
#print(ch_c)

ch_d = pd.read_excel(r'C:..\data\031122\dc_perfomance.xlsx', sheet_name='channel_d')
#print(ch_d)





gain_2x      = ch_a[['Input']].copy()
gain_11x     = ch_a[['Input']].copy()
gain_101x    = ch_a[['Input']].copy()

gain_s2_1x      = ch_a[['Input']].copy()
gain_s2_10x     = ch_a[['Input']].copy()

gain_factor_2x      = ch_a[['Input']].copy()
gain_factor_11x     = ch_a[['Input']].copy()
gain_factor_101x    = ch_a[['Input']].copy()

ch_a_2x = ch_a[['2x']].copy()
ch_b_2x = ch_b[['2x']].copy()
ch_c_2x = ch_c[['2x']].copy()
ch_d_2x = ch_d[['2x']].copy()

ch_a_2x = ch_a_2x.rename(columns={"2x": "ch_a"})
ch_b_2x = ch_b_2x.rename(columns={"2x": "ch_b"})
ch_c_2x = ch_c_2x.rename(columns={"2x": "ch_c"})
ch_d_2x = ch_d_2x.rename(columns={"2x": "ch_d"})

#print(ch_d)

ch_a_s2_1x      = ch_a[['S2: 1x']].copy()
ch_b_s2_1x      = ch_b[['S2: 1x']].copy()
ch_c_s2_1x      = ch_c[['S2: 1x']].copy()
ch_d_s2_1x      = ch_d[['S2: 1x']].copy()

ch_a_s2_10x     = ch_a[['S2: 10x']].copy()
ch_b_s2_10x     = ch_b[['S2: 10x']].copy()
ch_c_s2_10x     = ch_c[['S2: 10x']].copy()
ch_d_s2_10x     = ch_d[['S2: 10x']].copy()


ch_a_s2_1x      = ch_a_s2_1x.rename(columns={"S2: 1x": "ch_a"})
ch_b_s2_1x      = ch_b_s2_1x.rename(columns={"S2: 1x": "ch_b"})
ch_c_s2_1x      = ch_c_s2_1x.rename(columns={"S2: 1x": "ch_c"})
ch_d_s2_1x      = ch_d_s2_1x.rename(columns={"S2: 1x": "ch_d"})

ch_a_s2_10x     = ch_a_s2_10x.rename(columns={"S2: 10x": "ch_a"})
ch_b_s2_10x     = ch_b_s2_10x.rename(columns={"S2: 10x": "ch_b"})
ch_c_s2_10x     = ch_c_s2_10x.rename(columns={"S2: 10x": "ch_c"})
ch_d_s2_10x     = ch_d_s2_10x.rename(columns={"S2: 10x": "ch_d"})

gain_2x = gain_2x.join(ch_a_2x)
gain_2x = gain_2x.join(ch_b_2x)
gain_2x = gain_2x.join(ch_c_2x)
gain_2x = gain_2x.join(ch_d_2x)

gain_s2_1x      = gain_s2_1x.join(ch_a_s2_1x)
gain_s2_1x      = gain_s2_1x.join(ch_b_s2_1x)
gain_s2_1x      = gain_s2_1x.join(ch_c_s2_1x)
gain_s2_1x      = gain_s2_1x.join(ch_d_s2_1x)

gain_s2_10x     = gain_s2_10x.join(ch_a_s2_10x)
gain_s2_10x     = gain_s2_10x.join(ch_b_s2_10x)
gain_s2_10x     = gain_s2_10x.join(ch_c_s2_10x)
gain_s2_10x     = gain_s2_10x.join(ch_d_s2_10x)


ch_a_11x = ch_a[['11x']].copy()
ch_b_11x = ch_b[['11x']].copy()
ch_c_11x = ch_c[['11x']].copy()
ch_d_11x = ch_d[['11x']].copy()

ch_a_11x = ch_a_11x.rename(columns={"11x": "ch_a"})
ch_b_11x = ch_b_11x.rename(columns={"11x": "ch_b"})
ch_c_11x = ch_c_11x.rename(columns={"11x": "ch_c"})
ch_d_11x = ch_d_11x.rename(columns={"11x": "ch_d"})

gain_11x = gain_11x.join(ch_a_11x)
gain_11x = gain_11x.join(ch_b_11x)
gain_11x = gain_11x.join(ch_c_11x)
gain_11x = gain_11x.join(ch_d_11x)

ch_a_101x = ch_a[['101x']].copy()
ch_b_101x = ch_b[['101x']].copy()
ch_c_101x = ch_c[['101x']].copy()
ch_d_101x = ch_d[['101x']].copy()

ch_a_101x = ch_a_101x.rename(columns={"101x": "ch_a"})
ch_b_101x = ch_b_101x.rename(columns={"101x": "ch_b"})
ch_c_101x = ch_c_101x.rename(columns={"101x": "ch_c"})
ch_d_101x = ch_d_101x.rename(columns={"101x": "ch_d"})

gain_101x = gain_101x.join(ch_a_101x)
gain_101x = gain_101x.join(ch_b_101x)
gain_101x = gain_101x.join(ch_c_101x)
gain_101x = gain_101x.join(ch_d_101x)

########################### Plotting output vs input ###########################

fig1, ((ax1, ax2, ax3), (ax12, ax22, ax33)) = mp.subplots(2, 3)


gain_2x.plot(x="Input", y=["ch_a","ch_b","ch_d"],
        kind="line", figsize=(10, 10), **{'marker': 'o'},
        ax=ax1, grid='true')



gain_11x.plot(x="Input", y=["ch_a","ch_b","ch_d"],
        kind="line", figsize=(10, 10), **{'marker': 'o'},
        ax=ax2, grid='true')


gain_101x.plot(x="Input", y=["ch_a","ch_b","ch_d"],
        kind="line", figsize=(10, 10), **{'marker': 'o'},
        ax=ax3, grid='true')

gain_s2_1x.plot(x="Input", y=["ch_a", "ch_b", "ch_c", "ch_d"],
        kind="line", figsize=(10, 10), **{'marker': 'o'},
        ax=ax12, grid='true')


gain_s2_10x.plot(x="Input", y=["ch_a", "ch_b", "ch_c", "ch_d"],
        kind="line", figsize=(10, 10), **{'marker': 'o'},
        ax=ax22, grid='true')

ax1.set_title('2x gain, stage 1, OPA2189')
ax2.set_title('11x gain, stage 1, OPA2189')
ax3.set_title('101x gain, stage 1, OPA2189')

ax1.yaxis.set_label_text("Output [mV]")
ax2.yaxis.set_label_text("Output [mV]")
ax3.yaxis.set_label_text("Output [mV]")

ax1.xaxis.set_label_text("Input [mV]")
ax2.xaxis.set_label_text("Input [mV]")
ax3.xaxis.set_label_text("Input [mV]")

ax12.set_title('1x gain, stage 2, OPA189')
ax22.set_title('10x gain, stage 2, OPA189')


ax12.yaxis.set_label_text("Output [mV]")
ax22.yaxis.set_label_text("Output [mV]")


ax12.xaxis.set_label_text("Input [mV]")
ax22.xaxis.set_label_text("Input [mV]")


########################### Calculating th gain factor ###########################

gain_factor_2x      = gain_2x.copy()
gain_factor_11x     = gain_11x.copy()
gain_factor_101x    = gain_101x.copy()

gain_factor_s2_1x       = gain_s2_1x.copy()
gain_factor_s2_10x      = gain_s2_10x.copy()

gain_factor_2x['ch_a'] = gain_2x['ch_a'] / gain_2x['Input']
gain_factor_2x['ch_b'] = gain_2x['ch_b'] / gain_2x['Input']
#gain_factor_2x['ch_c'] = gain_2x['ch_c'] / gain_2x['Input']
gain_factor_2x['ch_d'] = gain_2x['ch_d'] / gain_2x['Input']

gain_factor_11x['ch_a']     = gain_11x['ch_a']  / gain_11x['Input']
gain_factor_11x['ch_b']     = gain_11x['ch_b']  / gain_11x['Input']
#gain_factor_11x['ch_c']     = gain_11x['ch_c']  / gain_11x['Input']
gain_factor_11x['ch_d']     = gain_11x['ch_d']  / gain_11x['Input']

gain_factor_101x['ch_a']    = gain_101x['ch_a'] / gain_101x['Input']
gain_factor_101x['ch_b']    = gain_101x['ch_b'] / gain_101x['Input']
#ain_factor_101x['ch_c']    = gain_101x['ch_c'] / gain_101x['Input']
gain_factor_101x['ch_d']    = gain_101x['ch_d'] / gain_101x['Input']

gain_factor_s2_1x['ch_a']       = gain_s2_1x['ch_a'] / gain_s2_1x['Input']
gain_factor_s2_1x['ch_b']       = gain_s2_1x['ch_b'] / gain_s2_1x['Input']
gain_factor_s2_1x['ch_c']       = gain_s2_1x['ch_c'] / gain_s2_1x['Input']
gain_factor_s2_1x['ch_d']       = gain_s2_1x['ch_d'] / gain_s2_1x['Input']

gain_factor_s2_10x['ch_a']      = gain_s2_10x['ch_a'] / gain_s2_10x['Input']
gain_factor_s2_10x['ch_b']      = gain_s2_10x['ch_b'] / gain_s2_10x['Input']
gain_factor_s2_10x['ch_c']      = gain_s2_10x['ch_c'] / gain_s2_10x['Input']
gain_factor_s2_10x['ch_d']      = gain_s2_10x['ch_d'] / gain_s2_10x['Input']



fig2, ((ax4, ax5, ax6), (ax42, ax52, ax62)) = mp.subplots(2, 3)

gain_factor_2x.plot(x="Input", y=["ch_a","ch_b","ch_d"],
        kind="line", figsize=(10, 10), **{'marker': 'o'},
        ax=ax4, grid='true')



gain_factor_11x.plot(x="Input", y=["ch_a","ch_b","ch_d"],
        kind="line", figsize=(10, 10), **{'marker': 'o'},
        ax=ax5, grid='true')



gain_factor_101x.plot(x="Input", y=["ch_a","ch_b","ch_d"],
        kind="line", figsize=(10, 10), **{'marker': 'o'},
        ax=ax6, grid='true')

gain_factor_s2_1x.plot(x="Input", y=["ch_a", "ch_b", "ch_c", "ch_d"],
        kind="line", figsize=(10, 10), **{'marker': 'o'},
        ax=ax42, grid='true')

gain_factor_s2_10x.plot(x="Input", y=["ch_a", "ch_b", "ch_c", "ch_d"],
        kind="line", figsize=(10, 10), **{'marker': 'o'},
        ax=ax52, grid='true')

ax4.set_title('2x gain factor, stage 1, OPA2189')
ax5.set_title('11x gain factor, stage 1, OPA2189')
ax6.set_title('101x gain factor, stage 1, OPA2189')

ax4.yaxis.set_label_text("Gain factor")
ax5.yaxis.set_label_text("Gain factor")
ax6.yaxis.set_label_text("Gain factor")

ax4.xaxis.set_label_text("Input [mV]")
ax5.xaxis.set_label_text("Input [mV]")
ax6.xaxis.set_label_text("Input [mV]")

ax42.set_title('1x gain factor, stage 2, OPA189')
ax52.set_title('10x gain factor, stage 2, OPA189')


ax42.yaxis.set_label_text("Gain factor")
ax52.yaxis.set_label_text("Gain factor")


ax42.xaxis.set_label_text("Input [mV]")
ax52.xaxis.set_label_text("Input [mV]")


########################### Calculating the gain factor error ###########################

gain_factor_error_2x      = gain_2x.copy()
gain_factor_error_11x     = gain_11x.copy()
gain_factor_error_101x    = gain_101x.copy()

gain_factor_error_s2_1x         = gain_s2_1x.copy()
gain_factor_error_s2_10x        = gain_s2_10x.copy()

gain_factor_error_2x['ch_a'] = (abs(2 - gain_factor_2x['ch_a'])/2) * 100
gain_factor_error_2x['ch_b'] = (abs(2 - gain_factor_2x['ch_b'])/2) * 100
#gain_factor_error_2x['ch_c'] = (abs(2 - gain_factor_2x['ch_c'])/2) * 100
gain_factor_error_2x['ch_d'] = (abs(2 - gain_factor_2x['ch_d'])/2) * 100

gain_factor_error_11x['ch_a'] = (abs(11 - gain_factor_11x['ch_a'])/11) * 100
gain_factor_error_11x['ch_b'] = (abs(11 - gain_factor_11x['ch_b'])/11) * 100
#gain_factor_error_11x['ch_c'] = (abs(11 - gain_factor_11x['ch_c'])/11) * 100
gain_factor_error_11x['ch_d'] = (abs(11 - gain_factor_11x['ch_d'])/11) * 100

gain_factor_error_101x['ch_a'] = (abs(101 - gain_factor_101x['ch_a'])/101) * 100
gain_factor_error_101x['ch_b'] = (abs(101 - gain_factor_101x['ch_b'])/101) * 100
#gain_factor_error_101x['ch_c'] = (abs(101 - gain_factor_101x['ch_c'])/101) * 100
gain_factor_error_101x['ch_d'] = (abs(101 - gain_factor_101x['ch_d'])/101) * 100

gain_factor_error_s2_1x['ch_a'] = (abs(1 - gain_factor_s2_1x['ch_a'])) * 100
gain_factor_error_s2_1x['ch_b'] = (abs(1 - gain_factor_s2_1x['ch_b'])) * 100
gain_factor_error_s2_1x['ch_c'] = (abs(1 - gain_factor_s2_1x['ch_c'])) * 100
gain_factor_error_s2_1x['ch_d'] = (abs(1 - gain_factor_s2_1x['ch_d'])) * 100

gain_factor_error_s2_10x['ch_a'] = (abs(10 - gain_factor_s2_10x['ch_a'])/10) * 100
gain_factor_error_s2_10x['ch_b'] = (abs(10 - gain_factor_s2_10x['ch_b'])/10) * 100
gain_factor_error_s2_10x['ch_c'] = (abs(10 - gain_factor_s2_10x['ch_c'])/10) * 100
gain_factor_error_s2_10x['ch_d'] = (abs(10 - gain_factor_s2_10x['ch_d'])/10) * 100

print((abs(10 - gain_factor_s2_10x['ch_a'])/10) * 100)
print((abs(10 - gain_factor_s2_10x['ch_b'])/10) * 100)
print((abs(10 - gain_factor_s2_10x['ch_c'])/10) * 100)
print((abs(10 - gain_factor_s2_10x['ch_d'])/10) * 100)
print("##############")
print(gain_factor_error_s2_10x)


fig3, ((ax7, ax8, ax9), (ax72, ax82, ax92))  = mp.subplots(2, 3)

gain_factor_error_2x.plot(x="Input", y=["ch_a","ch_b","ch_d"],
        kind="line", figsize=(10, 10), **{'marker': 'o'},
        ax=ax7, grid='true')



gain_factor_error_11x.plot(x="Input", y=["ch_a","ch_b","ch_d"],
        kind="line", figsize=(10, 10), **{'marker': 'o'},
        ax=ax8, grid='true')



gain_factor_error_101x.plot(x="Input", y=["ch_a","ch_b","ch_d"],
        kind="line", figsize=(10, 10), **{'marker': 'o'},
        ax=ax9, grid='true')

gain_factor_error_s2_1x.plot(x="Input", y=["ch_a", "ch_b", "ch_c", "ch_d"],
        kind="line", figsize=(10, 10), **{'marker': 'o'},
        ax=ax72, grid='true')

gain_factor_error_s2_10x.plot(x="Input", y=["ch_a", "ch_b", "ch_c", "ch_d"],
        kind="line", figsize=(10, 10), **{'marker': 'o'},
        ax=ax82, grid='true')



ax7.set_title('2x, error gain factor, stage 1, OPA2189')
ax8.set_title('11x error gain factor, stage 1, OPA2189')
ax9.set_title('101x error gain factor, stage 1, OPA2189')


ax7.yaxis.set_label_text("Gain factor error [%]")
ax8.yaxis.set_label_text("Gain factor error [%]")
ax9.yaxis.set_label_text("Gain factor error [%]")

ax7.xaxis.set_label_text("Input [mV]")
ax8.xaxis.set_label_text("Input [mV]")
ax9.xaxis.set_label_text("Input [mV]")

ax72.set_title('1x, error gain factor, stage 2, OPA189')
ax82.set_title('10x error gain factor, stage 2, OPA189')
#ax92.set_title('101x error gain factor, stage 1, OPA2189')


ax72.yaxis.set_label_text("Gain factor error [%]")
ax82.yaxis.set_label_text("Gain factor error [%]")
#ax92.yaxis.set_label_text("Gain factor error [%]")

ax72.xaxis.set_label_text("Input [mV]")
ax82.xaxis.set_label_text("Input [mV]")
ax92#.xaxis.set_label_text("Input [mV]")

mp.show()