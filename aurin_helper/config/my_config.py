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

# 2016 - 2020 migration, population data
MIGRATION_DB = 'aurin_migration_db'
MIGRATION_PATH = '/data/Aurin/Population/'
MIGRATION_INFO = {
    'financial_year': 'year',
    'migration_type': 'type',
    'sa4_code_2016': 'sa4_code',
    'sa4_name_2016': 'position',
    '_0_14': 'age_0_4',
    '_15_24': 'age_15_24',
    '_25_44': 'age_25_44',
    '_45_64': 'age_45_64',
    '_65_and_over': 'age_65_over',
    'all_ages': 'age_all'
}

BORN_PATH = '/data/Aurin/Population/born_2016.csv'
BORN_INFO = {
    'yr': 'year',
    'sa4_code_2016': 'sa4_code',
    'sa4_name_2016': 'position',
    'age_of_persons_born_overseas_census_0_4_years_num': 'age_0_4_num',
    'age_of_persons_born_overseas_census_5_9_years_num': 'age_5_9_num',
    'age_of_persons_born_overseas_census_10_14_years_num': 'age_10_14_num',
    'age_of_persons_born_overseas_census_15_19_years_num': 'age_15_19_num',
    'age_of_persons_born_overseas_census_20_24_years_num': 'age_20_24_num',
    'age_of_persons_born_overseas_census_25_29_years_num': 'age_25_29_num',
    'age_of_persons_born_overseas_census_30_34_years_num': 'age_30_34_num',
    'age_of_persons_born_overseas_census_35_39_years_num': 'age_35_39_num',
    'age_of_persons_born_overseas_census_40_44_years_num': 'age_40_44_num',
    'age_of_persons_born_overseas_census_45_49_years_num': 'age_45_49_num',
    'age_of_persons_born_overseas_census_50_54_years_num': 'age_50_54_num',
    'age_of_persons_born_overseas_census_55_59_years_num': 'age_55_59_num',
    'age_of_persons_born_overseas_census_60_64_years_num': 'age_60_64_num',
    'age_of_persons_born_overseas_census_65_69_years_num': 'age_65_69_num',
    'age_of_persons_born_overseas_census_70_74_years_num': 'age_70_74_num',
    'age_of_persons_born_overseas_census_75_79_years_num': 'age_75_79_num',
    'age_of_persons_born_overseas_census_80_84_years_num': 'age_80_84_num',
    'age_of_persons_born_overseas_census_85_years_and_over_num': 'age_80_over_num',
    'english_proficiency_persons_born_overseas_census_proficient_pc': 'english_pro_pc',
    'englsh_prfcncy_prsns_brn_ovrss_cnss_prfcnt_pc': 'english_poor_pc',
    'english_proficiency_persons_born_overseas_census_stated_pc': 'english_not_stated_pc',
    'population_of_persons_born_overseas_census_females_num': 'female_num',
    'population_of_persons_born_overseas_census_males_num': 'male_num',
    'population_of_persons_born_overseas_census_persons_num': 'person_num',
    'ttl_prsnl_incme_wkly_prsns_brn_ovrss_cnss_ernng_1_499_pr_wk_pc': 'income_1_499_week_pc',
    'tl_prsnl_incme_wkly_prsn_brn_ovrs_cns_erng_500_999_pr_wk_pc': 'income_500_999_week_pc',
    'tl_prsnl_incme_wkly_prsn_brn_ovrs_cns_erng_1000_1999_pr_wk_pc': 'income_1000_1999_week_pc',
    'tl_prsnl_incme_wkly_prsn_brn_ovrs_cns_erng_2000_2999_pr_wk_pc': 'income_2000_2999_week_pc',
    'ttl_prsnl_incme_wkly_prsns_brn_ovrss_cnss_ernng_3000_pr_wk_pc': 'income_3000_over_week_pc',
    'tl_prsnl_incme_wkly_prsn_brn_ovrs_cns_indqtly_dscrb_std_pc': 'income_not_stated_week_pc',
    'ttl_prsnl_incme_wkly_prsns_brn_ovrss_cnss_ernng_nl_pc': 'income_0_week_pc',
    'ttl_prsnl_incme_wkly_prsns_brn_ovrss_cnss_ngtve_pc': 'income_negative_week_pc',
    'yr_arrvl_of_prsns_brn_ovrss_cnss_arrvd_wthn_5_yrs_pc': 'arrived_in_5_year_pc',
    'yr_arrvl_of_prsns_brn_ovrss_cnss_arrvd_5_10_yrs_ago_pc': 'arrived_5_10_year_pc',
    'yr_arrvl_of_prsns_brn_ovrss_cnss_arrvd_10_yrs_ago_pc': 'arrived_over_10_year_pc',
    'year_arrival_of_persons_born_overseas_census_arrival_stated_pc': 'arrived_not_stated_pc'
}

