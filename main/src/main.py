"""
Marc Russell
2020 April 10th
Proud to Present My First Capstone Source Code
Car Accident Analysis (Accident? More Like Accidon't!)
This is so exciting! HI FUTURE MARC!
"""

import random
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

np.random.seed(42) # Don't Panic
plt.rcParams.update({'font.size': 13}) # For Frank

def plot_weather_cond(fileout_name):
    weather_cond_dict = {}
    weather_cond_tup_list = []

    for cond in df_accidents['Weather_Condition']:
        if cond not in weather_cond_dict:
            weather_cond_dict[cond] = len(df_accidents[df_accidents['Weather_Condition'] == cond])

    # Sort the list in population decsending order
    weather_cond_tup_list = sorted(weather_cond_dict.items() , reverse=True, key=lambda x: x[1])       
    weather_cond_tup_list.pop()

    weather_cond_list = []
    weather_cond_counts_list = []

    for cond, count in weather_cond_tup_list:
        weather_cond_list.append(cond)
        weather_cond_counts_list.append(count)
        
    fig, ax = plt.subplots(figsize=(10,6),dpi=200)
    ax.bar(weather_cond_list, weather_cond_counts_list, color='grey',width=0.8)

    ax.set_xlim([-0.5,8.5])
    plt.xticks(rotation=35, ha='right',fontsize=15)
    plt.ylabel('Accident Counts',fontsize=17)
    plt.xlabel('Weather Conditions',fontsize=17)

    ax.grid(False)
    plt.tight_layout()
    plt.savefig(fileout_name)

def plot_temp_counts(fileout_name):
    fig, ax = plt.subplots(figsize=(8,5))
    ax.hist(df_accidents['Temperature(F)'].dropna(), bins=100, color='#f5315f',edgecolor='orange')
    
    ax.set_ylabel('Accident Counts', fontsize = 15)
    ax.set_xlabel('Temperature (F)', fontsize = 15)
    ax.set_title('Accident Counts vs Temperature', fontsize = 17)
    
    ax.set_xlim([0,110])

    ax.grid(False)
    plt.tight_layout()
    plt.savefig(fileout_name)

def plot_precip_counts(fileout_name):
    fig, ax = plt.subplots(figsize=(8,5),dpi=500)
    ax.hist(df_accidents['Precipitation(in)'].dropna(), bins=200, edgecolor='lightgrey',color='grey')

    ax.set_title('Accident Count vs Precipitation Amount',fontsize=15)
    ax.set_ylabel('Accident Count',fontsize=16)
    ax.set_xlabel('Precipitation (in/hr)',fontsize=17)

    ax.set_xlim([0,20])
    ax.set_ylim([0,500])

    plt.xticks(fontsize=16)
    plt.yticks(fontsize=16)

    ax.grid(False)
    plt.tight_layout()
    plt.savefig(fileout_name)

def plot_visibility_counts(fileout_name):
    fig, ax = plt.subplots(figsize=(6,5),dpi=500)
    ax.hist(df_accidents['Visibility(mi)'].dropna(), bins=200,edgecolor='yellow',color='k', alpha=0.7)

    ax.set_title('Accident Count vs Visibility',fontsize=15)
    ax.set_ylabel('Accident Count',fontsize=14)
    ax.set_xlabel('Visibility (mi)',fontsize=15)

    ax.set_xlim([-0.4,11])
    ax.set_ylim([0,100000])
    plt.xticks(fontsize=16)

    ax.grid(False)
    plt.tight_layout()
    plt.savefig(fileout_name)

def plot_cali_map(fileout_name):
    fig, ax = plt.subplots(figsize=(7,7), dpi=500)
    ax.scatter(df_accidents['Start_Lng'], df_accidents['Start_Lat'],c='m', marker=',',alpha=0.06,s=0.05)

    ax.set_ylabel('Latitude', fontsize = 16)
    ax.set_xlabel('Longitude', fontsize = 16)
    ax.set_title('California Accident Map', fontsize = 18)

    ax.set_xlim([-127.7, -111.15])
    ax.set_ylim([31.46,43.2])

    ax.grid(False)
    plt.savefig(fileout_name, dpi=500)

def plot_nyc_map(fileout_name):
    fig, ax = plt.subplots(figsize=(7,7), dpi=500)
    ax.scatter(df_accidents['Start_Lng'], df_accidents['Start_Lat'],c='k', alpha='0.3', marker=',',s=0.05)
    
    ax.set_ylabel('Latitude', fontsize = 16)
    ax.set_xlabel('Longitude', fontsize = 16)
    ax.set_title('New York Accident Map', fontsize = 18)
    
    ax.set_xlim([-74.15,-73.75])
    ax.set_ylim([40.6,41.0])

    ax.grid(False)
    plt.tight_layout()
    plt.savefig(fileout_name, dpi=500)

