# Analysis   
First I analyzed the different format of input for each year and below are some findings.

From 2014, Office of Foreign Labor Certification changed the format name of columns inside the disclosure files.
Till 2014:	 
LCA_CASE_EMPLOYMENT_END_DATE	LCA_CASE_EMPLOYER_NAME	LCA_CASE_EMPLOYER_ADDRESS	LCA_CASE_EMPLOYER_CITY	LCA_CASE_EMPLOYER_STATE	LCA_CASE_EMPLOYER_POSTAL_CODE	LCA_CASE_SOC_CODE	LCA_CASE_SOC_NAME	LCA_CASE_JOB_TITLE	LCA_CASE_WAGE_RATE_FROM	LCA_CASE_WAGE_RATE_TO	LCA_CASE_WAGE_RATE_UNIT	FULL_TIME_POS	TOTAL_WORKERS	LCA_CASE_WORKLOC1_CITY	LCA_CASE_WORKLOC1_STATE	PW_1	PW_UNIT_1	PW_SOURCE_1	OTHER_WAGE_SOURCE_1	YR_SOURCE_PUB_1	LCA_CASE_WORKLOC2_CITY	LCA_CASE_WORKLOC2_STATE	PW_2	PW_UNIT_2 PW_SOURCE_2	OTHER_WAGE_SOURCE_2	YR_SOURCE_PUB_2	LCA_CASE_NAICS_CODE

From 2014:
CASE_NUMBER	CASE_STATUS	CASE_SUBMITTED	DECISION_DATE	VISA_CLASS	EMPLOYMENT_START_DATE	EMPLOYMENT_END_DATE	EMPLOYER_NAME	EMPLOYER_BUSINESS_DBA	EMPLOYER_ADDRESS	EMPLOYER_CITY	EMPLOYER_STATE	EMPLOYER_POSTAL_CODE	EMPLOYER_COUNTRY	EMPLOYER_PROVINCE	EMPLOYER_PHONE	EMPLOYER_PHONE_EXT	AGENT_REPRESENTING_EMPLOYER	AGENT_ATTORNEY_NAME	AGENT_ATTORNEY_CITY	AGENT_ATTORNEY_STATE	JOB_TITLE	SOC_CODE	SOC_NAME	NAICS_CODE	TOTAL_WORKERS	NEW_EMPLOYMENT	CONTINUED_EMPLOYMENT	CHANGE_PREVIOUS_EMPLOYMENT	NEW_CONCURRENT_EMPLOYMENT	CHANGE_EMPLOYER	AMENDED_PETITION	FULL_TIME_POSITION	PREVAILING_WAGE	PW_UNIT_OF_PAY	PW_WAGE_LEVEL	PW_SOURCE	PW_SOURCE_YEAR	PW_SOURCE_OTHER	WAGE_RATE_OF_PAY_FROM	WAGE_RATE_OF_PAY_TO	WAGE_UNIT_OF_PAY	H1B_DEPENDENT	WILLFUL_VIOLATOR	SUPPORT_H1B	LABOR_CON_AGREE	PUBLIC_DISCLOSURE_LOCATION	WORKSITE_CITY	WORKSITE_COUNTY	WORKSITE_STATE	WORKSITE_POSTAL_CODE	ORIGINAL_CERT_DATE


# Assumptions     

1. Input files are converted from xlsx  to csv format   
2. To calculate two metrics: **Top 10 Occupations** and **Top 10 States**, we will need few columns such as CASE_NUMBER, CASE_STATUS, OCCUPATION_NAME and STATE.   
3. From the initial analysis only two different names for each columns is present.  
4. In future the column names will not change. However, the position of column can change.    



# Approach  
1. Read from different format of csv to fixed format data structure only for 'CERTIFIED' cases.
2. Iterate through each row  and take the Occupation Name and State in default dict and increase count
3. Insert the data structure into .txt files

# Results  

Tested the code with  ./insight_testsuite/run_tests.sh and it is working fine.
However, the shell script is getting errored due to one condition:
diff: ./insight_testsuite/temp/output/top_10_occupations.txt: No such file or directory
diff: ./insight_testsuite/tests/test_1/output/top_10_occupations.txt: No such file or directory
-f ./insight_testsuite/temp/output/top_10_occupations.txt
[PASS]: test_1
diff: ./insight_testsuite/temp/output/top_10_states.txt: No such file or directory
diff: ./insight_testsuite/tests/test_1/output/top_10_states.txt: No such file or directory
[PASS]: test_1 top_10_states.txt
[Wed, Oct 24, 2018  8:42:46 PM] 1 of 1 tests passed
./insight_testsuite/run_tests.sh: line 112: ./insight_testsuite/results.txt: No such file or directory