BIRTH_PATH = '/data/Aurin/Population/birth_2016_2020.csv'
BIRTH_INFO = {
    'sa4_code': 'sa4_code',
    'sa4_name': 'position',
    '_2016_births_no': 'birth_2016_num',
    '_2017_births_no': 'birth_2017_num',
    '_2018_birthsa_no': 'birth_2018_num',
    '_2019_births_no': 'birth_2019_num',
    '_2020_births_no': 'birth_2020_num',
    '_2016_estimated_resident_population_persons': 'population_2016',
    '_2017_estimated_resident_populationa_persons': 'population_2017',
    '_2018_estimated_resident_populationa_persons': 'population_2018',
    '_2019_estimated_resident_populationa_persons': 'population_2019',
    '_2020_estimated_resident_populationa_persons': 'population_2020'
}


EMPLOYMENT_DB = 'aurin_employment_db'

UNEMPLOYMENT_PATH = '/data/Aurin/Employ/unemployment.csv'
UNEMPLOYMENT_INFO = {
    'mar_19': 'un_num_2019_3',
    'jun_19': 'un_num_2019_6',
    'sep_19': 'un_num_2019_9',
    'dec_19': 'un_num_2019_12',
    'mar_20': 'un_num_2020_3',
    'jun_20': 'un_num_2020_6',
    'sep_20': 'un_num_2020_9',
    'dec_20': 'un_num_2020_12',
    'mar_21': 'un_num_2021_3',
    'jun_21': 'un_num_2021_6',
    'sep_21': 'un_num_2021_9'
}

UNEMPLOYMENT_RATE_PATH = '/data/Aurin/Employ/unemployment_rate.csv'
UNEMPLOYMENT_RATE_INFO = {
    'mar_19': 'un_rate_2019_3',
    'jun_19': 'un_rate_2019_6',
    'sep_19': 'un_rate_2019_9',
    'dec_19': 'un_rate_2019_12',
    'mar_20': 'un_rate_2020_3',
    'jun_20': 'un_rate_2020_6',
    'sep_20': 'un_rate_2020_9',
    'dec_20': 'un_rate_2020_12',
    'mar_21': 'un_rate_2021_3',
    'jun_21': 'un_rate_2021_6',
    'sep_21': 'un_rate_2021_9'
}

EMPLOYMENT_PATH = '/data/Aurin/Employ/unemployment.csv'
EMPLOYMENT_INFO = {
    'mar_19': 'num_2019_3',
    'jun_19': 'num_2019_6',
    'sep_19': 'num_2019_9',
    'dec_19': 'num_2019_12',
    'mar_20': 'num_2020_3',
    'jun_20': 'num_2020_6',
    'sep_20': 'num_2020_9',
    'dec_20': 'num_2020_12',
    'mar_21': 'num_2021_3',
    'jun_21': 'num_2021_6',
    'sep_21': 'num_2021_9'
}





# education data, not useful for now
EDUCATION_DB = 'aurin_education_db'
EDUCATION_PATH = '/data/Aurin/Education/'
EDUCATION_INFO = {
    'yr': 'year',
    'sa4_code_2016': 'sa4_code',
    'sa4_name_2016': 'position',
    'highest_year_school_completed_persons_aged_15_years_census_8_pc': 'highest_year_less_8_pc',
    'hghst_yr_schl_cmpltd_prsns_agd_15_yrs_cnss_9_eqvlnt_pc': 'highest_year_9_pc',
    'hghst_yr_schl_cmpltd_prsns_agd_15_yrs_cnss_10_eqvlnt_pc': 'highest_year_10_pc',
    'hghst_yr_schl_cmpltd_prsns_agd_15_yrs_cnss_11_eqvlnt_pc': 'highest_year_11_pc',
    'hghst_yr_schl_cmpltd_prsns_agd_15_yrs_cnss_12_eqvlnt_pc': 'highest_year_12_pc',
    'hghst_yr_schl_cmpltd_prsns_agd_15_yrs_cnss_go_pc': 'not_go_to_shool_pc',
    'hghst_yr_schl_cmpltd_prsns_agd_15_yrs_cnss_of_sttd_pc': 'highest_year_not_stated_pc',
    'labour_force_status_persons_aged_15_years_census_employed_num': 'employed_num',
    'labour_force_status_persons_aged_15_years_census_unemployed_num': 'unemployed_num',
    'labour_force_status_persons_aged_15_years_census_num': 'labour_num',
    'labour_force_status_persons_aged_15_years_census_pc': 'not_labour_pc',
    'labour_force_status_persons_aged_15_years_census_stated_pc': 'labour_not_stated_pc',
    'lbr_frce_stts_prsns_agd_15_yrs_cnss_ttl_ppltn_and_ovr_nm': 'labour_total_num',
    'lbr_frce_stts_prsns_agd_15_yrs_cnss_unmplymnt_rte_pc': 'unemployed_rate'
}