def plot_denver_map(fileout_name):
    fig, ax = plt.subplots(figsize=(7,7),dpi=500)
    ax.scatter(df_accidents['Start_Lng'], df_accidents['Start_Lat'],c='darkred', alpha=0.5, marker=',',s=0.05)

    ax.set_ylabel('Latitude', fontsize = 16)
    ax.set_xlabel('Longitude', fontsize = 16)
    ax.set_title('Denver Accident Map', fontsize = 18)
    
    ax.set_xlim([-105.2,-104.8])
    ax.set_ylim([39.6,39.86])  

    ax.grid(False)
    plt.tight_layout()
    plt.savefig(fileout_name, dpi=500)

def plot_state_vs_state(fileout_name):
    state_population_dict = {
    'AL' : 3814879,
    # 'AK' : 551562,
    'AZ' : 5638481,
    'AR' : 2317649,
    'CA' : 30617582,
    'CO' : 4499217,
    'CT' : 2837847,
    'DC' : 703608,
    'DE' : 770192,
    'FL' : 17247808,
    'GA' : 8113542,
    # 'HI' : 1116004,
    'ID' : 1338864,
    'IL' : 9853946,
    'IN' : 5164245,
    'IA' : 2428229,
    'KS' : 2213064,
    'KY' : 3464802,
    'LA' : 3561164,
    'ME' : 1095370,
    'MD' : 4710993,
    'MA' : 5539703,
    'MI' : 7842924,
    'MN' : 4336475,
    'MS' : 2277566,
    'MO' : 4766843,
    'MT' : 840190,
    'NE' : 1458334,
    'NV' : 2387517,
    'NH' : 1104458,
    'NJ' : 6943612,
    'NM' : 1620991,
    'NY' : 15425262,
    'NC' : 8187369,
    'ND' : 581891,
    'OH' : 9111081,
    'OK' : 3004733,
    'OR' : 3351175,
    'PA' : 10167376,
    'RI' : 854866,
    'SC' : 4037531,
    'SD' : 667558,
    'TN' : 5319123,
    'TX' : 21596071,
    'UT' : 2274774,
    'VT' : 509984,
    'VA' : 6674671,
    'WA' : 5951832,
    'WV' : 1432580,
    'WI' : 4555837,
    'WY' : 445025
    }
    state_acc_dict = {}
    state_acc_tup_list = []
    state_acc_adj_dict = {}
    state_acc_adj_tup_list = []

    for state in state_population_dict:
        if state not in state_acc_dict:
            state_acc_dict[state] = len(df_accidents[df_accidents['State'] == state])

    # Sort the list in population decsending order
    state_acc_tup_list = sorted(state_acc_dict.items() , reverse=True, key=lambda x: x[1])       
    """     
    Adjusted accident counts = 
    state accident counts (over3.5 years) /
    population of state /
    3.5 to remove the year span
    """
    for state, pop in state_acc_tup_list:
        state_acc_adj_dict[state] = (pop / state_population_dict[state] / 3.5)
    state_acc_adj_tup_list = sorted(state_acc_adj_dict.items() , reverse=True, key=lambda x: x[1])       

    state_list_unadj = []
    pop_list_unadj = []
    for state, pop in state_acc_tup_list:
        state_list_unadj.append(state)
        pop_list_unadj.append(pop)

    state_list_adj = []
    pop_list_adj = []
    for state, pop in state_acc_adj_tup_list:
        state_list_adj.append(state)
        pop_list_adj.append(pop)

    fig, axs = plt.subplots(2, 2, figsize=(15,8), dpi=300)

    axs[0, 0].bar(state_list_unadj, pop_list_unadj, color='darkred')
    axs[0, 0].set_title('Heighest State Accident Rates (Unadjusted)', fontsize=16)
    axs[0, 0].set_xlim([-0.5,10.5])
    axs[0, 0].set_ylabel("Accident Counts")
    axs[0, 0].grid(False)

    axs[0, 1].bar(state_list_unadj, pop_list_unadj, color='darkred')
    axs[0, 1].set_title('Lowest State Accident Rates (Unadjusted)', fontsize=16)
    axs[0, 1].set_xlim([42.5,48.5])
    axs[0, 1].set_ylim([0,2000])
    axs[0, 1].set_ylabel("Accident Counts")
    axs[0, 1].grid(False)

    axs[1, 0].bar(state_list_adj, pop_list_adj, color='red', alpha=0.7)
    axs[1, 0].set_title('Heighest State Accident Rates (Adjusted)', fontsize=16)
    axs[1, 0].set_xlim([-0.5,10.5])
    axs[1, 0].set_ylabel("Accident Rates")
    axs[1, 0].grid(False)

    axs[1, 1].bar(state_list_adj, pop_list_adj, color='red', alpha=0.7)
    axs[1, 1].set_title('Lowest State Accident Rates (Adjusted)', fontsize=16)
    axs[1, 1].set_xlim([42.5,48.5])
    axs[1, 1].set_ylim([0,0.0004])
    axs[1, 1].set_ylabel("Accident Rates")
    axs[1, 1].grid(False)

    plt.tight_layout(pad=0.1, w_pad=0.7, h_pad=2)
    plt.savefig(fileout_name)

