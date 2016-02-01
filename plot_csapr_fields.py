from __future__ import print_function
import matplotlib.pyplot as plt
import pyart
import numpy as np

radar = pyart.io.read('110635.mdv')
nyquist = radar.instrument_parameters['nyquist_velocity']['data'][0]
for field in radar.fields.keys():
    radar.fields[field]['data'][:, -10:] = np.ma.masked

fields_to_plot = {
    'reflectivity': ('pyart_NWSRef', -30, 75),
    'velocity': ('pyart_NWSVel', -nyquist, nyquist),
    'spectrum_width': ('pyart_NWS_SPW', 0, nyquist),
    'normalized_coherent_power': ('pyart_Carbone17', 0.0, 1.0),
    'differential_reflectivity': ('pyart_RefDiff', 0, 8),
    'cross_correlation_ratio': ('pyart_RefDiff', 0.5, 1.05),
    'differential_phase': ('pyart_Wild25', -180, 180),
    'specific_differential_phase': ('pyart_Theodore16', -2, 5),
}

for field, (cmap, vmin, vmax) in fields_to_plot.items():

    print("Printing:", field)
    plt.figure()
    display = pyart.graph.RadarDisplay(radar)
    display.plot_ppi(field, cmap=cmap, vmin=vmin, vmax=vmax)
    plt.savefig('images/CSAPR_' + field + '.png')
