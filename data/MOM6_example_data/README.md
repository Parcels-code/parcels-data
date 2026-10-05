# MOM6_example_data

A small subset of MOM6 ocean model output, used to test and demonstrate
`parcels.convert.mom6_to_sgrid()`.

## Files

| File | Contents | Dimensions |
|---|---|---|
| `mom6_ssu.nc` | Surface zonal velocity `ssu` (m s-1), on U points | `time` = 5, `yh` = 40, `xq` = 41 |
| `mom6_ssv.nc` | Surface meridional velocity `ssv` (m s-1), on V points | `time` = 5, `yq` = 41, `xh` = 40 |
| `mom6_static.nc` | Grid: `geolon_c`, `geolat_c` (corners), `geolon`, `geolat` (centres), `wet` (land/sea mask) | `yh`, `xh` = 40; `yq`, `xq` = 41 |

## Source

- Model: MOM6-COBALT-NEP10k v1.0, Northeast Pacific regional configuration (~10 km),
  Changing Ecosystems and Fisheries Initiative (CEFI), NOAA.
- Experiment: hindcast, release `r20241015`, daily output, 1993–2019.
- Distributed through the NOAA PSL CEFI portal: https://psl.noaa.gov/cefi_portal/
- Velocities are the raw (unrotated) model output, i.e. along the grid's own i/j directions.

## Subset

- Time: first 5 daily records of 1993.
- Space: a 40 x 40 open-ocean box, model indices `xh` 211–250 and `yh` 318–357
  (corners `xq` 211–251 and `yq` 318–358), 0-based.
- The box contains no land cells and no missing corner coordinates.
- The output uses MOM6's symmetric layout: each axis has one more corner point than cell
  centres (`len(xq) == len(xh) + 1`).

Created with NCO:

```bash
I0=211; I1=250; J0=318; J1=357
ncks -O -4 -L 4 -d time,0,4 -d yh,$J0,$J1 -d xq,$I0,$((I1+1)) -v ssu \
     ssu.nep.full.hcast.daily.raw.r20241015.199301-201912.nc mom6_ssu.nc
ncks -O -4 -L 4 -d time,0,4 -d yq,$J0,$((J1+1)) -d xh,$I0,$I1 -v ssv \
     ssv.nep.full.hcast.daily.raw.r20241015.199301-201912.nc mom6_ssv.nc
ncks -O -4 -L 4 -d yh,$J0,$J1 -d xh,$I0,$I1 -d yq,$J0,$((J1+1)) -d xq,$I0,$((I1+1)) \
     -v geolon_c,geolat_c,geolon,geolat,wet ocean_static.nc mom6_static.nc
```

## Citation

If you use these data, please cite the model description paper:

> Drenkard, E. J., Stock, C. A., Ross, A. C., Teng, Y.-C., Cordero, T., Cheng, W., Adcroft, A.,
> Curchitser, E., Dussin, R., Hallberg, R., Hauri, C., Hedstrom, K., Hermann, A., Jacox, M. G.,
> Kearney, K. A., Pagès, R., Pilcher, D. J., Pozo Buil, M., Seelanki, V., and Zadeh, N. (2025).
> A regional physical–biogeochemical ocean model for marine resource applications in the
> Northeast Pacific (MOM6-COBALT-NEP10k v1.0). *Geoscientific Model Development*, 18, 5245–5290.
> https://doi.org/10.5194/gmd-18-5245-2025

and the model output archive:

> Drenkard, E., Stock, C. A., Ross, A. C., Teng, Y.-C., Cordero, T., Cheng, W., Adcroft, A.,
> Curchitser, E., Dussin, R., Hallberg, R., Hauri, C., Hedstrom, K., Hermann, A., Jacox, M. G.,
> Kearney, K. A., Pages, R., Pilcher, D. J., Pozo Buil, M., Seelanki, V., & Zadeh, N. (2024).
> Model output and analysis codes for initial submission of "A regional physical-biogeochemical
> ocean model for marine resource applications in the Northeast Pacific (MOM6-COBALT-NEP10k v1.0)"
> to GMD [Dataset]. Zenodo. https://doi.org/10.5281/zenodo.13936240

Subset prepared by Leilane Passos (Oregon State University).
