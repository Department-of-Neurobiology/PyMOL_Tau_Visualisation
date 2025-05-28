# === Define custom colors ===
set_color pastel_orange = [218/255.0, 118/255.0, 53/255.0]
set_color pastel_orange_light = [219/255.0, 153/255.0, 90/255.0]

set_color good_green = [70/255.0, 124/255.0, 41/255.0]
set_color good_blue = [35/255.0, 78/255.0, 135/255.0]
set_color good_blue_light = [150/255.0, 165/255.0, 185/255.0]

# === Paths and files ===
load C:\Users\NITru\OneDrive\Documents\PhD_work\Projects\NT_projects\DONE_projects\done_Review_tau_more_than_cytoskeletal_protein\figures_1_2_tau_structure_with_MT\hTau441wt_state_5_from_modified_pdb_version_with_sidechain_SCWRL.pdb

# === Define selections ===
select nterm, resi 1-171
select PRR, resi 172-243
select MBR, resi 244-368
select cterm, resi 369-442

# === General settings ===
hide all
toggle surface, met
show surface, all
# show mesh, binding_site

# Set transparency if needed
# set transparency, 0.2, tau_core
# set mesh_width, 0.5, binding_site

# === Apply colors ===
color good_green, nterm
# color good_blue_light, PRR
color grey70, PRR
color good_blue, MBR
# color good_blue_light, cterm
color grey70, cterm

# === Set view, background, etc. ===
zoom all
center all   
zoom all, -60

# Scene of MT with tau
# set_view (\
#    -0.007880771,   -0.864057839,    0.503331423,\
#     0.001372296,    0.503338873,    0.864088356,\
#    -0.999965966,    0.007500647,   -0.002780669,\
#     0.000487328,    0.000094891, -1030.805541992,\
#    42.327560425,  134.679244995,  307.071350098,\
#   101.607788086, 1960.032470703,  -49.999996185 )

# Single tau
# First try
# set_view (\
#      0.189049765,    0.773191392,    0.605333507,\
#      0.411342233,    0.497401655,   -0.763797760,\
#     -0.891654491,    0.393392503,   -0.224010020,\
#     -0.002041290,    0.000169665, -667.888549805,\
#    -21.664424896,   24.457353592, -165.326232910,\
#    179.599609375, 1156.195312500,  -20.000000000 )

set_view (\
     0.123416334,    0.978607059,    0.164581403,\
    -0.105858341,    0.177883059,   -0.978338480,\
    -0.986683965,    0.103321500,    0.125550479,\
    -0.002059542,    0.000939846, -780.456359863,\
   -23.169580460,   23.090576172, -164.663131714,\
   292.151916504, 1268.747802734,  -20.000000000 )

# === Render ===
bg_color white
set ray_opaque_background, 0
# or off
# set antialias, 2
# set ray_trace_mode, 0
set ray_trace_fog = 1
set ambient, 0.3
set spec_count, 3
ray 1400, 870

png C:\Users\NITru\OneDrive\Documents\PhD_work\Projects\NT_projects\DONE_projects\done_Review_tau_more_than_cytoskeletal_protein\figures_1_2_tau_structure_with_MT\20250406_extra_figures_RB\Figure_02a.png, dpi=300
