## Double-slit experiment example data

Mock data for the session 2 workshop exercise: building a `pynxtools` reader that produces a file compliant with the [`NXdouble_slit`](https://fairmat-nfdi.github.io/pynxtools/reference/application-definitions.html){:target="_blank" rel="noopener"} application definition.

### Files

| File | Description |
|---|---|
| `mock_data.h5` | Simulated 2D interference pattern from a double-slit experiment |
| `eln_data.yaml` | Electronic lab notebook metadata (title, timestamps, source type, slit material) |
| `config_file.json` | Mapping from data sources to `NXdouble_slit` template paths |
| `create_mock_data.py` | Script that regenerates `mock_data.h5` |

### HDF5 structure (`mock_data.h5`)

```
data/
  detector_data          (200, 100) int32    raw counts (Poisson noise)
  x_pixels               (200,)     int32    pixel indices 0..199
  y_pixels               (100,)     int32    pixel indices 0..99
  interference_data      (200, 100) float32  normalized interference intensity
  x_offset               (200,)     float32  horizontal offset from centre (mm)
  y_offset               (100,)     float32  vertical offset from centre (mm)
metadata/instrument/
  source/wavelength               float64   532.0    nm
  source/coherence_length         float64    10.0    mm
  double_slit/x_gap               float64     0.1    mm
  double_slit/slit_separation     float64     0.5    mm
  detector/distance               float64  1000.0    mm
```

Run `python create_mock_data.py` from this directory to regenerate `mock_data.h5`.
