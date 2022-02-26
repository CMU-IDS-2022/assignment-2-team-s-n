# Project name

![image](https://user-images.githubusercontent.com/95111909/155821283-3cb6f9e5-11c5-487f-8b91-7350d80e8a1c.png)


The above screenshot shows the Landing Page of our Interactive Dashboard which reflects the Crimes in Chicago (From 2018 to 2020)
-- Because the data for this topic was very huge (2001 to 2020), we have filtered the date of crime to 2018.

**Brief Descritpion:** Dataset reflects the reported incidents of crime in the city of Chicago from 2018 to 2020. We have used Streamlit App to analyze this data in detail.
We have utilized Python (Jupyter Notebook uploaded in the master branch) to clean the data along with complete the exploratory data analysis (EDA). The insights from the data are mentioned in the Jupyter Notebook.

We have downsized the data because of the huge volume. So instead of presenting our dashboard from 2001 to 2020 we have filtered it to 2018 to 2020.


## Project Goals

**Goal: To analyze the crime rate in Chicago from 2018 to 2020** Describe the question that you are enabling a user to answer. The question should be compelling and the solution should be focused on helping users achieve their goals. 

**Question - Can we find specific locations which were popular between 2018 and 2020 where people were attacked the most? This data can be used to avoid future incidents to take place.**

**Answer - In order to answer the above question, we have utilized various graphs and charts (Interactive in nature).**

**Step 1**: Firstly, we divided the Location Types from 100+ locations to 10 broad categories:
The categories include: 'RESIDENCE', 'STREET', 'OFFICE', 'OTHER', 'SCHOOL', 'SIDEWALK','AIRPORT', 'VEHICLE', 'PARKING', 'LIBRARY'
SUMMARY: These categories can help understand which are the most unsafe locations where people are mostly attacked. We can probably take measures to increase safety.

**Step 2**: After dividing our data into the above mentioned categories, we have created interactive charts namely:
1. Number of Arrests happening
2. Top Locations where the crime has taken place
3. Count of crime over the years
4. Number of incidents handled by various Polic Districts

**Step 3**: Users can use these charts to get specific answers. Use various filters available.

## Design

**The design decision was made to keep the dashboard simple and interactive so that it is self explanatory for the users to use it** How did you choose your particular visual encodings and interaction techniques? What alternatives did you consider and how did you arrive at your ultimate choices?

1. The first choice was to create checkboxes so that the dashboard does not look overly cluttered. If the user wants to look for the data, they can click on "Show Table" option. If they want to see the graphs and work around with them, then they can click on "Show the graphs" option.
2. The "Show table" option consists of the sample dataset that we have. It has 5 rows so that the users can get an understanding of what sort of data is available when they are interacting with the charts.
3. The "Show the graphs" option consists of all the interactive charts that our team has created in order to answer the above imposed question.
4. The charts have various filters and dropdown options so that the users can experiment with the underlying data.
5. The charts are also interlinked to one another.



## Development

TODO: **Overview of the Development Process** Describe how the work was split among the team members. Include a commentary on the development process, including answers to the following questions: Roughly how much time did you spend developing your application (in people-hours)? What aspects took the most time?

## Success Story

TODO:  **A success story of your project.** Describe an insight or discovery you gain with your application that relates to the goals of your project.
