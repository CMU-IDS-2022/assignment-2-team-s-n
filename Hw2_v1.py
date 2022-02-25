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

os.chdir("C:\Carnegie Mellon University\Spring22\Interactive Data Science\HW2_Streamlit")
print("Directory changed")


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

st.title("Crimes in Chicago (2001 to 2020)")
with st.spinner(text="Loading data..."):
    df = load_data()
    
    data = df[['ID', 'Block', 'Primary Type','Location Description Modified','Year','Police Districts','Arrest','Latitude','Longitude']].copy()
    
    #REFERENCE - https://stackoverflow.com/questions/62315591/altair-select-all-values-when-using-binding-select
    location_list = list(data['Location Description Modified'].unique()) + [None]

    
    input_dropdown = alt.binding_select(options=location_list)
    selection = alt.selection_single(fields=['Location Description Modified'], bind=input_dropdown, name='Location')
    
   
    
    #NOT TAKING OR SHOWING THE NULL VALUES
    st.header("Welcome to our Interactive Dashboard..")
    st.header("Some information about the data ..")
    st.text("Dataset reflects the reported incidents of crime in the city of Chicago from 2001 to 2020.")
    st.text("Brushes have been added to all the visuals. Feel free to explore!")
        
    
   #Lets keep a checkbox for showing the table. Sample Dataset:
    st.header("Sample Dataset")
    st.text("Click on the checkbox to see the data")
    if st.checkbox('Show Table'):
        selected_rows = df[~df.isnull()]
        st.dataframe(selected_rows.head(5))
    
    #LETS TRY CREATING BRUSHES
    arrest_brush = alt.selection_multi(fields=['Arrest'])
    location_brush = alt.selection_multi(fields=['Location Description Modified'])
    district_brush = alt.selection_multi(fields=['Police Districts'])
    year_brush = alt.selection_multi(fields=['Year'])


    st.header("Interactive Graphs")
    if st.checkbox('Show the graphs'):
        
        
        #Creating a selection box:
        st.header("Arrested? (Change True or False)")
        arrests_selectbox = st.selectbox("Lets see the Arrest vs Non-Arrest Count", data['Arrest'].unique())
        arrest_df = data[data['Arrest'] == arrests_selectbox]
        
        
        st.write(len(arrest_df))
        st.write("")
        
        location_selectbox = st.selectbox("Location Counts", data['Location Description Modified'].unique())
        location_df = data[data['Location Description Modified'] == location_selectbox]
        
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

    #REFERENCE - https://towardsdatascience.com/how-to-create-interactive-and-elegant-plot-with-altair-8dd87a890f2a

        
    #Altair chart to show the number of crime at different locations
        
        
        st.header("Top Locations (Where the incident occurred)")
        st.write("Select the options from the drop down below")
        
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
        width=800,
        height=300
        ).add_selection(
        selection
        ).transform_filter(
        selection
        ).interactive().add_selection(location_brush)
            
        st.altair_chart(location, use_container_width=True)

        
    # # Altair chart to show the number of crime in various years
        
        
        
            
        st.header("Most Crimes Across Years")
        st.write("Click on any year to specifically see the count. Brush has been created")
        
        
        year = alt.Chart(data).transform_filter(year_brush).mark_bar().encode(
        y=alt.Y('count()'),
        x=alt.X('Year', sort='-y'),
        color = alt.Color('Year'),
        tooltip =['Year','Police Districts','Location Description Modified']
        ).interactive(
        ).transform_window(
        rank='rank(count())',
        sort=[alt.SortField('count()', order='descending')]
        ).properties(
        width=800,
        height=300
        ).interactive().add_selection(year_brush)
            
        st.altair_chart(year, use_container_width=True)
  
        
        st.header("Most popular location each year")
        st.write("Try changing the year to see specific count")
        
        
        year_selectbox = st.selectbox("Yearly Count of Incidents", data['Year'].unique())
        year_df = data[data['Year'] == year_selectbox]
        
        st.write(len(year_df))
        st.write("")
        
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
    
    
    
        st.header("Number of Crimes handled by a Police District")
        st.write("Try changing the year to see specific count")
        
        
    
    #Altair chart that helps understand the most popular location each year
        police_districts = alt.Chart(year_df).transform_filter(district_brush).mark_point().encode(
        alt.X('Police Districts', scale=alt.Scale(zero=False)),
        alt.Y('count()', scale=alt.Scale(zero=False)),
        tooltip =['Year','Police Districts','Location Description Modified']
        ).properties(
        width=800,
        height=300
        ).interactive().add_selection(district_brush)
            
        st.altair_chart(police_districts, use_container_width=True)
        
        
        
        
        
        
        
        
        
        
        
        




