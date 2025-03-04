<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" lang="en" xml:lang="en"><head>

<meta charset="utf-8">
<meta name="generator" content="quarto-1.6.33">

<meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=yes">


<title>EDA Notes for Habitat Suitability</title>
<style>
code{white-space: pre-wrap;}
span.smallcaps{font-variant: small-caps;}
div.columns{display: flex; gap: min(4vw, 1.5em);}
div.column{flex: auto; overflow-x: auto;}
div.hanging-indent{margin-left: 1.5em; text-indent: -1.5em;}
ul.task-list{list-style: none;}
ul.task-list li input[type="checkbox"] {
  width: 0.8em;
  margin: 0 0.8em 0.2em -1em; /* quarto-specific, see https://github.com/quarto-dev/quarto-cli/issues/4556 */ 
  vertical-align: middle;
}
/* CSS for syntax highlighting */
pre > code.sourceCode { white-space: pre; position: relative; }
pre > code.sourceCode > span { line-height: 1.25; }
pre > code.sourceCode > span:empty { height: 1.2em; }
.sourceCode { overflow: visible; }
code.sourceCode > span { color: inherit; text-decoration: inherit; }
div.sourceCode { margin: 1em 0; }
pre.sourceCode { margin: 0; }
@media screen {
div.sourceCode { overflow: auto; }
}
@media print {
pre > code.sourceCode { white-space: pre-wrap; }
pre > code.sourceCode > span { display: inline-block; text-indent: -5em; padding-left: 5em; }
}
pre.numberSource code
  { counter-reset: source-line 0; }
pre.numberSource code > span
  { position: relative; left: -4em; counter-increment: source-line; }
pre.numberSource code > span > a:first-child::before
  { content: counter(source-line);
    position: relative; left: -1em; text-align: right; vertical-align: baseline;
    border: none; display: inline-block;
    -webkit-touch-callout: none; -webkit-user-select: none;
    -khtml-user-select: none; -moz-user-select: none;
    -ms-user-select: none; user-select: none;
    padding: 0 4px; width: 4em;
  }
pre.numberSource { margin-left: 3em;  padding-left: 4px; }
div.sourceCode
  {   }
@media screen {
pre > code.sourceCode > span > a:first-child::before { text-decoration: underline; }
}
</style>


<script src="notes_files/libs/clipboard/clipboard.min.js"></script>
<script src="notes_files/libs/quarto-html/quarto.js"></script>
<script src="notes_files/libs/quarto-html/popper.min.js"></script>
<script src="notes_files/libs/quarto-html/tippy.umd.min.js"></script>
<script src="notes_files/libs/quarto-html/anchor.min.js"></script>
<link href="notes_files/libs/quarto-html/tippy.css" rel="stylesheet">
<link href="notes_files/libs/quarto-html/quarto-syntax-highlighting-07ba0ad10f5680c660e360ac31d2f3b6.css" rel="stylesheet" id="quarto-text-highlighting-styles">
<script src="notes_files/libs/bootstrap/bootstrap.min.js"></script>
<link href="notes_files/libs/bootstrap/bootstrap-icons.css" rel="stylesheet">
<link href="notes_files/libs/bootstrap/bootstrap-fe6593aca1dacbc749dc3d2ba78c8639.min.css" rel="stylesheet" append-hash="true" id="quarto-bootstrap" data-mode="light">


</head>

<body class="fullcontent">

<div id="quarto-content" class="page-columns page-rows-contents page-layout-article">

<main class="content" id="quarto-document-content">

<header id="title-block-header" class="quarto-title-block default">
<div class="quarto-title">
<h1 class="title">EDA Notes for Habitat Suitability</h1>
</div>



<div class="quarto-title-meta">

    
  
    
  </div>
  


</header>


