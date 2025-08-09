# streamlit_tutorial

This repo can teach you how to create and deploy data apps in Python using
[Streamlit](https://streamlit.io/). It contains:

  * A small to help you get started with Streamlit. This app contains interesting, real-world data.
  * Instructions for installing and running the sample app on your local machine.
  * Exercises to improve the app. Completing these exercises is where most of your learning will happen.
  * Instructions for deploying your app to the internet, so that you can share the finished app with friends and family.

The final app you build will look like this:

### Install the software

This tutorial requires you to have your own fork of this repo, and a copy of your forked repo on your local machine. It
also requires you to have [uv](https://docs.astral.sh/uv/) installed.

1. Start by forking this repository
   ([instructions](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo?tool=desktop)).
1. Clone your fork of this repo to your local machine ([instructions](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository)).
1. Install uv ([instructions](https://docs.astral.sh/uv/#installation)). 

### Run the app locally

The core of this tutorial is a set of exercises where I ask you to modify the demo app. Before you can work on the exercises,
you must first run the demo app. And before you can do that, you must first create a virtual environment for the
project.

1. In the project directory type `uv sync`. This will create a virtual environment with the project's dependencies in `.venv`. 
1. In the project directory type `source .venv/bin/activate`. This will activate the project's virtual environment. 
1. In the project directory type `streamlit run streamlit_app.py`. 

This last command should cause a browser to open with the app running. It should look like this: 

If you see this, then congratulations! The setup is complete and you can now focus on learning Streamlit :)

### Learn the basics of Streamlit

1. While the app is running, open up the file ([streamlit_app.py](streamlit_app.py)). Can you guess what each line of
   the app is doing?
1. Streamlit apps can reload after you make changes to the source code - you don't need to stop and restart the app. 
1. While the app is running, change the text in the
   `st.header` call (line 7) to be "Changes in US State Demographics Over Time". Save the file. The app should now have
   a button in the upper right that says "Rerun". Click it. The app should update with
   the new text.
1. If you'd like a more structured introduction to Streamlit, take a loook at the free course
   [30 Days of Streamlit](https://blog.streamlit.io/30-days-of-streamlit/) - that was my first introduction to
   Streamlit, and I got a lot out of it.
   
### Exercises 

The best way to test and improve your knowledge of Streamlit is to tackle some exercises. Open up the file
   [exercises.md](exercises.md) and try to tackle the exercises. These exercises cover:
1. Adding a new graph.
1. Adding a new select box for user input.
1. Creating a tab for each graph. 
   
My solution to those exercises is in `solution_app.py`.

### Publish your app

Streamlit makes it easy to deploy their apps. Deploying is free via their [Community
Cloud](https://streamlit.io/cloud). When you complete the exercises, I encourage you to deploay your finished app and share it with your friends and family. 

1. When your app is running, there should be a "Deploy" button on the upper right. Click it and follow the instructions
   to deploy the app.

### Conclusion

I hope this tutorial made you comfortable with the basics of Streamlit. If you found it helpful, please give the repo a star and share it with your friends. 

If you have feedback on
the tutorial, you can contact me via my [website](https://arilamstein.com/).