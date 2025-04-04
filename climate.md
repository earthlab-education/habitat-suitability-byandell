---
jupyter: python3
title: Habitat suitability under climate change
toc-title: Table of contents
---

Left to do:

-   Expand out all datasets for comparison.
    -   Code is in place.
-   Harmonize all datasets and build fuzzy logic.
    -   `reproject` code in place.
    -   see [notes on
        skfuzzy](https://github.com/byandell-envsys/landmapy/blob/main/notes.qmd#fuzzy-logic-model-27-feb-2025)
-   Spruce up graphics, possibly using
    -   slider widget (see code below in [Climate model
        data](#climate-model-data) section)
    -   matplotlib with multiple subplots (see [6 Mar
        notes](https://github.com/byandell-envsys/landmapy/blob/main/notes.qmd#notes-6-mar-2025))

Python code setup:

::: {.cell execution_count="1"}
``` {.python .cell-code}
pip install --quiet git+https://github.com/byandell-envsys/landmapy.git
```
:::

::: {.cell execution_count="2"}
``` {.python .cell-code}
import pandas as pd
import geopandas as gpd # read geojson file into gdf
import matplotlib.pyplot as plt # Overlay raster and vector data
import xarray as xr

from landmapy.initial import create_data_dir # create (or retrieve) data directory
from landmapy.plot import plot_gdf_state # plot gdf with state overlay
from landmapy.plot import plot_gdf_da # plot GDF over DA
from landmapy.plot import plot_das # plot DAs in rows
from landmapy.process import da_combine
from landmapy.polaris import merge_soil # merge soil data from GDF
from landmapy.srtm import srtm_download, srtm_slope # process SRTM data
from landmapy.thredds import process_maca, maca_year # process MACA THREDDS
from landmapy.explore import ramp_logic # ramp for fuzzy logic
```
:::

## INTRODUCTION

Our changing climate is changing where key grassland species can live,
and grassland management and restoration practices will need to take
this into account ([Kane et
al. 2017](https://www.frontiersin.org/articles/10.3389/fpls.2017.00730/full)).

In this coding challenge, create a habitat suitability model for a
species of your choice that lives in the continental United States
(CONUS). We have this limitation because the downscaled climate data we
suggest, the [MACAv2 dataset](https://www.climatologylab.org/maca.html),
is only available in CONUS. If you find other downscaled climate data at
an appropriate resolution you are welcome to choose a different study
area. If you don't have anything in mind, you can take a look at
*Sorghastrum nutans*, a grass native to North America. In the past 50
years, its range has moved northward ([GBIF *S.
nutans*](https://www.gbif.org/species/2704414)).

Your suitability assessment will be based on combining multiple data
layers related to soil, topography, and climate. You will also need to
create a **modular, reproducible, workflow** using functions and loops.
To do this effectively, we recommend planning your code out in advance
using a technique such as pseudocode outline or a flow diagram. We
recommend planning each of the blocks below out into multiple steps. It
is unnecessary to write a step for every line of code unles you find
that useful. As a rule of thumb, aim for 2-5 line code chuck for major
structure steps.

### References

-   [Spring 3. Habitat Suitabilty under Climate
    Change](https://cu-esiil-edu.github.io/esiil-learning-portal/foundations/notebooks/13-habitat-climate-change/climate.html)
    (updated project)
-   [Fall 5. Habitat Suitability Coding
    Challenge](https://cu-esiil-edu.github.io/esiil-learning-portal/foundations/notebooks/08-habitat/habitat.html)
    (original project with code hints)
-   [Notes](notes.qmd) (notes from class discussions)
-   [Yandell Fall
    Project](https://github.com/byandell-envsys/habitatSuitability)
    -   [buffalo.md](https://github.com/byandell-envsys/habitatSuitability/blob/main/buffalo.md)
        (rendered Markdown)
    -   [buffalo.qmd](https://github.com/byandell-envsys/habitatSuitability/blob/main/buffalo.qmd)
        (Quarto source)
    -   [landmapy](https://github.com/byandell-envsys/landmapy) (Python
        package)

## STEP 1: STUDY OVERVIEW

Before you begin coding, you will need to design your study.

**Reflect and Respond:** What question do you hope to answer about
potential future changes in habitat suitability?

YOUR QUESTION HERE

### Species

Select the species you want to study, and research it's habitat
parameters in scientific studies or other reliable sources. You will
want to look for reviews or overviews of the data, since an individual
study may not have the breadth needed for this purpose. In the US, the
National Resource Conservation Service can have helpful fact sheets
about different species. University Extension programs are also good
resources for summaries.

Based on your research, select soil, topographic, and climate variables
that you can use to determine if a particular location and time period
is a suitable habitat for your species.

**Reflect and Respond:** Write a description of your species. What
habitat is it found in? What is its geographic range? What, if any, are
conservation threats to the species? What data will shed the most light
on habitat suitability for this species?

YOUR SPECIES DESCRIPTION HERE

#### Blue Stem Description

Big bluestem is a warm-season grass native to the eastern two thirds of
the United States from the mid-western short grass prairies to the
coastal plain. It grows to 6 to 8 feet with short and scaly rhizomes and
leaves that vary from light yellow-green to burgundy. The seed head is
coarse and not fluffy, typically with three spikelets looking like a
turkey foot.

Below are two pictures of me and my (leashed) dog, Kylie, on a walk in
[Prairie Moraine County Park (Dane Co,
WI)](https://parks-lwrd.danecounty.gov/park/PrairieMoraine) surrounded
by bluestem. We were walking on the [Ice Age National Scenic Trail
Corridor](https://parks-lwrd.danecounty.gov/documents/PDFs/Maps/PrairieMoraine-OverviewWeb.pdf)
just north of the dog part. The [Ice Age
Trail](https://www.iceagetrail.org/) is a 1000-mile system that
comprises a unique boundary separating the glaciated and "driftless"
regions across the state of Wisconsin. Bluestem is found along much of
this trail system.

<p float="center">
`<img src="images/bluestemdog.png" width="350" />`{=html}
`<img src="images/bluestemfield.png" width="350" />`{=html}
</p>

Bluestem can tolerate a wide variety of well-drained soils and typically
does well on low fertility sites. Big blue is commonly used in erosion
control plantings. While it may be slow to get started, it eventually
provides excellent stability for sandy areas. It is also a good native
choice for grazing forage and provides excellent wildlife habitat.
Bobwhite quail and other ground-nesting birds use this clump-forming
grass for nesting and forage cover. In the longleaf pine ecosystem, the
perennial big bluestem contributes to the fine flashy fuel needed for
the maintenance of the ecosystem.

Bluestem can be used in the restoration of native vegetation in
agricultural or pasture areas. It is adapted to conventional tillage or
native seed no-till drill. Seeding rate for big bluestem ranges from 4
to 12 pounds per acre, lower for wildlife (quail) habitat establishment.
Local ecotypes are best when restoring native vegetation areas.

Bluestem grasses have root systems that reach significant depths. In
Buffalo Gap National Grassland, these grasses typically develop roots
that extend up to 5 feet deep. This deep root system helps them access
water and nutrients from deeper soil layers, making them resilient in
the semi-arid conditions of the grassland.

Blue Stem, according to [Greg](https://greg.app/), "need well-drained,
nutrient-rich soils. The best soil types for this grass are sandy loam
or loamy soil, which provide the right balance of drainage and
nutrients. Aim for an organic matter content of 5-10%. This range is
crucial for optimal growth, as it enhances soil fertility and structure.
The ideal pH range for Big Bluestem is between 6.0 and 7.0. This
slightly acidic to neutral pH is essential for nutrient availability,
ensuring your plants can absorb what they need to thrive."

[Gardners.com](https://www.gardeners.com/how-to/what-type-of-soil-do-you-have/9120.html)
has a [soil simplex
figure](https://www.gardeners.com/globalassets/articles/gardening/2014content/9120-soil-texture-triangle-sample.png),
which puts sandy loam and loamy sand at 50-85% sand.

![](https://www.gardeners.com/globalassets/articles/gardening/2014content/9120-soil-texture-triangle-sample.png){fig-align="center"}

According to the USDA Natural Resources Convervations Service: Plant
Guide: [Little
Bluestem](https://plants.usda.gov/DocumentLibrary/plantguide/pdf/pg_scsc.pdf)
"is a tallgrass prairie increaser and mixed prairie decreaser. Little
bluestem typically occurs on dry upland sites, especially on ridges,
hilltops, and steep slopes. It also occurs on limey sub-irrigated sites
and in prairie fens. It is found in areas receiving 10 to 60 inches of
mean annual precipitation and plant hardiness zones 3 to 9." [Plant
profile page](https://plants.usda.gov/plant-profile/SCHIZ4).

[Big
Bluestem](https://www.nrcs.usda.gov/sites/default/files/2022-09/BigBluestem.pdf)
"is climatically adapted throughout the Midwest and Northeast on
moderately well drained through excessively well drained soils. It is
adapted to a range of other soil limitations such as shallow depth, low
pH, and low fertility." [Plant profile
page](https://plants.usda.gov/plant-profile/ANGE).

While I could use [GBIF](https://www.gbif.org/) to find crowd-sourced
records, these two species are widely found across North America. For
more on using GBIF with Python, see

-   [GBIF Class
    Notes](https://github.com/earthlab-education/habitat-suitability-byandell/blob/main/notes.md#gbif-review-25-feb-2025)
    -   [notes.qmd](https://github.com/earthlab-education/habitat-suitability-byandell/blob/main/notes.qmd)
    -   [notes_gbif.qmd](https://github.com/earthlab-education/habitat-suitability-byandell/blob/main/notes_gbif.qmd)
-   [gbif.py](https://github.com/byandell-envsys/landmapy/blob/main/landmapy/gbif.py)
    module in [landmapy](https://github.com/byandell-envsys/landmapy)
    package
    -   [siberian_crane.qmd](https://github.com/earthlab-education/species-distribution-coding-challenge-byandell/blob/main/siberian_crane.qmd)
        (use of `gbif.py` module)

### Sites

Select at least two site to study, such as two of the U.S. National
Grasslands. You can download the [National Grassland
Units](https://data.fs.usda.gov/geodata/edw/edw_resources/shp/S_USA.NationalGrassland.zip)
and select your study sites. Generate a site map for each location.

When selecting your sites, you might want to look for places that are
marginally habitable for this species, since those locations will be
most likely to show changes due to climate.

**Reflect and Respond:** Write a site description for each of your
sites, or for all of your sites as a group if you have chosen a large
number of linked sites. What differences or trends do you expect to see
among your sites?

#### Buffalo Gap and Oglala National Grasslands

This project examines habitat suitability for [Blue
Stem](https://greg.app/big-bluestem-soil/) in the [Buffalo
Gap](https://www.fs.usda.gov/recarea/nebraska/recarea/?recid=30329) and
[Oglala](https://www.fs.usda.gov/recarea/nebraska/recarea/?recid=30328)
National Grasslands.

Resources:

-   [PAD-US](https://www.usgs.gov/programs/gap-analysis-project/science/pad-us-data-overview)
    -   [PADUS4_0_State_SD_GDB](https://www.sciencebase.gov/catalog/item/652d4f80d34e44db0e2ee45c#:~:text=PADUS4_0_State_SD_GDB)
        (834KB zip)
-   Duan K, Sun G, Sun S et al. (2016) Divergence of ecosystem services
    in U.S. National Forests and Grasslands under a changing climate.
    Sci Rep 6, 24441. [DOI:
    10.1038/srep24441](https://doi.org/10.1038/srep24441)
-   Brown RN, Percivalle C, Narkiewicz S, DeCuollo S (2010) Relative
    Rooting Depths of Native Grasses and Amenity Grasses with Potential
    for Use on Roadsides in New England. HortScience 45: 393-400. [DOI:
    10.21273/HORTSCI.45.3.393](https://doi.org/10.21273/HORTSCI.45.3.393)
-   [USFS National
    Grasslands](https://www.fs.usda.gov/managing-land/national-forests-grasslands/national-grasslands)
    -   [Units
        ZIPfile](https://data.fs.usda.gov/geodata/edw/edw_resources/shp/S_USA.NationalGrassland.zip)
    -   [USFS Maps](https://www.fs.usda.gov/visit/maps)
    -   [USFS ArcGIS Grassland
        Units](https://data-usfs.hub.arcgis.com/datasets/usfs::national-grassland-units-feature-layer/explore?location=41.300146%2C-107.829591%2C6.23)
        -   [USFS IVM Digital Map](https://www.fs.usda.gov/ivm/)
        -   [Download PDF or JPG
            Map](https://experience.arcgis.com/experience/9ab8d03e2bec4d7fbfc27ba836e70aed/page/Forest-Series/#data_s=id%3AdataSource_2-Forest_Series_Index_6205%3A1430)
        -   [ArcGIS Map
            Viewer](https://www.arcgis.com/home/webmap/viewer.html)
        -   Great resource for plant growth characteristics:
            <https://plants.usda.gov/>

These contiguous grasslands are located in [Oceti Sakowin
Oyate](https://americanindian.si.edu/nk360/plains-belonging-nation/oceti-sakowin),
also known as the Lakota Nation or Great Sioux Nation, and in the US
states of South Dakota and Nebraska. For more information see [Oceti
Sakowin Essential Understandings &
Standards](https://sdtribalrelations.sd.gov/docs/OSEUs-18.pdf).

Get grassland GeoDataFrames and focus on desired sites. Pseudocode:

``` python
data_dir = create_data_dir('habitat')
grassland_url = f"{data_dir}/National_Grassland_Units_(Feature_Layer).geojson"
grassland_gdf = gpd.read_file(grassland_url)
buffalo_gdf = grassland_gdf.loc[grassland_gdf['GRASSLANDNAME'].isin(
    ["Buffalo Gap National Grassland", "Oglala National Grassland"])]
plot_gdf_state(buffalo_gdf, aiannh=True)
```

Python code detail:

:::: {.cell execution_count="3"}
``` {.python .cell-code}
%store -r buffalo_gdf
try:
    buffalo_gdf
except NameError:
    data_dir = create_data_dir('habitat')
    # Read all grasslands GeoJSON into `grassland_gdf`.
    grassland_url = f"{data_dir}/National_Grassland_Units_(Feature_Layer).geojson"
    grassland_gdf = gpd.read_file(grassland_url)
    # Subset to desired locations.
    buffalo_gdf = grassland_gdf.loc[grassland_gdf['GRASSLANDNAME'].isin(
        ["Buffalo Gap National Grassland", "Oglala National Grassland"])]
    %store buffalo_gdf
    print("buffalo_gdf created and stored")
else:
    print("buffalo_gdf retrieved from StoreMagic")
```

::: {.cell-output .cell-output-stdout}
    buffalo_gdf retrieved from StoreMagic
:::
::::

Black line separates South Dakota from Nebraska; red line outlines part
of Pine Ridge Reservation.

:::: {.cell fig-title="Buffalo and Oglala Grasslands with Pine Ridge (red) and SD/NE (black)" execution_count="4"}
``` {.python .cell-code}
plot_gdf_state(buffalo_gdf, aiannh=True)
```

::: {.cell-output .cell-output-display}
![](climate_files/figure-markdown/fig-grasslands-output-1.png){#fig-grasslands}
:::
::::

### Time periods

In general when studying climate, we are interested in **climate
normals**, which are typically calculated from 30 years of data so that
they reflect the climate as a whole and not a single year which may be
anomalous. So if you are interested in the climate around 2050, download
at least data from 2035-2065.

**Reflect and Respond:** Select at least two 30-year time periods to
compare, such as historical and 30 years into the future. These time
periods should help you to answer your scientific question.

#### Selected time periods

-   `2006-2025`: recent 30 years
-   `2036-2065`: 2050 +/- 15 years

### Climate models

There is a great deal of uncertainty among the many global climate
models available. One way to work with the variety is by using an
**ensemble** of models to try to capture that uncertainty. This also
gives you an idea of the range of possible values you might expect! To
be most efficient with your time and computing resources, you can use a
subset of all the climate models available to you. However, for each
scenario, you should attempt to include models that are:

-   Warm and wet
-   Warm and dry
-   Cold and wet
-   Cold and dry

for each of your sites.

To figure out which climate models to use, you will need to access
summary data near your sites for each of the climate models. You can do
this using the [Climate Futures Toolbox Future Climate Scatter
tool](https://climatetoolbox.org/tool/Future-Climate-Scatter). There is
no need to write code to select your climate models, since this choice
is something that requires your judgement and only needs to be done
once.

<p float="center">
`<img src="images/FutureClimate_45.png" width="350" />`{=html}
`<img src="images/FutureClimate_85.png" width="350" />`{=html}
</p>

If your question requires it, you can also choose to include multiple
climate variables, such as temperature and precipitation, and/or
multiple emissions scenarios, such as RCP4.5 and RCP8.5.

Choose at least 4 climate models that cover the range of possible future
climate variability at your sites. How did you choose?

LIST THE CLIMATE MODELS YOU SELECTED HERE AND CITE THE CLIMATE TOOLBOX

## STEP 2: DATA ACCESS

### Soil data

The [POLARIS dataset](http://hydrology.cee.duke.edu/POLARIS/) is a
convenient way to uniformly access a variety of soil parameters such as
pH and percent clay in the US. It is available for a range of depths (in
cm) and split into 1x1 degree tiles.

Write a **function with a numpy-style docstring** that will download
POLARIS data for a particular location, soil parameter, and soil depth.
Your function should account for the situation where your site boundary
crosses over multiple tiles, and merge the necessary data together.

Then, use loops to download and organize the rasters you will need to
complete this section. Include soil parameters that will help you to
answer your scientific question. We recommend using a soil depth that
best corresponds with the rooting depth of your species.

Download soil raster layer for **sand** covering study area envelope
using the [POLARIS
dataset](http://hydrology.cee.duke.edu/POLARIS/PROPERTIES/v1.0/).
Considering `sand` percentage `mean`. POLARIS data are available at 6
depths, and Bluestem has roots down to 5 feet (150 cm), which is the
lowest strata measured (100-200 cm). Data in the [sand 100-200 cm
directory](http://hydrology.cee.duke.edu/POLARIS/PROPERTIES/v1.0/sand/mean/100_200/)
are saved as separate tif files by longitude. Buffalo Gap National
Grassland is at (centroid) 43.4375° N, 103.0505° W, while Oglala
National Grassland is at 42.9404° N, 103.5900° W. Below we use the
`.total_bounds` extension on `buffalo_gdf` with the `merge_soil()`
function in the
[landmapy.polaris](https://github.com/byandell-envsys/landmapy/blob/main/landmapy/polaris.py)
module to automate finding bounds.

#### Sand Soil Measure

Get and show `mean` of `sand` at depth `100-200m` with functions. Merge
soil tiles to create `buffalo_da` and plot. Pseudocode:

``` python
buffalo_da = merge_soil(buffalo_gdf, "sand", "mean", "100_200")`
plot_gdf_da(buffalo_gdf, buffalo_da)
```

Python code detail:

:::: {.cell execution_count="5"}
``` {.python .cell-code}
print(buffalo_gdf.total_bounds)
%store -r buffalo_da
try:
    buffalo_da
except NameError:
    buffalo_da = merge_soil(buffalo_gdf)
    print("buffalo_da merged soil from buffalo_gdf and stored")
else:
    print("buffalo_da soil merge retrieved")
```

::: {.cell-output .cell-output-stdout}
    [-104.05473027   42.74093601 -101.47233564   43.99459902]
    buffalo_da soil merge retrieved
:::
::::

:::: {.cell fig-title="Percent Sand in Soil overlaid by Grasslands" execution_count="6"}
``` {.python .cell-code}
buffalo_gdf['color'] = ['white','red']
plot_gdf_da(buffalo_gdf, buffalo_da, cmap='viridis')
```

::: {.cell-output .cell-output-display}
![](climate_files/figure-markdown/fig-soil-output-1.png){#fig-soil}
:::
::::

### Topographic data

One way to access reliable elevation data is from the [SRTM
dataset](https://www.earthdata.nasa.gov/data/instruments/srtm),
available through the [earthaccess
API](https://earthaccess.readthedocs.io/en/latest/quick-start/).

Write a **function with a numpy-style docstring** that will download
SRTM elevation data for a particular location and calculate any
additional topographic variables you need such as slope or aspect.

Then, use loops to download and organize the rasters you will need to
complete this section. Include topographic parameters that will help you
to answer your scientific question.

> **Warning**
>
> Be careful when computing the slope from elevation that the units of
> elevation match the projection units (e.g. meters and meters, not
> meters and degrees). You will need to project the SRTM data to
> complete this calculation correctly.

Pseudocode:

``` python
elevation_dir = create_data_dir('habitat/srtm')
srtm_da = srtm_download(buffalo_gdf, elevation_dir, 0.1)
slope_da = srtm_slope(srtm_da)
plot_das(da_combine(srtm_da, slope_da, contrast=False), gdf=buffalo_gdf)
```

Python code detail:

::: {.cell execution_count="7"}
``` {.python .cell-code}
project_dir = create_data_dir('habitat')
elevation_dir = create_data_dir('habitat/srtm')

srtm_da = srtm_download(buffalo_gdf, elevation_dir, 0.1)
slope_da = srtm_slope(srtm_da)
```
:::

:::: {.cell execution_count="8"}
``` {.python .cell-code}
%store slope_da
```

::: {.cell-output .cell-output-stdout}
    Stored 'slope_da' (DataArray)
:::
::::

:::: {.cell fig-title="Elevation overlaid by Grasslands" execution_count="9"}
``` {.python .cell-code}
plot_gdf_da(buffalo_gdf, srtm_da, cmap='terrain')
```

::: {.cell-output .cell-output-display}
![](climate_files/figure-markdown/fig-srtm-output-1.png){#fig-srtm}
:::
::::

:::: {.cell fig-title="Slope overlaid by Grasslands" execution_count="10"}
``` {.python .cell-code}
plot_gdf_da(buffalo_gdf, slope_da, cmap='terrain')
```

::: {.cell-output .cell-output-display}
![](climate_files/figure-markdown/fig-slope-output-1.png){#fig-slope}
:::
::::

Alternate plot only inside grasslands. Want to smooth over `buffalo_gdf`
to fill in internal holes.

:::: {.cell fig-title="Slope clipped by Grasslands" execution_count="11"}
``` {.python .cell-code}
slope_clip_da = slope_da.rio.clip(buffalo_gdf.geometry)
slope_clip_da.plot(cmap='terrain')
#buffalo_gdf.boundary.plot(ax=plt.gca(), color = "black", linewidth=0.5)
plt.show()
```

::: {.cell-output .cell-output-display}
![](climate_files/figure-markdown/fig-slopeclip-output-1.png){#fig-slopeclip}
:::
::::

### Climate model data

You can use MACAv2 data for historical and future climate data. Be sure
to compare at least two 30-year time periods (e.g. historical vs. 10
years in the future) for at least four of the CMIP models. Overall, you
should be downloading at least 8 climate rasters for each of your sites,
for a total of 16. **You will *need* to use loops and/or functions to do
this cleanly!**.

Write a **function with a numpy-style docstring** that will download
MACAv2 data for a particular climate model, emissions scenario, spatial
domain, and time frame. Then, use loops to download and organize the 16+
rasters you will need to complete this section. The MACAv2 dataset is
accessible from their [Thredds
server](http://thredds.northwestknowledge.net:8080/thredds/reacch_climate_CMIP5_macav2_catalog2.html).
Include an arrangement of sites, models, emissions scenarios, and time
periods that will help you to answer your scientific question.

Project precipation `pr` under representative concentration pathway
scenarios `rcp45` and `rcp85` for years `2006-2035` and `2036-2065`.

Pseudocode:

``` python
info_df, maca_da = process_maca({'buffalo': buffalo_gdf})
maca_rcp_2025_da = da_combine(
    maca_year(maca_da[1], 2025),
    maca_year(maca_da[0], 2025))
plot_das(maca_rcp_2025_da, gdf = buffalo_gdf, onebar = False)
```

Python code detail:

::::: {.cell execution_count="12"}
``` {.python .cell-code}
info_df, maca_da = process_maca({'buffalo': buffalo_gdf},
    scenarios=['pr'], climates=['rcp85', 'rcp45'], years=[2006,2065])
info_df
```

::: {.cell-output .cell-output-stdout}
    Years: 2006 2065
:::

::: {.cell-output .cell-output-display execution_count="63"}
<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>

      site_name   scenario   climate
  --- ----------- ---------- ---------
  0   buffalo     pr         rcp85
  1   buffalo     pr         rcp45

</div>
:::
:::::

:::: {.cell execution_count="13"}
``` {.python .cell-code}
%store maca_da
```

::: {.cell-output .cell-output-stdout}
    Stored 'maca_da' (list)
:::
::::

::: {.cell execution_count="14"}
``` {.python .cell-code}
maca_rcp_2025_da = da_combine(maca_year(maca_da[1], 2025), maca_year(maca_da[0], 2025))
```
:::

:::: {.cell fig-title="RCP 4.5 vs 8.5 for 2025" execution_count="15"}
``` {.python .cell-code}
# 0 = `rcp85`, 1 = `rcp45`
plot_das(maca_rcp_2025_da, gdf = buffalo_gdf, onebar = False)
del maca_rcp_2025_da
```

::: {.cell-output .cell-output-display}
![](climate_files/figure-markdown/fig-maca-output-1.png){#fig-maca}
:::
::::

::::: {.cell fig-title="RCP 8.5 2006-2065" execution_count="16"}
``` {.python .cell-code}
plot_das(maca_da[0][[0,10,20,29]], gdf = buffalo_gdf)
plot_das(maca_da[0][[59,50,40,30]], gdf = buffalo_gdf)
```

::: {.cell-output .cell-output-display}
![](climate_files/figure-markdown/fig-maca85-output-1.png){#fig-maca85-1
ref-parent="fig-maca85"}
:::

::: {.cell-output .cell-output-display}
![](climate_files/figure-markdown/fig-maca85-output-2.png){#fig-maca85-2
ref-parent="fig-maca85"}
:::
:::::

::::: {.cell fig-title="RCP 4.5 2006-2065" execution_count="17"}
``` {.python .cell-code}
plot_das(maca_da[1][[0,10,20,29,]], gdf = buffalo_gdf)
plot_das(maca_da[1][[59,50,40,30]], gdf = buffalo_gdf)
```

::: {.cell-output .cell-output-display}
![](climate_files/figure-markdown/fig-maca45-output-1.png){ref-parent="fig-maca45"}
:::

::: {.cell-output .cell-output-display}
![](climate_files/figure-markdown/fig-maca45-output-2.png){#fig-maca45-2
ref-parent="fig-maca45"}
:::
:::::

::: {.cell execution_count="18"}
``` {.python .cell-code}
maca_now_da = da_combine(
    maca_da[1][list(range(30))].mean(dim='time'),
    maca_da[0][list(range(30))].mean(dim='time'))
maca_fut_da = da_combine(
    maca_da[1][list(range(30,60))].mean(dim='time'),
    maca_da[0][list(range(30,60))].mean(dim='time'))
```
:::

:::: {.cell fig-title="Mean Change by RCP for 2006-2035" execution_count="19"}
``` {.python .cell-code}
plot_das(maca_now_da, onebar=False)
```

::: {.cell-output .cell-output-display}
![](climate_files/figure-markdown/fig-dasnow-output-1.png){#fig-dasnow}
:::
::::

:::: {.cell fig-title="Mean Change by RCP for 2036-2065" execution_count="20"}
``` {.python .cell-code}
plot_das(maca_fut_da, onebar=False)
```

::: {.cell-output .cell-output-display}
![](climate_files/figure-markdown/fig-dasfut-output-1.png){#fig-dasfut}
:::
::::

**Reflect and Respond:** Make sure to include a description of the
climate data and how you selected your models. Include a citation of the
MACAv2 data
</p>
</div>
</div>

YOUR CLIMATE DATA DESCRIPTION AND CITATIONS HERE

## STEP 3: HARMONIZE DATA

Make sure that the grids for all your data match each other. Check out
the [`ds.rio.reproject_match()`
method](https://corteva.github.io/rioxarray/stable/examples/reproject_match.html#Reproject-Match)
from `rioxarray`. Make sure to use the data source that has the highest
resolution as a template!

> **Warning**
>
> If you are reprojecting data as you need to here, the order of
> operations is important! Recall that reprojecting will typically tilt
> your data, leaving narrow sections of the data at the edge blank.
> However, to reproject efficiently it is best for the raster to be as
> small as possible before performing the operation. We recommend the
> following process:
>
>     1. Crop the data, leaving a buffer around the final boundary
>     2. Reproject to match the template grid (this will also crop any leftovers off the image)

See
[3_harmonize](https://github.com/byandell-envsys/habitatSuitability/blob/main/3_harmonize.ipynb).

:::: {.cell execution_count="21"}
``` {.python .cell-code}
%store -r buffalo_gdf, buffalo_da, slope_da, maca_da
```

::: {.cell-output .cell-output-stdout}
    no stored variable or alias buffalo_gdf,
    no stored variable or alias buffalo_da,
    no stored variable or alias slope_da,
:::
::::

:::: {.cell execution_count="22"}
``` {.python .cell-code}
print(slope_da.shape)
print(buffalo_da.shape)
print(maca_da[0].shape)
```

::: {.cell-output .cell-output-stdout}
    (5680, 10504)
    (4893, 10018)
    (60, 36, 68)
:::
::::

Get mean across 30-year intervals for two eras and two RCP levels.

::: {.cell execution_count="23"}
``` {.python .cell-code}
maca_das = xr.concat(
    [maca_da[1][list(range(30))].mean(dim='time'),
    maca_da[0][list(range(30))].mean(dim='time'),
    maca_da[1][list(range(30,60))].mean(dim='time'),
    maca_da[0][list(range(30,60))].mean(dim='time')],
    dim = 'era_rcp')
era_rcp = ['now45','now85','fut45','fut85']
maca_das = maca_das.assign_coords(era_rcp=era_rcp)
```
:::

Reproject sand and maca DAs with slope, and clip to grassland
boundaries.

::: {.cell execution_count="24"}
``` {.python .cell-code}
sand_da = buffalo_da.rio.reproject_match(slope_da).rio.clip(buffalo_gdf.geometry)
slope_da_clip = slope_da.rio.clip(buffalo_gdf.geometry)
```
:::

::: {.cell execution_count="25"}
``` {.python .cell-code}
maca_clip_da = {}
for i in list(range(maca_das.shape[0])):
    maca_clip_da[era_rcp[i]] = maca_das[i].rio.reproject_match(slope_da).rio.clip(buffalo_gdf.geometry)
```
:::

:::: {.cell fig-title="Slope and Sand Clipped to Grasslands" execution_count="26"}
``` {.python .cell-code}
slope_da_clip.plot()
sand_da.plot()
```

::: {.cell-output .cell-output-display}
![](climate_files/figure-markdown/fig-slopesandclip-output-1.png){#fig-slopesandclip}
:::
::::

## STEP 4: DEVELOP A FUZZY LOGIC MODEL

Rough plan:

-   Fuzzy Logic on images
    -   migrate from my `ramp_logic()` to skfuzzy (see
        [notes_fuzzy.qmd](https://github.com/byandell-envsys/landmapy/blob/main/notes.qmd#fuzzy-logic-model-27-feb-2025))
    -   build images and do algebra on them
-   Relationships of values
    -   reorg sand, slope and precip (maca) over time das into dataframe
        (columns for lon, lat, characteristics)
    -   explore with plots using plotnine/ggplot2
    -   perhaps come up with better fuzzy logic

A fuzzy logic model is one that is built on expert knowledge rather than
training data. You may wish to use the
[`scikit-fuzzy`](https://pythonhosted.org/scikit-fuzzy/) library, which
includes many utilities for building this sort of model. In particular,
it contains a number of **membership functions** that can convert your
data into values from 0 to 1 using information such as, for example, the
maximum, minimum, and optimal values for soil pH.

To train a fuzzy logic habitat suitability model:

1.  Research S. nutans, and find out what optimal values are for each
    variable you are using (e.g. soil pH, slope, and current
    climatological annual precipitation).
2.  For each **digital number** in each raster, assign a **continuous**
    value from 0 to 1 for how close that grid square is to the optimum
    range (1=optimal, 0=incompatible).
3.  Combine your layers by multiplying them together. This will give you
    a single suitability number for each square.
4.  Optionally, you may apply a suitability threshold to make the most
    suitable areas pop on your map.

> **Tip**
>
> If you use mathematical operators on a raster in Python, it will
> automatically perform the operation for every number in the raster.
> This type of operation is known as a **vectorized** function. **DO NOT
> DO THIS WITH A LOOP!**. A vectorized function that operates on the
> whole array at once will be much easier and faster.

## Fuzzy Model

-   use hill functions to transform harmonized DataArrays into 0-1
    DataArrays
-   multiply them together

See

-   [4_build](https://github.com/byandell-envsys/habitatSuitability/blob/main/4_build.ipynb)
-   [SciKit Fuzzy](https://pypi.org/project/scikit-fuzzy/)

Set thresholds:

-   sand at 55 to 85
-   slope \< 10
-   pr above 650

``` {.python .cell-code}
ramp_logic(maca_2010_da, (500, 550), (700, 750)).plot()
```

``` {.python .cell-code}
ramp_logic(sand_da, (50, 60), (80, 90)).plot()
```

``` {.python .cell-code}
ramp_logic(slope_da, (0, 5), (15, 20)).plot()
```

## STEP 5: PRESENT YOUR RESULTS

Generate some plots that show your key findings. Don't forget to
interpret your plots!

::: {.cell highlight="true" execution_count="30"}
``` {.python .cell-code}
# Create plots
```
:::

YOUR PLOT INTERPRETATION HERE
