
import itertools
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.stats.api as sms
from scipy.stats import ttest_1samp, shapiro, levene, ttest_ind, mannwhitneyu, pearsonr, spearmanr, kendalltau, \
    f_oneway, kruskal
from statsmodels.stats.proportion import proportions_ztest

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', 10)
pd.set_option('display.float_format', lambda x: '%.5f' % x)

# It will be checked which one brings more profit or not.
# Control group new feature, test group old feature
control_group = pd.read_excel("facebook_ads_test_and_control.xlsx", sheet_name = "Control Group")
test_group = pd.read_excel("facebook_ads_test_and_control.xlsx", sheet_name = "Test Group")
control_group.head()


############## TASK 1 #######################
# Hypothesis testing
# HO: M1 = M2 : There is no significant difference between the means of earning amounts between the control group and the test group.
# H1: M1 != M2

############## TASK 2 #######################

# Assumption of normality
# H0: Assumption of normal distribution is provided.
# H1:..not provided.

test_stat, pvalue = shapiro(control_group['Earning'].dropna())
print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue)) # p-value !< 0.05 so H0 CANNOT BE REJECTED. Normality provided.

test_stat, pvalue = shapiro(test_group['Earning'].dropna())
print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue)) # p-value !< 0.05 so H0 CANNOT BE REJECTED. Normality provided.

# Variance homogeneity
# H0: Variances are Homogeneous
# H1: Variances Are Not Homogeneous

test_stat, pvalue = levene(control_group['Earning'].dropna(),
                           test_group['Earning'].dropna())

print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue)) #p-value !< 0.05 so H0 CANNOT BE REJECTED. Homogeneity provided.

# Two-sample t-test (parametric test) to ensure normality and homogeneity

test_stat, pvalue = ttest_ind(control_group['Earning'],
                              test_group['Earning'],
                              equal_var=True) # A parameter that accepts variance homogeneity

print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))


# if p-value < 0.05 then reject HO.
# if p-value is not < 0.05 then H0 CAN NOT BE REJECTED.

# The test result is p value = 0.0000, so HO is REJECTED. That is, there is a significant difference between the means of the groups.

################TASK 3######################

# Firstly, I used Shapiro and Levene tests to check assumptions.
# I used a two-sample parametric t-test since both assumptions were met.

################ TASK 4 ###################

# According to our test results, averagebidding is higher than maximumbidding.
# We have seen that it brings more conversions. therefore bombabomba.com may want to switch to using the averagebidding bidding type for advertising.
