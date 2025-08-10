# Exercises

After getting the app to work, try to make the following improvements:

1. **Add a second graph** that shows the change in Median Household Income over time. You can do this by copy-pasting the
   code that makes the first graph and modifying it slightly. Place the new graph below the total population graph.
1. **Add a second select box** that lets users select which demographic to display (i.e., population or income).
1. **Use the value from the new select box** to determine which graph to show. For example, if the user selects "New York"
   and "Median Household Income", display only the income graph for New York.
1. **Separate the graph and income into tabs** to improve layout. Having both on the same page can be cluttered. Create
   two tabs: one for the graph, one for the dataframe. Streamlit's documentation on tabs is
   [here](https://docs.streamlit.io/develop/api-reference/layout/st.tabs).
   
You can view my solution to these exercises in `solution_app.py`.