# streamlit_tutorial

This repo walks you through creating and deploying a data app in Python using
[Streamlit](https://streamlit.io/). It contains:

  * A small demo app to help you get started with Streamlit. This app contains interesting, real-world data.
  * Instructions for installing and running the demo app on your local machine.
  * Exercises for improving the app. These exercises cover common real-world tasks that come up when
    working with Streamlit.
  * Instructions for deploying your app to the internet. This will let you share your finished app with friends and family.

You can view a copy of the final app [here](https://arilamstein-tutorial.streamlit.app/).

### Prerequisites

This tutorial assumes that you have some familiarity with the terminal / command line. 

Prior exposure to git, github and Python would be helpful but is not required. 

You do not need to have Python installed on your machine prior to starting this tutorial. 

### Setup

1. Fork this repository in github
   ([instructions](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo?tool=desktop)).
1. Clone your fork of this repo to your local machine ([instructions](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository)).
1. Install [uv](https://docs.astral.sh/uv/) ([instructions](https://docs.astral.sh/uv/#installation)). 
1. In your terminal, navigate to the directory that contains this repository and type `uv sync`. This will create a
   virtual environment in the project's `.venv` directory.  

The above instructions need to be executed just once.

### Running the app

After completing the steps in the "Setup" section you can now run the demo app.

1. First activate the project's virtual environment: In the terminal, navigate to the project's directory and type `source .venv/bin/activate`.
1. Type `streamlit run streamlit_app.py` in the project's directory. 

A browser should open that contains the demo app. It should look like this:
<p align="center">
  <img src="screenshot-demo-app.png" alt="Demo App Screenshot" width="50%">
</p>


### Learn the basics of Streamlit

1. While the app is running, open up the file [streamlit_app.py](streamlit_app.py). Can you guess what each line of
   the file does?
1. Streamlit apps can reload after you make changes to the source code. That is, you don't need to stop and restart the app to
   see the result of your changes. 
1. While the app is running, change the text in the
   `st.header` call (line 7) to be "Changes in US State Demographics Over Time". Save the file. 
1. The app should now have
   a button in the upper right that says "Rerun". Click it. The app should update with the new text.
1. If you'd like a more structured introduction to Streamlit, I recommend the free course
   [30 Days of Streamlit](https://blog.streamlit.io/30-days-of-streamlit/).
   
### Exercises 

The best way to test and improve your knowledge of Streamlit is to tackle some exercises. Open up the file
   [exercises.md](exercises.md) and try to complete the exercises. They cover:
1. Adding a new graph.
1. Adding a new select box for user input.
1. Creating tabs. 
   
My solution to these exercises is in `solution_app.py`.

### Publish your app

Streamlit makes it easy to share your app with others. When your app is running, there should be a "Deploy" button in
the upper right. Click it and follow the instructions that appear.

After you finish the exercises, I encourage you to deploy your app and share the link with friends and family!

### Conclusion

You have now cloned, modified and deployed your first Streamlit app!.

If you found this tutorial helpful, please give the repo a star and share it with your friends. 

If you have feedback on the tutorial, you can contact me via my [website](https://arilamstein.com/).