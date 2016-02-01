import numpy as np
import matplotlib.pyplot as plt
import pyart


cmap_list = [
    'pyart_NWSRef',
    'pyart_NWSVel',
    'pyart_NWS_SPW',

    'pyart_RefDiff',
    'pyart_RRate11',
    'pyart_Cat12',
    'pyart_LangRainbow12',

    'pyart_EWilson17',
    'pyart_GrMg16',
    'pyart_PD17',
    'pyart_SCook18',
    'pyart_StepSeq25',
    'pyart_Theodore16',
    'pyart_Wild25',
    'pyart_Carbone11',
    'pyart_Carbone17',
    'pyart_Carbone42',

    # three color
    'pyart_BuOrR14',
    'pyart_RdYlBu11b',

    # Two color
    'pyart_BlueBrown10',
    'pyart_BlueBrown11',
    'pyart_BrBu10',
    'pyart_BrBu12',
    'pyart_BuGr14',
    'pyart_BuGy8',
    'pyart_BuOr8',
    'pyart_BuOr10',
    'pyart_BuOr12',
    'pyart_BuDOr12',
    'pyart_BuDOr18',
    'pyart_BuDRd12',
    'pyart_BuDRd18',

    # One color
    'pyart_Bu10',
    'pyart_Bu7',
    'pyart_Gray5',
    'pyart_Gray9',
    'pyart_SymGray12',

]
nrows = len(cmap_list)
gradient = np.linspace(0, 1, 256)
gradient = np.vstack((gradient, gradient))

# borrows from colormaps_reference matplotlib example
fig, axes = plt.subplots(nrows=nrows, figsize=(8, 8))
fig.subplots_adjust(top=0.95, bottom=0.01, left=0.2, right=0.99)
axes[0].set_title('Py-ART colormaps', fontsize=14)

for ax, name in zip(axes, cmap_list):
    ax.imshow(gradient, aspect='auto', cmap=plt.get_cmap(name))
    pos = list(ax.get_position().bounds)
    x_text = pos[0] - 0.01
    y_text = pos[1] + pos[3]/2.
    fig.text(x_text, y_text, name, va='center', ha='right', fontsize=10)

# Turn off *all* ticks & spines, not just the ones with colormaps.
for ax in axes:
    ax.set_axis_off()


plt.savefig('images/pyart_colormaps.png')
plt.show()
