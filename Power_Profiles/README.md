# Code used to create power profiles

## Current Contents
* power_profiles.py which contains code for 2D and 3D power profiles
* kw_only.csv which contains a sample dataset that can be used with the tool.

## Code Book
This script allows the user to do power profile analysis for various sites. This is achieved by treating each plotting sub-type as a class (for example, all 2D plots are contained within the monthly_2d_plots class)

**Charting Classes:**
1. Yearly 3D Plot (yearly_3d_plot) -  This class currently only contains a yearly 3D profile. The overall quailty of the plot is not that great and could use improvements. Also consider changing class name and including other 3D plots.
    
    _Functions_
    * get_kw_data - this function simply asks for the location of hourly CSV data. The funciton checks to make sure that the listed file is a csv. The function also removes unsupported seperators ("/" or "\") from the path.

    * make_plot - This is the actual plotting function. It reshapes the csv data (which is a property of the class) so that the profiles can be shown on a month by month average.  

2. Monthly 2D Plots (monthly_2D_plots) - This class plots monthly demand profiles and supports several options which are oulined in the functions below.

    _Functions_
    * get_kw_data - This function simply asks for the location of hourly CSV data. The funciton checks to make sure that the listed file is a csv. The function also removes unsupported seperators ("/" or "\") from the path.

    * monthly_analysis_avg_profile - Defines the months of the year for slicing data

    *  combine_monthly_plots - Asks the users which months should be plotted on the same graph. 