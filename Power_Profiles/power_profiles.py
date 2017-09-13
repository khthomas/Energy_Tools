# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 14:51:18 2017

@author: kthomas

This is the start of a project that aims to make a toolset for modeling power profiles.
The goal is to be able to take houly or 15 minute data and make different power profiles.
Right now this tool can:
    1. Make a 3D chart (that needs some contour lines)
    2. Make a 2D chart for each month of the year
    3. Show the plots individually
    4. Combine all of the plots into one yearly plot

To Do:
    1. Make the combined plot funciton take only certain months
    2. Find a way to include title, xlabel, and ylabel
    3. Update daily function to plot the day by day power consumption (for historical analysis)
    4. incorporate proper datetime?
"""

import pandas as pd
import numpy as np
from numpy import *
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib import pylab as p
import mpl_toolkits.mplot3d.axes3d as p3

class yearly_3D_plot:
    
    def __init__(self):
        self.kwData = pd.DataFrame()
        self.xData = np.array(range(1,366))
        self.yData = np.array(range(1,25))
        self.kwPlot = p.figure(figsize=(10,10))
        
    def get_kw_data(self):
        file = input("\n\n Paste name of yearly kW data (expecting 1 reading per hour) \n")
        
        if ".csv" not in file:
            print("\n\n Please upload a CSV file")
            self.get_kw_data()
    
        if ".csv" in file:
            file = file.replace("file:///","").replace("\\","//").replace("/", "//")
            self.kwData = pd.read_csv(file)
    
    def make_plot(self):
        X, Y = p.meshgrid(self.xData, self.yData)
        zData = np.array(self.kwData)
        zData = zData.reshape((len(self.yData), len(self.xData)))
        ax = p3.Axes3D(self.kwPlot)
        ax.contour3D(X,Y,zData)
        ax.set_xlabel('Day of Year')
        ax.set_ylabel('Hour of Day')
        ax.set_zlabel('kW')
        
class monthly_2D_plots:
    
    def __init__(self):
        self.kwData = pd.DataFrame()
        self.jan_plot = plt.plot()
        self.feb_plot = p.figure(figsize=(10,10))
        self.mar_plot = p.figure(figsize=(10,10))
        self.apr_plot = p.figure(figsize=(10,10))
        self.may_plot = p.figure(figsize=(10,10))
        self.jun_plot = p.figure(figsize=(10,10))
        self.jul_plot = p.figure(figsize=(10,10))
        self.aug_plot = p.figure(figsize=(10,10))
        self.sep_plot = p.figure(figsize=(10,10))
        self.octb_plot = p.figure(figsize=(10,10))
        self.nov_plot = p.figure(figsize=(10,10))
        self.dec_plot = p.figure(figsize=(10,10))
        self.combPlot = plt.plot()
        
    def get_kw_data(self):
        file = input("\n\n Paste name of yearly kW data (expecting 1 reading per hour) \n")
        
        if ".csv" not in file:
            print("\n\n Please upload a CSV file")
            self.get_kw_data()
    
        if ".csv" in file:
            file = file.replace("file:///","").replace("\\","//").replace("/", "//")
            self.kwData = pd.read_csv(file)
            
    def monthly_analysis_daily(self):
        jan = range(1, (24*31) + 1)
        feb = range(jan[-1], (jan[-1] + 24 * 28) + 1)
        mar = range(feb[-1], (feb[-1] + 24 * 31) + 1)
        apr = range(mar[-1], (mar[-1] + 24 * 30) + 1)
        may = range(apr[-1], (apr[-1] + 24 * 31) + 1)
        jun = range(may[-1], (may[-1] + 24 * 30) + 1)
        jul = range(jun[-1], (jun[-1] + 24 * 31) + 1)
        aug = range(jul[-1], (jul[-1] + 24 * 31) + 1)
        sep = range(aug[-1], (aug[-1] + 24 * 30) + 1)
        octb = range(sep[-1], (sep[-1] + 24 * 31) + 1)
        nov = range(octb[-1], (octb[-1] + 24 * 30) + 1)
        dec = range(nov[-1], (nov[-1] + 24 * 31) + 1)
        
        months = [jan, feb, mar, apr, may, jun, jul, aug, sep, octb, nov, dec]
        
                
    def monthly_analysis_avg_profile(self):
        jan = range(1, (24*31) + 1)
        feb = range(jan[-1], (jan[-1] + 24 * 28) + 1)
        mar = range(feb[-1], (feb[-1] + 24 * 31) + 1)
        apr = range(mar[-1], (mar[-1] + 24 * 30) + 1)
        may = range(apr[-1], (apr[-1] + 24 * 31) + 1)
        jun = range(may[-1], (may[-1] + 24 * 30) + 1)
        jul = range(jun[-1], (jun[-1] + 24 * 31) + 1)
        aug = range(jul[-1], (jul[-1] + 24 * 31) + 1)
        sep = range(aug[-1], (aug[-1] + 24 * 30) + 1)
        octb = range(sep[-1], (sep[-1] + 24 * 31) + 1)
        nov = range(octb[-1], (octb[-1] + 24 * 30) + 1)
        dec = range(nov[-1], (nov[-1] + 24 * 31) + 1)
        
        months = [jan, feb, mar, apr, may, jun, jul, aug, sep, octb, nov, dec]
        mplots = [self.jan_plot, self.feb_plot, self.mar_plot, self.apr_plot, 
                 self.may_plot, self.jun_plot, self.jul_plot, self.aug_plot,
                 self.sep_plot, self.octb_plot, self.nov_plot, self.dec_plot]
        
        for month in months:
            outcome = []
            for num in range(0,24):
                outcome.append(average(self.kwData["kW"][month[0]:month[-1]][num::24]))
        
            if month == jan:
                self.jan_plot = outcome
            if month == feb:
                self.feb_plot = outcome
            if month == mar:
                self.mar_plot = outcome
            if month == apr:
                self.apr_plot = outcome
            if month == may:
                self.may_plot = outcome
            if month == jun:
                self.jun_plot = outcome
            if month == jul:
                self.jul_plot = outcome
            if month == aug:
                self.aug_plot = outcome
            if month == sep:
                self.sep_plot = outcome
            if month == octb:
                self.octb_plot = outcome
            if month == nov:
                self.nov_plot = outcome
            if month == dec:
                self.dec_plot = outcome
            
    def combine_monthly_plots(self):
        response = input("""What months do you want to plot on the same graph? \n
                         Input months by their number (ex: January = 1) \n
                         You can enter multiple numbers seperated by spaces (1 2 3) \n
                         To get all plots enter ALL\n""")
        
        if response.lower() == "all":
            self.combPlot = plt.plot(self.jan_plot)
            self.combPlot = plt.plot(self.feb_plot)
            self.combPlot = plt.plot(self.mar_plot)
            self.combPlot = plt.plot(self.apr_plot)
            self.combPlot = plt.plot(self.may_plot)
            self.combPlot = plt.plot(self.jun_plot)
            self.combPlot = plt.plot(self.jul_plot)
            self.combPlot = plt.plot(self.aug_plot)
            self.combPlot = plt.plot(self.sep_plot)
            self.combPlot = plt.plot(self.octb_plot)
            self.combPlot = plt.plot(self.nov_plot)
            self.combPlot = plt.plot(self.dec_plot)
            
    def plot_month(self, x):
        mDict = {
                "1": self.jan_plot,
                "2": self.feb_plot,
                "3": self.mar_plot,
                "4": self.apr_plot,
                "5": self.may_plot,
                "6": self.jun_plot,
                "7": self.jul_plot,
                "8": self.aug_plot,
                "9": self.sep_plot,
                "10": self.octb_plot,
                "11": self.nov_plot,
                "12": self.dec_plot
                }
        plt.plot(mDict[str(x)], xlabel="Hour of Day", ylabel="Power (kW)")


              
        #this gets the average value of the first hour in Jan... need to develop a loop to get all hours
        #self.jan_plot = plt.plot(average(self.kwData["kW"][jan[0]:jan[-1]][0::24]))
        
        

def make_plots(month_profile):
    output = []
    for x in range(0,24):
        output.append(average(month_profile["kW"][x::24]))
    
    plt.plot(output)
    plt.xlabel("Hour of Day")
    plt.xlabel("Power (kW)")
    


def yearly_view():
    test = yearly_3D_plot()
    test.get_kw_data()
    test.make_plot()
    test.kwPlot

def monthly_avg():
    monthTest = monthly_2D_plots()
    monthTest.get_kw_data()
    monthTest.monthly_analysis_avg_profile()
    #monthTest.combine_monthly_plots()
    #monthTest.plot



#yearly_view()
monthly_avg()
