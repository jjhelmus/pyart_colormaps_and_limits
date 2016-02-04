from __future__ import print_function
import matplotlib.pyplot as plt
import pyart
import numpy as np

radar = pyart.io.read('XSW110520105408.RAW7HHF')
nyquist = radar.instrument_parameters['nyquist_velocity']['data'][0]

fields_to_plot = {
    'reflectivity': ('pyart_NWSRef', -30, 75),
    'corrected_reflectivity': ('pyart_NWSRef', -30, 75),
    'total_power': ('pyart_NWSRef', -30, 75),
    'velocity': ('pyart_BuDRd18', -nyquist, nyquist),
    'spectrum_width': ('pyart_NWS_SPW', 0, nyquist),
    'normalized_coherent_power': ('pyart_Carbone17', 0.0, 1.0),
    'differential_reflectivity': ('pyart_RefDiff', 0, 8),
    'corrected_differential_reflectivity': ('pyart_RefDiff', 0, 8),
    'cross_correlation_ratio': ('pyart_RefDiff', 0.5, 1.05),
    'differential_phase': ('pyart_Wild25', -180, 180),
    'specific_differential_phase': ('pyart_Theodore16', -2, 5),
    'radar_echo_classification': ('pyart_LangRainbow12', 0, 11),
}

for field, (cmap, vmin, vmax) in fields_to_plot.items():

    print("Printing:", field)
    plt.figure()
    display = pyart.graph.RadarDisplay(radar)
    display.plot_ppi(field, cmap=cmap, vmin=vmin, vmax=vmax)
    plt.savefig('images/XSAPR_' + field + '.png')
