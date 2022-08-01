# -*- coding: utf-8 -*-

"""
29/07/22

This is a python photon shielding tool to look at half value thickness for different materials.
"""
import numpy as np
import pandas as pd

def read_file(filename):

    data = pd.read_csv(filename)
    return data

#find hvl
def convert_hvl(mass_attenuations, densities):

    attenuation_lead = densities[0] * mass_attenuations.loc[:,"Lead"]
    attenuation_concrete = densities[1] * mass_attenuations.loc[:,"Concrete"]
    attenuation_iron = densities[2] * mass_attenuations.loc[:,"Iron"]
    attenuations = pd.DataFrame({'Lead':attenuation_lead, 'Concrete':attenuation_concrete, "Iron":attenuation_iron})
    return np.log(2) / attenuations

density_lead = 11.29 #gram/cm3
density_iron =7.874 #gram/c3
density_concrete = 2.4 #gram/cm3

material_values = read_file("material_values.csv")

density_materials = np.array([density_lead, density_concrete, density_iron])
#convert to half value thicknesses
material_values.loc[:,("Lead","Concrete", "Iron")] = convert_hvl(material_values.loc[:,("Lead","Concrete", "Iron")], density_materials)

number_photons = 1e3

#plot the hvl
material_values.plot(kind='scatter',x='Energy', y='Lead')
material_values.plot(kind='scatter',x='Energy', y='Concrete')
material_values.plot(kind='scatter',x='Energy', y='Iron')
