import pandas as pd

import src.utilis as utl
import src.query as q
import matplotlib.pyplot as plt

print("Making responses...")

# 1) Provide the total number of candidates that have received an invitation
# and the total number of candidates that have accepted an invitation.

response_1 = utl.run_query(q.question_1)

# 2) What is the total rate of accepted invitations? What percentage of
# candidates have accepted an invitation?

response_2a = utl.run_query(q.question_2a)

response_2b = utl.run_query(q.question_2b)

# 3) What is the distribution of candidates by age? What is the distribution
# of candidates by gender? What is the distribution of candidates by
# salary range?

data_q3 = utl.run_query(q.data_question_3)

response_3a = utl.get_var_distibution(data_q3, "age")
response_3b = utl.get_var_distibution(data_q3, "gender")
response_3c = utl.get_var_distibution(data_q3, "salary_range")

del data_q3

#4) Consider the distinct segments age, gender, salary range and candidate residence city (only the first
# 10 most populated cities in the db). Are there significant differences of acceptance rate within such
# segments? Argue the answer.

data_q4 = utl.run_query(q.data_question_4)


response_4a = utl.get_var_groupby_avg(data_q4, "age", "acceptation_rate")
response_4b = utl.get_var_groupby_avg(data_q4, "gender", "acceptation_rate")
response_4c = utl.get_var_groupby_avg(data_q4, "salary_range", "acceptation_rate")
response_4d = utl.get_var_groupby_avg(data_q4, "location", "acceptation_rate")


#5) What is the average work experience time?
response_5 = utl.run_query(q.question_5)

#6a) How many work experiences a candidate have on average?
response_6a = utl.run_query(q.question_6a)
#6b) What is the distribution by industry of work experience

data_q6 = utl.run_query(q.question_6b)

response_6b = dict()
for industry_name, data_industry in data_q6.groupby("industry_name"):

    bins,freq,_ = plt.hist(data_industry["work_experience_months"])

    response_6b[industry_name] = {'bins':bins, 'freq':freq}

    plt.title('Histogram of workexperience for {0}'.format(industry_name))
    plt.ylabel('Count')
    plt.xlabel('Workexperience in Years')
    plt.show()

response_6b = pd.DataFrame(response_6b).T
response_6b["industry_name"] = response_6b.index
response_6b = response_6b[["industry_name", "bins", "freq"]]


# 7) What is the average number of candidates that have accepted an
# invitation per post for the jobs
# published in the month of January 2019? Plot the cohort time line (on job # published) by month.

