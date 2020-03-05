all_candidates = """SELECT *
                        FROM candidate
                  """

all_candidates_appl = """SELECT *
                            FROM candidate_application
                      """

all_work_experience = """SELECT *
                            FROM work_experience
                      """

all_job_listing = """SELECT *
                        FROM job_listing
                     """

question_1 = """
    SELECT
        COUNT(DISTINCT candidate_id) AS num_candidates_received_invitation,
        COUNT(DISTINCT CASE
                WHEN date_accepted IS NOT NULL THEN candidate_id
            END) AS num_candidates_accepted_invitation
    FROM
        candidate_application

"""

question_2a = """
SELECT
    AVG(CASE
        WHEN date_accepted IS NOT NULL THEN 1
        ELSE 0
    END) AS rate_accepted_invitations
FROM
    candidate_application
"""



question_2b = """
    SELECT
     COUNT(DISTINCT candidate_id)*1.0 / COUNT(DISTINCT CASE
            WHEN date_recommanded IS NOT NULL THEN candidate_id
        END)*1.0 AS percentage_candidates_have_accepted
     FROM
         candidate_application
"""

# workaround to calculate age: https://stackoverflow.com/questions/3123951

data_question_3 = """SELECT id,
                            case
                                when date(birthdate, '+' ||
                                    (strftime('%Y', 'now') - strftime('%Y', birthdate)) ||
                                    ' years') <= date('now')
                                then strftime('%Y', 'now') - strftime('%Y', birthdate)
                                else strftime('%Y', 'now') - strftime('%Y', birthdate) - 1
                            end
                            as age,
                            gender,
                            salary_range
                            FROM candidate
                      """


data_question_4 = """
WITH RECURSIVE
  locationes AS (
            SELECT
               location
            FROM
               candidate
            GROUP BY location
            ORDER BY COUNT(id) DESC
            LIMIT 10),
  acceptations  as (
            SELECT
               candidate_id,
               SUM(CASE
                  WHEN date_accepted IS NOT NULL THEN 1
                  ELSE 0
               END) * 1.0 / COUNT(*) * 1.0 AS acceptation_rate
            FROM
               candidate_application
            GROUP BY candidate_id)

SELECT candidate.id,
     case
        when date(candidate.birthdate, '+' ||
               (strftime('%Y', 'now') - strftime('%Y', candidate.birthdate)) ||
               ' years') <= date('now')
        then strftime('%Y', 'now') - strftime('%Y', candidate.birthdate)
        else strftime('%Y', 'now') - strftime('%Y', candidate.birthdate) - 1
     end
     as age,
     candidate.gender,
     candidate.salary_range,
     candidate.location,
      acceptations.acceptation_rate
     FROM candidate
     INNER join locationes on (candidate.location=locationes.location)
      INNER JOIN acceptations ON(candidate.ID= acceptations.candidate_id)
"""


question_5 = """
        WITH RECURSIVE
          candidate_experience AS (
            SELECT
                candidate_id,
                SUM((JULIANDAY(ending_date) - JULIANDAY(starting_date)) / 30) AS work_experience_months
            FROM
             work_experience
          GROUP BY candidate_id
        )
        SELECT
            AVG(work_experience_months) AS avg_work_experience_months,
            AVG(work_experience_months) / 12 AS avg_work_experience_years
        FROM
            candidate_experience

"""

question_6a = """
        WITH RECURSIVE
          candidate_experience AS (
        SELECT
            candidate_id,
            count(*) as n_jobs
        FROM
            work_experience
        GROUP BY candidate_id
        )
        select avg(n_jobs) as avg_work_experiences
        from candidate_experience
"""

# to be honest, this query is not totally right, because one should count
# not only the experience on current job, but also previuos jobs , on this # calculation I'm actually making average time on the job :(,  but I do.

question_6b = """
            SELECT
                candidate_id,
                industry_name,
                (JULIANDAY(ending_date) - JULIANDAY(starting_date)) / 360 AS work_experience_months
            FROM
             work_experience

"""
