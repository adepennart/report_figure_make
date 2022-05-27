#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Title: plot_neuprint.py
Date: May 27th, 2022
Author: Auguste de Pennart
Description:
    plots a 2D representation of the neuPRINT neuron(s) of interest

List of functions:
    No user defined functions are used in the program.

List of "non standard modules"
    No "non standard modules" are used in the program.

Procedure:
    1. Takes drosophila E-PG and P-EN neurons
    2. logs into Catmaid account
    3. plots neurons in 2D

Usage:
    python plot_neuprint.py

known error:
    1. does not take csv files
    2. not sure if checked whether same number of neurons to colours
 """

# import modules
# ----------------------------------------------------------------------------------------
import matplotlib.pyplot as plt
import navis
import matplotlib.colors
import navis.interfaces.neuprint as neu
import time
from plot_functions import *
#neuprint specific
from neuprint import Client, fetch_neurons, skeleton_df_to_swc

# variables
# --------------------------------------------------------------------------------------
skeletons = []
volumes=[]
neu_col=[]
neu_RGB=['#E72B78','#22B8C0']
neur=['EPG.+L6','PEN.+L6']
vol=['EB','PB','NO','FB']
vol_col=['0,1,0,0.1','0,1,0,0.1','0,1,0,0.05','0,1,0,0.05']
cmap=[]
vol_list=[]
neur_col_dict={}
outputfile='fly_fig'

# main code
# --------------------------------------------------------------------------------------

c = neu.Client('neuprint.janelia.org', dataset='hemibrain:v1.2.1')
c.fetch_version()

for i in range(0,len(neu_RGB)):
    RGB = matplotlib.colors.to_rgba(neu_RGB[i], 1)
    neu_col.append(RGB)
    # print(type(RGB))
    temp_neur_col_dict=colour_parser(neu_col[i],neur[i])
    neur_col_dict = {**neur_col_dict, **temp_neur_col_dict}
# print(neur_col_dict)
for neuron, colour in neur_col_dict.items():
    post_neurons, _ = fetch_neurons(neuron)
    for i, bodyId in enumerate(post_neurons['bodyId']):
        s = c.fetch_skeleton(bodyId, format='swc')
        # print(s)
        cmap.append(colour)
        skeletons.append(s)

skeletons = navis.read_swc(skeletons)
# print(skeletons)
# print(cmap)

vol_colour_dict = colour_parser(vol_col,vol)
for vol, col in vol_colour_dict.items():
    # print(vol)
    vol = neu.fetch_roi(vol)
    vol.color = col
    vol_list.append(vol)

figure_build(skeletons, cmap,volume=vol_list,show_plot=True,outputfile=outputfile)