<ul>
<li><a href="#fuzzy-logic-model-27-feb-2025">Fuzzy Logic Model 27 Feb 2025</a></li>
<li><a href="#gbif-review-25-feb-2025">GBIF review 25 Feb 2025</a></li>
<li><a href="#classes-20-feb-2025">Classes 20 Feb 2025</a></li>
</ul>
<section id="fuzzy-logic-model-27-feb-2025" class="level2">
<h2 class="anchored" data-anchor-id="fuzzy-logic-model-27-feb-2025">Fuzzy Logic Model 27 Feb 2025</h2>
<p>You can find it hereLinks to an external site., or under the “Modules” section on Canvas. Elsa has also provided a link to a conversation with ChatGPTLinks to an external site. that she had on how to implement fuzzy models using scikit-fuzzy in Python, as another resource for you.</p>
<ul>
<li>Elsa demo
<ul>
<li><a href="https://canvas.colorado.edu/courses/115453/modules/items/6282073">Elsa Video on Fuzzy Logic</a></li>
<li><a href="https://chatgpt.com/share/67c094af-9724-8000-9004-6f25d266cd85">Elsa ChatGPT</a></li>
<li><a href="https://github.com/earthlab-education/habitat-suitability-byandell/blob/main/notes_fuzzy.qmd">notes_fuzzy.qmd</a></li>
</ul></li>
<li><a href="https://github.com/byandell-envsys/habitatSuitability/blob/main/4_build.ipynb">Fall 2024 habitatSuitability/4_build</a></li>
<li><a href="https://pypi.org/project/scikit-fuzzy/">SciKit Fuzzy</a>
<ul>
<li><a href="https://scikit-fuzzy.readthedocs.io/en/latest/">SciKit Fuzzy readthedocs</a></li>
</ul></li>
<li><a href="https://www.middlewaysociety.org/books/psychology-books/thinking-fast-and-slow-by-daniel-kahneman/">Daniel Kahneman (2011) Thinking Fast and Slow</a></li>
</ul>
<p>A fuzzy logic model is one that is built on expert knowledge rather than training data. You may wish to use the <a href="https://pythonhosted.org/scikit-fuzzy/"><code>scikit-fuzzy</code></a> library, which includes many utilities for building this sort of model. In particular, it contains a number of <strong>membership functions</strong> that can convert your data into values from 0 to 1 using information such as, for example, the maximum, minimum, and optimal values for soil pH.</p>
<p>To train a fuzzy logic habitat suitability model:</p>
<ol type="1">
<li>Research S. nutans, and find out what optimal values are for each variable you are using (e.g.&nbsp;soil pH, slope, and current climatological annual precipitation).</li>
<li>For each <strong>digital number</strong> in each raster, assign a <strong>continuous</strong> value from 0 to 1 for how close that grid square is to the optimum range (1=optimal, 0=incompatible).</li>
<li>Combine your layers by multiplying them together. This will give you a single suitability number for each square.</li>
<li>Optionally, you may apply a suitability threshold to make the most suitable areas pop on your map.</li>
</ol>
<blockquote class="blockquote">
<p><strong>Tip</strong></p>
<p>If you use mathematical operators on a raster in Python, it will automatically perform the operation for every number in the raster. This type of operation is known as a <strong>vectorized</strong> function. <strong>DO NOT DO THIS WITH A LOOP!</strong>. A vectorized function that operates on the whole array at once will be much easier and faster.</p>
</blockquote>
<ul>
<li>use hill functions to transform harmonized DataArrays into 0-1 DataArrays</li>
<li>multiply them together</li>
</ul>
<p>Resources:</p>
<ul>
<li><a href="https://www.nrcs.usda.gov/plantmaterials/etpmcpg13196.pdf">USDA Natural Resources Convervations Service: Plant Guide: Indiangrass</a></li>
</ul>
<div id="a4327be3" class="cell" data-execution_count="1">
<div class="sourceCode cell-code" id="cb1"><pre class="sourceCode python code-with-copy"><code class="sourceCode python"><span id="cb1-1"><a href="#cb1-1" aria-hidden="true" tabindex="-1"></a><span class="co">#conda install skfuzzy</span></span></code><button title="Copy to Clipboard" class="code-copy-button"><i class="bi"></i></button></pre></div>
</div>
<p>Libraries</p>
<div id="226a89c0" class="cell" data-execution_count="2">
<div class="sourceCode cell-code" id="cb2"><pre class="sourceCode python code-with-copy"><code class="sourceCode python"><span id="cb2-1"><a href="#cb2-1" aria-hidden="true" tabindex="-1"></a><span class="co">#pip install --quiet git+https://github.com/byandell-envsys/landmapy.git</span></span></code><button title="Copy to Clipboard" class="code-copy-button"><i class="bi"></i></button></pre></div>
</div>
<p>Libraries</p>
<div id="3739041b" class="cell" data-execution_count="3">
<div class="sourceCode cell-code" id="cb3"><pre class="sourceCode python code-with-copy"><code class="sourceCode python"><span id="cb3-1"><a href="#cb3-1" aria-hidden="true" tabindex="-1"></a><span class="im">from</span> math <span class="im">import</span> floor, ceil</span>
<span id="cb3-2"><a href="#cb3-2" aria-hidden="true" tabindex="-1"></a><span class="im">import</span> cartopy.crs <span class="im">as</span> ccrs</span>
<span id="cb3-3"><a href="#cb3-3" aria-hidden="true" tabindex="-1"></a><span class="im">import</span> geopandas <span class="im">as</span> gpd</span>
<span id="cb3-4"><a href="#cb3-4" aria-hidden="true" tabindex="-1"></a><span class="im">import</span> hvplot.pandas</span>
<span id="cb3-5"><a href="#cb3-5" aria-hidden="true" tabindex="-1"></a><span class="im">import</span> hvplot.xarray</span>
<span id="cb3-6"><a href="#cb3-6" aria-hidden="true" tabindex="-1"></a><span class="im">import</span> numpy <span class="im">as</span> np</span>
<span id="cb3-7"><a href="#cb3-7" aria-hidden="true" tabindex="-1"></a><span class="im">import</span> rioxarray <span class="im">as</span> rxr</span>
<span id="cb3-8"><a href="#cb3-8" aria-hidden="true" tabindex="-1"></a><span class="im">import</span> rioxarray.merge <span class="im">as</span> rxrmerge</span>
<span id="cb3-9"><a href="#cb3-9" aria-hidden="true" tabindex="-1"></a><span class="im">import</span> skfuzzy</span>
<span id="cb3-10"><a href="#cb3-10" aria-hidden="true" tabindex="-1"></a><span class="im">import</span> xarray <span class="im">as</span> xr</span></code><button title="Copy to Clipboard" class="code-copy-button"><i class="bi"></i></button></pre></div>
</div>
<p>My version:</p>
<div class="sourceCode" id="cb4"><pre class="sourceCode python code-with-copy"><code class="sourceCode python"><span id="cb4-1"><a href="#cb4-1" aria-hidden="true" tabindex="-1"></a><span class="im">from</span> landmapy.initial <span class="im">import</span> create_data_dir <span class="co"># create (or retrieve) data directory</span></span>
<span id="cb4-2"><a href="#cb4-2" aria-hidden="true" tabindex="-1"></a><span class="im">from</span> landmapy.plot <span class="im">import</span> plot_gdf_state <span class="co"># plot gdf with state overlay</span></span>
<span id="cb4-3"><a href="#cb4-3" aria-hidden="true" tabindex="-1"></a></span>
<span id="cb4-4"><a href="#cb4-4" aria-hidden="true" tabindex="-1"></a><span class="op">%</span>store <span class="op">-</span>r buffalo_gdf</span>
<span id="cb4-5"><a href="#cb4-5" aria-hidden="true" tabindex="-1"></a><span class="cf">try</span>:</span>
<span id="cb4-6"><a href="#cb4-6" aria-hidden="true" tabindex="-1"></a>    buffalo_gdf</span>
<span id="cb4-7"><a href="#cb4-7" aria-hidden="true" tabindex="-1"></a><span class="cf">except</span> <span class="pp">NameError</span>:</span>
<span id="cb4-8"><a href="#cb4-8" aria-hidden="true" tabindex="-1"></a>    data_dir <span class="op">=</span> create_data_dir(<span class="st">'habitat'</span>)</span>
<span id="cb4-9"><a href="#cb4-9" aria-hidden="true" tabindex="-1"></a>    <span class="co"># Read all grasslands GeoJSON into `grassland_gdf`.</span></span>
<span id="cb4-10"><a href="#cb4-10" aria-hidden="true" tabindex="-1"></a>    grassland_url <span class="op">=</span> <span class="ss">f"</span><span class="sc">{</span>data_dir<span class="sc">}</span><span class="ss">/National_Grassland_Units_(Feature_Layer).geojson"</span></span>
<span id="cb4-11"><a href="#cb4-11" aria-hidden="true" tabindex="-1"></a>    grassland_gdf <span class="op">=</span> gpd.read_file(grassland_url)</span>
<span id="cb4-12"><a href="#cb4-12" aria-hidden="true" tabindex="-1"></a>    <span class="co"># Subset to desired locations.</span></span>
<span id="cb4-13"><a href="#cb4-13" aria-hidden="true" tabindex="-1"></a>    buffalo_gdf <span class="op">=</span> grassland_gdf.loc[grassland_gdf[<span class="st">'GRASSLANDNAME'</span>].isin(</span>
<span id="cb4-14"><a href="#cb4-14" aria-hidden="true" tabindex="-1"></a>        [<span class="st">"Buffalo Gap National Grassland"</span>, <span class="st">"Oglala National Grassland"</span>])]</span>
<span id="cb4-15"><a href="#cb4-15" aria-hidden="true" tabindex="-1"></a>    <span class="op">%</span>store buffalo_gdf</span>
<span id="cb4-16"><a href="#cb4-16" aria-hidden="true" tabindex="-1"></a>    <span class="bu">print</span>(<span class="st">"buffalo_gdf created and stored"</span>)</span>
<span id="cb4-17"><a href="#cb4-17" aria-hidden="true" tabindex="-1"></a><span class="cf">else</span>:</span>
<span id="cb4-18"><a href="#cb4-18" aria-hidden="true" tabindex="-1"></a>    <span class="bu">print</span>(<span class="st">"buffalo_gdf retrieved from StoreMagic"</span>)</span></code><button title="Copy to Clipboard" class="code-copy-button"><i class="bi"></i></button></pre></div>
<p>Elsa’s version</p>
<div id="937b2401" class="cell" data-execution_count="4">
<div class="sourceCode cell-code" id="cb5"><pre class="sourceCode python code-with-copy"><code class="sourceCode python"><span id="cb5-1"><a href="#cb5-1" aria-hidden="true" tabindex="-1"></a>grassland_url <span class="op">=</span> (</span>
<span id="cb5-2"><a href="#cb5-2" aria-hidden="true" tabindex="-1"></a>    <span class="st">"https://data.fs.usda.gov/geodata/edw/edw_resources/shp/S_USA.NationalGrassland.zip"</span>)</span>
<span id="cb5-3"><a href="#cb5-3" aria-hidden="true" tabindex="-1"></a>grassland_gdf <span class="op">=</span> gpd.read_file(grassland_url)</span>
<span id="cb5-4"><a href="#cb5-4" aria-hidden="true" tabindex="-1"></a>grassland_gdf.info</span></code><button title="Copy to Clipboard" class="code-copy-button"><i class="bi"></i></button></pre></div>
</div>
<div id="a4d87238" class="cell" data-execution_count="5">
<div class="sourceCode cell-code" id="cb6"><pre class="sourceCode python code-with-copy"><code class="sourceCode python"><span id="cb6-1"><a href="#cb6-1" aria-hidden="true" tabindex="-1"></a>oglala_gdf <span class="op">=</span> grassland_gdf[grassland_gdf.GRASSLANDN.<span class="bu">str</span>.contains(<span class="st">'Oglala'</span>)]</span>
<span id="cb6-2"><a href="#cb6-2" aria-hidden="true" tabindex="-1"></a>(</span>
<span id="cb6-3"><a href="#cb6-3" aria-hidden="true" tabindex="-1"></a>    oglala_gdf</span>
<span id="cb6-4"><a href="#cb6-4" aria-hidden="true" tabindex="-1"></a>    .to_crs(ccrs.Mercator())</span>
<span id="cb6-5"><a href="#cb6-5" aria-hidden="true" tabindex="-1"></a>    .hvplot(tiles<span class="op">=</span><span class="st">'EsriNatGeo'</span>, line_width<span class="op">=</span><span class="dv">3</span>, fill_color<span class="op">=</span><span class="va">None</span>)</span>
<span id="cb6-6"><a href="#cb6-6" aria-hidden="true" tabindex="-1"></a>)</span></code><button title="Copy to Clipboard" class="code-copy-button"><i class="bi"></i></button></pre></div>
</div>
<div id="e3f3cea6" class="cell" data-execution_count="6">
<div class="sourceCode cell-code" id="cb7"><pre class="sourceCode python code-with-copy"><code class="sourceCode python"><span id="cb7-1"><a href="#cb7-1" aria-hidden="true" tabindex="-1"></a>oglala_gdf</span></code><button title="Copy to Clipboard" class="code-copy-button"><i class="bi"></i></button></pre></div>
</div>
<div id="d2606116" class="cell" data-execution_count="7">
<div class="sourceCode cell-code" id="cb8"><pre class="sourceCode python code-with-copy"><code class="sourceCode python"><span id="cb8-1"><a href="#cb8-1" aria-hidden="true" tabindex="-1"></a><span class="im">from</span> landmapy.polaris <span class="im">import</span> merge_soil</span>
<span id="cb8-2"><a href="#cb8-2" aria-hidden="true" tabindex="-1"></a></span>
<span id="cb8-3"><a href="#cb8-3" aria-hidden="true" tabindex="-1"></a>ph_da <span class="op">=</span> merge_soil(oglala_gdf, <span class="st">"ph"</span>, <span class="st">"mean"</span>, <span class="st">"60_100"</span>, <span class="fl">0.1</span>)</span>
<span id="cb8-4"><a href="#cb8-4" aria-hidden="true" tabindex="-1"></a>ph_da.plot()</span></code><button title="Copy to Clipboard" class="code-copy-button"><i class="bi"></i></button></pre></div>
</div>
<div id="822eb8c0" class="cell" data-execution_count="8">
<div class="sourceCode cell-code" id="cb9"><pre class="sourceCode python code-with-copy"><code class="sourceCode python"><span id="cb9-1"><a href="#cb9-1" aria-hidden="true" tabindex="-1"></a><span class="im">from</span> landmapy.thredds <span class="im">import</span> process_maca</span>
<span id="cb9-2"><a href="#cb9-2" aria-hidden="true" tabindex="-1"></a></span>
<span id="cb9-3"><a href="#cb9-3" aria-hidden="true" tabindex="-1"></a>maca_df <span class="op">=</span> process_maca({<span class="st">'oglala'</span>: oglala_gdf}, [<span class="st">'pr'</span>], [<span class="st">'rcp45'</span>], (<span class="dv">2011</span>, <span class="dv">2040</span>))</span></code><button title="Copy to Clipboard" class="code-copy-button"><i class="bi"></i></button></pre></div>
</div>
<p>This part differs from Elsa’s demo. She ended her loop with (ignoring buffer) <code>periods.append(period_da)</code>, so there is just the DataArray <code>periods</code>.</p>
<p>For the Fall project, I constructed (in <code>process_maca()</code>) I did <code>maca_da_list.append(dict(..., da = maca_da))</code> so that the DataArray ended up as part of the <code>dict()</code>. Then I converted to a DataFrame <code>maca_df = pd.DataFrame(maca_da_list)</code>. To pull out the DataFrame <code>da</code> requires the following step:</p>
<div id="828b2303" class="cell" data-execution_count="9">
<div class="sourceCode cell-code" id="cb10"><pre class="sourceCode python code-with-copy"><code class="sourceCode python"><span id="cb10-1"><a href="#cb10-1" aria-hidden="true" tabindex="-1"></a>maca0_da <span class="op">=</span> maca_df.loc[<span class="dv">1</span>, <span class="st">'da'</span>]</span></code><button title="Copy to Clipboard" class="code-copy-button"><i class="bi"></i></button></pre></div>
</div>
<div id="729d3931" class="cell" data-execution_count="10">
<div class="sourceCode cell-code" id="cb11"><pre class="sourceCode python code-with-copy"><code class="sourceCode python"><span id="cb11-1"><a href="#cb11-1" aria-hidden="true" tabindex="-1"></a>maca_da <span class="op">=</span> (</span>
<span id="cb11-2"><a href="#cb11-2" aria-hidden="true" tabindex="-1"></a>    xr.concat(maca_df[<span class="st">'da'</span>].tolist(), dim<span class="op">=</span><span class="st">'five_year'</span>)</span>
<span id="cb11-3"><a href="#cb11-3" aria-hidden="true" tabindex="-1"></a>    .isel(five_year<span class="op">=</span><span class="dv">0</span>)</span>
<span id="cb11-4"><a href="#cb11-4" aria-hidden="true" tabindex="-1"></a>)</span></code><button title="Copy to Clipboard" class="code-copy-button"><i class="bi"></i></button></pre></div>
</div>
<p>I checked with the following code that the dimension ‘five_year’ appears to be redundant. Hoping this is true.</p>
<div class="sourceCode" id="cb12"><pre class="sourceCode python code-with-copy"><code class="sourceCode python"><span id="cb12-1"><a href="#cb12-1" aria-hidden="true" tabindex="-1"></a>maca_da <span class="op">=</span> xr.concat(maca_df[<span class="st">'da'</span>].tolist(), dim<span class="op">=</span><span class="st">'five_year'</span>)</span>
<span id="cb12-2"><a href="#cb12-2" aria-hidden="true" tabindex="-1"></a>m0 <span class="op">=</span> maca_da.isel(five_year<span class="op">=</span><span class="dv">0</span>)</span>
<span id="cb12-3"><a href="#cb12-3" aria-hidden="true" tabindex="-1"></a>m1 <span class="op">=</span> maca_da.isel(five_year<span class="op">=</span><span class="dv">2</span>)</span>
<span id="cb12-4"><a href="#cb12-4" aria-hidden="true" tabindex="-1"></a>(m0<span class="op">-</span>m1).<span class="bu">sum</span>()</span></code><button title="Copy to Clipboard" class="code-copy-button"><i class="bi"></i></button></pre></div>
<div id="6ba00c52" class="cell" data-execution_count="11">
<div class="sourceCode cell-code" id="cb13"><pre class="sourceCode python code-with-copy"><code class="sourceCode python"><span id="cb13-1"><a href="#cb13-1" aria-hidden="true" tabindex="-1"></a><span class="bu">print</span>(maca0_da.dims)</span>
<span id="cb13-2"><a href="#cb13-2" aria-hidden="true" tabindex="-1"></a><span class="bu">print</span>(maca0_da.shape)</span>
<span id="cb13-3"><a href="#cb13-3" aria-hidden="true" tabindex="-1"></a><span class="bu">print</span>(maca_da.dims)</span>
<span id="cb13-4"><a href="#cb13-4" aria-hidden="true" tabindex="-1"></a><span class="bu">print</span>(maca_da.shape)</span></code><button title="Copy to Clipboard" class="code-copy-button"><i class="bi"></i></button></pre></div>
</div>
<p>Sum over time within each year over the 30 years (‘time’), reprojecting to shape of <code>ph_da</code>.</p>
<div id="cf335494" class="cell" data-execution_count="12">
<div class="sourceCode cell-code" id="cb14"><pre class="sourceCode python code-with-copy"><code class="sourceCode python"><span id="cb14-1"><a href="#cb14-1" aria-hidden="true" tabindex="-1"></a>precip_da <span class="op">=</span> (</span>
<span id="cb14-2"><a href="#cb14-2" aria-hidden="true" tabindex="-1"></a>    xr.concat(maca_da, dim<span class="op">=</span><span class="st">'time'</span>)</span>
<span id="cb14-3"><a href="#cb14-3" aria-hidden="true" tabindex="-1"></a>    .resample({<span class="st">'time'</span>: <span class="st">'YE'</span>})</span>
<span id="cb14-4"><a href="#cb14-4" aria-hidden="true" tabindex="-1"></a>    .<span class="bu">sum</span>()</span>
<span id="cb14-5"><a href="#cb14-5" aria-hidden="true" tabindex="-1"></a>    .rio.write_crs(<span class="dv">4236</span>) </span>
<span id="cb14-6"><a href="#cb14-6" aria-hidden="true" tabindex="-1"></a>    .rio.reproject_match(ph_da)</span>
<span id="cb14-7"><a href="#cb14-7" aria-hidden="true" tabindex="-1"></a>)</span></code><button title="Copy to Clipboard" class="code-copy-button"><i class="bi"></i></button></pre></div>
</div>
<div id="1ef32011" class="cell" data-execution_count="13">
<div class="sourceCode cell-code" id="cb15"><pre class="sourceCode python code-with-copy"><code class="sourceCode python"><span id="cb15-1"><a href="#cb15-1" aria-hidden="true" tabindex="-1"></a><span class="bu">print</span>(precip_da.shape)</span>
<span id="cb15-2"><a href="#cb15-2" aria-hidden="true" tabindex="-1"></a><span class="bu">print</span>(precip_da.dims)</span></code><button title="Copy to Clipboard" class="code-copy-button"><i class="bi"></i></button></pre></div>
</div>
<div id="83c3864b" class="cell" data-execution_count="14">
<div class="sourceCode cell-code" id="cb16"><pre class="sourceCode python code-with-copy"><code class="sourceCode python"><span id="cb16-1"><a href="#cb16-1" aria-hidden="true" tabindex="-1"></a>precip_min_da <span class="op">=</span> precip_da.<span class="bu">min</span>(<span class="st">'time'</span>)</span>
<span id="cb16-2"><a href="#cb16-2" aria-hidden="true" tabindex="-1"></a>precip_max_da <span class="op">=</span> precip_da.<span class="bu">max</span>(<span class="st">'time'</span>)</span>
<span id="cb16-3"><a href="#cb16-3" aria-hidden="true" tabindex="-1"></a>precip_mean_da <span class="op">=</span> precip_da.mean(<span class="st">'time'</span>)</span></code><button title="Copy to Clipboard" class="code-copy-button"><i class="bi"></i></button></pre></div>
</div>
<div id="b1c26301" class="cell" data-execution_count="15">
<div class="sourceCode cell-code" id="cb17"><pre class="sourceCode python code-with-copy"><code class="sourceCode python"><span id="cb17-1"><a href="#cb17-1" aria-hidden="true" tabindex="-1"></a>precip_mean_da.plot()</span></code><button title="Copy to Clipboard" class="code-copy-button"><i class="bi"></i></button></pre></div>
</div>
<div id="571bc601" class="cell" data-execution_count="16">
<div class="sourceCode cell-code" id="cb18"><pre class="sourceCode python code-with-copy"><code class="sourceCode python"><span id="cb18-1"><a href="#cb18-1" aria-hidden="true" tabindex="-1"></a>precip_min_da.plot()</span></code><button title="Copy to Clipboard" class="code-copy-button"><i class="bi"></i></button></pre></div>
</div>
<div id="8a5183f4" class="cell" data-execution_count="17">
<div class="sourceCode cell-code" id="cb19"><pre class="sourceCode python code-with-copy"><code class="sourceCode python"><span id="cb19-1"><a href="#cb19-1" aria-hidden="true" tabindex="-1"></a>precip_max_da.plot()</span></code><button title="Copy to Clipboard" class="code-copy-button"><i class="bi"></i></button></pre></div>
</div>
<p>Precipitation in mm. (11-45in = 279-1143mm)</p>
<section id="non-fuzzy-logic-model" class="level3">
<h3 class="anchored" data-anchor-id="non-fuzzy-logic-model">Non-fuzzy logic model</h3>
<div id="ae45012e" class="cell" data-execution_count="18">
<div class="sourceCode cell-code" id="cb20"><pre class="sourceCode python code-with-copy"><code class="sourceCode python"><span id="cb20-1"><a href="#cb20-1" aria-hidden="true" tabindex="-1"></a>((precip_mean_da <span class="op">&gt;</span> <span class="dv">95</span>) <span class="op">&amp;</span> (precip_max_da <span class="op">&lt;</span> <span class="dv">800</span>)).plot()</span></code><button title="Copy to Clipboard" class="code-copy-button"><i class="bi"></i></button></pre></div>
</div>
<div id="530a2f3b" class="cell" data-execution_count="19">
<div class="sourceCode cell-code" id="cb21"><pre class="sourceCode python code-with-copy"><code class="sourceCode python"><span id="cb21-1"><a href="#cb21-1" aria-hidden="true" tabindex="-1"></a>precip_min_da.plot.hist()</span></code><button title="Copy to Clipboard" class="code-copy-button"><i class="bi"></i></button></pre></div>
</div>
</section>
<section id="fuzzy-logic" class="level3">
<h3 class="anchored" data-anchor-id="fuzzy-logic">Fuzzy logic</h3>
<p><a href="https://scikit-fuzzy.readthedocs.io/en/latest/api/skfuzzy.html?highlight=trimf#skfuzzy.trimf">trimf</a> is triangle. It takes a 1-D array, but we have 2-D array</p>
<div id="808df4a0" class="cell" data-execution_count="20">
<div class="sourceCode cell-code" id="cb22"><pre class="sourceCode python code-with-copy"><code class="sourceCode python"><span id="cb22-1"><a href="#cb22-1" aria-hidden="true" tabindex="-1"></a>ph <span class="op">=</span> [<span class="fl">4.8</span>, <span class="dv">8</span>]</span>
<span id="cb22-2"><a href="#cb22-2" aria-hidden="true" tabindex="-1"></a>tri <span class="op">=</span> [ph[<span class="dv">0</span>], (ph[<span class="dv">0</span>] <span class="op">+</span> ph[<span class="dv">1</span>])<span class="op">/</span><span class="dv">2</span>, ph[<span class="dv">1</span>]]</span>
<span id="cb22-3"><a href="#cb22-3" aria-hidden="true" tabindex="-1"></a>shape <span class="op">=</span> ph_da.values.shape</span>
<span id="cb22-4"><a href="#cb22-4" aria-hidden="true" tabindex="-1"></a>ph_fuzz <span class="op">=</span> ph_da.copy()</span>
<span id="cb22-5"><a href="#cb22-5" aria-hidden="true" tabindex="-1"></a>ph_fuzz.values <span class="op">=</span> (</span>
<span id="cb22-6"><a href="#cb22-6" aria-hidden="true" tabindex="-1"></a>    np.reshape(</span>
<span id="cb22-7"><a href="#cb22-7" aria-hidden="true" tabindex="-1"></a>        skfuzzy.trimf(ph_da.values.flatten(), tri),</span>
<span id="cb22-8"><a href="#cb22-8" aria-hidden="true" tabindex="-1"></a>    shape)</span>
<span id="cb22-9"><a href="#cb22-9" aria-hidden="true" tabindex="-1"></a>)</span>
<span id="cb22-10"><a href="#cb22-10" aria-hidden="true" tabindex="-1"></a>ph_fuzz.plot()</span></code><button title="Copy to Clipboard" class="code-copy-button"><i class="bi"></i></button></pre></div>
</div>
<div id="54821567" class="cell" data-execution_count="21">
<div class="sourceCode cell-code" id="cb23"><pre class="sourceCode python code-with-copy"><code class="sourceCode python"><span id="cb23-1"><a href="#cb23-1" aria-hidden="true" tabindex="-1"></a>trap <span class="op">=</span> [ph[<span class="dv">0</span>], (<span class="dv">2</span> <span class="op">*</span> ph[<span class="dv">0</span>] <span class="op">+</span> ph[<span class="dv">1</span>])<span class="op">/</span><span class="dv">3</span>, (ph[<span class="dv">0</span>] <span class="op">+</span> <span class="dv">2</span> <span class="op">*</span> ph[<span class="dv">1</span>]) <span class="op">/</span><span class="dv">3</span>, ph[<span class="dv">1</span>]]</span>
<span id="cb23-2"><a href="#cb23-2" aria-hidden="true" tabindex="-1"></a>shape <span class="op">=</span> ph_da.values.shape</span>
<span id="cb23-3"><a href="#cb23-3" aria-hidden="true" tabindex="-1"></a>ph_fuzz <span class="op">=</span> ph_da.copy()</span>
<span id="cb23-4"><a href="#cb23-4" aria-hidden="true" tabindex="-1"></a>ph_fuzz.values <span class="op">=</span> (</span>
<span id="cb23-5"><a href="#cb23-5" aria-hidden="true" tabindex="-1"></a>    np.reshape(</span>
<span id="cb23-6"><a href="#cb23-6" aria-hidden="true" tabindex="-1"></a>        skfuzzy.trapmf(ph_da.values.flatten(), trap),</span>
<span id="cb23-7"><a href="#cb23-7" aria-hidden="true" tabindex="-1"></a>    shape)</span>
<span id="cb23-8"><a href="#cb23-8" aria-hidden="true" tabindex="-1"></a>)</span>
<span id="cb23-9"><a href="#cb23-9" aria-hidden="true" tabindex="-1"></a>ph_fuzz.plot()</span></code><button title="Copy to Clipboard" class="code-copy-button"><i class="bi"></i></button></pre></div>
</div>
<div id="06ee6a1c" class="cell" data-execution_count="22">
<div class="sourceCode cell-code" id="cb24"><pre class="sourceCode python code-with-copy"><code class="sourceCode python"><span id="cb24-1"><a href="#cb24-1" aria-hidden="true" tabindex="-1"></a>pr <span class="op">=</span> [<span class="dv">310</span>, <span class="dv">700</span>]</span>
<span id="cb24-2"><a href="#cb24-2" aria-hidden="true" tabindex="-1"></a>trap <span class="op">=</span> [pr[<span class="dv">0</span>], (<span class="dv">2</span> <span class="op">*</span> pr[<span class="dv">0</span>] <span class="op">+</span> pr[<span class="dv">1</span>])<span class="op">/</span><span class="dv">3</span>, (pr[<span class="dv">0</span>] <span class="op">+</span> <span class="dv">2</span> <span class="op">*</span> pr[<span class="dv">1</span>]) <span class="op">/</span><span class="dv">3</span>, pr[<span class="dv">1</span>]]</span>
<span id="cb24-3"><a href="#cb24-3" aria-hidden="true" tabindex="-1"></a>shape <span class="op">=</span> precip_min_da.values.shape</span>
<span id="cb24-4"><a href="#cb24-4" aria-hidden="true" tabindex="-1"></a>precip_fuzz <span class="op">=</span> precip_min_da.copy()</span>
<span id="cb24-5"><a href="#cb24-5" aria-hidden="true" tabindex="-1"></a>precip_fuzz.values <span class="op">=</span> (</span>
<span id="cb24-6"><a href="#cb24-6" aria-hidden="true" tabindex="-1"></a>    np.reshape(</span>
<span id="cb24-7"><a href="#cb24-7" aria-hidden="true" tabindex="-1"></a>        skfuzzy.trapmf(precip_min_da.values.flatten(), trap),</span>
<span id="cb24-8"><a href="#cb24-8" aria-hidden="true" tabindex="-1"></a>    shape)</span>
<span id="cb24-9"><a href="#cb24-9" aria-hidden="true" tabindex="-1"></a>)</span>
<span id="cb24-10"><a href="#cb24-10" aria-hidden="true" tabindex="-1"></a>precip_fuzz.plot()</span></code><button title="Copy to Clipboard" class="code-copy-button"><i class="bi"></i></button></pre></div>
</div>
<p><a href="https://scikit-fuzzy.readthedocs.io/en/latest/api/skfuzzy.html?highlight=dsw_mult#skfuzzy.dsw_mult">dsw_mult</a></p>
<p>but could use regular mult</p>
<div id="3dbfb8dd" class="cell" data-execution_count="23">
<div class="sourceCode cell-code" id="cb25"><pre class="sourceCode python code-with-copy"><code class="sourceCode python"><span id="cb25-1"><a href="#cb25-1" aria-hidden="true" tabindex="-1"></a>(ph_fuzz <span class="op">*</span> precip_fuzz).plot(robust<span class="op">=</span><span class="va">True</span>)</span></code><button title="Copy to Clipboard" class="code-copy-button"><i class="bi"></i></button></pre></div>
</div>
<div id="b5aa3567" class="cell" data-execution_count="24">
<div class="sourceCode cell-code" id="cb26"><pre class="sourceCode python code-with-copy"><code class="sourceCode python"><span id="cb26-1"><a href="#cb26-1" aria-hidden="true" tabindex="-1"></a>((ph_fuzz <span class="op">*</span> precip_fuzz) <span class="op">&gt;</span> <span class="fl">0.05</span>).plot()</span></code><button title="Copy to Clipboard" class="code-copy-button"><i class="bi"></i></button></pre></div>
</div>
</section>
</section>
<section id="gbif-review-25-feb-2025" class="level2">
<h2 class="anchored" data-anchor-id="gbif-review-25-feb-2025">GBIF review 25 Feb 2025</h2>
<ul>
<li>Katherine Siegel Demo
<ul>
<li><a href="https://canvas.colorado.edu/courses/115453/modules/items/6278820">Katherine Siegel Video</a></li>
<li><a href="https://github.com/earthlab-education/habitat-suitability-byandell/blob/main/notes_gbif.qmd">notes_gbif.qmd</a></li>
</ul></li>
<li>https://pygbif.readthedocs.io/en/latest/</li>
<li>https://github.com/earthlab-education/species-distribution-coding-challenge-byandell/blob/main/notebooks/siberian-crane-species-download.ipynb</li>
<li>earthlab-education and look at repos</li>
<li><a href="https://github.com/earthlab-education/species-distribution-coding-challenge-byandell">Fall 2024 Species</a>
<ul>
<li><a href="https://github.com/earthlab-education/species-distribution-coding-challenge-byandell/blob/main/gbif.py">gbif.py</a></li>
<li><a href="https://github.com/earthlab-education/species-distribution-coding-challenge-byandell/blob/main/sandhill_crane.qmd">sandhill_crane.qmd</a></li>
<li><a href="https://github.com/earthlab-education/species-distribution-coding-challenge-byandell/blob/main/siberian_crane.qmd">siberian_crane.qmd</a></li>
</ul></li>
</ul>
<div id="4a28b920" class="cell" data-execution_count="25">
<div class="sourceCode cell-code" id="cb27"><pre class="sourceCode python code-with-copy"><code class="sourceCode python"><span id="cb27-1"><a href="#cb27-1" aria-hidden="true" tabindex="-1"></a><span class="co">#pip install pygbif</span></span></code><button title="Copy to Clipboard" class="code-copy-button"><i class="bi"></i></button></pre></div>
</div>
<div id="a4fa4cf8" class="cell" data-execution_count="26">
<div class="sourceCode cell-code" id="cb28"><pre class="sourceCode python code-with-copy"><code class="sourceCode python"><span id="cb28-1"><a href="#cb28-1" aria-hidden="true" tabindex="-1"></a><span class="co">## reproducible file paths</span></span>
<span id="cb28-2"><a href="#cb28-2" aria-hidden="true" tabindex="-1"></a><span class="im">import</span> os</span>
<span id="cb28-3"><a href="#cb28-3" aria-hidden="true" tabindex="-1"></a><span class="im">from</span> glob <span class="im">import</span> glob</span>
<span id="cb28-4"><a href="#cb28-4" aria-hidden="true" tabindex="-1"></a><span class="im">import</span> pathlib</span>
<span id="cb28-5"><a href="#cb28-5" aria-hidden="true" tabindex="-1"></a></span>
<span id="cb28-6"><a href="#cb28-6" aria-hidden="true" tabindex="-1"></a><span class="co">## GBIF packages</span></span>
<span id="cb28-7"><a href="#cb28-7" aria-hidden="true" tabindex="-1"></a><span class="im">import</span> pygbif.occurrences <span class="im">as</span> occ</span>
<span id="cb28-8"><a href="#cb28-8" aria-hidden="true" tabindex="-1"></a><span class="im">import</span> pygbif.species <span class="im">as</span> species</span>
<span id="cb28-9"><a href="#cb28-9" aria-hidden="true" tabindex="-1"></a><span class="im">from</span> getpass <span class="im">import</span> getpass</span>
<span id="cb28-10"><a href="#cb28-10" aria-hidden="true" tabindex="-1"></a></span>
<span id="cb28-11"><a href="#cb28-11" aria-hidden="true" tabindex="-1"></a><span class="co">## unzip and handle gbif data</span></span>
<span id="cb28-12"><a href="#cb28-12" aria-hidden="true" tabindex="-1"></a><span class="im">import</span> zipfile</span>
<span id="cb28-13"><a href="#cb28-13" aria-hidden="true" tabindex="-1"></a><span class="im">import</span> time</span>
<span id="cb28-14"><a href="#cb28-14" aria-hidden="true" tabindex="-1"></a></span>
<span id="cb28-15"><a href="#cb28-15" aria-hidden="true" tabindex="-1"></a><span class="co">## spatial data</span></span>
<span id="cb28-16"><a href="#cb28-16" aria-hidden="true" tabindex="-1"></a><span class="im">import</span> geopandas <span class="im">as</span> gpd</span>
<span id="cb28-17"><a href="#cb28-17" aria-hidden="true" tabindex="-1"></a><span class="im">import</span> xrspatial <span class="im">as</span> xr</span>
<span id="cb28-18"><a href="#cb28-18" aria-hidden="true" tabindex="-1"></a></span>
<span id="cb28-19"><a href="#cb28-19" aria-hidden="true" tabindex="-1"></a><span class="co">## other data</span></span>
<span id="cb28-20"><a href="#cb28-20" aria-hidden="true" tabindex="-1"></a><span class="im">import</span> numpy <span class="im">as</span> np</span>
<span id="cb28-21"><a href="#cb28-21" aria-hidden="true" tabindex="-1"></a><span class="im">import</span> pandas <span class="im">as</span> pd</span>
<span id="cb28-22"><a href="#cb28-22" aria-hidden="true" tabindex="-1"></a><span class="im">import</span> rioxarray <span class="im">as</span> rxr</span>
<span id="cb28-23"><a href="#cb28-23" aria-hidden="true" tabindex="-1"></a><span class="im">import</span> rioxarray.merge <span class="im">as</span> rxrm</span>
<span id="cb28-24"><a href="#cb28-24" aria-hidden="true" tabindex="-1"></a></span>
<span id="cb28-25"><a href="#cb28-25" aria-hidden="true" tabindex="-1"></a><span class="co">## invalid geometries</span></span>
<span id="cb28-26"><a href="#cb28-26" aria-hidden="true" tabindex="-1"></a><span class="im">from</span> shapely.geometry <span class="im">import</span> MultiPolygon, Polygon</span>
<span id="cb28-27"><a href="#cb28-27" aria-hidden="true" tabindex="-1"></a></span>
<span id="cb28-28"><a href="#cb28-28" aria-hidden="true" tabindex="-1"></a><span class="co">## viz data</span></span>
<span id="cb28-29"><a href="#cb28-29" aria-hidden="true" tabindex="-1"></a><span class="im">import</span> holoviews <span class="im">as</span> hv</span>
<span id="cb28-30"><a href="#cb28-30" aria-hidden="true" tabindex="-1"></a><span class="im">import</span> hvplot.pandas</span>
<span id="cb28-31"><a href="#cb28-31" aria-hidden="true" tabindex="-1"></a><span class="im">import</span> hvplot.xarray</span></code><button title="Copy to Clipboard" class="code-copy-button"><i class="bi"></i></button></pre></div>
</div>
<div id="af9a4efd" class="cell" data-execution_count="27">
<div class="sourceCode cell-code" id="cb29"><pre class="sourceCode python code-with-copy"><code class="sourceCode python"><span id="cb29-1"><a href="#cb29-1" aria-hidden="true" tabindex="-1"></a><span class="co"># make repro file paths</span></span>
<span id="cb29-2"><a href="#cb29-2" aria-hidden="true" tabindex="-1"></a>data_dir <span class="op">=</span> os.path.join(</span>
<span id="cb29-3"><a href="#cb29-3" aria-hidden="true" tabindex="-1"></a>    <span class="co"># home directory</span></span>
<span id="cb29-4"><a href="#cb29-4" aria-hidden="true" tabindex="-1"></a>    pathlib.Path.home(),</span>
<span id="cb29-5"><a href="#cb29-5" aria-hidden="true" tabindex="-1"></a>    </span>
<span id="cb29-6"><a href="#cb29-6" aria-hidden="true" tabindex="-1"></a>    <span class="co">### eda directory</span></span>
<span id="cb29-7"><a href="#cb29-7" aria-hidden="true" tabindex="-1"></a>    <span class="st">'earth-analytics'</span>,</span>
<span id="cb29-8"><a href="#cb29-8" aria-hidden="true" tabindex="-1"></a>    <span class="st">'data'</span>,</span>
<span id="cb29-9"><a href="#cb29-9" aria-hidden="true" tabindex="-1"></a>    <span class="st">'hab_suit'</span></span>
<span id="cb29-10"><a href="#cb29-10" aria-hidden="true" tabindex="-1"></a>)</span>
<span id="cb29-11"><a href="#cb29-11" aria-hidden="true" tabindex="-1"></a>os.makedirs(data_dir, exist_ok <span class="op">=</span> <span class="va">True</span>)</span></code><button title="Copy to Clipboard" class="code-copy-button"><i class="bi"></i></button></pre></div>
</div>
<p>Sutdy species: Lupinus argenteus (silvery lupine)</p>
<div id="28755b92" class="cell" data-execution_count="28">
<div class="sourceCode cell-code" id="cb30"><pre class="sourceCode python code-with-copy"><code class="sourceCode python"><span id="cb30-1"><a href="#cb30-1" aria-hidden="true" tabindex="-1"></a>gbif_dir <span class="op">=</span> os.path.join(data_dir, <span class="st">'gbif_lupine'</span>)</span></code><button title="Copy to Clipboard" class="code-copy-button"><i class="bi"></i></button></pre></div>
</div>
<div id="d779d42e" class="cell" data-execution_count="29">
<div class="sourceCode cell-code" id="cb31"><pre class="sourceCode python code-with-copy"><code class="sourceCode python"><span id="cb31-1"><a href="#cb31-1" aria-hidden="true" tabindex="-1"></a>reset_credentials <span class="op">=</span> <span class="va">False</span></span>
<span id="cb31-2"><a href="#cb31-2" aria-hidden="true" tabindex="-1"></a></span>
<span id="cb31-3"><a href="#cb31-3" aria-hidden="true" tabindex="-1"></a>credentials <span class="op">=</span> <span class="bu">dict</span>(</span>
<span id="cb31-4"><a href="#cb31-4" aria-hidden="true" tabindex="-1"></a>    GBIF_USER<span class="op">=</span>(<span class="bu">input</span>, <span class="st">'GBIF username:'</span>),</span>
<span id="cb31-5"><a href="#cb31-5" aria-hidden="true" tabindex="-1"></a>    GBIF_PWD<span class="op">=</span>(getpass, <span class="st">'GBIF password:'</span>),</span>
<span id="cb31-6"><a href="#cb31-6" aria-hidden="true" tabindex="-1"></a>    GBIF_EMAIL<span class="op">=</span>(<span class="bu">input</span>, <span class="st">'GBIF email:'</span>)</span>
<span id="cb31-7"><a href="#cb31-7" aria-hidden="true" tabindex="-1"></a>)</span>
<span id="cb31-8"><a href="#cb31-8" aria-hidden="true" tabindex="-1"></a><span class="cf">for</span> env_variable, (prompt_func, prompt_text) <span class="kw">in</span> credentials.items():</span>
<span id="cb31-9"><a href="#cb31-9" aria-hidden="true" tabindex="-1"></a>    <span class="cf">if</span> reset_credentials <span class="kw">and</span> (env_variable <span class="kw">in</span> os.environ):</span>
<span id="cb31-10"><a href="#cb31-10" aria-hidden="true" tabindex="-1"></a>        os.environ.pop(env_variable)</span>
<span id="cb31-11"><a href="#cb31-11" aria-hidden="true" tabindex="-1"></a>    <span class="cf">if</span> <span class="kw">not</span> env_variable <span class="kw">in</span> os.environ:</span>
<span id="cb31-12"><a href="#cb31-12" aria-hidden="true" tabindex="-1"></a>        os.environ[env_variable] <span class="op">=</span> prompt_func(prompt_text)</span></code><button title="Copy to Clipboard" class="code-copy-button"><i class="bi"></i></button></pre></div>
</div>
<p>Now in GBIF. Supply species code.</p>
<div id="fe382b53" class="cell" data-execution_count="30">
<div class="sourceCode cell-code" id="cb32"><pre class="sourceCode python code-with-copy"><code class="sourceCode python"><span id="cb32-1"><a href="#cb32-1" aria-hidden="true" tabindex="-1"></a>species_name <span class="op">=</span> <span class="st">'Lupinus argenteus'</span></span>
<span id="cb32-2"><a href="#cb32-2" aria-hidden="true" tabindex="-1"></a>species_info <span class="op">=</span> species.name_lookup(species_name, rank<span class="op">=</span><span class="st">'SPECIES'</span>)</span>
<span id="cb32-3"><a href="#cb32-3" aria-hidden="true" tabindex="-1"></a><span class="co"># grab first</span></span>
<span id="cb32-4"><a href="#cb32-4" aria-hidden="true" tabindex="-1"></a>first_result <span class="op">=</span> species_info[<span class="st">'results'</span>][<span class="dv">0</span>]</span>
<span id="cb32-5"><a href="#cb32-5" aria-hidden="true" tabindex="-1"></a>species_key <span class="op">=</span> first_result[<span class="st">'nubKey'</span>]</span>
<span id="cb32-6"><a href="#cb32-6" aria-hidden="true" tabindex="-1"></a>first_result[<span class="st">'species'</span>], species_key</span></code><button title="Copy to Clipboard" class="code-copy-button"><i class="bi"></i></button></pre></div>
</div>
<div id="b84be069" class="cell" data-execution_count="31">
<div class="sourceCode cell-code" id="cb33"><pre class="sourceCode python code-with-copy"><code class="sourceCode python"><span id="cb33-1"><a href="#cb33-1" aria-hidden="true" tabindex="-1"></a><span class="co">## assign species code</span></span>
<span id="cb33-2"><a href="#cb33-2" aria-hidden="true" tabindex="-1"></a>species_key <span class="op">=</span> <span class="dv">2964374</span></span></code><button title="Copy to Clipboard" class="code-copy-button"><i class="bi"></i></button></pre></div>
</div>
<p>Do this once. Had trouble withing loop below so tried outside.</p>
<div class="sourceCode" id="cb34"><pre class="sourceCode python code-with-copy"><code class="sourceCode python"><span id="cb34-1"><a href="#cb34-1" aria-hidden="true" tabindex="-1"></a>gbif_query <span class="op">=</span> occ.download([</span>
<span id="cb34-2"><a href="#cb34-2" aria-hidden="true" tabindex="-1"></a>        <span class="ss">f"speciesKey = </span><span class="sc">{</span>species_key<span class="sc">}</span><span class="ss">"</span>,</span>
<span id="cb34-3"><a href="#cb34-3" aria-hidden="true" tabindex="-1"></a>        <span class="st">"hasCoordinate = True"</span></span>
<span id="cb34-4"><a href="#cb34-4" aria-hidden="true" tabindex="-1"></a>    ])</span>
<span id="cb34-5"><a href="#cb34-5" aria-hidden="true" tabindex="-1"></a>gbif_query</span></code><button title="Copy to Clipboard" class="code-copy-button"><i class="bi"></i></button></pre></div>
<div id="42c72e63" class="cell" data-execution_count="32">
<div class="sourceCode cell-code" id="cb35"><pre class="sourceCode python code-with-copy"><code class="sourceCode python"><span id="cb35-1"><a href="#cb35-1" aria-hidden="true" tabindex="-1"></a>gbif_pattern <span class="op">=</span> os.path.join(gbif_dir, <span class="st">'*.csv'</span>)</span>
<span id="cb35-2"><a href="#cb35-2" aria-hidden="true" tabindex="-1"></a><span class="co">## download once</span></span>
<span id="cb35-3"><a href="#cb35-3" aria-hidden="true" tabindex="-1"></a><span class="cf">if</span> <span class="kw">not</span> glob(gbif_pattern):</span>
<span id="cb35-4"><a href="#cb35-4" aria-hidden="true" tabindex="-1"></a>    <span class="co">#***with error status code 503check your number of active downloads***</span></span>
<span id="cb35-5"><a href="#cb35-5" aria-hidden="true" tabindex="-1"></a>    gbif_query <span class="op">=</span> occ.download([</span>
<span id="cb35-6"><a href="#cb35-6" aria-hidden="true" tabindex="-1"></a>        <span class="ss">f"speciesKey = </span><span class="sc">{</span>species_key<span class="sc">}</span><span class="ss">"</span>,</span>
<span id="cb35-7"><a href="#cb35-7" aria-hidden="true" tabindex="-1"></a>        <span class="st">"hasCoordinate = True"</span></span>
<span id="cb35-8"><a href="#cb35-8" aria-hidden="true" tabindex="-1"></a>    ])</span>
<span id="cb35-9"><a href="#cb35-9" aria-hidden="true" tabindex="-1"></a></span>
<span id="cb35-10"><a href="#cb35-10" aria-hidden="true" tabindex="-1"></a>    <span class="cf">if</span> <span class="kw">not</span> <span class="st">'GBIF_DOWNLOAD_KEY'</span> <span class="kw">in</span> os.environ:</span>
<span id="cb35-11"><a href="#cb35-11" aria-hidden="true" tabindex="-1"></a>        os.environ[<span class="st">'GBIF_DOWNLOAD_KEY'</span>] <span class="op">=</span> gbif_query[<span class="dv">0</span>]</span>
<span id="cb35-12"><a href="#cb35-12" aria-hidden="true" tabindex="-1"></a>        download_key <span class="op">=</span> os.environ[<span class="st">'GBIF_DOWNLOAD_KEY'</span>]</span>
<span id="cb35-13"><a href="#cb35-13" aria-hidden="true" tabindex="-1"></a>        <span class="co"># wait for download to build</span></span>
<span id="cb35-14"><a href="#cb35-14" aria-hidden="true" tabindex="-1"></a>        wait <span class="op">=</span> occ.download_meta(download_key)</span>
<span id="cb35-15"><a href="#cb35-15" aria-hidden="true" tabindex="-1"></a>        <span class="cf">while</span> <span class="kw">not</span> wait <span class="op">==</span> <span class="st">'SUCCEEDED'</span>:</span>
<span id="cb35-16"><a href="#cb35-16" aria-hidden="true" tabindex="-1"></a>            wait <span class="op">=</span> occ.download_meta(download_key)[<span class="st">'status'</span>]</span>
<span id="cb35-17"><a href="#cb35-17" aria-hidden="true" tabindex="-1"></a>            time.sleep(<span class="dv">5</span>)</span>
<span id="cb35-18"><a href="#cb35-18" aria-hidden="true" tabindex="-1"></a></span>
<span id="cb35-19"><a href="#cb35-19" aria-hidden="true" tabindex="-1"></a>    <span class="co"># download data</span></span>
<span id="cb35-20"><a href="#cb35-20" aria-hidden="true" tabindex="-1"></a>    <span class="co"># ***'function' object has no attribute 'get'***</span></span>
<span id="cb35-21"><a href="#cb35-21" aria-hidden="true" tabindex="-1"></a>    download_info <span class="op">=</span> occ.download_get(</span>
<span id="cb35-22"><a href="#cb35-22" aria-hidden="true" tabindex="-1"></a>        os.environ[<span class="st">'GBIF_DOWNLOAD_KEY'</span>],</span>
<span id="cb35-23"><a href="#cb35-23" aria-hidden="true" tabindex="-1"></a>        path <span class="op">=</span> data_dir</span>
<span id="cb35-24"><a href="#cb35-24" aria-hidden="true" tabindex="-1"></a>    )</span>
<span id="cb35-25"><a href="#cb35-25" aria-hidden="true" tabindex="-1"></a>    <span class="co"># unzip</span></span>
<span id="cb35-26"><a href="#cb35-26" aria-hidden="true" tabindex="-1"></a>    <span class="cf">with</span> zipfile.ZipFile(download_info[<span class="st">'path'</span>]) <span class="im">as</span> download_zip:</span>
<span id="cb35-27"><a href="#cb35-27" aria-hidden="true" tabindex="-1"></a>        download_zip.extractall(path <span class="op">=</span> gbif_dir)</span>
<span id="cb35-28"><a href="#cb35-28" aria-hidden="true" tabindex="-1"></a></span>
<span id="cb35-29"><a href="#cb35-29" aria-hidden="true" tabindex="-1"></a><span class="co">## find csv file path</span></span>
<span id="cb35-30"><a href="#cb35-30" aria-hidden="true" tabindex="-1"></a>gbif_path <span class="op">=</span> glob(gbif_pattern)[<span class="dv">0</span>]</span></code><button title="Copy to Clipboard" class="code-copy-button"><i class="bi"></i></button></pre></div>
</div>
</section>
<section id="classes-20-feb-2025" class="level2">
<h2 class="anchored" data-anchor-id="classes-20-feb-2025">Classes 20 Feb 2025</h2>
<ul>
<li><a href="https://canvas.colorado.edu/courses/115453/modules/items/6273791">Katherine Siegel Video on Classes</a></li>
<li><a href="https://github.com/earthlab-education/habitat-suitability-byandell/blob/main/notes_class.qmd">notes_class.qmd</a></li>
<li><a href="https://github.com/byandell-envsys/EarthDataAnalytics/blob/main/references.md#classes">EDA Reference for Python Coding: Classes</a> for references and discussion of classes.</li>
</ul>
<p>A <a href="https://docs.python.org/3/tutorial/classes.html">class</a> is a function with output of an object that has new methods, which are in turn functions defined in the class. In addition, the <code>@property</code> decorator defines attributes for the object. The main use of classes are to:</p>
<ul>
<li>add functionality to class</li>
<li>streamline different functions with same parameters to keep track of metadata</li>
</ul>
<section id="examples" class="level3">
<h3 class="anchored" data-anchor-id="examples">Examples</h3>
<p>Simple example with representer <code>__repr__</code>.</p>
<div id="3c2c48ff" class="cell" data-execution_count="33">
<div class="sourceCode cell-code" id="cb36"><pre class="sourceCode python code-with-copy"><code class="sourceCode python"><span id="cb36-1"><a href="#cb36-1" aria-hidden="true" tabindex="-1"></a><span class="im">import</span> pandas <span class="im">as</span> pd</span>
<span id="cb36-2"><a href="#cb36-2" aria-hidden="true" tabindex="-1"></a><span class="im">import</span> xarray <span class="im">as</span> xr</span>
<span id="cb36-3"><a href="#cb36-3" aria-hidden="true" tabindex="-1"></a></span>
<span id="cb36-4"><a href="#cb36-4" aria-hidden="true" tabindex="-1"></a><span class="kw">class</span> ArrayDataFrame(pd.DataFrame): <span class="co"># inherits pd.DataFrame class</span></span>
<span id="cb36-5"><a href="#cb36-5" aria-hidden="true" tabindex="-1"></a></span>
<span id="cb36-6"><a href="#cb36-6" aria-hidden="true" tabindex="-1"></a>    <span class="kw">def</span> set_array_column(<span class="va">self</span>, arrays):</span>
<span id="cb36-7"><a href="#cb36-7" aria-hidden="true" tabindex="-1"></a>        <span class="va">self</span>[<span class="st">'arrays'</span>] <span class="op">=</span> arrays</span>
<span id="cb36-8"><a href="#cb36-8" aria-hidden="true" tabindex="-1"></a>        <span class="cf">return</span> <span class="va">self</span></span>
<span id="cb36-9"><a href="#cb36-9" aria-hidden="true" tabindex="-1"></a></span>
<span id="cb36-10"><a href="#cb36-10" aria-hidden="true" tabindex="-1"></a>    <span class="kw">def</span> <span class="fu">__repr__</span>(<span class="va">self</span>):</span>
<span id="cb36-11"><a href="#cb36-11" aria-hidden="true" tabindex="-1"></a>        for_printing <span class="op">=</span> <span class="va">self</span>.copy()</span>
<span id="cb36-12"><a href="#cb36-12" aria-hidden="true" tabindex="-1"></a>        for_printing.arrays <span class="op">=</span> [arr.<span class="bu">min</span>() <span class="cf">for</span> arr <span class="kw">in</span> <span class="va">self</span>.arrays]</span>
<span id="cb36-13"><a href="#cb36-13" aria-hidden="true" tabindex="-1"></a>        <span class="cf">return</span> for_printing.<span class="fu">__repr__</span>()</span></code><button title="Copy to Clipboard" class="code-copy-button"><i class="bi"></i></button></pre></div>
</div>
<div id="438fbd85" class="cell" data-execution_count="34">
<div class="sourceCode cell-code" id="cb37"><pre class="sourceCode python code-with-copy"><code class="sourceCode python"><span id="cb37-1"><a href="#cb37-1" aria-hidden="true" tabindex="-1"></a>ArrayDataFrame({<span class="st">'url'</span>: [<span class="st">'https://...'</span>]}).set_array_column([xr.DataArray()])</span></code><button title="Copy to Clipboard" class="code-copy-button"><i class="bi"></i></button></pre></div>
</div>
<p>Show example where class would help.</p>
<div id="fa062aeb" class="cell" data-execution_count="35">
<div class="sourceCode cell-code" id="cb38"><pre class="sourceCode python code-with-copy"><code class="sourceCode python"><span id="cb38-1"><a href="#cb38-1" aria-hidden="true" tabindex="-1"></a><span class="im">import</span> random</span>
<span id="cb38-2"><a href="#cb38-2" aria-hidden="true" tabindex="-1"></a><span class="im">import</span> numpy <span class="im">as</span> np</span>
<span id="cb38-3"><a href="#cb38-3" aria-hidden="true" tabindex="-1"></a><span class="im">import</span> xarray <span class="im">as</span> xr</span>
<span id="cb38-4"><a href="#cb38-4" aria-hidden="true" tabindex="-1"></a></span>
<span id="cb38-5"><a href="#cb38-5" aria-hidden="true" tabindex="-1"></a><span class="kw">def</span> gen_data_array(size<span class="op">=</span><span class="dv">10</span>):</span>
<span id="cb38-6"><a href="#cb38-6" aria-hidden="true" tabindex="-1"></a>    data <span class="op">=</span> (</span>
<span id="cb38-7"><a href="#cb38-7" aria-hidden="true" tabindex="-1"></a>        np.array([random.gauss(<span class="dv">0</span>,<span class="dv">1</span>) <span class="cf">for</span> _ <span class="kw">in</span> <span class="bu">range</span>(size<span class="op">**</span><span class="dv">2</span>)]).reshape(size, size))</span>
<span id="cb38-8"><a href="#cb38-8" aria-hidden="true" tabindex="-1"></a>    data <span class="op">=</span> xr.DataArray(</span>
<span id="cb38-9"><a href="#cb38-9" aria-hidden="true" tabindex="-1"></a>        data <span class="op">=</span> data,</span>
<span id="cb38-10"><a href="#cb38-10" aria-hidden="true" tabindex="-1"></a>        coords <span class="op">=</span> {</span>
<span id="cb38-11"><a href="#cb38-11" aria-hidden="true" tabindex="-1"></a>            <span class="st">'x'</span>: [i <span class="op">*</span> random.uniform(<span class="dv">0</span>,<span class="dv">1</span>) <span class="cf">for</span> i <span class="kw">in</span> <span class="bu">range</span>(size)],</span>
<span id="cb38-12"><a href="#cb38-12" aria-hidden="true" tabindex="-1"></a>            <span class="st">'y'</span>: [i <span class="op">*</span> random.uniform(<span class="dv">0</span>,<span class="dv">1</span>) <span class="cf">for</span> i <span class="kw">in</span> <span class="bu">range</span>(size)]</span>
<span id="cb38-13"><a href="#cb38-13" aria-hidden="true" tabindex="-1"></a>        },</span>
<span id="cb38-14"><a href="#cb38-14" aria-hidden="true" tabindex="-1"></a>        dims<span class="op">=</span>[<span class="st">'x'</span>,<span class="st">'y'</span>]</span>
<span id="cb38-15"><a href="#cb38-15" aria-hidden="true" tabindex="-1"></a>    )</span>
<span id="cb38-16"><a href="#cb38-16" aria-hidden="true" tabindex="-1"></a>    <span class="cf">return</span> data</span></code><button title="Copy to Clipboard" class="code-copy-button"><i class="bi"></i></button></pre></div>
</div>
<div id="edad5cb2" class="cell" data-execution_count="36">
<div class="sourceCode cell-code" id="cb39"><pre class="sourceCode python code-with-copy"><code class="sourceCode python"><span id="cb39-1"><a href="#cb39-1" aria-hidden="true" tabindex="-1"></a>gen_data_array(<span class="dv">10</span>)</span></code><button title="Copy to Clipboard" class="code-copy-button"><i class="bi"></i></button></pre></div>
</div>
<div id="34c71af8" class="cell" data-execution_count="37">
<div class="sourceCode cell-code" id="cb40"><pre class="sourceCode python code-with-copy"><code class="sourceCode python"><span id="cb40-1"><a href="#cb40-1" aria-hidden="true" tabindex="-1"></a>df_len <span class="op">=</span> <span class="dv">10</span></span>
<span id="cb40-2"><a href="#cb40-2" aria-hidden="true" tabindex="-1"></a>my_df <span class="op">=</span> pd.DataFrame({</span>
<span id="cb40-3"><a href="#cb40-3" aria-hidden="true" tabindex="-1"></a>    <span class="st">'id'</span>: <span class="bu">list</span>(<span class="bu">range</span>(df_len)),</span>
<span id="cb40-4"><a href="#cb40-4" aria-hidden="true" tabindex="-1"></a>    <span class="st">'array'</span>: [gen_data_array(<span class="dv">10</span>) <span class="cf">for</span> _ <span class="kw">in</span> <span class="bu">range</span>(df_len)]</span>
<span id="cb40-5"><a href="#cb40-5" aria-hidden="true" tabindex="-1"></a>})</span>
<span id="cb40-6"><a href="#cb40-6" aria-hidden="true" tabindex="-1"></a><span class="bu">print</span>(my_df)</span></code><button title="Copy to Clipboard" class="code-copy-button"><i class="bi"></i></button></pre></div>
</div>
<div id="c4fad7c6" class="cell" data-execution_count="38">
<div class="sourceCode cell-code" id="cb41"><pre class="sourceCode python code-with-copy"><code class="sourceCode python"><span id="cb41-1"><a href="#cb41-1" aria-hidden="true" tabindex="-1"></a><span class="kw">class</span> FunDataFrame(pd.DataFrame):</span>
<span id="cb41-2"><a href="#cb41-2" aria-hidden="true" tabindex="-1"></a>    <span class="co"># represent</span></span>
<span id="cb41-3"><a href="#cb41-3" aria-hidden="true" tabindex="-1"></a>    <span class="kw">def</span> <span class="fu">__repr__</span>(<span class="va">self</span>):</span>
<span id="cb41-4"><a href="#cb41-4" aria-hidden="true" tabindex="-1"></a>        <span class="cf">return</span> <span class="st">'stuff!'</span></span></code><button title="Copy to Clipboard" class="code-copy-button"><i class="bi"></i></button></pre></div>
</div>
<div id="b10d3377" class="cell" data-execution_count="39">
<div class="sourceCode cell-code" id="cb42"><pre class="sourceCode python code-with-copy"><code class="sourceCode python"><span id="cb42-1"><a href="#cb42-1" aria-hidden="true" tabindex="-1"></a>my_df</span></code><button title="Copy to Clipboard" class="code-copy-button"><i class="bi"></i></button></pre></div>
</div>
<p>Add ipython method (under the hood concept)</p>
<div id="a62a2323" class="cell" data-execution_count="40">
<div class="sourceCode cell-code" id="cb43"><pre class="sourceCode python code-with-copy"><code class="sourceCode python"><span id="cb43-1"><a href="#cb43-1" aria-hidden="true" tabindex="-1"></a><span class="kw">class</span> FunDataFrame(pd.DataFrame):</span>
<span id="cb43-2"><a href="#cb43-2" aria-hidden="true" tabindex="-1"></a>    <span class="co"># represent</span></span>
<span id="cb43-3"><a href="#cb43-3" aria-hidden="true" tabindex="-1"></a>    <span class="kw">def</span> <span class="fu">__repr__</span>(<span class="va">self</span>):</span>
<span id="cb43-4"><a href="#cb43-4" aria-hidden="true" tabindex="-1"></a>        <span class="cf">return</span> <span class="st">'stuff!'</span></span>
<span id="cb43-5"><a href="#cb43-5" aria-hidden="true" tabindex="-1"></a>    <span class="co"># ipython method</span></span>
<span id="cb43-6"><a href="#cb43-6" aria-hidden="true" tabindex="-1"></a>    <span class="kw">def</span> _repr_html_(<span class="va">self</span>):</span>
<span id="cb43-7"><a href="#cb43-7" aria-hidden="true" tabindex="-1"></a>        <span class="cf">return</span> <span class="st">'more stuff!!!'</span></span></code><button title="Copy to Clipboard" class="code-copy-button"><i class="bi"></i></button></pre></div>
</div>
<div id="cce46510" class="cell" data-execution_count="41">
<div class="sourceCode cell-code" id="cb44"><pre class="sourceCode python code-with-copy"><code class="sourceCode python"><span id="cb44-1"><a href="#cb44-1" aria-hidden="true" tabindex="-1"></a>my_df</span></code><button title="Copy to Clipboard" class="code-copy-button"><i class="bi"></i></button></pre></div>
</div>
<div id="8b045467" class="cell" data-execution_count="42">
<div class="sourceCode cell-code" id="cb45"><pre class="sourceCode python code-with-copy"><code class="sourceCode python"><span id="cb45-1"><a href="#cb45-1" aria-hidden="true" tabindex="-1"></a><span class="kw">class</span> FunDataFrame(pd.DataFrame):</span>
<span id="cb45-2"><a href="#cb45-2" aria-hidden="true" tabindex="-1"></a></span>
<span id="cb45-3"><a href="#cb45-3" aria-hidden="true" tabindex="-1"></a>    <span class="co"># attribute to make a dataframe</span></span>
<span id="cb45-4"><a href="#cb45-4" aria-hidden="true" tabindex="-1"></a>    <span class="at">@property</span></span>
<span id="cb45-5"><a href="#cb45-5" aria-hidden="true" tabindex="-1"></a>    <span class="kw">def</span> _df_for_repr_(<span class="va">self</span>):</span>
<span id="cb45-6"><a href="#cb45-6" aria-hidden="true" tabindex="-1"></a>        df <span class="op">=</span> <span class="va">self</span>.drop(columns <span class="op">=</span> [<span class="st">'array'</span>]).copy()</span>
<span id="cb45-7"><a href="#cb45-7" aria-hidden="true" tabindex="-1"></a>        <span class="cf">return</span> df</span>
<span id="cb45-8"><a href="#cb45-8" aria-hidden="true" tabindex="-1"></a>    <span class="co"># represent</span></span>
<span id="cb45-9"><a href="#cb45-9" aria-hidden="true" tabindex="-1"></a>    <span class="kw">def</span> <span class="fu">__repr__</span>(<span class="va">self</span>):</span>
<span id="cb45-10"><a href="#cb45-10" aria-hidden="true" tabindex="-1"></a>        <span class="cf">return</span> <span class="va">self</span>._df_for_repr_.<span class="fu">__repr__</span>()</span>
<span id="cb45-11"><a href="#cb45-11" aria-hidden="true" tabindex="-1"></a>    <span class="co"># ipython method</span></span>
<span id="cb45-12"><a href="#cb45-12" aria-hidden="true" tabindex="-1"></a>    <span class="kw">def</span> _repr_html_(<span class="va">self</span>):</span>
<span id="cb45-13"><a href="#cb45-13" aria-hidden="true" tabindex="-1"></a>        <span class="cf">return</span> <span class="va">self</span>._df_for_repr_._repr_html_()</span></code><button title="Copy to Clipboard" class="code-copy-button"><i class="bi"></i></button></pre></div>
</div>
<div id="c20117d2" class="cell" data-execution_count="43">
<div class="sourceCode cell-code" id="cb46"><pre class="sourceCode python code-with-copy"><code class="sourceCode python"><span id="cb46-1"><a href="#cb46-1" aria-hidden="true" tabindex="-1"></a>my_df</span></code><button title="Copy to Clipboard" class="code-copy-button"><i class="bi"></i></button></pre></div>
</div>
<p>Set up my dataframe class to show what I want</p>
<div id="1ab10e6d" class="cell" data-execution_count="44">
<div class="sourceCode cell-code" id="cb47"><pre class="sourceCode python code-with-copy"><code class="sourceCode python"><span id="cb47-1"><a href="#cb47-1" aria-hidden="true" tabindex="-1"></a><span class="kw">class</span> FunDataFrame(pd.DataFrame):</span>
<span id="cb47-2"><a href="#cb47-2" aria-hidden="true" tabindex="-1"></a></span>
<span id="cb47-3"><a href="#cb47-3" aria-hidden="true" tabindex="-1"></a>    <span class="co"># define array_types (does not appear to be used yet) </span></span>
<span id="cb47-4"><a href="#cb47-4" aria-hidden="true" tabindex="-1"></a>    array_types <span class="op">=</span> [xr.DataArray]</span>
<span id="cb47-5"><a href="#cb47-5" aria-hidden="true" tabindex="-1"></a></span>
<span id="cb47-6"><a href="#cb47-6" aria-hidden="true" tabindex="-1"></a>    <span class="co"># attribute to return `array_cols`</span></span>
<span id="cb47-7"><a href="#cb47-7" aria-hidden="true" tabindex="-1"></a>    <span class="at">@property</span></span>
<span id="cb47-8"><a href="#cb47-8" aria-hidden="true" tabindex="-1"></a>    <span class="kw">def</span> array_cols(<span class="va">self</span>):</span>
<span id="cb47-9"><a href="#cb47-9" aria-hidden="true" tabindex="-1"></a>        array_cols <span class="op">=</span> []</span>
<span id="cb47-10"><a href="#cb47-10" aria-hidden="true" tabindex="-1"></a>        <span class="cf">for</span> col <span class="kw">in</span> <span class="va">self</span>:</span>
<span id="cb47-11"><a href="#cb47-11" aria-hidden="true" tabindex="-1"></a>            <span class="cf">if</span> <span class="bu">type</span>(<span class="va">self</span>[col][<span class="dv">0</span>]) <span class="op">==</span> xr.DataArray:</span>
<span id="cb47-12"><a href="#cb47-12" aria-hidden="true" tabindex="-1"></a>                array_cols.append(col)</span>
<span id="cb47-13"><a href="#cb47-13" aria-hidden="true" tabindex="-1"></a>                <span class="cf">return</span> array_cols</span>
<span id="cb47-14"><a href="#cb47-14" aria-hidden="true" tabindex="-1"></a></span>
<span id="cb47-15"><a href="#cb47-15" aria-hidden="true" tabindex="-1"></a>    <span class="co"># more complicated attribute</span></span>
<span id="cb47-16"><a href="#cb47-16" aria-hidden="true" tabindex="-1"></a>    <span class="at">@property</span></span>
<span id="cb47-17"><a href="#cb47-17" aria-hidden="true" tabindex="-1"></a>    <span class="kw">def</span> _df_for_repr_(<span class="va">self</span>):</span>
<span id="cb47-18"><a href="#cb47-18" aria-hidden="true" tabindex="-1"></a>        df <span class="op">=</span> <span class="va">self</span>.drop(columns <span class="op">=</span> <span class="va">self</span>.array_cols).copy()</span>
<span id="cb47-19"><a href="#cb47-19" aria-hidden="true" tabindex="-1"></a>        <span class="cf">for</span> array_col <span class="kw">in</span> <span class="va">self</span>.array_cols:</span>
<span id="cb47-20"><a href="#cb47-20" aria-hidden="true" tabindex="-1"></a>            arr_str_list <span class="op">=</span> []</span>
<span id="cb47-21"><a href="#cb47-21" aria-hidden="true" tabindex="-1"></a>            <span class="cf">for</span> arr <span class="kw">in</span> <span class="va">self</span>[array_col]:</span>
<span id="cb47-22"><a href="#cb47-22" aria-hidden="true" tabindex="-1"></a>                arr_min <span class="op">=</span> <span class="bu">round</span>(<span class="bu">float</span>(arr.x.<span class="bu">min</span>()), <span class="dv">2</span>)</span>
<span id="cb47-23"><a href="#cb47-23" aria-hidden="true" tabindex="-1"></a>                arr_max <span class="op">=</span> <span class="bu">round</span>(<span class="bu">float</span>(arr.x.<span class="bu">max</span>()), <span class="dv">2</span>)</span>
<span id="cb47-24"><a href="#cb47-24" aria-hidden="true" tabindex="-1"></a>                arr_str_list.append(</span>
<span id="cb47-25"><a href="#cb47-25" aria-hidden="true" tabindex="-1"></a>                    <span class="ss">f'DataArray(x (</span><span class="sc">{</span>arr_min<span class="sc">}</span><span class="ss">, </span><span class="sc">{</span>arr_max<span class="sc">}</span><span class="ss">))'</span></span>
<span id="cb47-26"><a href="#cb47-26" aria-hidden="true" tabindex="-1"></a>                )</span>
<span id="cb47-27"><a href="#cb47-27" aria-hidden="true" tabindex="-1"></a>            df[array_col] <span class="op">=</span> arr_str_list</span>
<span id="cb47-28"><a href="#cb47-28" aria-hidden="true" tabindex="-1"></a>            <span class="co">#df[array_col] = ['DataArray' for _ in range(len(df))]</span></span>
<span id="cb47-29"><a href="#cb47-29" aria-hidden="true" tabindex="-1"></a>        <span class="cf">return</span> df</span>
<span id="cb47-30"><a href="#cb47-30" aria-hidden="true" tabindex="-1"></a>    </span>
<span id="cb47-31"><a href="#cb47-31" aria-hidden="true" tabindex="-1"></a>    <span class="co"># represent</span></span>
<span id="cb47-32"><a href="#cb47-32" aria-hidden="true" tabindex="-1"></a>    <span class="kw">def</span> <span class="fu">__repr__</span>(<span class="va">self</span>):</span>
<span id="cb47-33"><a href="#cb47-33" aria-hidden="true" tabindex="-1"></a>        <span class="cf">return</span> <span class="va">self</span>._df_for_repr_.<span class="fu">__repr__</span>()</span>
<span id="cb47-34"><a href="#cb47-34" aria-hidden="true" tabindex="-1"></a>    <span class="co"># ipython method</span></span>
<span id="cb47-35"><a href="#cb47-35" aria-hidden="true" tabindex="-1"></a>    <span class="kw">def</span> _repr_html_(<span class="va">self</span>):</span>
<span id="cb47-36"><a href="#cb47-36" aria-hidden="true" tabindex="-1"></a>        <span class="cf">return</span> <span class="va">self</span>._df_for_repr_._repr_html_()</span></code><button title="Copy to Clipboard" class="code-copy-button"><i class="bi"></i></button></pre></div>
</div>
<div id="6321d3c4" class="cell" data-execution_count="45">
<div class="sourceCode cell-code" id="cb48"><pre class="sourceCode python code-with-copy"><code class="sourceCode python"><span id="cb48-1"><a href="#cb48-1" aria-hidden="true" tabindex="-1"></a>my_df <span class="op">=</span> FunDataFrame({</span>
<span id="cb48-2"><a href="#cb48-2" aria-hidden="true" tabindex="-1"></a>    <span class="st">'id'</span>: <span class="bu">list</span>(<span class="bu">range</span>(df_len)),</span>
<span id="cb48-3"><a href="#cb48-3" aria-hidden="true" tabindex="-1"></a>    <span class="st">'array'</span>: [gen_data_array(<span class="dv">10</span>) <span class="cf">for</span> _ <span class="kw">in</span> <span class="bu">range</span>(df_len)],</span>
<span id="cb48-4"><a href="#cb48-4" aria-hidden="true" tabindex="-1"></a>    <span class="st">'array2'</span>: [gen_data_array(<span class="dv">10</span>) <span class="cf">for</span> _ <span class="kw">in</span> <span class="bu">range</span>(df_len)]})</span>
<span id="cb48-5"><a href="#cb48-5" aria-hidden="true" tabindex="-1"></a>my_df</span></code><button title="Copy to Clipboard" class="code-copy-button"><i class="bi"></i></button></pre></div>
</div>
</section>
</section>

