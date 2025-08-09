# streamlit_tutorial

This repo walks you through creating and deploy a data app in Python using
[Streamlit](https://streamlit.io/). It contains:

  * A small demo app to help you get started with Streamlit. This app contains interesting, real-world data.
  * Instructions for installing and running the demo app on your local machine.
  * Exercises for improving the app. Completing these exercises will help you create your own Streamlit apps in the future.
  * Instructions for deploying your app to the internet. This will let you share the finished app with your friends and family.

You can view a copy of the final app [here](https://arilamstein-tutorial.streamlit.app/).

### Setup

This tutorial requires you to have your own fork of this repo, and a copy of your forked repo on your local machine. It
also requires you to create a virtual environment for the project using [uv](https://docs.astral.sh/uv/).

1. Start by forking this repository
   ([instructions](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo?tool=desktop)).
1. Clone your fork of this repo to your local machine ([instructions](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository)).
1. Install uv ([instructions](https://docs.astral.sh/uv/#installation)). 
1. In your terminal, navigate to the directory that contains this repository and type `uv sync`. This will create a
   virtual environment in the project's `.venv` directory. This virtual environment will contain the same version of
   Python I used when developing this project. It will also contain the same version of each package I used when creating this project. 

The above instructions need to be executed just once.

### Running the app

In order to run the app, you must first activate the virtual environment. To to this, type `source .venv/bin/activate`
in the project directory. 

To run the app, type `streamlit run streamlit_app.py` in the project directory. A browser should open that contains the demo app.

### Learn the basics of Streamlit

1. While the app is running, open up the file ([streamlit_app.py](streamlit_app.py)). Can you guess what each line of
   the app is doing?
1. Streamlit apps can reload after you make changes to the source code - you don't need to stop and restart the app to
   see the result of your changes. 
1. While the app is running, change the text in the
   `st.header` call (line 7) to be "Changes in US State Demographics Over Time". Save the file. The app should now have
   a button in the upper right that says "Rerun". Click it. The app should update with the new text.
1. If you'd like a more structured introduction to Streamlit, take a loook at the free course
   [30 Days of Streamlit](https://blog.streamlit.io/30-days-of-streamlit/). That course was my first introduction to
   Streamlit, and I found it helpful.
   
### Exercises 

The best way to test and improve your knowledge of Streamlit is to tackle some exercises. Open up the file
   [exercises.md](exercises.md) and try to complete the exercises. These exercises cover:
1. Adding a new graph.
1. Adding a new select box for user input.
1. Creating a tab for each graph. 
   
My solution to those exercises is in `solution_app.py`.

### Publish your app

Streamlit makes it easy to deploy your apps. Deploying is free via Streamlit's [Community Cloud](https://streamlit.io/cloud). After you complete the exercises, I encourage you to deploy your finished app and share it with your friends and family. 

When your app is running, there should be a "Deploy" button on the upper right. Click it and follow the instructions to deploy the app.

### Conclusion

I hope this tutorial made you comfortable with the basics of Streamlit. If you found it helpful, please give the repo a star and share it with your friends. 

If you have feedback on the tutorial, you can contact me via my [website](https://arilamstein.com/).