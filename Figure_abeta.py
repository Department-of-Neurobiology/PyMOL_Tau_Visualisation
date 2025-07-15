# === Define custom colors ===
set_color pastel_orange = [218/255.0, 118/255.0, 53/255.0]
set_color pastel_orange_light = [219/255.0, 153/255.0, 90/255.0]

set_color good_green = [70/255.0, 124/255.0, 41/255.0]
set_color good_blue = [35/255.0, 78/255.0, 135/255.0]
set_color good_blue_light = [150/255.0, 165/255.0, 185/255.0]

set_color burgundy_red = [128/255.0, 0/255.0, 32/255.0]

# === Paths and files ===
fetch 2mxu, type=pdb

set seq_view, 1

# === Define selections ===

# select cterm, resi 369-442

# === Apply colors ===

color burgundy_red, all

# === General settings ===
hide everything, all
show cartoon, all
show surface, all
set transparency, 0.5, all

# === Set view, background, etc. ===
zoom all
center all   
zoom all, -60

# Aggregates
set_view (\
    -0.397292703,   -0.778250456,    0.486290157,\
    -0.209239453,   -0.439124048,   -0.873717546,\
     0.893517494,   -0.448873043,    0.011622384,\
     0.000004061,    0.000029147, -174.314743042,\
     2.494416714,    1.704046249,    0.750788450,\
  -1914.202880859, 2262.832763672,  -20.000000000 )
   
# === Render ===
bg_color white
set ray_opaque_background, 0
# or off
# set antialias, 2
# set ray_trace_mode, 0
set ray_trace_fog = 1
set ambient, 0.3
set spec_count, 3
ray 1600, 1200

png C:\Users\NITru\OneDrive\Documents\PhD_work\Projects\NT_projects\DONE_projects\done_Review_tau_more_than_cytoskeletal_protein\figures_1_2_tau_structure_with_MT\20250406_extra_figures_RB\Figure_abeta.png, dpi=300
