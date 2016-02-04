from __future__ import print_function
import matplotlib.pyplot as plt
import pyart
import numpy as np

radar = pyart.io.read('sgpwsacrcwrhiC1.a1.20120820.204016.nc')
nyquist = radar.instrument_parameters['nyquist_velocity']['data'][0]

fields_to_plot = {
    'reflectivity': ('pyart_NWSRef', -30, 75),
    'mean_doppler_velocity': ('pyart_BuDRd18', -nyquist, nyquist),
    'spectral_width': ('pyart_NWS_SPW', 0, nyquist),
    'snr': ('pyart_Carbone17', -20, 30),
    'linear_depolarization_ratio': ('pyart_SCook18', -40, 0),
}

for field, (cmap, vmin, vmax) in fields_to_plot.items():

    print("Printing:", field)
    plt.figure()
    display = pyart.graph.RadarDisplay(radar)
    display.plot_rhi(field, cmap=cmap, vmin=vmin, vmax=vmax)
    plt.savefig('images/WSACR_' + field + '.png')