def plot_time_day(fileout_name):
    # sorted time_list is a hour:minute list of all accidents
    time_list = []
    for i in df_accidents['Start_Time']:
        time_list.append(i[-8:-3])
    (time_list).sort()

    fig, ax = plt.subplots(figsize=(8,5),dpi=500)
    ax.hist(time_list, bins=2400, color='b', edgecolor='#93cc8b')

    ax.set_ylabel('Number of Accident')
    ax.set_xlabel('Hours of the Day')
    ax.set_title('Accident Count throughout the Day')

    plt.xticks(['00:00','08:00','17:30','24:00'], rotation='horizontal')
    plt.axvline(x= '08:00',ymax=0.94, linewidth=1.5, color='k', linestyle='--')
    plt.axvline(x= '17:20',ymax=0.65, linewidth=1.5, color='k', linestyle='--')
    
    ax.grid(False)
    plt.tight_layout()
    plt.savefig(fileout_name, dpi = 400)

def plot_time_month(fileout_name):
    # sorted month:day_list is a hour:minute list of all accidents
    month_day_list = []
    for i in df_accidents['Start_Time']:
        month_day_list.append(i[5:10])
    month_day_list.sort()

    color1='#8ecc87'
    fig, ax = plt.subplots(figsize=(9,5),dpi=400)
    ax.hist(month_day_list, bins=365, color=color1, edgecolor=color1)

    ax.set_xlim(xmin='04-01',xmax='04-30')
    ax.set_ylim([0,12000])

    ax.set_ylabel('Number of Accident',fontsize=15)
    ax.set_xlabel('April 2017 (Weekends Shaded)',fontsize=16)
    ax.set_title('Accident Count throughout April 2017',fontsize=16)
    ax.grid(False)

    # Add grey shading over the weekends manually
    for weekend in ['04-08','04-15','04-22','04-29']:
        plt.axvline(x= weekend,
                    ymax=1, 
                    linewidth=38, 
                    color='k',
                    alpha=0.1
                )

    plt.xticks(('04-01','04-07','04-14','04-21','04-30'),
            ('1st', '7th','14th','21st','30th'),
            rotation=0,
            fontsize=15
            )

    plt.tight_layout()
    plt.savefig(fileout_name, dpi = 400)

def plot_time_year(fileout_name):
    month_day_list = []
    for i in df_accidents['Start_Time']:
        month_day_list.append(i[5:10])
    month_day_list.sort()

    year_list = []
    for i in df_accidents['Start_Time']:
        year_list.append(i[0:4])
    year_list.sort()

    color1='#7ea879'
    fig, ax = plt.subplots(figsize=(9,5),dpi=500)
    ax.hist(month_day_list, bins=365, color=color1, edgecolor=color1)

    ax.set_ylabel('Number of Accident',fontsize=15)
    ax.set_xlabel('Days of the Year',fontsize=15)
    ax.set_title('Accident Count throughout the Year',fontsize=16)
    ax.grid(False)

    # Dotted line on Dec 25th
    plt.axvline(x= '12-25',
                ymax=0.205, 
                linewidth=0.45, 
                color='k', 
                linestyle='--')

    plt.xticks(('01-15', '04-01', '06-15', '09-10', '12-01', '12-25'),
            ('January', 'April','June','September','Dec.  ','  25th'),
            rotation=0,
            fontsize=15
            )

    plt.tight_layout()
    plt.savefig(fileout_name, dpi = 400)

if __name__ == '__main__':
    
    df_accidents = pd.DataFrame()
    df_tax = pd.DataFrame()
    df_accidents = pd.read_csv('../data/US_Accidents_Dec19.csv')
    df_tax = pd.read_csv('../data/county_level_datasets/Income.csv')
 
    plot_weather_cond('../img/weather_vs_count.png')
    plot_temp_counts('../img/temp_counts.png')
    plot_precip_counts('../img/precip_counts')
    plot_visibility_counts('../img/visibility_counts.png')
    plot_cali_map('../img/cali_map1.png')
    plot_nyc_map('../img/nyc_map1.png')
    plot_denver_map('../img/denver_map1.png')
    plot_state_vs_state('../img/state_acc_count_rate.png')
    plot_time_day('../img/accident-count-throughout-the-day-3.png')
    plot_time_month('../img/accident-count-throughout-april.png')
    plot_time_year('../img/accident-count-throughout-the-year.png')