# === Define custom colors ===
set_color pastel_orange = [218/255.0, 118/255.0, 53/255.0]
set_color pastel_orange_light = [219/255.0, 153/255.0, 90/255.0]

set_color good_green = [70/255.0, 124/255.0, 41/255.0]
set_color good_blue = [35/255.0, 78/255.0, 135/255.0]
set_color good_blue_light = [150/255.0, 165/255.0, 185/255.0]

# === Paths and files ===
load C:\Users\NITru\OneDrive\Documents\PhD_work\Projects\NT_projects\DONE_projects\done_Review_tau_more_than_cytoskeletal_protein\figures_1_2_tau_structure_with_MT\20250406_extra_figures_RB\7nrq.cif

set seq_view, 1

# === Define selections ===
\ select 7nrq_state1, 7nrq and state 1

select nterm, resi 1-171
select PRR, resi 172-243
select MBR, resi 244-368
select cterm, resi 369-442

# MBR that is actually shown in state 1 264-326
# 198-243 1-46
# 244-368 47-171
# 369-399 172-202

# === Apply colors ===
color good_green, nterm
color gray80, PPR
color good_blue, MBR
color gray80, cterm

# === General settings ===
hide everzthing, all
show cartoon, all
show surface, all
set transparency, 0.5, all

# === Set view, background, etc. ===
zoom all
center all   
zoom all, -60

# Aggregates
set_view (\
    -0.900494874,   -0.378042817,   -0.214923769,\
    -0.318110704,    0.909630179,   -0.267174244,\
     0.296503425,   -0.172219589,   -0.939376652,\
     0.000000000,    0.000000000, -295.096740723,\
   135.331344604,  135.444320679,  145.915649414,\
   210.321807861,  379.871551514,  -20.000000000 )
   
# === Render ===
bg_color white
set ray_opaque_background, 0
# or off
# set antialias, 2
# set ray_trace_mode, 0
set ray_trace_fog = 1
set ambient, 0.3
set spec_count, 3
ray 1200, 900

png C:\Users\NITru\OneDrive\Documents\PhD_work\Projects\NT_projects\DONE_projects\done_Review_tau_more_than_cytoskeletal_protein\figures_1_2_tau_structure_with_MT\20250406_extra_figures_RB\Figure_01b.png, dpi=300