# -*- coding: utf-8 -*-
"""
Created on Fri Feb 18 13:46:54 2022

@author: shreya & nikita
Team N&S
"""

#REFERENCE - Motivation from Lecture Code

from re import U
import streamlit as st
import pandas as pd
import altair as alt
import os

#os.chdir("C:\Carnegie Mellon University\Spring22\Interactive Data Science\HW2_Streamlit")
#print("Directory changed")
#REFERENCE - https://towardsdatascience.com/how-to-create-interactive-and-elegant-plot-with-altair-8dd87a890f2a

import webbrowser

@st.cache
def load_data():
    """
    Write 1-2 lines of code here to load the data from CSV to a pandas dataframe
    and return it.
    """
    #REMOVING THE INDEX COLUMN
    df = pd.read_csv("Crime_2001_data_prepared.csv", index_col=[0], nrows=50000)
    return df
    #pass


# MAIN CODE

st.title("Crimes in Chicago (2018 to 2020)")
st.header("Shreya Bedi & Nikita Jyoti")
with st.spinner(text="Loading data..."):
    df = load_data()
    
    data = df[['ID', 'Primary Type','Location Description Modified','Year','Police Districts','Arrest']].copy()
    
    #REFERENCE - https://stackoverflow.com/questions/62315591/altair-select-all-values-when-using-binding-select
    location_list = list(data['Location Description Modified'].unique()) + [None]

    
    input_dropdown = alt.binding_select(options=location_list)
    selection = alt.selection_single(fields=['Location Description Modified'], bind=input_dropdown, name='New')
    
    
    #NOT TAKING OR SHOWING THE NULL VALUES IN THE DATASET
    st.header("Welcome to our Interactive Dashboard..")
    st.header("Some information about the data ..")
    st.write("Dataset reflects the reported incidents of crime in the city of Chicago from 2018 to 2020.")
    st.write("Brushes have been added to all the visuals. Feel free to explore!")
        
   #Creating checkbox for showing the table. Sample Dataset:
    st.header("Sample Dataset")
    st.write("Click on the checkbox to see the data")
    if st.checkbox('Show Table'):
        selected_rows = df[~df.isnull()]
        st.dataframe(selected_rows.head(5))
        
    st.write("If we look at the data closely, out of all the columns that we had in the dataset, we chose the most important ones that can help us understand the exact nature of the crime. The ID column describes the unique number which is assigned to the crime incident. Primary Type column will help understand what sort of a crime was it. For example - Was it theft, deceptive practice, and so on.. Location description column will help understand the exact location where the crime took place. We have divided this column into 10 major categories. Arrest columns will decribe if the person who committed the crime was arrested or not. Feel free to check the graphs below to help answer these questions. Police district tells the exact district where the incident took place and who handled it")
    
    #CREATING BRUSHES FOR DIFFERENT USES
    arrest_brush = alt.selection_multi(fields=['Arrest'])
    location_brush = alt.selection_multi(fields=['Location Description Modified'])
    district_brush = alt.selection_multi(fields=['Police Districts'])
    year_brush = alt.selection_multi(fields=['Year'])


    #Code starts from here for the interactive graphs
    st.header("Interactive Graphs")
    st.write("NOTE: All of the visualizations can be enlarged using the pinch arrow icon placed next to the top right corner of each chart. Additionally, you can click on the 3 dots for more export options. Each chart also incorporates an on-hover tooltip to provide further interactivity.")
    if st.checkbox('Show the graphs'):
        
        #CHART 1:
        
        #Creating a selection box:
        st.header("Arrested? (Change True or False)")
        arrests_selectbox = st.selectbox("Lets see the Arrest vs Non-Arrest Count", data['Arrest'].unique())
        arrest_df = data[data['Arrest'] == arrests_selectbox]

        #Showing the length of the number of arrests that happened vs did not happen
        st.write("Feel free to choose True and False from the dropdown. True stands for the total number of arrests that happened. False stands for the actual incident taking place but unfortunately arrest did not take place.")
        st.write(len(arrest_df))
        st.write("")
        st.write("According to our analysis after looking that the True vs False counts, more incidents did not lead to an arrest compared to the number of arrests happening. This data is strictly from 2018 to 2020. One reason why arrests did not happen might be because the incidents were not of that extreme crime level and were pardoned with a fine and/or a court hearing. Another reason can be that police was not able to locate the culprit behind crimes and thus the case remians open. A third reason could be that the case was transferred to another police district.")
        
        st.write("Now, lets take a look at the primary type of crime that happened where arrest took place vs did not take place.")
        st.header("Primary Type of Crime")
        

        primary_type = alt.Chart(data).transform_filter(arrest_brush).mark_bar().encode(
        y=alt.Y('count()'),
        x=alt.X('Primary Type', sort='-y'),
        color = alt.Color('Arrest'),
        tooltip =['Year','Police Districts','Location Description Modified', 'Arrest']
        ).interactive(
        ).transform_window(
        rank='rank(count())',
        sort=[alt.SortField('count()', order='descending')]
        ).properties(
        width=1000,
        height=500
        ).interactive().add_selection(arrest_brush)
        
        st.altair_chart(primary_type, use_container_width=True)
        
        
        st.write("Click on various Primary Types to see more detailed view. The graph is interactive in nature.")
        st.write("The two colors - Orange and Blue help us distinguish if an arrest was made or not. Clearly looking at the graph we can see that between 2018 and 2020 many arrests were not made. Looking closely many arrests were made for Narcotics possession or usage. Alarmingly, many theft type of crime incidents did not lead to an arrest. This is something that the authorities can work towards -- prevent crime incidents from happening in the future according to the statistics. As this chart provides a breakdown according to category, the police can draw clear insights and pick a category or two where processes could be improved.")
        
        # ------------------------------------------------------------------------------------------------------------
        # MAKING CODE DISTINCTION FOR DIFFERENT SET OF RELATED GRAPHS
        # ------------------------------------------------------------------------------------------------------------
        
        #CHART 2:
            
        st.header("Location Selection")
        st.write("Change the Location Type to see how many arrests were made vs not made in places that fall under that type.")
        location_selectbox = st.selectbox("Location Type", data['Location Description Modified'].unique())
        location_df = data[data['Location Description Modified'] == location_selectbox]
        
        st.write("Feel free to choose the different location types where crimes were committed. The count below shows how many incidents took place at the selected location type. Again, the blue bar indicates arrests not made, whereas, orange represents the arrests made.")
        st.write(len(location_selectbox))
        st.write("")
    
        
        #We want to firstly understand the number of arrests made vs not made:  
        st.write("Change the Location to see how many arrests were made vs not made in a given location")
        arrest = alt.Chart(location_df).transform_filter(arrest_brush).mark_bar().encode(
        y=alt.Y('count()'),
        x=alt.X('Arrest', sort='-y'),
        color = alt.Color('Arrest'),
        tooltip =['Year','Police Districts','Location Description Modified']
        ).interactive(
        ).transform_window(
        rank='rank(count())',
        sort=[alt.SortField('count()', order='descending')]
        ).properties(
        width=800,
        height=300
        ).interactive().add_selection(arrest_brush)

        st.altair_chart(arrest, use_container_width=True)
        
        st.write("Analyzing the chart, arrests were not made for most crimes committed in all of the various types of locations. Only a few locations exist such as - SIDEWALKS, VEHICLES, where arrests made were more in number than the cases where they were not.")
        st.write("Conclusion from this graph analysis - Stricter security is required at other locations. Perhaps, the current resources and measures in place are not enough to gather sufficient evidence required for making an arrest. An example could be installing more CCTV cameras and increasing surveillance.")
       
        # ------------------------------------------------------------------------------------------------------------
        # MAKING CODE DISTINCTION FOR DIFFERENT SET OF RELATED GRAPHS
        # ------------------------------------------------------------------------------------------------------------
    
        #Altair chart to show the number of crime at different locations
        st.header("Top Locations (Where crime was committed)")
        st.write("Select an option from the drop down menu below to see filtered results.")
        
        location = alt.Chart(data).transform_filter(location_brush).mark_bar().encode(
        y=alt.Y('count()'),
        x=alt.X('Location Description Modified', sort='-y'),
        color = alt.Color('Location Description Modified'),
        tooltip =['Year','Police Districts','Location Description Modified']
        ).interactive(
        ).transform_window(
        rank='rank(count())',
        sort=[alt.SortField('count()', order='descending')]
        ).properties(
        width=900,
        height=300
        ).add_selection(
        selection
        ).transform_filter(
        selection
        ).interactive().add_selection(location_brush)
            
        st.altair_chart(location, use_container_width=True)
        
        st.write("Choosing null in the graph means that no specific Location Description was chosen. This will show all the types of locations available. However, feel free to choose any one specific Location Type and hover over to understand and get more detailed analysis of the data points. The graph shows total number of crimes committed by the location type.")

        st.write("From an initial overview it seems like the chart shows data for only 2018. This is only natural since this is the year with the highest number of cases (~40k), whereas, 2019 and 2020 had much lesser cases in comparison. This may be due to the lockdown following COVID-19 outbreak where supplies were limited and stores were closed. Our analysis shows that mostly crime took place at the following locations - RESIDENCE, STREET or SIDEWALKS. These could be identified as high risk zones where a crime is most likely to occur. The police could increase surveillance here.")

        # ------------------------------------------------------------------------------------------------------------
        # MAKING CODE DISTINCTION FOR DIFFERENT SET OF RELATED GRAPHS
        # ------------------------------------------------------------------------------------------------------------
        
        #Altair chart to show the number of crime in various years
        st.header("Most popular location each year")
        st.write("Try changing the year to see specific count")
        
        #Created a year selection box for the below visual
        year_selectbox = st.selectbox("Yearly Count of Incidents", data['Year'].unique())
        year_df = data[data['Year'] == year_selectbox]
        
        st.write(len(year_df))
        st.write("")
        st.write("The count above shows the number of crime incidences took place in a given year. Feel free to see the count for different years")
        
        # Altair chart to show the number of crime in various years and locations
        year_wise_location = alt.Chart(year_df).transform_filter(location_brush).mark_bar().encode(
        x=alt.X('Location Description Modified'),
        y=alt.Y('count()'),
        color = alt.Color('Year'),
        tooltip =['Year','Police Districts','Location Description Modified']
        ).interactive(
        ).transform_window(
        rank='rank(count())',
        sort=[alt.SortField('count()', order='descending')]
        ).properties(
        width=800,
        height=300
        ).interactive().add_selection(location_brush)
            
        st.altair_chart(year_wise_location, use_container_width=True)
    
        st.write("Concluding our analysis for this graph: ")
        st.write("Every year (2018,2019,2020), most of the crime incidents take place either on the Streets or within the house of an individual. Measures should be taken to understand and help prevent these crimes in the future.")
    
        # ------------------------------------------------------------------------------------------------------------
        # MAKING CODE DISTINCTION FOR DIFFERENT SET OF RELATED GRAPHS
        # ------------------------------------------------------------------------------------------------------------
        
        st.header("Number of Crime Incidents handled by a Police District")
        st.write("Try changing the year to see specific count")
        
        #Altair chart that helps understand how many incidents were handled by the various districts.
        st.write("This graph shows the number of crime incidents handled by various Police Districts. This can help us analyze which are the districts where most number of crimes took place between 2018 and 2020.")
        police_districts = alt.Chart(year_df).transform_filter(district_brush).mark_point().encode(
        alt.X('Police Districts', scale=alt.Scale(zero=False)),
        alt.Y('count()', scale=alt.Scale(zero=False)),
        tooltip =['Year','Police Districts','Location Description Modified']
        ).properties(
        width=800,
        height=300
        ).interactive().add_selection(district_brush)
            
        st.altair_chart(police_districts, use_container_width=True)
        
        st.write("Feel free to click on any Pointer District pointer in the graph. You can even hover over the various points to see more detailed information about the data points. This graph also supports zoom in and zoom out operations in the minimized view itself.")
        
        
        
        st.header("Conclusion")
        st.write("Based on the visualizations above, we can assess the crime rate in Chicago between 2018 and 2020. We see, (particularly from Graph 4) that the number of crimes committed have reduced from 2018 (about 40,000) to about 5000 in 2019 and finally about 4000 in the year 2020. Detailed analysis of location specific crime or arrest rate can also be carried out.")
        st.write("Overall, this was a fun project that provided an opportunity to perform an introductory analysis of data. Deciding upon the visualizations to answer the question we chose, was a task we enjoyed. We hope you liked our project. THANK YOU!")        
        
        
        
        
        
        
        
        




