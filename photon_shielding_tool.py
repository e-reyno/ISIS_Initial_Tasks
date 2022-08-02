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


def plot_material_hvl(material_data):
    
    material_data.plot(kind='scatter', x='Energy', y='Lead')
    material_data.plot(kind='scatter', x='Energy', y='Concrete')
    material_data.plot(kind='scatter', x='Energy', y='Iron')
    
    return None


def find_dose_reduction(initial_dose, final_dose):
    
    return initial_dose / final_dose


def find_number_required_hvl(initial_dose, final_dose):
    return (np.log(final_dose) - np.log(initial_dose)) / np.log(0.5)


def find_required_hvl(energy, material_hvl, initial_dose, final_dose):
    
    i = find_energy_index(energy, material_hvl.loc[:, "Energy"])
    number_hvl = find_number_required_hvl(initial_dose, final_dose)
    hvl_array = np.array([material_hvl.loc[i,"Lead"], material_hvl.loc[i,"Concrete"], material_hvl.loc[i, "Iron"] ])
    hvl_required = np.rint(number_hvl * hvl_array)
    return hvl_required

def main():
    density_lead = 11.29  # gram/cm3
    density_iron = 7.874  # gram/c3
    density_concrete = 2.4  # gram/cm3

    photon_energy = 2.4  # MeV
    final_dose_rate = 0.0001
    initial_dose_rate =  0.1

    material_values = read_file("material_values.csv")

    density_materials = np.array([density_lead, density_concrete, density_iron])
    # convert to half value thicknesses
    material_values.loc[:, ("Lead", "Concrete", "Iron")] = convert_hvl(material_values.loc[:, ("Lead", "Concrete", "Iron")],
                                                                       density_materials)
    dose_reduction_factor = find_dose_reduction(initial_dose_rate, final_dose_rate)
    hvl_required = find_required_hvl(photon_energy, material_values, initial_dose_rate, final_dose_rate)
    print("The number of half life thicknesses to  reduce the dose rate by a factor of " , 
          dose_reduction_factor , " is " , hvl_required ," for lead, concrete and iron respectively.")

    plot_material_hvl(material_values)
    

if __name__ == "__main__":
    main()