</main>
<!-- /main column -->
<script id="quarto-html-after-body" type="application/javascript">
window.document.addEventListener("DOMContentLoaded", function (event) {
  const toggleBodyColorMode = (bsSheetEl) => {
    const mode = bsSheetEl.getAttribute("data-mode");
    const bodyEl = window.document.querySelector("body");
    if (mode === "dark") {
      bodyEl.classList.add("quarto-dark");
      bodyEl.classList.remove("quarto-light");
    } else {
      bodyEl.classList.add("quarto-light");
      bodyEl.classList.remove("quarto-dark");
    }
  }
  const toggleBodyColorPrimary = () => {
    const bsSheetEl = window.document.querySelector("link#quarto-bootstrap");
    if (bsSheetEl) {
      toggleBodyColorMode(bsSheetEl);
    }
  }
  toggleBodyColorPrimary();  
  const icon = "";
  const anchorJS = new window.AnchorJS();
  anchorJS.options = {
    placement: 'right',
    icon: icon
  };
  anchorJS.add('.anchored');
  const isCodeAnnotation = (el) => {
    for (const clz of el.classList) {
      if (clz.startsWith('code-annotation-')) {                     
        return true;
      }
    }
    return false;
  }
  const onCopySuccess = function(e) {
    // button target
    const button = e.trigger;
    // don't keep focus
    button.blur();
    // flash "checked"
    button.classList.add('code-copy-button-checked');
    var currentTitle = button.getAttribute("title");
    button.setAttribute("title", "Copied!");
    let tooltip;
    if (window.bootstrap) {
      button.setAttribute("data-bs-toggle", "tooltip");
      button.setAttribute("data-bs-placement", "left");
      button.setAttribute("data-bs-title", "Copied!");
      tooltip = new bootstrap.Tooltip(button, 
        { trigger: "manual", 
          customClass: "code-copy-button-tooltip",
          offset: [0, -8]});
      tooltip.show();    
    }
    setTimeout(function() {
      if (tooltip) {
        tooltip.hide();
        button.removeAttribute("data-bs-title");
        button.removeAttribute("data-bs-toggle");
        button.removeAttribute("data-bs-placement");
      }
      button.setAttribute("title", currentTitle);
      button.classList.remove('code-copy-button-checked');
    }, 1000);
    // clear code selection
    e.clearSelection();
  }
  const getTextToCopy = function(trigger) {
      const codeEl = trigger.previousElementSibling.cloneNode(true);
      for (const childEl of codeEl.children) {
        if (isCodeAnnotation(childEl)) {
          childEl.remove();
        }
      }
      return codeEl.innerText;
  }
  const clipboard = new window.ClipboardJS('.code-copy-button:not([data-in-quarto-modal])', {
    text: getTextToCopy
  });
  clipboard.on('success', onCopySuccess);
  if (window.document.getElementById('quarto-embedded-source-code-modal')) {
    // For code content inside modals, clipBoardJS needs to be initialized with a container option
    // TODO: Check when it could be a function (https://github.com/zenorocha/clipboard.js/issues/860)
    const clipboardModal = new window.ClipboardJS('.code-copy-button[data-in-quarto-modal]', {
      text: getTextToCopy,
      container: window.document.getElementById('quarto-embedded-source-code-modal')
    });
    clipboardModal.on('success', onCopySuccess);
  }
    var localhostRegex = new RegExp(/^(?:http|https):\/\/localhost\:?[0-9]*\//);
    var mailtoRegex = new RegExp(/^mailto:/);
      var filterRegex = new RegExp('/' + window.location.host + '/');
    var isInternal = (href) => {
        return filterRegex.test(href) || localhostRegex.test(href) || mailtoRegex.test(href);
    }
    // Inspect non-navigation links and adorn them if external
 	var links = window.document.querySelectorAll('a[href]:not(.nav-link):not(.navbar-brand):not(.toc-action):not(.sidebar-link):not(.sidebar-item-toggle):not(.pagination-link):not(.no-external):not([aria-hidden]):not(.dropdown-item):not(.quarto-navigation-tool):not(.about-link)');
    for (var i=0; i<links.length; i++) {
      const link = links[i];
      if (!isInternal(link.href)) {
        // undo the damage that might have been done by quarto-nav.js in the case of
        // links that we want to consider external
        if (link.dataset.originalHref !== undefined) {
          link.href = link.dataset.originalHref;
        }
      }
    }
  function tippyHover(el, contentFn, onTriggerFn, onUntriggerFn) {
    const config = {
      allowHTML: true,
      maxWidth: 500,
      delay: 100,
      arrow: false,
      appendTo: function(el) {
          return el.parentElement;
      },
      interactive: true,
      interactiveBorder: 10,
      theme: 'quarto',
      placement: 'bottom-start',
    };
    if (contentFn) {
      config.content = contentFn;
    }
    if (onTriggerFn) {
      config.onTrigger = onTriggerFn;
    }
    if (onUntriggerFn) {
      config.onUntrigger = onUntriggerFn;
    }
    window.tippy(el, config); 
  }
  const noterefs = window.document.querySelectorAll('a[role="doc-noteref"]');
  for (var i=0; i<noterefs.length; i++) {
    const ref = noterefs[i];
    tippyHover(ref, function() {
      // use id or data attribute instead here
      let href = ref.getAttribute('data-footnote-href') || ref.getAttribute('href');
      try { href = new URL(href).hash; } catch {}
      const id = href.replace(/^#\/?/, "");
      const note = window.document.getElementById(id);
      if (note) {
        return note.innerHTML;
      } else {
        return "";
      }
    });
  }
  const xrefs = window.document.querySelectorAll('a.quarto-xref');
  const processXRef = (id, note) => {
    // Strip column container classes
    const stripColumnClz = (el) => {
      el.classList.remove("page-full", "page-columns");
      if (el.children) {
        for (const child of el.children) {
          stripColumnClz(child);
        }
      }
    }
    stripColumnClz(note)
    if (id === null || id.startsWith('sec-')) {
      // Special case sections, only their first couple elements
      const container = document.createElement("div");
      if (note.children && note.children.length > 2) {
        container.appendChild(note.children[0].cloneNode(true));
        for (let i = 1; i < note.children.length; i++) {
          const child = note.children[i];
          if (child.tagName === "P" && child.innerText === "") {
            continue;
          } else {
            container.appendChild(child.cloneNode(true));
            break;
          }
        }
        if (window.Quarto?.typesetMath) {
          window.Quarto.typesetMath(container);
        }
        return container.innerHTML
      } else {
        if (window.Quarto?.typesetMath) {
          window.Quarto.typesetMath(note);
        }
        return note.innerHTML;
      }
    } else {
      // Remove any anchor links if they are present
      const anchorLink = note.querySelector('a.anchorjs-link');
      if (anchorLink) {
        anchorLink.remove();
      }
      if (window.Quarto?.typesetMath) {
        window.Quarto.typesetMath(note);
      }
      // TODO in 1.5, we should make sure this works without a callout special case
      if (note.classList.contains("callout")) {
        return note.outerHTML;
      } else {
        return note.innerHTML;
      }
    }
  }
  for (var i=0; i<xrefs.length; i++) {
    const xref = xrefs[i];
    tippyHover(xref, undefined, function(instance) {
      instance.disable();
      let url = xref.getAttribute('href');
      let hash = undefined; 
      if (url.startsWith('#')) {
        hash = url;
      } else {
        try { hash = new URL(url).hash; } catch {}
      }
      if (hash) {
        const id = hash.replace(/^#\/?/, "");
        const note = window.document.getElementById(id);
        if (note !== null) {
          try {
            const html = processXRef(id, note.cloneNode(true));
            instance.setContent(html);
          } finally {
            instance.enable();
            instance.show();
          }
        } else {
          // See if we can fetch this
          fetch(url.split('#')[0])
          .then(res => res.text())
          .then(html => {
            const parser = new DOMParser();
            const htmlDoc = parser.parseFromString(html, "text/html");
            const note = htmlDoc.getElementById(id);
            if (note !== null) {
              const html = processXRef(id, note);
              instance.setContent(html);
            } 
          }).finally(() => {
            instance.enable();
            instance.show();
          });
        }
      } else {
        // See if we can fetch a full url (with no hash to target)
        // This is a special case and we should probably do some content thinning / targeting
        fetch(url)
        .then(res => res.text())
        .then(html => {
          const parser = new DOMParser();
          const htmlDoc = parser.parseFromString(html, "text/html");
          const note = htmlDoc.querySelector('main.content');
          if (note !== null) {
            // This should only happen for chapter cross references
            // (since there is no id in the URL)
            // remove the first header
            if (note.children.length > 0 && note.children[0].tagName === "HEADER") {
              note.children[0].remove();
            }
            const html = processXRef(null, note);
            instance.setContent(html);
          } 
        }).finally(() => {
          instance.enable();
          instance.show();
        });
      }
    }, function(instance) {
    });
  }
      let selectedAnnoteEl;
      const selectorForAnnotation = ( cell, annotation) => {
        let cellAttr = 'data-code-cell="' + cell + '"';
        let lineAttr = 'data-code-annotation="' +  annotation + '"';
        const selector = 'span[' + cellAttr + '][' + lineAttr + ']';
        return selector;
      }
      const selectCodeLines = (annoteEl) => {
        const doc = window.document;
        const targetCell = annoteEl.getAttribute("data-target-cell");
        const targetAnnotation = annoteEl.getAttribute("data-target-annotation");
        const annoteSpan = window.document.querySelector(selectorForAnnotation(targetCell, targetAnnotation));
        const lines = annoteSpan.getAttribute("data-code-lines").split(",");
        const lineIds = lines.map((line) => {
          return targetCell + "-" + line;
        })
        let top = null;
        let height = null;
        let parent = null;
        if (lineIds.length > 0) {
            //compute the position of the single el (top and bottom and make a div)
            const el = window.document.getElementById(lineIds[0]);
            top = el.offsetTop;
            height = el.offsetHeight;
            parent = el.parentElement.parentElement;
          if (lineIds.length > 1) {
            const lastEl = window.document.getElementById(lineIds[lineIds.length - 1]);
            const bottom = lastEl.offsetTop + lastEl.offsetHeight;
            height = bottom - top;
          }
          if (top !== null && height !== null && parent !== null) {
            // cook up a div (if necessary) and position it 
            let div = window.document.getElementById("code-annotation-line-highlight");
            if (div === null) {
              div = window.document.createElement("div");
              div.setAttribute("id", "code-annotation-line-highlight");
              div.style.position = 'absolute';
              parent.appendChild(div);
            }
            div.style.top = top - 2 + "px";
            div.style.height = height + 4 + "px";
            div.style.left = 0;
            let gutterDiv = window.document.getElementById("code-annotation-line-highlight-gutter");
            if (gutterDiv === null) {
              gutterDiv = window.document.createElement("div");
              gutterDiv.setAttribute("id", "code-annotation-line-highlight-gutter");
              gutterDiv.style.position = 'absolute';
              const codeCell = window.document.getElementById(targetCell);
              const gutter = codeCell.querySelector('.code-annotation-gutter');
              gutter.appendChild(gutterDiv);
            }
            gutterDiv.style.top = top - 2 + "px";
            gutterDiv.style.height = height + 4 + "px";
          }
          selectedAnnoteEl = annoteEl;
        }
      };
      const unselectCodeLines = () => {
        const elementsIds = ["code-annotation-line-highlight", "code-annotation-line-highlight-gutter"];
        elementsIds.forEach((elId) => {
          const div = window.document.getElementById(elId);
          if (div) {
            div.remove();
          }
        });
        selectedAnnoteEl = undefined;
      };
        // Handle positioning of the toggle
    window.addEventListener(
      "resize",
      throttle(() => {
        elRect = undefined;
        if (selectedAnnoteEl) {
          selectCodeLines(selectedAnnoteEl);
        }
      }, 10)
    );
    function throttle(fn, ms) {
    let throttle = false;
    let timer;
      return (...args) => {
        if(!throttle) { // first call gets through
            fn.apply(this, args);
            throttle = true;
        } else { // all the others get throttled
            if(timer) clearTimeout(timer); // cancel #2
            timer = setTimeout(() => {
              fn.apply(this, args);
              timer = throttle = false;
            }, ms);
        }
      };
    }
      // Attach click handler to the DT
      const annoteDls = window.document.querySelectorAll('dt[data-target-cell]');
      for (const annoteDlNode of annoteDls) {
        annoteDlNode.addEventListener('click', (event) => {
          const clickedEl = event.target;
          if (clickedEl !== selectedAnnoteEl) {
            unselectCodeLines();
            const activeEl = window.document.querySelector('dt[data-target-cell].code-annotation-active');
            if (activeEl) {
              activeEl.classList.remove('code-annotation-active');
            }
            selectCodeLines(clickedEl);
            clickedEl.classList.add('code-annotation-active');
          } else {
            // Unselect the line
            unselectCodeLines();
            clickedEl.classList.remove('code-annotation-active');
          }
        });
      }
  const findCites = (el) => {
    const parentEl = el.parentElement;
    if (parentEl) {
      const cites = parentEl.dataset.cites;
      if (cites) {
        return {
          el,
          cites: cites.split(' ')
        };
      } else {
        return findCites(el.parentElement)
      }
    } else {
      return undefined;
    }
  };
  var bibliorefs = window.document.querySelectorAll('a[role="doc-biblioref"]');
  for (var i=0; i<bibliorefs.length; i++) {
    const ref = bibliorefs[i];
    const citeInfo = findCites(ref);
    if (citeInfo) {
      tippyHover(citeInfo.el, function() {
        var popup = window.document.createElement('div');
        citeInfo.cites.forEach(function(cite) {
          var citeDiv = window.document.createElement('div');
          citeDiv.classList.add('hanging-indent');
          citeDiv.classList.add('csl-entry');
          var biblioDiv = window.document.getElementById('ref-' + cite);
          if (biblioDiv) {
            citeDiv.innerHTML = biblioDiv.innerHTML;
          }
          popup.appendChild(citeDiv);
        });
        return popup.innerHTML;
      });
    }
  }
});
</script>
</div> <!-- /content -->




</body></html>