# Fuel Economy Prediction and Deployment of a Machine Learning model with FLask API on AWS EC2 Instance
This project focuses on harnessing machine learning algorithms to predict the fuel economy of light-duty vehicles, enhancing skills, and gaining a deeper understanding of deploying machine learning models in real-world applications. The deployment is achieved using a Flask Python application on an AWS EC2 instance

## Introduction
Fuel economy is an important consideration for consumers when purchasing a vehicle, and it is often used as a standard metric for comparing the efficiency of different cars, trucks, and other vehicles. It is a measurement of how many mile or kilometers a vehicle can travel on a specific amount of fuel.It is influenced by various factors, including th vehicle's engine efficiency, weight, vehicle category and some other factors. It is measure in "MPG" (miles per gall n) in the United States or "L/100km" (liters per 100 kilometers) in most countries.

Higher fuel economy means that a vehicle can travel a greater distance on a given amount of fuel, which is typially desirable because it leads to cost savings for the vehicle owner and reduces the environmental impact of drivng by lowering fuel consumption and emissions.


## Problem Statement
The project aims to predict the fuel efficiency of light-duty vehicles accurately.
Deployment on AWS EC2 with Flask is necessary to make the model accessible over the internet.

## Project Overview
1. Data Collection: Gather relevant data on vehicle attributes.
2. Data Preprocessing: Clean, normalize, and transform the data to prepare it for machine learning.
3. Feature Engineering: Select or create the most relevant features for the prediction model.
4. Model Selection: Choose an appropriate machine learning algorithm for fuel economy prediction.
5. Model Training: Train the selected model on historical data.
6. Model Evaluation: Assess the model's performance using various metrics like R-squared and Root Mean Square Error (RMSE).
7. Flask API Development: Develop a Flask application to expose the trained model via an API.
8. AWS EC2 Setup: Set up an EC2 instance on Amazon Web Services (AWS) for hosting the Flask application.

## Environment, Tools and Libraries
1. Pandas for data manipulation 
2. Numpy for mathematical calculation and analysis 
3. Seaborn and Matplotlib for visualization and insights
4. Python 3.11 Environment 
5. Jupyter and Microsoft Excel as tools  
6. Sklearn for Machine Learning and preprocessing

## Project Structure
This project is organized into five major parts:

i.    Data Folder: This directory contains the data required for building our machine learning model.

ii.   XGBR_Feul_Economy.pkl: This is pickle file containing our trained machine learning model.

iii.  The main.py: This file houses the Flask APIs responsible for handling vehicle data input through a Graphical User Interface (GUI) or API calls. It then computes the predicted Fuel economy of the vehicle based on our model and returns the result. This is the core of the application, where predictions are made and served to users.

iv.   static Folder: The static folder contains Cascading Style Sheets (CSS) files used for styling the application's user interface. It is responsible for adjusting content size, spacing, color, and adding decorative features like animations that enhance the visual appeal and usability of the user interface.

v.    templates Folder: Inside the templates folder, you will find HTML templates that enable users to input life expectancy features and display the predicted Fuel economy of the vehicles.

## Detailed Steps
a. Data Collection
Identify and acquire a dataset containing vehicle-related features and fuel efficiency records.
Ensure data quality by addressing missing values and outliers.

b. Data Preprocessing
Clean the data by handling missing values and outliers.
Normalize or scale numerical features to ensure consistent input for the model.

c. Feature Engineering
Select relevant features based on domain knowledge and feature importance analysis.
Create new features if necessary, such as convertion of Fuel economy to k/l engine efficiency.

d. Model Selection
Choose an appropriate machine learning algorithm.

e. Model Training
Split the data into training and testing sets.
Train the selected model on the training data.

f. Model Evaluation
Evaluate the model's performance on the testing data using appropriate evaluation metrics.
Fine-tune the model if necessary to improve performance.

g. Flask API Development
Develop a Flask application that loads the trained model.
Create API endpoints for receiving input data and returning predictions.

h. AWS EC2 Setup
Create an AWS EC2 instance with the desired configuration.
Install necessary dependencies, including Python, Flask, and any required libraries.
Deploy the Flask application on the EC2 instance.

Deployment
Ensure the Flask application is accessible over the internet via the EC2 instance's public IP or domain.
Implement security measures to protect the API and sensitive data.

## Conclusion
This project offers hands-on experience in the entire machine learning pipeline, from data collection to deployment on AWS EC2.
It enhances skills in data preprocessing, feature engineering, model selection, and web application development with Flask.
The deployment on AWS EC2 demonstrates how to make machine learning models accessible for practical use.
