import os
import xarray as xr
import numpy as np
from aqua_fetch import CAMELS_DE
from hydrodataset import HydroDataset
from tqdm import tqdm
from hydroutils import hydro_file


class CamelsDe(HydroDataset):
    """CAMELS-DE dataset class extending RainfallRunoff.

    This class provides access to the CAMELS-DE dataset, which contains hourly
    hydrological and meteorological data for various watersheds.
    """

    def __init__(self, data_path, region=None, download=False, cache_path=None):
        """Initialize CAMELS-DE dataset."""
        super().__init__(data_path, cache_path=cache_path)
        self.region = region
        self.download = download
        try:
            self.aqua_fetch = CAMELS_DE(data_path)
        except Exception:
            check_zip_extract = False
            zip_files = ["camels_de.zip"]
            for filename in tqdm(zip_files, desc="Checking zip files"):
                extracted_dir = self.data_source_dir.joinpath(
                    "CAMELS_DE", filename[:-4]
                )
                if not extracted_dir.exists():
                    check_zip_extract = True
                    break
            if check_zip_extract:
                hydro_file.zip_extract(self.data_source_dir.joinpath("CAMELS_DE"))
            self.aqua_fetch = CAMELS_DE(data_path)

    @property
    def _attributes_cache_filename(self):
        return "camels_de_attributes.nc"

    @property
    def _timeseries_cache_filename(self):
        return "camels_de_timeseries.nc"

    @property
    def default_t_range(self):
        return ["1951-01-01", "2020-12-31"]





    def _get_attribute_units(self):
        return {
            # 地形特征
            "dis_m3_": "m^3/s",
            "run_mm_": "millimeter",
            "inu_pc_": "percent",
            "lka_pc_": "1e-1 * percent",
            "lkv_mc_": "1e6 * m^3",
            "rev_mc_": "1e6 * m^3",
            "dor_pc_": "percent (x10)",
            "ria_ha_": "hectares",
            "riv_tc_": "1e3 * m^3",
            "gwt_cm_": "centimeter",
            "ele_mt_": "meter",
            "slp_dg_": "1e-1 * degree",
            "sgr_dk_": "decimeter/km",
            "clz_cl_": "dimensionless",
            "cls_cl_": "dimensionless",
            "tmp_dc_": "degree_Celsius",
            "pre_mm_": "millimeters",
            "pet_mm_": "millimeters",
            "aet_mm_": "millimeters",
            "ari_ix_": "1e-2",
            "cmi_ix_": "1e-2",
            "snw_pc_": "percent",
            "glc_cl_": "dimensionless",
            "glc_pc_": "percent",
            "pnv_cl_": "dimensionless",
            "pnv_pc_": "percent",
            "wet_cl_": "dimensionless",
            "wet_pc_": "percent",
            "for_pc_": "percent",
            "crp_pc_": "percent",
            "pst_pc_": "percent",
            "ire_pc_": "percent",
            "gla_pc_": "percent",
            "prm_pc_": "percent",
            "pac_pc_": "percent",
            "tbi_cl_": "dimensionless",
            "tec_cl_": "dimensionless",
            "fmh_cl_": "dimensionless",
            "fec_cl_": "dimensionless",
            "cly_pc_": "percent",
            "slt_pc_": "percent",
            "snd_pc_": "percent",
            "soc_th_": "tonne/hectare",
            "swc_pc_": "percent",
            "lit_cl_": "dimensionless",
            "kar_pc_": "percent",
            "ero_kh_": "kg/hectare/year",
            "pop_ct_": "1e3",
            "ppd_pk_": "1/km^2",
            "urb_pc_": "percent",
            "nli_ix_": "1e-2",
            "rdd_mk_": "meter/km^2",
            "hft_ix_": "1e-1",
            "gad_id_": "dimensionless",
            "gdp_ud_": "dimensionless",
            "hdi_ix_": "1e-3",
        }

    def _get_timeseries_units(self):
        return [
            "m^3/s",  # q_cms_obs
            "mm/day",  # q_mm_obs
            "m",  # water_level
            "mm/day",  # pcp_mm_mean
            "mm/day",  # pcp_mm_min
            "mm/day",  # pcp_mm_median
            "mm/day",  # pcp_mm_max
            "mm/day",  # pcp_mm_std
            "%",  # rh_%
            "%",  # rh_%_min
            "%",  # rh_%_med
            "%",  # rh_%_max
            "%",  # rh_%_std
            "Wm^2",  # solrad_wm2_mean
            "Wm^2",  # solrad_wm2_min
            "Wm^2",  # solrad_wm2_med
            "Wm^2",  # solrad_wm2_max
            "Wm^2",  # solrad_wm2_std
            "°C",  # airtemp_C_mean
            "°C",  # airtemp_C_min
            "°C",  # airtemp_C_max
        ]