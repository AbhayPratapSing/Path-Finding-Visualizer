from tkinter import CENTER, Menu
from turtle import width
from click import style
import streamlit as st
import pygame
from Astr import main as Astr

WIDTH = 800

st.title( 'Path Finding Visualizer')
st.image('maze1.jpg')
#st.subheader('Tag Line')


Astr(WIDTH)
def overview():
    st.header('Path Finding Algorithms')
    st.markdown('Path finding algorithms build on top of graph search algorithms and explore routes between nodes, starting at one node and traversing through relationships until the destination has been reached. These algorithms find the cheapest path in terms of the number of hops or weight.', unsafe_allow_html=False)
    st.image('maze3.gif')
    st.header('Features')
    

def main():
    options = ('Visualize Algorithm', 'View Algorithm', 'Tools Used')
    selOption = st.radio("Choose an Option",options)

    if(selOption==options[0]):
        AlgoOptions()
    elif(selOption==options[1]):
         View_Algorithm()
    elif(selOption==options[2]):
         Tool_Used()
  
def AlgoOptions():
    st.header('1. A Star Algorithm')
    astr = st.button('Visualize A Star')
    if(astr):
        Astr(WIDTH)
    st.header('2. Dijkstra Algorithm')
    dijkstra = st.button('Visualize Dijkstra ')
    st.header('3. Swarm Algorithm')
    Swarm = st.button('Visualize Swarm ')
    st.header('4. Breadth-first Search')
    bfs = st.button('Visualize BFS ')
    st.header('5. Depth-first Search')
    dfs = st.button('Visualize DFS ')

def View_Algorithm():
    st.header('1. A Star Algorithm')
    st.header('2. Dijkstra Algorithm')
    st.header('3. Swarm Algorithm')
    st.header('4. Breadth-first Search')
    st.header('5. Depth-first Search') 
    
def Tool_Used():
    st.header('Developer')
    st.text('* Web Browser (Google Chrome, Firefox )')
    st.text('* Python 3.9 or Above')
    st.text('* Vs code')
    st.text('* Frontend Framework – Streamlit')
    st.header('Client')
    st.text('* Browser		:	Google Chrome, Mozilla Firefox')
    st.text('* Operating System	:	Any O.S. Windows/Linux')


sidebar = st.sidebar
sidebar.header('Select Algo')
pages = ['OverView', 'Main']
page = sidebar.selectbox('Choose an Option', pages)
if(page == pages[0]):
    overview()
elif(page == pages[1]):
    main()
    