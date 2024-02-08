![banner](Media/Banner.png)

![Python version](https://img.shields.io/badge/Python%20version-3.10%2B-lightgrey)
![GitHub last commit](https://img.shields.io/github/last-commit/afnanurrahim/New-york-taxi-ETA)
![Type of ML](https://img.shields.io/badge/Type%20of%20ML-%20Regression-red)
![License](https://img.shields.io/badge/License-MIT-green)
[![Open Source Love svg1](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)


## Authors

- [@afnanurrahim](https://github.com/afnanurrahim)

## Table of Contents

  - [Business problem](#business-problem)
  - [Data source](#data-source)
  - [Tech Stack](#tech-stack)
  - [Pipeline](#pipeline)
  - [Results](#results)
  - [Lessons learned](#lessons-learned)
  - [Limitation and what can be improved](#limitation-and-what-can-be-improved)
  - [App deployed on FastAPI](#app-deployed-on-fastapi)
  - [Repository structure](#repository-structure)
  - [License](#license)

## Business problem

This FastAPI web application aims to predict the estimated time of arrival (ETA) for New York City taxis in 2021. The prediction is based on factors such as the hour of the day, traffic conditions, holidays, weather etc. providing valuable insights for taxi service optimization.

## Data source
- [TLC Trip Record Data](https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page)
- [Hourly weather Dataset](https://mesonet.agron.iastate.edu/request/download.phtml?network=NY_ASOS)

## Tech Stack
- Python
- FastAPI  (For building the api)
- Streamlit  (For error analyzer web app)
- Tableau    (For Data visualization)
- Hugginface   (For web app deployment)

## App deployed on FastAPI
![FastAPI gif](Media/Api.gif)

## Repository structure
```

├── 4_ETA
│   ├── 1_weather_EDA.ipynb                         <- EDA on New York's hourly weather data.
│   ├── 2_combine_parquet.ipynb                     <- Combining monthly trips data.
│   ├── 3_trips_EDA.ipynb                           <- EDA on trips along with combining all dataset into one.
│   ├── 4_Uni_Bi_Multivariate_analysis.ipynb        <- Analysis on variables relationship.
│   ├── 5_feature_selection.ipynb                   <- Feature selection techniques.
│   ├── 6_Data_visualization_Tableau.ipynb          <- Data preparation for Tableau.
│   ├── 7_Model_building.ipynb                      <- Building model for prediction
│   │
│   ├── FastAPI                           
│   │   ├── Dockerfile                              <- Docker file
│   │   ├── Features.py                             <- Class for assistance of main.py
│   │   ├── main.py                                 <- Contains the FastAPI web app
│   │   ├── get_categorical_values.ipynb            <- Getting label encoded values used in ML model
│   │   ├── requirements.txt                        <- FastAPI dependencies
│   │
│   ├── Model_dashboard
│   │   ├── prediction_dataset.ipynb                <- creating dataset for analyzing predictions
│   │   ├── app.py                                  <- Streamlit app that analyze error with independent variables. 
│   │
│   ├── Tableau                           
│       ├── borough_info.csv                         <- Contains traffic info about each Borough
│       ├── borough_path.csv                         <- Contains info about inter Borough trips 
│       ├── location_info.csv                        <- Contains traffic info about different neighborhoods in NYC
│       ├── time_only.csv                            <- Info of traffic based on weekdays, hour of day, month, etc.
│   
├── Media
│   ├── Api.gif                                      <- FastAPI app gif
│   ├── Banner.png                                   <- README file banner
│   ├── MAE.png                                      <- Train and validation set mean absolute error
│   ├── error_analyzer.gif                           <- Error analyzer web app gif 
│   ├── tableau.gif                                  <- Tableau dashboard gif
│
│
├── 1_Data_Exploration.ipynb                         <- Basic overiew on dataset
│
│
├── 2_Sampling.ipynb                                 <- Sampling on the large dataset 
│
│
├── 3_population_vs_sample.ipynb                     <- Comparison of population vs sampled data
│
│
├── LICENSE                                       <- license file.
│
├── README.md                                     <- this readme file.

```

## License
MIT License

Copyright (c) 2024 afnanurrahim

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
