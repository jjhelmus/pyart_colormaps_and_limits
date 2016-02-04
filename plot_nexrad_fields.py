from __future__ import print_function
import matplotlib.pyplot as plt
import pyart
import numpy as np

radar = pyart.io.read('KLOT20130418_043539_V06.gz')
nyquist = radar.instrument_parameters['nyquist_velocity']['data'][1]

fields_to_plot = {
    'reflectivity': ('pyart_NWSRef', -30, 75),
    'velocity': ('pyart_BuDRd18', -nyquist, nyquist),
    'spectrum_width': ('pyart_NWS_SPW', 0, nyquist),
    'differential_reflectivity': ('pyart_RefDiff', -1, 8),
    'cross_correlation_ratio': ('pyart_RefDiff', 0.5, 1.05),
    'differential_phase': ('pyart_Wild25', -180, 180),
}

for field, (cmap, vmin, vmax) in fields_to_plot.items():

    print("Printing:", field)
    plt.figure()
    display = pyart.graph.RadarDisplay(radar)
    if field in ['velocity', 'spectrum_width']:
        scan = 1
    else:
        scan = 0
    display.plot_ppi(field, sweep=scan, cmap=cmap, vmin=vmin, vmax=vmax)
    display.set_limits(ylim=(-320, 320), xlim=(-320, 320))
    plt.savefig('images/NEXRAD_' + field + '.png')
