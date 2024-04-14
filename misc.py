#other functions we used for getting useful data

import pandas as pd
import numpy as np
import os
import seaborn as sns
import matplotlib.pyplot as plt
from datetime import timedelta

accepted_df = contacts[contacts['accepted'] == True]
guests_accepted = accepted_df['id_guest'].unique()

sub_df1 = searches[searches['id_user'].isin(guests_accepted)]

display(sub_df1.describe())

booked_df = contacts[contacts['booked'] == True]
guests_booked = booked_df['id_guest'].unique()

sub_df2 = searches[searches['id_user'].isin(guests_booked)]

display(sub_df2.describe())

not_booked_df = contacts[contacts['booked'] == False]
guests_not_booked = booked_df['id_guest'].unique()

sub_df3 = searches[~searches['id_user'].isin(guests_booked)]

display(sub_df3.describe())
