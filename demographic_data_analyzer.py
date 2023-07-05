import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts()

    # What is the average age of men?
    average_age_men = round(df.loc[df['sex'] == 'Male', 'age'].mean(), 1)

    # What is the percentage of people who have a Bachelor's degree?
    education = df['education'].value_counts()
    percentage_bachelors = round(education['Bachelors'] / df.shape[0] * 100, 1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?
    # I got the solution for this part of the question from: https://replit.com/@MYSan7/demographic-data-analyzer#demographic_data_analyzer.py 

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education = df[df.education.isin(['Bachelors', 'Masters', 'Doctorate'])]
    lower_education = df[~df.education.isin(['Bachelors', 'Masters', 'Doctorate'])]

    # percentage with salary >50K
    higher_education_rich = round((higher_education[higher_education.salary == '>50K'].salary.count() / higher_education.shape[0]) * 100, 1)
    lower_education_rich = round((lower_education[lower_education.salary == '>50K'].salary.count() / lower_education.shape[0]) * 100, 1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = df[df['hours-per-week'] == min_work_hours]

    rich_percentage = round(num_min_workers[num_min_workers.salary == '>50K'].salary.count() / num_min_workers.shape[0] * 100, 1)

    # What country has the highest percentage of people that earn >50K?
    number_of_people = df.groupby('native-country').count()
    number_of_people['total'] = number_of_people['age']
    number_of_people = number_of_people['total']
    
    number_of_highearners = df[df['salary'] == '>50K'].groupby('native-country').count()
    # This line was to clean up the columns, if there is a better way to do this please let me know!
    number_of_highearners['counter'] = number_of_highearners['age']
    number_of_highearners = number_of_highearners['counter']
    
    number_of_highearners_percent = number_of_highearners / number_of_people * 100

    highest_earning_country = number_of_highearners_percent.idxmax()
    highest_earning_country_percentage = round(number_of_highearners_percent.max(), 1)

    # Identify the most popular occupation for those who earn >50K in India.
    india_people = df[(df['native-country'] == 'India')]
    india_highearners = india_people[india_people.salary == '>50K']
    india_highearning_jobs = india_highearners.groupby(by = 'occupation').count()

    # This line was to clean up the columns, if there is a better way to do this please let me know!
    india_highearning_jobs['count'] = india_highearning_jobs['age']
    india_highearning_jobs = india_highearning_jobs['count']
    top_IN_occupation = india_highearning_jobs.idxmax()

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }