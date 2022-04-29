# test config file
# local development -> change this to your local configuration
USERNAME = 'admin'
PASSWORD = 'password'

# save to local for now
LOCAL_DB = 'http://'+ USERNAME + ':'+ PASSWORD + '@127.0.0.1:5984/'


# 2014 - 2019 income data
# some data will be null in later years
# _m    -> million dollar
# _pure -> without allowance from government
# _pc   -> percentage
INCOME_PATH = '/data/Aurin/Income/'
INCOME_DB = 'aurin_income_db'
INCOME_INFO = {
    'sa4_code_2016': 'sa4_code',
    'sa4_name_2016': 'position',
    'yr': 'year',
    'estimates_personal_income_year_ended_30_june_mean_employee': 'mean_employee_income_year',
    'equivalised_total_household_income_census_median_weekly': 'total_household_income_week',
    'estimates_personal_income_year_ended_30_june_median_employee': 'median_employee_income_year',
    'estimates_personal_income_year_ended_30_june_total_employee_m': 'total_employee_income_year_m',
    'estm_prsnl_incme_yr_end_30_jne_mdn_tl_excl_gvrnmt_pns_alwncs': 'median_employee_income_year_pure',
    'estm_prsnl_incme_yr_end_30_jne_mn_tl_excl_gvrnmt_pns_alwncs': 'mean_employee_income_year_pure',
    'estm_prsnl_incme_yr_end_30_jne_tl_excl_gvrnmt_pns_alwncs_m': 'total_employee_income_year_m_pure',
    'tl_prsnl_incme_wkly_prsn_agd_15_yrs_cns_erng_1000_1999_pr_wk_pc': 'income_1000_1999_week_pc',
    'tl_prsnl_incme_wkly_prsn_agd_15_yrs_cns_erng_2000_2999_pr_wk_pc': 'income_2000_2999_week_pc',
    'tl_prsnl_incme_wkly_prsn_agd_15_yrs_cns_erng_500_999_pr_wk_pc': 'income_500_999_week_pc',
    'tl_prsnl_incme_wkly_prsn_agd_15_yrs_cns_indqtly_dscrb_std_pc': 'income_not_stated_week_pc',
    'ttl_prsnl_incme_wkly_prsns_agd_15_yrs_cnss_ernng_1_499_pr_wk_pc': 'income_1_499_week_pc',
    'ttl_prsnl_incme_wkly_prsns_agd_15_yrs_cnss_ernng_3000_pr_wk_pc': 'income_3000_week_pc',
    'ttl_prsnl_incme_wkly_prsns_agd_15_yrs_cnss_ernng_nl_pc': 'income_0_week_pc',
    'ttl_prsnl_incme_wkly_prsns_agd_15_yrs_cnss_ngtve_pc': 'income_negative_week_pc'
}


# 2011 - 2021 rental affordability index data
RAI_FILE_PATH = '/data/Aurin/House/RAI_2011_2021.csv'
USELESS_INFO = ['geography_name','unique_id', 'state', 'city']
HOUSE_PRICE_RAI_DB = 'aurin_rai_db'


# 2014 - 2017 house/unit sale/rent price data
HOUSE_PRICE_PATH = '/data/Aurin/House/'
HOUSE_PRICE_DB = 'aurin_house_price_db'
HOUSE_PRICE_TIME = ['2014/', '2015/', '2016/', '2017/']
HOUSE_PRICE_INFO = {
    'datemonth': 'month', 
    'dateyear': 'year', 
    'propertycategorisation': 'type', 
    'sa42016code': 'sa4_code', 
    'sa42016name': 'position',
    'for_rent_home_lease_averageprice': 'rent_avg', 
    'for_rent_home_lease_maximumprice': 'rent_max',
    'for_rent_home_lease_medianprice': 'rent_mid', 
    'for_rent_home_lease_minimumprice': 'rent_min', 
    'for_sale_both_auction_private_treaty_averageprice': 'sale_avg',
    'for_sale_both_auction_private_treaty_maximumprice': 'sale_max',
    'for_sale_both_auction_private_treaty_medianprice': 'sale_mid',
    'for_sale_both_auction_private_treaty_minimumprice': 'sale_min'
    }