
import pandas as pd
import warnings
warnings.filterwarnings('ignore')
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', 150)

import matplotlib.pyplot as plt
import seaborn as sns
import os
import json


def plt_hist_with_hue(target_one:pd.DataFrame, target_cero: pd.DataFrame, feature:str)->plt:
    """Plot 2 histograms in 1 plot, with alpha 

    Args:
        target_one (pd.DataFrame): dataframe with target value = 1
        target_cero (pd.DataFrame): dataframe with target value = 0
        feature (str): feature name 

    Returns:
        plt: matplot lib chart
    """
    red_blue = ['#EF4836','#19B5FE']
    palette = sns.color_palette(red_blue)
    sns.set_palette(palette)
    sns.set_style("white")

    fig,ax = plt.subplots(figsize=(20, 7))

    #   {feature}
    plt.title(f'{feature}\nDistribution', fontsize=16)
    target_one[f'{feature}'].hist( alpha=0.7, bins=30, label = 'Fraud')
    target_cero[f'{feature}'].hist( alpha=0.7, bins=30, label = 'Not Fraud')
    plt.legend(loc = 'upper right', fontsize=14)
    plt.xlabel(f'{feature}', fontsize=14)
    plt.ylabel('Count', fontsize=14)
    # fig.tight_layout()
    plt.show()

def plot_bar_according_to_target(target_one: pd.DataFrame,target_cero:pd.DataFrame,feature:str, show_n_values:int, vertical_var = True,normalize:bool = False, size = 'small')->plt:
    """Bar plot with 2 target values

    Args:
        target_one (pd.DataFrame): dataframe with target value = 1
        target_cero (pd.DataFrame): dataframe with target value = 0
        feature (str): feature name
        show_n_values (int): number of values to show in the plot
        vertical_var (bool, optional): Vertical bar or horizontal bar. Defaults to True.
        normalize (bool, optional): proportions instead of count. Defaults to False.
        size (str, optional): size of the plot. Defaults to 'small'.

    Returns:
        plt: matplot lib chart
    """

    kind_ = 'bar' if vertical_var == True else 'barh'
    
    if size == 'small':
        size_ = (12,5)
    elif size == 'medium':
        size_ =  (20,7)
    elif size == 'large':
        size_ =  (30,11)
    
    
    if show_n_values == '':
        fig, axs = plt.subplots(1,2,figsize = size_)
        left_plot_target_true = target_one[feature].value_counts(normalize = normalize).plot(kind = kind_ , title = f'Fraud vs {feature}',ax=axs[0], color = '#EF4836',label = 'Fraud', alpha = 0.5, legend = True)
        right_plot_target_false = target_cero[feature].value_counts(normalize = normalize).plot(kind = kind_, title = f'Not Fraud vs {feature}',ax=axs[1], color = '#19B5FE',label = 'Not Fraud', alpha = 0.5, legend = True)
        axs[0].legend(loc = 'upper right', fontsize=14)
        axs[1].legend(loc = 'upper right', fontsize=14)
    else:
        fig, axs = plt.subplots(1,2,figsize = size_)
        left_plot_target_true = target_one[feature].value_counts(normalize = normalize).head(show_n_values).plot(kind = kind_ , title = f'Fraud vs {feature}',ax=axs[0], color = '#EF4836',label = 'Fraud', alpha = 0.5, legend = True)
        right_plot_target_false = target_cero[feature].value_counts(normalize = normalize).head(show_n_values).plot(kind = kind_, title = f'Not Fraud vs {feature}',ax=axs[1], color = '#19B5FE',label = 'Not Fraud', alpha = 0.5, legend = True)
        axs[0].legend(loc = 'upper right', fontsize=14)
        axs[1].legend(loc = 'upper right', fontsize=14)

def plt_hist_without_hue(target_one: pd.DataFrame,target_cero:pd.DataFrame,feature:str, size = 'small')->plt:
    """Hist plot with 2 target values without hue

    Args:
        target_one (pd.DataFrame): dataframe with target value = 1
        target_cero (pd.DataFrame): dataframe with target value = 0
        feature (str): feature name
        size (str, optional): size of the plot. Defaults to 'small'.

    Returns:
        plt: matplot lib chart
    """

    
    if size == 'small':
        size_ = (12,5)
    elif size == 'medium':
        size_ =  (20,7)
    elif size == 'large':
        size_ =  (30,11)
    
    
    sns.set_style("white")
    fig, axs = plt.subplots(1,2,figsize = size_)
    plt.title(f'{feature}\nDistribution', fontsize=16)
    left_plot_target_true = target_one[f'{feature}'].hist( alpha=0.7, bins=30, label = 'Fraud',ax=axs[0], color = '#EF4836')
    plt.title(f'{feature}\nDistribution', fontsize=16)
    right_plot_target_false = target_cero[f'{feature}'].hist( alpha=0.7, bins=30, label = 'Not Fraud',ax=axs[1], color = '#19B5FE')

    axs[0].legend(loc = 'upper right', fontsize=14)
    axs[0].set_title(f'{feature}\nDistribution', fontsize=16)
    axs[0].set_xlabel(f'{feature}', fontsize=14)
    axs[0].set_ylabel('Count', fontsize=14)
    
    axs[1].legend(loc = 'upper right', fontsize=14)
    axs[1].set_title(f'Not {feature}\nDistribution', fontsize=16)
    axs[1].set_xlabel(f'{feature}', fontsize=14)
    axs[1].set_ylabel('Count', fontsize=14)

def plot_single_bar(dataframe: pd.DataFrame,feature:str, show_n_values:int, vertical_var = True,normalize:bool = False, size = 'small')->plt:
    """Sngle bar plot

    Args:
        dataframe (pd.DataFrame): dataframe 
        feature (str): feature name
        show_n_values (int): number of values to show in the plot
        vertical_var (bool, optional): Vertical bar or horizontal bar. Defaults to True.
        normalize (bool, optional): proportions instead of count. Defaults to False.
        size (str, optional): size of the plot. Defaults to 'small'.

    Returns:
        plt: matplot lib chart
    """

    kind_ = 'bar' if vertical_var == True else 'barh'
    
    if size == 'small':
        size_ = (12,5)
    elif size == 'medium':
        size_ =  (20,7)
    elif size == 'large':
        size_ =  (30,11)
    
    
    if show_n_values == '':
        fig, axs = plt.subplots(figsize = size_)
        single_bar_plot = dataframe[feature].value_counts(normalize = normalize).plot(kind = kind_, color = '#19B5FE', alpha = 0.5, legend = True)
    else:
        fig, axs = plt.subplots(figsize = size_)
        single_bar_plot = dataframe[feature].value_counts(normalize = normalize).head(show_n_values).plot(kind = kind_, color = '#19B5FE', alpha = 0.5, legend = True)

    plt.title(f'{feature}\nProportion', fontsize = 14)
    plt.legend(loc = 'upper right', fontsize=14)
