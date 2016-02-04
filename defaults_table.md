| Field                                 | Default colormap          | vmin        | vmax          | Notes                     | Example   |
| :------------------------------------ | :-----------------:       | :-------:   | :-------:     | :-----------------------  | :-------- |
|                                       |                           |             |               |                           |           |
| reflectivity                          |   pyart_NWSRef            |   -30       |   75          | NEXRAD limits             | Yes       |
| corrected_reflectivity                |   pyart_NWSRef            |   -30       |   75          | NEXRAD limits             | Yes       |
| total_power                           |   pyart_NWSRef            |   -30       |   75          | NEXRAD limits             | Yes       |
| signal_to_noise_ratio                 |   pyart_Carbone17         |   -20       |   30          |                           | Yes       |
|                                       |                           |             |               |                           |           |
| velocity                              |   pyart_NWSVel            |   -nyq      |   nyq         | +/- Nyquist velocity      | Yes       |
| corrected_velocity                    |   pyart_NWSVel            |   -nyq      |   nyq         | +/- Nyquist velocity      | No        |
| eastward_wind_component               |   pyart_NWSVel            |   -nyq      |   nyq         | +/- Nyquist velocity      | No        |
| northward_wind_component              |   pyart_NWSVel            |   -nyq      |   nyq         | +/- Nyquist velocity      | No        |
| vertical_wind_component               |   pyart_NWSVel            |   -nyq      |   nyq         | +/- Nyquist velocity      | No        |
|                                       |                           |             |               |                           |           |
| spectrum_width                        |   pyart_NWS_SPW           |   0         |   nyq         |                           | Yes       |
|                                       |                           |             |               |                           |           |
| normalized_coherent_power             |   pyart_Carbone17         |   0.0       |   1.0         |                           | Yes       |
|                                       |                           |             |               |                           |           |
| differential_reflectivity             |   pyart_RefDiff           |   0         |   8           |                           | Yes       |
| corrected_differential_reflectivity   |   pyart_RefDiff           |   0         |   8           |                           | Yes       |
|                                       |                           |             |               |                           |           |
| cross_correlation_ratio               |   pyart_RefDiff           |   0.5       |   1.05        |                           | Yes       |
|                                       |                           |             |               |                           |           |
| differential_phase                    |   pyart_Wild25            |   -180      |   180         |                           | Yes       |
| unfolded_differential_phase           |   pyart_Wild25            |   -360      |   -360        |                           | No        |
| corrected_differential_phase          |   pyart_Wild25            |   -360      |   -360        |                           | No        |
|                                       |                           |             |               |                           |           |
| specific_differential_phase           |   pyart_Theodore16        |   -2        |   5           |                           | Yes       |
| corrected_specific_differential_phase |   pyart_Theodore16        |   -2        |   5           |                           | No        |
|                                       |                           |             |               |                           |           |
| linear_depolarization_ratio           |   pyart_SCook18           |   -40       |   0           |                           | Yes       |
| linear_depolarization_ratio_h         |   pyart_SCook18           |   -40       |   0           |                           | No        |
| linear_depolarization_ratio_v         |   pyart_SCook18           |   -40       |   0           |                           | No        |
|                                       |                           |             |               |                           |           |
| rain_rate                             |   pyart_RRate11           |   0         |   150         | 150 mm -> 5.9 inches      | No        |
| radar_estimated_rain_rate             |   pyart_RRate11           |   0         |   150         | 150 mm -> 5.9 inches      | No        |
|                                       |                           |             |               |                           |           |
| radar_echo_classification             |   pyart_LangRainbow12     |   0         |   11          |                           | Yes       |
|                                       |                           |             |               |                           |           |
| specific_attenuation                  | pyart_Carbone17           | 0           | 10            |                           | No        |
|                                       |                           |             |               |                           |           |
| differential_phase_texture            | pyart_BlueBrown11         | 0           | 180           |                           | No        |
|                                       |                           |             |               |                           |           |
| height                                | pyart_SCook18             | 0           | 20000         | 20 km                     | No        |
| interpolated_profile                  | pyart_SCook18             | 0           | 10000         | 10 km                     | No        |

The reflectivity colormap and limits will also be used for the following fields:

* CZ
* DZ
* AZ
* Z
* DBZ
* DBZH
* DBZ_S
* DBZ_K
* reflectivity_horizontal
* corr_reflectivity
