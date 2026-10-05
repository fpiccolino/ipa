# IPA – InSAR Product Analysis

**IPA (InSAR Product Analysis)** is an open-source QGIS plugin designed for the comprehensive evaluation, processing, and interpretation of Synthetic Aperture Radar Interferometry (InSAR) and Multi-Temporal InSAR (MTInSAR) products.

The plugin provides a unified, tabbed graphical interface enabling preliminary feasibility assessments over a digital elevation model (DEM), reliability estimation of single differential interferograms, and advanced spatial/temporal statistical analysis of MTInSAR displacement time series.

---

## Key Features

The plugin is structured into three main operational modules:

### 1. InSAR Feasibility Analysis (Predictive / DEM-based)
- **Satellite Orbit Setup**: Configuration of pass mode (Ascending/Descending) and geometry with built-in nominal orbital presets (Sentinel-1, COSMO-SkyMed/CSG, TerraSAR-X, ALOS-1/2, SAOCOM, ENVISAT, ERS-1/2) or manual parameter entry.
- **Geometric Distortion Index (GDI)**: Evaluation of local terrain slope/aspect relative to the radar Line-Of-Sight (LOS) to detect foreshortening and visibility issues (-1 to 1 continuous scale).
- **Layover/Shadow Mask**: Directional radial ray-tracing algorithm generating categorical visibility maps (Good, Shadow, Layover).
- **Slope2LOS Projection Factor**: Dimensionless factor projecting downslope unit vectors onto the radar LOS, with user-definable slope thresholding to filter flat terrain.

### 2. InSAR Product Analysis (Post-processing on Interferograms)
- **InSAR Sensitivity Map (ISM)**: Generates a normalized spatial sensitivity layer (0 to 1) combining geometric visibility (Slope2LOS) with local InSAR coherence.
- **Sigmoid Coherence Weighting**: Optional sigmoid weighting function (calibrated via *Steepness* and *Midpoint* parameters) to suppress phase noise in vegetated/low-coherence areas while highlighting coherent targets.

### 3. MTInSAR Product Analysis (Vector Points / PS-DS Processing)
- **GDI on Point Catalogues**: Samples DEM slope/aspect and calculates GDI directly for each coherent target.
- **Slope Velocity Conversion (V_SLOPE)**: Projects mean LOS displacement velocities into downslope directions using a single-cycle attribute write provider.
- **Spatial Distribution Analysis**: Evaluates point target clustering and spatial density using the Clark–Evans Nearest-Neighbor Index ($R$, $Z$-score, percentage of area coverage $PCT$, and void detection flags).
- **Temporal Trend Analysis**: Automated nonlinear kinematic model selection (linear, quadratic acceleration, cubic, quartic, unclassified) driven by Fuzzy Entropy ($FE_1$–$FE_5$), Fisher statistics ($F, FA$), $R^2$, and Akaike Information Criterion ($AIC$).
- **Interactive Time-Series Visualization**: Canvas map-tool allowing on-the-fly chart inspection of measured time series and fitted polynomial curves directly by clicking on map targets.

---

## Technical Architecture & Usability

- **Non-Blocking Background Threads**: Computationally intensive tasks (ray tracing, statistical regressions, large array operations) run asynchronously to keep QGIS fully responsive.
- **Smart Form Filtering**: Dropdown selections automatically filter layers according to input requirements (rasters for DEM/coherence; point vectors for MTInSAR).
- **Automatic Styling**: Results are added directly to the QGIS map canvas and styled with dedicated grayscale, color ramp, or categorical symbologies.

---

## System Requirements

| Component | Minimum Version | Notes |
| :--- | :--- | :--- |
| **QGIS** | 3.34.4 – Prizren | Host GIS Platform (Python 3.x API) |
| **Python** | 3.9.5 | Bundled with standard QGIS distributions |
| **GDAL** | 3.3 | Spatial raster and vector data provider |
| **NumPy** | 1.20 | Vectorized multi-dimensional array operations |
| **SciPy** | 1.6 | Numerical routines & nonlinear curve fitting |

> *Note: NumPy and SciPy are pre-installed in standard standalone and OSGeo4W QGIS distributions. No additional manual Python setup is needed.*

---

## Installation

### Method 1: QGIS Official Plugin Repository (Recommended)
1. Open QGIS and go to **Plugins** > **Manage and Install Plugins...**
2. In the **Settings** tab, make sure **"Show also experimental plugins"** is checked.
3. In the **All** tab, search for **IPA – InSAR Product Analysis**.
4. Click **Install Plugin**.

### Method 2: Install from ZIP
1. Download or clone this repository as a `.zip` archive.
2. In QGIS, navigate to **Plugins** > **Manage and Install Plugins...** > **Install from ZIP**.
3. Select the `ipa.zip` file and click **Install Plugin**.

---

## Authors & Maintainers

- **Fabio Bovenga** – *Conceptualization, methodology, mathematical formulations, testing* (CNR-IREA).
- **Fabio Piccolino** – *Software development, Python/PyQGIS implementation, maintenance* (Politecnico di Bari).

---

## Contributions & Acknowledgments

The development of the IPA QGIS plugin was supported in part by:
- **Regione Puglia (Italy)** under project *"Utilizzo di intelligenza artificiale e dati satellitari per il monitoraggio dell'instabilità del territorio"*, POC PUGLIA FESR-FSE 2014/2020 – Programma Regionale RIPARTI (Grant agreement `01975b92`).
- **European Union – Next Generation EU**, Mission 4, Component 2, CUP `H53D23001660006` (PRIN22 Project *"MIRAGE: Mass movement Investigation and prediction through geomorphology, Remote sensing and Artificial intelligence"*).

---

## Scientific References

If you use IPA in your research, please cite:

- Bovenga, F., Pasquariello, G., & Refice, A. (2021). *Statistically-Based Trend Analysis of MTInSAR Displacement Time Series*. Remote Sensing, 13(12), 2302. https://doi.org/10.3390/rs13122302
- Bovenga, F., & Piccolino, F. (2025). *InSAR Product Analysis (IPA): a QGIS tool for slope instability assessment based on SAR interferometry*. EGU General Assembly 2025, Vienna, Austria, EGU25-17224. https://doi.org/10.5194/egusphere-egu25-17224
- Bovenga, F., Argentiero, I., & Piccolino, F. (2026). *Methodologies and functionalities for a QGIS-based analysis of DInSAR/MTInSAR products*. 13th International Workshop on Advances in the Science and Applications of SAR Interferometry (FRINGE 2026), Krakow, Poland.

---

## License

This plugin is free software licensed under the **GNU General Public License v3.0 (GPLv3)**. See the [LICENSE](LICENSE) file for more details. Documentation content is licensed under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).
