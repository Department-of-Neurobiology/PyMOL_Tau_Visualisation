# === Define custom colors ===
set_color pastel_orange = [218/255.0, 118/255.0, 53/255.0]
set_color pastel_orange_light = [219/255.0, 153/255.0, 90/255.0]

set_color good_green = [70/255.0, 124/255.0, 41/255.0]
set_color good_blue = [35/255.0, 78/255.0, 135/255.0]
set_color good_blue_light = [150/255.0, 165/255.0, 185/255.0]

set_color burgundy_red = [128/255.0, 0/255.0, 32/255.0]

# === Paths and files ===
fetch 5o3L, type=pdb
set seq_view, 1

# === Define selections ===
# select cterm, resi 369-442

# === Apply colors ===
color good_blue, all

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
     0.809309363,   -0.563116074,    0.167086944,\
     0.558985054,    0.825742662,    0.075392872,\
    -0.180425793,    0.032382999,    0.983055294,\
    -0.000121266,   -0.000020414, -202.494659424,\
   183.050262451,  142.413452148,  145.318634033,\
  -7186.566894531, 7591.561523438,  -20.000000000 )
   
# === Render ===
bg_color white
set ray_opaque_background, 0
# or off
# set antialias, 2
# set ray_trace_mode, 0
set ray_trace_fog = 1
set ambient, 0.3
set spec_count, 3
ray 1600, 900

png C:\Users\NITru\OneDrive\Documents\PhD_work\Projects\NT_projects\DONE_projects\done_Review_tau_more_than_cytoskeletal_protein\figures_1_2_tau_structure_with_MT\20250406_extra_figures_RB\Figure_tau_PHF_AD.png, dpi=300
