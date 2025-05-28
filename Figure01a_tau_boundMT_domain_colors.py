# === Define custom colors ===
set_color pastel_orange = [218/255.0, 118/255.0, 53/255.0]
set_color pastel_orange_light = [219/255.0, 153/255.0, 90/255.0]
set_color vanilla = [240/255.0, 240/255.0, 220/255.0]
# old [214/255.0, 212/255.0, 160/255.0]

set_color good_green = [70/255.0, 124/255.0, 41/255.0]
set_color good_blue = [35/255.0, 78/255.0, 135/255.0]
set_color good_blue_light = [150/255.0, 165/255.0, 185/255.0]

# === Paths and files ===
# load C:\Users\NITru\OneDrive\Documents\PhD_work\Projects\NT_projects\DONE_projects\done_Review_tau_more_than_cytoskeletal_protein\figures_1_2_tau_structure_with_MT\hTau441wt_state_5_from_modified_pdb_version_with_sidechain_SCWRL.pdb

# === General settings ===
hide all
show surface, all
color vanilla, all
set transparency, 0.0, all
# IMPORTANT not working
hide surface, hTau441wt_state_5_from_modified_pdb_version_with_sidechain_SCWRL_4
hide surface, hTau441wt_state_5_from_modified_pdb_version_with_sidechain_SCWRL_5
# show mesh, binding_site

# Set transparency if needed
# set transparency, 0.2, tau_core
# set mesh_width, 0.5, binding_site

# === Define selections ===
select nterm_free, hTau441wt_state_5_from_modified_pdb_version_with_sidechain_SCWRL_2 and resi 1-171
select nterm, hTau441wt_state_5_from_modified_pdb_version_with_sidechain_SCWRL and resi 1-171

select PRR_free, hTau441wt_state_5_from_modified_pdb_version_with_sidechain_SCWRL_2 and resi 172-243
select PRR, hTau441wt_state_5_from_modified_pdb_version_with_sidechain_SCWRL and resi 172-243

select MBR_free, hTau441wt_state_5_from_modified_pdb_version_with_sidechain_SCWRL_2 and resi 244-368
select MBR_my, hTau441wt_state_5_from_modified_pdb_version_with_sidechain_SCWRL_Copy and resi 244-368
select MBR_my_2, hTau441wt_state_5_from_modified_pdb_version_with_sidechain_SCWRL and resi 244-368
select MBR_full_my, R1 or R2 or R3 or R4 or MBR_my or missing

select cterm_free, hTau441wt_state_5_from_modified_pdb_version_with_sidechain_SCWRL_2 and resi 369-442
select cterm, hTau441wt_state_5_from_modified_pdb_version_with_sidechain_SCWRL_Copy and resi 369-442

# === Apply colors ===
color good_green, nterm or NTR_free

color grey70, PRR or PRR_free

color good_blue, MBR_free or MBR_my_2
color good_blue, MBR_full_my or MBR_my
# they overlap a bit so first Nterm, set the NTR better in the future

color grey70, cterm or cterm_free


# === Set tubulin colors ===
select extratub, 6cvn_0003 and chain A

# Group all alpha-tubulins - pastel_orange
select orange_group, extratub or tuba2 or tuba5 or tuba8 or tuba10
color pastel_orange, orange_group

# Group all beta-tubulins - pastel_orange_light 
select orange_light_group, tubb1 or tubb3 or tubb4 or tubb6 or tubb9 or tubb11 or tubb12
color pastel_orange_light, orange_light_group

delete orange_group
delete orange_light_group

# === Set transparency ===
# # Tau regions
# set transparency, 0.0, nterm or NTR_free
# set transparency, 0.0, PRR or PRR_free
# set transparency, 0.0, MBR_free or MBR_my_2
# set transparency, 0.0, MBR_full_my or MBR_my
# set transparency, 0.0, cterm or cterm_free
# 
# # Tubulin selections
# set transparency, 0.0, extratub
# set transparency, 0.0, tuba2
# set transparency, 0.0, tubb1
# set transparency, 0.0, tubb3
# set transparency, 0.0, tubb4
# set transparency, 0.0, tuba5
# set transparency, 0.0, tubb6
# set transparency, 0.0, tuba7
# set transparency, 0.0, tuba8
# set transparency, 0.0, tubb9
# set transparency, 0.0, tubb11
# set transparency, 0.0, tuba10
# set transparency, 0.0, tubb12

# === Set view, background, etc. ===
zoom all
center all   
zoom all, -60

# Scene of full tau
set_view (\
    -0.024420783,    0.426329374,   -0.904238939,\
     0.021778747,    0.904518962,    0.425874412,\
     0.999462605,   -0.009292882,   -0.031373940,\
    -0.000890374,   -0.001219359, -737.600585938,\
   342.489837646,  449.322814941,  244.551788330,\
   199.115951538, 1275.964965820,  -49.999996185 )
   
# === Render ===
bg_color white
set ray_opaque_background, 0
# or off
# set antialias, 2
# set ray_trace_mode, 0
set ray_trace_fog = 1
set ambient, 0.3
set spec_count, 3
ray 3000, 2610

png C:\Users\NITru\OneDrive\Documents\PhD_work\Projects\NT_projects\DONE_projects\done_Review_tau_more_than_cytoskeletal_protein\figures_1_2_tau_structure_with_MT\20250406_extra_figures_RB\Figure_01a.png, dpi=300
