from glob import glob

import numpy as np
import xarray as xr

files = glob("aifs-single_*subset.nc")

for f in files:
    ds_tmp = xr.open_dataset(f, engine="netcdf4").load()
    filetime = f.replace("aifs-single_", "").replace("_subset.nc", "").replace("_", "-")
    filetime = " ".join(filetime.rsplit("-", 1))
    time = np.datetime64(f"{filetime}:00:00")

    ds_tmp = ds_tmp.assign_coords(time=[time])
    ds_tmp.to_netcdf(f, mode="w", format="NETCDF4")

ds_all = xr.open_mfdataset(files, data_vars="minimal", coords="minimal", compat="override",)
print(ds_all)