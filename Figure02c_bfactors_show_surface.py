# === Define custom colors ===
set_color pastel_orange = [218/255.0, 118/255.0, 53/255.0]
set_color pastel_orange_light = [219/255.0, 153/255.0, 90/255.0]

set_color good_green = [70/255.0, 124/255.0, 41/255.0]
set_color good_blue = [35/255.0, 78/255.0, 135/255.0]
set_color good_blue_light = [150/255.0, 165/255.0, 185/255.0]

set_color custom_middle = [150/255.0, 122/255.0, 184/255.0]
set_color custom_dark = [89/255.0, 64/255.0, 119/255.0]
cmd.set_color("custom_middle", [150/255.0, 122/255.0, 184/255.0])
cmd.set_color("custom_dark", [89/255.0, 64/255.0, 119/255.0])

# === Paths and files ===
load C:\Users\NITru\OneDrive\Documents\PhD_work\Projects\NT_projects\DONE_projects\done_Review_tau_more_than_cytoskeletal_protein\figures_1_2_tau_structure_with_MT\hTau441wt_state_5_from_modified_pdb_version_with_sidechain_SCWRL.pdb



# Reassigning B-Factors and Coloring
# It is commonplace to replace the B-Factor column of a protein with some other biochemical property at that residue, observed from some calculation or experiment. PyMOL can easily reassign the B-Factors and color them, too. The following example will load a protein, set ALL it's B Factors to "0", read in a list of properties for each alpha carbon in the proteins, assign those new values as the B-Factor values and color by the new values. This example is possible because commands PyMOL does not recognize are passed to the Python interpreter --- a very powerful tool. 
# open the file of new values (just 1 column of numbers, one for each alpha carbon)
inFile = open(r"C:\Users\NITru\OneDrive\Documents\PhD_work\Projects\NT_projects\DONE_projects\done_Review_tau_more_than_cytoskeletal_protein\figures_1_2_tau_structure_with_MT\pymol_scripts\disorder_bfactors.txt", 'r')
# create the global, stored array
stored.newB = []
# read the new B factors from file
for line in inFile.readlines(): stored.newB.append( float(line) )
# close the input file
inFile.close()
# clear out the old B Factors
alter hTau441wt_state_5_from_modified_pdb_version_with_sidechain_SCWRL, b=0.0
# update the B Factors with new properties
alter hTau441wt_state_5_from_modified_pdb_version_with_sidechain_SCWRL and n. CA, b=stored.newB.pop(0)
# color the protein based on the new B Factors of the alpha carbons
# cmd.spectrum("b", "grey90_grey_grey10","hTau441wt_state_5_from_modified_pdb_version_with_sidechain_SCWRL and n. CA")

cmd.spectrum("b", "grey90 custom_middle custom_dark", "hTau441wt_state_5_from_modified_pdb_version_with_sidechain_SCWRL and n. CA")



# === Define selections ===
select nterm, resi 1-171
select PRR, resi 172-243
select MBR, resi 244-368
select cterm, resi 369-442

# === General settings ===
hide all
# toggle surface, met
show surface, all
# show mesh, binding_site

# Set transparency if needed
# set transparency, 0.2, tau_core
# set mesh_width, 0.5, binding_site

create ca_obj, hTau441wt_state_5_from_modified_pdb_version_with_sidechain_SCWRL and name ca 
ramp_new ramp_obj, ca_obj, [0, 10], [-1, -1, 0]
set surface_color, ramp_obj, hTau441wt_state_5_from_modified_pdb_version_with_sidechain_SCWRL
hide all
show surface

# === Apply colors ===
# color good_blue_light, PRR
# color good_blue_light, cterm
set surface_color, grey70, PRR
set surface_color, grey70, cterm

# === Set view, background, etc. ===
zoom all
center all   
zoom all, -60

# Single tau
set_view (\
     0.189049765,    0.773191392,    0.605333507,\
     0.411342233,    0.497401655,   -0.763797760,\
    -0.891654491,    0.393392503,   -0.224010020,\
    -0.002041290,    0.000169665, -667.888549805,\
   -21.664424896,   24.457353592, -165.326232910,\
   179.599609375, 1156.195312500,  -20.000000000 )

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

# the ramp has to be hidden manually - ?

png C:\Users\NITru\OneDrive\Documents\PhD_work\Projects\NT_projects\DONE_projects\done_Review_tau_more_than_cytoskeletal_protein\figures_1_2_tau_structure_with_MT\20250406_extra_figures_RB\Figure_02c.png, dpi=300

# Color the protein based on the new B Factors of the alpha carbons
# cmd.spectrum("b", "grey90_grey_grey10","hTau441wt_state_5_from_modified_pdb_version_with_sidechain_SCWRL and n. CA")
# Or 
# cmd.spectrumany count, lightgray gray darkgray,hTau441wt_state_5_from_modified_pdb_version_with_sidechain_SCWRL and n. CA
