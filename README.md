# InsideAI Assignment 1

The code procedure works like this,

1) Download the IMBD dataset from Kaggle and use preprocess.py file to preprocess the IMBD dataset, at the preprocess.py will give you dataset.jason
2) The dataset.json is gereated from preprocess.py, which has the names and place as jason objects and entries are from Named entities of  IMBD dataset
3) Index html is written which take Name(text) as input and gices the output based on dataset.json, if the input is there in name entity(in dataset.json) ,it prints "Name" ,if the input is in place entity(in dataset.json, it prints place in all other cases, it will print "data not found"
4) app.py is the main file to get the web app, run this code it will give you a webpage and you can give the Name in the webpage and click submit,it will give the output

5) Note: I didnt focus on design part of webpage(CSS part), so the web page is a basic webpage
6) This github only contains raw code and input and ouput screenshots ( but inorder to work on your side, you must a develop a virtual envirionment and need to install some dependices)
