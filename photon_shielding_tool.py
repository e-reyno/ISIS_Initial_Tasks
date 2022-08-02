# -*- coding: utf-8 -*-
"""
29/07/22

This is a python photon shielding tool to look at half value thickness for different materials.
"""
import numpy as np
import pandas as pd


def read_file(filename):
    """
    Parameters
    ----------
    filename : string
    Returns
    -------
    data : panda dataframe contianing file data
    """
    data = pd.read_csv(filename)
    return data


# find hvl
def convert_hvl(mass_attenuations, densities):
    """
    Parameters
    ----------
    mass_attenuations : panda dataframe
    materials mass attenuation values at specific energies
    densities : numpy array of floats
    density array for materials

    Returns
    -------
    panda dataframe
    calculation of the half value layer (thickness)
        DESCRIPTION.

    """
    attenuation_lead = densities[0] * mass_attenuations.loc[:, "Lead"]
    attenuation_concrete = densities[1] * mass_attenuations.loc[:, "Concrete"]
    attenuation_iron = densities[2] * mass_attenuations.loc[:, "Iron"]
    attenuations = pd.DataFrame({'Lead': attenuation_lead, 'Concrete': attenuation_concrete, "Iron": attenuation_iron})
    return np.log(2) / attenuations


def find_energy_index(energy_required, data):
    """
    Parameters
    ----------
    energy_required : float
    data : panada series of energy

    Returns
    -------
    index : integer
    index in dataframe matching energy above the required
    """
    index = (data > energy_required).idxmax()
    return index


density_lead = 11.29  # gram/cm3
density_iron = 7.874  # gram/c3
density_concrete = 2.4  # gram/cm3

material_values = read_file("material_values.csv")

density_materials = np.array([density_lead, density_concrete, density_iron])
# convert to half value thicknesses
material_values.loc[:, ("Lead", "Concrete", "Iron")] = convert_hvl(material_values.loc[:, ("Lead", "Concrete", "Iron")],
                                                                   density_materials)

# plot the hvl
material_values.plot(kind='scatter', x='Energy', y='Lead')
material_values.plot(kind='scatter', x='Energy', y='Concrete')
material_values.plot(kind='scatter', x='Energy', y='Iron')

# energy
photon_energy = 2.4  # MeV
rate_photons = 100  # per minute

i = find_energy_index(photon_energy, material_values.loc[:, "Energy"])
lead_half_thickness = material_values.loc[i, ("Lead")]
concrete_half_thickness = material_values.loc[i, "Concrete"]
iron_half_thickness = material_values.loc[i, "Iron"]

print("For a photon energy of", photon_energy, ", a half-value thickness required for"
      " lead, concrete and steel are {0:0.4f} {1:0.4f}, {2:0.4f}.".format(lead_half_thickness,
                                                                          concrete_half_thickness, iron_half_thickness))
