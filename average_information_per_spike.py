# -*- coding: utf-8 -*-
"""
Created on Sun Sep 13 19:17:23 2015

@author: maria
"""
from scipy import io
import numpy as np
import matplotlib.pyplot as plt

'''
This code implements information theoretic computations from 
"Bayesian Brain--Probabilistic Approaches to Neural Coding",
chapter "Spike Coding", Adrienne Fairhall, page 21,
formula 2.10 for the calculation of information 
per spike given a spike raster.
We use data from the www.crcns.org, mouse Lateral Geniculate
Nucleus data.
'''


#The first axis in the data array corresponds to trial, 
#second axis to time points
#4.5 seconds in each trial, each bin is one milliseconds 
#(Exclude the final time point for convenience)
data=io.loadmat('mlgnori_02.mat')['mlgn'][0][0][0][10][:,:-1]
#2

#Compute a mean_firing_rate for each trial
def compute_mean_firing_rates(data):
    mean_firing_rates=[]
    for trial in range(0,data.shape[0]):
        mean_firing_rate=float(np.count_nonzero(data[trial,:]))/(data.shape[1])
        mean_firing_rates.append(mean_firing_rate)
    return mean_firing_rates    

#Compute trial averaged firing rate with a certain time-bin resolution
def compute_trial_averaged_firing_rate(data,delta_t):
    nr_of_bins=data.shape[1]/delta_t
    bins=np.split(data,nr_of_bins,axis=1)
    trial_averaged_firing_rate=[]
    for time_bin in range(0,len(bins)):
        count=np.count_nonzero(bins[time_bin])
        normalized_count=(np.float(count)/data.shape[0])/delta_t
        for t in range(0,delta_t):        
            trial_averaged_firing_rate.append(normalized_count)
    trial_averaged_firing_rate=np.array(trial_averaged_firing_rate)
    return trial_averaged_firing_rate


def compute_average_information_per_spike(data,delta_t):
    numerical_epsilon=1
    trial_averaged_firing_rate=compute_trial_averaged_firing_rate(data,delta_t)
    mean_firing_rates=compute_mean_firing_rates(data)
    information_per_spike_in_trials=[]
    for trial in range(0,data.shape[0]):
        quotient=np.divide(trial_averaged_firing_rate,mean_firing_rates[trial])      
        log=np.log2(quotient)
        #Handle negative infinities that produce nan's when multiplied by 0
        for index in range(0,log.shape[0]):
            if np.isneginf(log[index])==True:
                log[index]=0
        information_per_spike=(float(1)/data.shape[1])*np.sum(np.multiply(quotient,log))
        information_per_spike_in_trials.append(information_per_spike)
    information_per_spike_in_trials=np.array(information_per_spike_in_trials)   
    mean_information_across_trials=np.mean(information_per_spike_in_trials)
    return information_per_spike_in_trials,mean_information_across_trials
        
    
#delta_t in ms
delta_t=50
information,mean=compute_average_information_per_spike(data,delta_t)
print information
print mean

#plt.plot(information)

rate=compute_trial_averaged_firing_rate(data,delta_t)
print sum(rate)/data.shape[1]
mean=compute_mean_firing_rates(data)
print np.mean(np.array(mean))
plt.plot(rate)
print 'mean', mean
#print 



stim=io.loadmat('mlgnori_02.mat')['mlgn'][0][0][1][0,2]
print stim.shape

