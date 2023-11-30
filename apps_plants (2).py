import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


#Load 
def load_data():
    data = pd.read_csv('sf.csv')
    return data

def descriptive_analysis(data):
    return data.describe()


def plot_distribution(data, column):
    plt.figure(figsize=(10,6))
    sns.histplot(data[column],kde=True)
    plt.title(f"Distribusi {column}")
    plt.xlabel(column)
    plt.ylabel('Frekuensi')
    
    mean_val = data[column].mean()
    plt.axvline(mean_val, color='r', linestyle='dashed',linewidth=2)
    plt.text(mean_val*1.1, plt.ylim()[1]*0.9,f'Rata-rata:{mean_val:.2f}', color='r')
    st.pyplot(plt)       
    
data = load_data()
st.title("Analyze of Agricultural Data")

#Menu
st.sidebar.title('Navigasi')
page = st.sidebar.radio("Menu Navigation",
                        [':house: Title', ':memo: Data Explanation', ':bar_chart: Data Picture',':chart_with_upwards_trend: Data Visualization'])


if page == ':house: Tittle':
    st.header('Welcome to the Agricultural Data Analysis Web :bar_chart:')
    st.write('This application provides analysis of agricultural conditions.')

elif page ==':memo: Data Explanation':
    st.header('Data Explanation')
    st.write("""
    This data contains information regarding agricultural conditions which include:
    - Nitrogen (N)
    - Phosphorus (P)
    - Potassium (K)
    - Temperature
    - Humidity
    - pH
    - Rainfall
    - Plant Labels
    This data can be used to analyze the optimal growing conditions for different crops, monitor farming practices, and make informed decisions to improve crop yield and quality. It provides valuable insights for farmers and agricultural researchers to optimize farming techniques and enhance agricultural productivity.
    
    The following is a sample of raw data used on this website:
    """)
    st.dataframe(data) 

elif page ==':bar_chart: Data Picture':
    st.header('Data Picture')
    st.write('The following is a descriptive analysis of datasetL:')
    st.dataframe(descriptive_analysis(data))
    

elif page ==':chart_with_upwards_trend: Data Visualization':
    st.header('Data Visualization')
    column = st.selectbox('Select Columns For Visualization', data.columns)
    plot_distribution(data,column)
    
    st.write(f"""
    The graph above shows the distribution of column values '{column}'. The red dotted line shows the average value.
    Hal ini dapat membantu dalam memahami sebaran data dan mengidentifikasi nilai yang umum atau tidak biasa.
    """)
    
    
    
    st.write('Plant Label Distribution:')
    plt.figure(figsize=(10,6))
    ax = sns.countplot(data=data, x='label')
    plt.xticks(rotation=45)
    plt.title('Plant Label Distribution')
    plt.xlabel('Label Distribution')
    plt.ylabel('Sum')
    
    st.pyplot(plt)
    
    

    
    
    




            
        





