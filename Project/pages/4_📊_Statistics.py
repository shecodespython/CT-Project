import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import numpy as np


st.set_page_config(
    page_title="Finance Calculator - Statistics",
    page_icon="💰",
)

st.title("📊 Statistics")

with open('main_style.css') as f:
    css = f.read()

st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)


custom_colors = ['#FD9564']
df1 = pd.read_csv('linkedin.csv')
colors = ['#E3463F', '#B46382', '#FD9564',  '#483D8B','#213890','#D8A7B1', '#4682B4']


#Visualization about Frequency of Job by Location
def frequencyOfJobLocations():
   st.write("### Frequency of Job by Location")
   location_counts = df1['Location'].value_counts()

   filtered_locations = location_counts[location_counts > 5]
   fig = px.bar(
        x=filtered_locations.index,
        y=filtered_locations.values,
        orientation='v',
        color_discrete_sequence=custom_colors
    )
   
   fig.update_layout(
    xaxis=dict(
        tickfont=dict(
            color='white',  
            size=14        
        ),
        title="Frequency",
        title_font = dict(
             color = 'white'
        )
    ),
    yaxis=dict(
        tickfont=dict(
            color='white',  
            size=14         
        ),
        title="Location",
        title_font = dict(
             color = 'white'
        )
    )
    )

   st.write(fig)


#Visualization about Recently Posted Jobs
def jobPostedRecently():
    st.write("### Recently Posted Jobs")
    date_counts = df1['Date'].value_counts()
    
    index = pd.Index(df1['Date'].unique())
    fig = px.scatter(
        x=index,
        y=date_counts,
        color_discrete_sequence=custom_colors
    )

    
    fig.update_layout(
    xaxis=dict(
        tickfont=dict(
            color='white',  
            size=14        
        ),
        title = 'Numbers of Jobs',
        title_font = dict(
             color = 'white'
        ),
    ),
    yaxis=dict(
        tickfont=dict(
            color='white',  
            size=14         
        ),
        title = 'Date',
        title_font = dict(
             color = 'white'
        )
    )
    )


    st.write(fig)


#Visualization about Frequency of Jobs by Company
def FrequencyofJobsbyCompany():
    st.write("### Frequency of Jobs by Company")
    company_counts = df1['Company'].value_counts()

    filtered_companies = company_counts[company_counts > 2]

    fig = px.bar(
        x=filtered_companies.index,
        y=filtered_companies.values,
        orientation='v',
        color_discrete_sequence=custom_colors
    )



    fig.update_layout(
    xaxis=dict(
        tickfont=dict(
            color='white',  
            size=14        
        ),
        title = 'Companies',
        title_font = dict(
             color = 'white'
        )
    ),
    yaxis=dict(
        tickfont=dict(
            color='white',  
            size=14         
        ),
        title = 'Frequency',
        title_font = dict(
             color = 'white'
        )
    )
    )

    st.write(fig)


#Visualization about Frequency of Different Job Statuses
def FrequencyofDifferentJobStatuses():
    st.write("### Frequency of Different Job Statuses")
    status_counts = df1['Status'].value_counts()


    fig = px.pie(values=status_counts.values, names=status_counts.index, color_discrete_sequence=colors)
    
    fig.update_layout(
        font=dict(
            size=14,  
            color='white' 
        )
    )
    
    st.write(fig)



df2 = pd.read_csv('salaries.csv')

#Visualization about Averages Salaries by Jobs
def AverageSalariesbyJob():
    st.write("### Averages Salaries by Jobs")
    fig = px.bar(
        x=df2["Job"],
        y=df2["Average Salary"],
        orientation='v',
        color_discrete_sequence=custom_colors
    )

    fig.update_layout(
    xaxis=dict(
        tickfont=dict(
            color='white',  
            size=14        
        ),
        title = 'Job',
        title_font = dict(
             color = 'white'
        )
    ),
    yaxis=dict(
        tickfont=dict(
            color='white',  
            size=14         
        ),
        title = 'Salary',
        title_font = dict(
             color = 'white'
        )
    )
    )

    st.write(fig)

#Visualization about Minimum Salaries by Jobs
def MinimumSalariesByJob():
    st.write("### Minimum Salaries by Jobs")
    fig = px.bar(
        x=df2["Job"],
        y=df2["Min Salary"],
        orientation='v',
        color_discrete_sequence=custom_colors
    )

    fig.update_layout(
    xaxis=dict(
        tickfont=dict(
            color='white',  
            size=14        
        ),
        title = 'Job',
        title_font = dict(
             color = 'white'
        )
    ),
    yaxis=dict(
        tickfont=dict(
            color='white',  
            size=14         
        ),
        title = 'Salary',
        title_font = dict(
             color = 'white'
        )
    )
    )

    st.write(fig)


#Visualization about Maximum Salaries by Jobs
def MaximumSalariesByJob():
    st.write("### Maximum Salaries by Jobs")
    fig = px.bar(
        x=df2["Job"],
        y= df2["Max Salary"],
        orientation='v',
        color_discrete_sequence=custom_colors
    )

    fig.update_layout(
    xaxis=dict(
        tickfont=dict(
            color='white',  
            size=14        
        ),
        title = 'Job',
        title_font = dict(
             color = 'white'
        )
    ),
    yaxis=dict(
        tickfont=dict(
            color='white',  
            size=14         
        ),
        title = 'Salary',
        title_font = dict(
             color = 'white'
        )
    )
    )

    st.write(fig)


frequencyOfJobLocations()
jobPostedRecently()
FrequencyofJobsbyCompany()
FrequencyofDifferentJobStatuses()

