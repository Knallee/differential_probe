import pandas as pd
import matplotlib.pyplot as mp

ch_a = pd.read_excel(r'C:\work\microradar\hardware\current_measurements\data\031122\dc_perfomance.xlsx', sheet_name='channel_a')
#print(ch_a)

ch_b = pd.read_excel(r'C:\work\microradar\hardware\current_measurements\data\031122\dc_perfomance.xlsx', sheet_name='channel_b')
#print(ch_b)

ch_c = pd.read_excel(r'C:\work\microradar\hardware\current_measurements\data\031122\dc_perfomance.xlsx', sheet_name='channel_c')
#print(ch_c)

ch_d = pd.read_excel(r'C:\work\microradar\hardware\current_measurements\data\031122\dc_perfomance.xlsx', sheet_name='channel_d')
#print(ch_d)



gain_2x      = ch_a[['Input']].copy()
gain_11x     = ch_a[['Input']].copy()
gain_101x    = ch_a[['Input']].copy()

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

gain_2x = gain_2x.join(ch_a_2x)
gain_2x = gain_2x.join(ch_b_2x)
gain_2x = gain_2x.join(ch_c_2x)
gain_2x = gain_2x.join(ch_d_2x)

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


fig1, ((ax1, ax2, ax3)) = mp.subplots(1, 3)


gain_2x.plot(x="Input", y=["ch_a","ch_b","ch_d"],
        kind="line", figsize=(10, 10), **{'marker': 'o'},
        ax=ax1, grid='true')



gain_11x.plot(x="Input", y=["ch_a","ch_b","ch_d"],
        kind="line", figsize=(10, 10), **{'marker': 'o'},
        ax=ax2, grid='true')



gain_101x.plot(x="Input", y=["ch_a","ch_b","ch_d"],
        kind="line", figsize=(10, 10), **{'marker': 'o'},
        ax=ax3, grid='true')

ax1.set_title('2x gain, stage 1, OPA2189')
ax2.set_title('11x gain, stage 1, OPA2189')
ax3.set_title('101x gain, stage 1, OPA2189')


ax1.yaxis.set_label_text("Output [mV]")
ax2.yaxis.set_label_text("Output [mV]")
ax3.yaxis.set_label_text("Output [mV]")

ax1.xaxis.set_label_text("Input [mV]")
ax2.xaxis.set_label_text("Input [mV]")
ax3.xaxis.set_label_text("Input [mV]")

########################### Calculating th gain factor ###########################

gain_factor_2x      = gain_2x.copy()
gain_factor_11x     = gain_11x.copy()
gain_factor_101x    = gain_101x.copy()

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

print(gain_factor_11x['ch_a'])

fig2, (ax4, ax5, ax6) = mp.subplots(1, 3)

gain_factor_2x.plot(x="Input", y=["ch_a","ch_b","ch_d"],
        kind="line", figsize=(10, 10), **{'marker': 'o'},
        ax=ax4, grid='true')



gain_factor_11x.plot(x="Input", y=["ch_a","ch_b","ch_d"],
        kind="line", figsize=(10, 10), **{'marker': 'o'},
        ax=ax5, grid='true')



gain_factor_101x.plot(x="Input", y=["ch_a","ch_b","ch_d"],
        kind="line", figsize=(10, 10), **{'marker': 'o'},
        ax=ax6, grid='true')

ax4.set_title('2x gain factor, stage 1, OPA2189')
ax5.set_title('11x gain factor, stage 1, OPA2189')
ax6.set_title('101x gain factor, stage 1, OPA2189')


ax4.yaxis.set_label_text("Gain factor")
ax5.yaxis.set_label_text("Gain factor")
ax6.yaxis.set_label_text("Gain factor")

ax4.xaxis.set_label_text("Input [mV]")
ax5.xaxis.set_label_text("Input [mV]")
ax6.xaxis.set_label_text("Input [mV]")

########################### Calculating the gain factor error ###########################

gain_factor_error_2x      = gain_2x.copy()
gain_factor_error_11x     = gain_11x.copy()
gain_factor_error_101x    = gain_101x.copy()

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

print((abs(101 - gain_factor_101x['ch_a'])/101) * 100)



fig3, (ax7, ax8, ax9) = mp.subplots(1, 3)

gain_factor_error_2x.plot(x="Input", y=["ch_a","ch_b","ch_d"],
        kind="line", figsize=(10, 10), **{'marker': 'o'},
        ax=ax7, grid='true')



gain_factor_error_11x.plot(x="Input", y=["ch_a","ch_b","ch_d"],
        kind="line", figsize=(10, 10), **{'marker': 'o'},
        ax=ax8, grid='true')



gain_factor_error_101x.plot(x="Input", y=["ch_a","ch_b","ch_d"],
        kind="line", figsize=(10, 10), **{'marker': 'o'},
        ax=ax9, grid='true')

ax7.set_title('2x, error gain factor, stage 1, OPA2189')
ax8.set_title('11x error gain factor, stage 1, OPA2189')
ax9.set_title('101x error gain factor, stage 1, OPA2189')


ax7.yaxis.set_label_text("Gain factor error [%]")
ax8.yaxis.set_label_text("Gain factor error [%]")
ax9.yaxis.set_label_text("Gain factor error [%]")

ax7.xaxis.set_label_text("Input [mV]")
ax8.xaxis.set_label_text("Input [mV]")
ax9.xaxis.set_label_text("Input [mV]")





mp.show()