# Project name

![image](https://user-images.githubusercontent.com/95111909/155821283-3cb6f9e5-11c5-487f-8b91-7350d80e8a1c.png)


The above screenshot shows the Landing Page of our Interactive Data Science application that reflects the [Crimes in Chicago (From 2018 to 2020)](https://data.cityofchicago.org/Public-Safety/Crimes-2001-to-present-Dashboard/5cd6-ry5g).
-- Because the dataset was very large (2001 to 2020), we have filtered the date of crime from 2018 to 2020 for the purpose of this assignment.

**Brief Description:** The dataset reflects the reported incidents of crime in the city of Chicago from 2018 to 2020. Detailed analysis of data has been done using the Streamlit app.
Python (Jupyter Notebook uploaded in the master branch) has been used to clean the data and carry out exploratory data analysis (EDA). The insights from the data are mentioned in the Jupyter Notebook.

We have downsized the data because of the huge volume. So instead of presenting our dashboard from 2001 to 2020, we have filtered it to 2018 to 2020.


## Project Goals

**Goal: To analyze the crime rate in Chicago from 2018 to 2020** 
The given dataset contains information such as type of crime, type of location, district, whether an arrest was made, the year when the crime took place, area, and so on. These features will help explore crime rates in-depth and find out the answer to our question.

**Question - Can we find specific locations which were popular between 2018 and 2020 where people were attacked the most? This data can be used to avoid future incidents to take place.**

**Answer - In order to answer the above question, we have utilized various graphs and charts (Interactive in nature).**

**Step 1**: Firstly, we divided the Location Types from 100+ locations into 10 broad categories. The categories include: 
'RESIDENCE', 'STREET', 'OFFICE', 'OTHER', 'SCHOOL', 'SIDEWALK','AIRPORT', 'VEHICLE', 'PARKING', 'LIBRARY'
SUMMARY: These categories can help identify the most unsafe locations where people are most likely to get attacked. Then, effective measures can be taken to increase safety and/or patrolling in these areas by involving the police or local neighborhood watch.

**Step 2**: After dividing data into the aforementioned categories, we created interactive charts to visualize findings. The charts are named as follows:
1. Number of Arrests happening
2. Top Locations where the crime has taken place
3. Count of crime over the years
4. Number of incidents handled by various Polic Districts

**Step 3**: Users can interact with these charts to get specific answers. Filters have been implemented for an in-depth assessment by selecting certain features.

## Design

**The design decision was made to keep the dashboard simple and interactive so that it is self-explanatory and easy to use.** 

1. The first choice was to create checkboxes so that the dashboard does not look overly cluttered. If the user wants to look for the data, they can click on the "Show Table" option. If they want to see the graphs and work around them, then they can click on the "Show the graphs" option.
2. The "Show table" option consists of the sample dataset that we have. It has 5 rows so that the users can get an understanding of what sort of data is available when they are interacting with the charts.
3. The "Show the graphs" option consists of all the interactive charts that our team has created in order to answer the above-imposed question.
4. The charts have various filters and dropdown options so that the users can experiment with the underlying data.
5. The charts are also interlinked to one another.



## Development

**Overview of the Development Process**
Our team consists of a member experienced in data analysis and a beginner. Due to these dynamics, the assignment was completed well before the deadline. Over the course of 3 weeks, we gave it about 3-5 hours per week.

We chose the data set and Shreya performed the necessary cleaning to prepare the data for further analysis. We then brainstormed the questions this analysis could answer and came up with the graphs. Nikita prepared these and Shreya uploaded them on GitHub. Both team members worked on documentation. Coming up with the interactive visualization took the most time, second to deciding the question our analysis aimed to answer.

Overall, this was a fun project that provided an opportunity to perform an introductory analysis of data. Deciding upon the visualizations to answer the question we chose, was a task we enjoyed.

## Success Story

**A success story of your project.**
The assignment mentions scoping of the project as one of the main challenges. We achieved this effectively as we went over the guidelines in the beginning and gradually paced our work over the duration of 3 weeks instead of leaving everything for the eleventh hour. 

Furthermore, the assignment also states not to provide an exhaustive account of our data exploration ("Do not feel obligated to try to convey everything about the data: focus on a compelling subset."). We were able to adhere to this ask by scaling down the very large dataset of Crime in Chicago from 2001 to 2018. It describes the crime incidents between 2018 to 2020 in our application.