option = st.selectbox(
    'Average, Minimum or Maximum Salary: ',
    ('None','Average Salary', 'Minimum Salary', 'Maximum Salary'))

if option == 'None':
    st.write()
elif option == 'Average Salary':
    AverageSalariesbyJob()
elif option == 'Minimum Salary':
    MinimumSalariesByJob()
else:
    MaximumSalariesByJob()



df = pd.read_csv("finance_jobs.csv")

st.title('Job Selection')

pd.set_option('display.max_columns', None)
pd.set_option('display.expand_frame_repr', False)

# Organize multiselect boxes in two columns for a side-by-side layout
col1, col2 = st.columns(2)

with col1:
        selected_job_title = st.multiselect('Select Job Title', df['JobTitle(Grouped)'].unique())

with col2:
        selected_position = st.multiselect('Select Position', df['Position'].unique())

with col1:
        selected_city = st.multiselect('Select City', df['City'].unique())

with col2:
        selected_status = st.multiselect('Select Status', df['HiringStatus'].unique())

# Debug: Print selected values
#st.write("### Selected Values")
##st.write(f"Selected Job Title: {selected_job_title}")
#st.write(f"Selected Position: {selected_position}")
#st.write(f"Selected City: {selected_city}")
#st.write(f"Selected Status: {selected_status}")

# Filter the DataFrame based on selected values
filtered_df = df[
    (df['JobTitle(Grouped)'].isin(selected_job_title)) &
    (df['Position'].isin(selected_position)) &
    (df['City'].isin(selected_city)) &
    (df['HiringStatus'].isin(selected_status))
]



# Display only specified columns from the filtered DataFrame
if not filtered_df.empty:
    filtered_df = filtered_df.rename(columns={'JobTitle(Grouped)': 'Job Title', 'DateSinceFormated': 'Date of Upload'})

    # Display the number of total jobs after filtering
    st.write("### Number of Jobs Found")
    st.write(len(filtered_df))

    # Display the 10 most recently posted jobs by date
    st.write("### 10 Most Recently Posted Jobs")
    recent_jobs = filtered_df[['Job Title', 'Position', 'Company', 'City', 'HiringStatus', 'Date of Upload']]\
    .sort_values(by='Date of Upload', ascending=False).head(10).reset_index(drop=True)
    st.table(recent_jobs)

    # Top 5 companies that appear most frequently
    top_companies = filtered_df['Company'].value_counts().head(5).reset_index()
    top_companies.columns = ['Company', 'Count']
    st.write("### Top 5 Companies by Opportunity Count")

    fig = px.bar(
        x=top_companies['Company'],
        y= top_companies['Count'],
        orientation='v',
        color_discrete_sequence=custom_colors
    )

    fig.update_layout(
    xaxis=dict(
        tickfont=dict(
            color='white',  
            size=14        
        ),
        title = 'Companies',
        title_font = dict(
             color = 'white'
        )
    ),
    yaxis=dict(
        tickfont=dict(
            color='white',  
            size=14         
        ),
        title = 'Counts of Opportunities',
        title_font = dict(
             color = 'white'
        )
    )
    )

    st.write(fig)
    

    # Number of jobs per city
    city_count = filtered_df['City'].value_counts().reset_index()
    city_count.columns = ['City', 'Count']
    st.write("### Number of Jobs in Each City")
    
    fig = px.bar(
        x=city_count['City'],
        y=city_count['Count'],
        orientation='v',
        color_discrete_sequence=custom_colors
    )

    fig.update_layout(
    xaxis=dict(
        tickfont=dict(
            color='white',  
            size=14        
        ),
        title = 'Location',
        title_font = dict(
             color = 'white'
        )
    ),
    yaxis=dict(
        tickfont=dict(
            color='white',  
            size=14         
        ),
        title = 'Number of Jobs',
        title_font = dict(
             color = 'white'
        )
    )
    )

    st.write(fig)

    # Number of jobs per hiring status
    hiring_status_count = filtered_df['HiringStatus'].value_counts().reset_index()
    hiring_status_count.columns = ['Hiring Status', 'Count']
    st.write("### Number of Jobs by Hiring Status")

    fig = px.pie(df, values=hiring_status_count['Count'], names=hiring_status_count['Hiring Status'], color_discrete_sequence=colors)
   
    fig.update_layout(
        font=dict(
            size=14,  
            color='white' 
        )
    )
   
    st.write(fig)

    # Number of jobs per position type
    # Plotting the count of all position types
    position_count = filtered_df['Position'].value_counts().reset_index()
    position_count.columns = ['Position', 'Count']
    st.write("### Number of Jobs by Position Type")


    fig = px.pie(df, values=position_count['Count'], names=position_count['Position'], color_discrete_sequence=colors)

    fig.update_layout(
        font=dict(
            size=14,  
            color='white' 
        )
    )

    st.write(fig)

    # Top 5 most frequent jobs by date
    top_jobs_by_date = filtered_df['Job Title'].value_counts().head(5).reset_index()
    top_jobs_by_date.columns = ['Job Title', 'Count']
    st.write("### Top 5 Most Frequent Jobs by Date")
    
    fig = px.bar(
        x=top_jobs_by_date['Job Title'],
        y= top_jobs_by_date['Count'],
        orientation='v',
        color_discrete_sequence=custom_colors
    )

    fig.update_layout(
    xaxis=dict(
        tickfont=dict(
            color='white',  
            size=14        
        ),
        title = 'Job',
        title_font = dict(
             color = 'white'
        )
    ),
    yaxis=dict(
        tickfont=dict(
            color='white',  
            size=14         
        ),
        title = 'Frequency',
        title_font = dict(
             color = 'white'
        )
    )
    )

    st.write(fig)
else:
    st.write("The specified job is not found.")