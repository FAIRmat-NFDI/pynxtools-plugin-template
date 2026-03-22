# Copyright The NOMAD Authors.
#
# This file is part of NOMAD. See https://nomad-lab.eu for further info.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Create mock HDF5 data for the double-slit experiment reader exercise."""

import numpy as np
import h5py

# ── Physical parameters ───────────────────────────────────────────────────────
WAVELENGTH_NM = 532.0           # nm  (green laser)
WAVELENGTH_MM = WAVELENGTH_NM * 1e-6  # convert nm → mm for pattern formula
SLIT_SEPARATION_MM = 0.5        # mm  centre-to-centre distance between the two slits
X_GAP_MM = 0.1                  # mm  width of each individual slit
DETECTOR_DISTANCE_MM = 1000.0   # mm  (1 m from slit plane to detector surface)
COHERENCE_LENGTH_MM = 10.0      # mm  temporal coherence length of the source

# ── Detector grid ─────────────────────────────────────────────────────────────
N_X, N_Y = 200, 100             # pixels along horizontal and vertical axes
PIXEL_SIZE_MM = 0.05            # mm per pixel

x_pixels = np.arange(N_X, dtype=np.int32)
y_pixels = np.arange(N_Y, dtype=np.int32)

# Physical spatial offset from the detector centre (mm)
x_offset = ((x_pixels - N_X // 2) * PIXEL_SIZE_MM).astype(np.float32)
y_offset = ((y_pixels - N_Y // 2) * PIXEL_SIZE_MM).astype(np.float32)

# ── Double-slit interference pattern ─────────────────────────────────────────
# I(x) = sinc²(π·a·x / λ·L) · cos²(π·d·x / λ·L)
# where a = slit width, d = slit separation, λ = wavelength, L = distance.
# np.sinc(u) = sin(π·u) / (π·u), so sinc_arg is divided by π already.
X, _ = np.meshgrid(x_offset, y_offset, indexing="ij")  # shape (N_X, N_Y)

sinc_arg = X_GAP_MM * X / (WAVELENGTH_MM * DETECTOR_DISTANCE_MM)
envelope = np.sinc(sinc_arg) ** 2

cos_arg = np.pi * SLIT_SEPARATION_MM * X / (WAVELENGTH_MM * DETECTOR_DISTANCE_MM)
fringe = np.cos(cos_arg) ** 2

intensity = (envelope * fringe).astype(np.float32)  # normalised to [0, 1]

# Raw detector data: Poisson noise around ~2000 peak counts
rng = np.random.default_rng(42)
detector_data = rng.poisson(2000.0 * intensity + 5).astype(np.int32)

# ── HDF5 structure ────────────────────────────────────────────────────────────
data_structure = {
    "data": {
        "detector_data": detector_data,    # (N_X, N_Y) int32  – raw pixel counts
        "x_pixels": x_pixels,             # (N_X,)     int32  – 0-based pixel indices
        "y_pixels": y_pixels,             # (N_Y,)     int32  – 0-based pixel indices
        "interference_data": intensity,   # (N_X, N_Y) float32 – normalised intensity
        "x_offset": x_offset,            # (N_X,)     float32 – mm from centre
        "y_offset": y_offset,            # (N_Y,)     float32 – mm from centre
    },
    "metadata": {
        "instrument": {
            "source": {
                "wavelength": WAVELENGTH_NM,            # nm
                "coherence_length": COHERENCE_LENGTH_MM, # mm
            },
            "double_slit": {
                "x_gap": X_GAP_MM,                      # mm
                "slit_separation": SLIT_SEPARATION_MM,  # mm
            },
            "detector": {
                "distance": DETECTOR_DISTANCE_MM,       # mm
            },
        },
    },
}


def create_hdf5_group(group, structure):
    """Recursively populate an HDF5 group from a nested dict."""
    for key, value in structure.items():
        if isinstance(value, dict):
            create_hdf5_group(group.create_group(key), value)
        else:
            group.create_dataset(key, data=value)


with h5py.File("mock_data.h5", "w") as hdf:
    create_hdf5_group(hdf, data_structure)

print("Created mock_data.h5")
print(f"  data/detector_data:      {detector_data.shape} {detector_data.dtype}")
print(f"  data/interference_data:  {intensity.shape} {intensity.dtype}")
print(f"  data/x_pixels:           {x_pixels.shape}")
print(f"  data/y_pixels:           {y_pixels.shape}")
