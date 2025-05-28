# === Paths and files ===
load C:\Users\NITru\OneDrive\Documents\PhD_work\Projects\NT_projects\DONE_projects\done_Review_tau_more_than_cytoskeletal_protein\figures_1_2_tau_structure_with_MT\hTau441wt_state_5_from_modified_pdb_version_with_sidechain_SCWRL.pdb

# Run plugin APBS with default
# install libraries - only works on license version not open-source
# conda install -c conda-forge apbs pdb2pqr

# For open_source:
# PyMOL -> open model -> Plugins -> APBS Electrostatics -> Advanced configuration -> C:\\Users\\NITru\\Tools\\APBS-3.0.0\\bin\\apbs.exe (downloaded from https://github.com/Electrostatics/apbs-pdb2pqr/releases)





# === Define custom colors ===
set_color pastel_orange = [218/255.0, 118/255.0, 53/255.0]
set_color pastel_orange_light = [219/255.0, 153/255.0, 90/255.0]

set_color good_green = [70/255.0, 124/255.0, 41/255.0]
set_color good_blue = [35/255.0, 78/255.0, 135/255.0]
set_color good_blue_light = [150/255.0, 165/255.0, 185/255.0]

# === Define selections ===
# Electrostatic potential surface
select PRR_run01, resi 172-243 and prep*
select cterm_run01, resi 369-441 and prep*

# === General settings ===
hide all
# toggle surface, met
# show surface, all
# show mesh, binding_site

# Set transparency if needed
# set transparency, 0.2, tau_core
# set mesh_width, 0.5, binding_site

show surface, prepared01

# === Apply colors ===
# Electrostatic potential surface - has to be by surface_color to overwrite
set surface_color, grey70, PRR_run01
set surface_color, grey70, cterm_run01

# === Set view, background, etc. ===
zoom all
center all   
zoom all, -60

# Single tau
set_view (\
     0.123416334,    0.978607059,    0.164581403,\
    -0.105858341,    0.177883059,   -0.978338480,\
    -0.986683965,    0.103321500,    0.125550479,\
    -0.002059542,    0.000939846, -780.456359863,\
   -23.169580460,   23.090576172, -164.663131714,\
   292.151916504, 1268.747802734,  -20.000000000 )
  
disable apbs_ramp01
 
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


png C:\Users\NITru\OneDrive\Documents\PhD_work\Projects\NT_projects\DONE_projects\done_Review_tau_more_than_cytoskeletal_protein\figures_1_2_tau_structure_with_MT\20250406_extra_figures_RB\Figure_02b.png, dpi=300
