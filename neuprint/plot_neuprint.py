#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Title: plot_pymaid.py
Date: May 19th, 2022
Author: Auguste de Pennart
Description:
    plots a 2D representation of the neuron(s) of interest

List of functions:
    No user defined functions are used in the program.

List of "non standard modules"
    No "non standard modules" are used in the program.

Procedure:
    1. Takes project id and either json file or, via standard input, neuron(s) of interest
    2. logs into Catmaid account
    3. plots neurons in 2D with optional print to output file

Usage:
    python plot_pymaid.py [-h] [-v] -i PROJECT_ID
                      (-j JSON | -n NEURON [NEURON ...]) [-J] [-a]
                      [-c COLOUR [COLOUR ...]] [-V VOLUME [VOLUME ...]]
                      [-C VOLUME_COLOUR [VOLUME_COLOUR ...]]
                      [-p PERSPECTIVE PERSPECTIVE PERSPECTIVE] [-o OUTPUT]
                      [-s]

known error:
    1. does not take csv files
    2. not sure if checked whether same number of neurons to colours

 """

# import modules
# ----------------------------------------------------------------------------------------
# import re  # module for using regex
import argparse #module for terminal use
# import pandas as pd
import matplotlib.pyplot as plt
import navis
import matplotlib.colors
# import json
import navis.interfaces.neuprint as neu
# import bokeh.palettes
# import os
import time
# from plot_functions import angle_build, figure_build, print_to_output, colour_parser
from plot_functions import *
#neuprint specific
from neuprint import Client, fetch_neurons, skeleton_df_to_swc
#timer
start_time = time.time()
'__main__'

# variables
# --------------------------------------------------------------------------------------
skeletons = []
volumes=[]
neu_col=[]
# neu_col=['0,0,1','1,0,0']
neu_RGB=['#E72B78','#22B8C0']
neur=['EPG.+L6','PEN.+L6']
vol=['EB','PB','NO','FB']
vol_col=['0,1,0,0.1','0,1,0,0.1','0,1,0,0.05','0,1,0,0.05']
skel={}
# cmap={}
cmap=[]
vol_list=[]
neur_col_dict={}
# main code
# --------------------------------------------------------------------------------------

c = neu.Client('neuprint.janelia.org', dataset='hemibrain:v1.2.1')
c.fetch_version()

# for col in neu_RGB:
for i in range(0,len(neu_RGB)):
    RGB = matplotlib.colors.to_rgba(neu_RGB[i], 1)
    neu_col.append(RGB)
    # print(type(RGB))
    temp_neur_col_dict=colour_parser(neu_col[i],neur[i])
    neur_col_dict = {**neur_col_dict, **temp_neur_col_dict}
print(neur_col_dict)
for neuron, colour in neur_col_dict.items():
    post_neurons, _ = fetch_neurons(neuron)
    for i, bodyId in enumerate(post_neurons['bodyId']):
        s = c.fetch_skeleton(bodyId, format='swc')
        # print(s)
        # skel[s]=colour
        # cmap[bodyId]=colour
        cmap.append(colour)
        # tempcmap = colour_neuron(bodyId, colour)
        skeletons.append(s)
        # cmap = {**cmap, **tempcmap}

skeletons = navis.read_swc(skeletons)
# print(skeletons)
# print(cmap)

vol_colour_dict = colour_parser(vol_col,vol)
for vol, col in vol_colour_dict.items():
#     vol.color = colour
#     print(vol)
    vol = neu.fetch_roi(vol)
    vol.color = col
    vol_list.append(vol)

figure_build(skeletons, cmap,volume=vol_list,show_plot=True)




# post_neurons, _ = fetch_neurons('EPG.+L6')
# pre_neurons, _ = fetch_neurons('PEN.+L6')
# EB = neu.fetch_roi('EB')
# volumes.append(EB)
# PB = neu.fetch_roi('PB')
# volumes.append(PB)
# print(post_neurons)
# print(_)

# Download some skeletons as DataFrames and attach columns for bodyId and color

# for i, bodyId in enumerate(post_neurons['bodyId']):
#     s = c.fetch_skeleton(bodyId, format='swc')
#     # print(s)
#     skeletons.append(s)
#
# for i, bodyId in enumerate(pre_neurons['bodyId']):
#     s = c.fetch_skeleton(bodyId, format='swc')
#     # print(s)
#     skeletons.append(s)

# skeletons = navis.read_swc(skeletons)
# # print(skeletons)
#
# vol_colour_dict = colour_parser(['0,1,0,0.1','0,1,0,0.1'],volumes)
# for vol in volumes:
#     vol.color = colour
# vol.color = colour
# vol_list.append(vol)
# # fig, ax = navis.plot2d([skeletons,EB,PB], color='b')
# # plt.savefig(f'test.pdf', transparent=True)
# # plt.show()
# figure_build(skeletons, colour=['b','r'],volume=volumes,outputfile='drosophila_fig')#, args.perspective, args.no_show))
# print("--- %s seconds ---" % (time.time() - start_time))

