<p align="center">
  <img src="./static/asset/title.png" width="600px"/>
</p>

![License](https://img.shields.io/badge/license-MIT-blue)
![Contributors](https://img.shields.io/github/contributors/prmditya/phish-guard)


AI Powered Website for identifying phishing website from URL. 

## **Table of Contents**
- [**Table of Contents**](#table-of-contents)
- [**About the Project**](#about-the-project)
- [**Features**](#features)
- [**Technologies Used**](#technologies-used)
- [**Installation**](#installation)
  - [Steps](#steps)
- [**Usage**](#usage)
- [**License**](#license)
- [**Contributing**](#contributing)
- [**Acknowledgments**](#acknowledgments)

---

## **About the Project**
Phish Guard is a website developed using machine learning to detect phishing websites based on the provided URL. This project was created as part of the final project assignment for the Intelligent Systems course.

---

## **Features**
Highlight the key features of this project.  
- **URL Phishing Detection**: Detects whether a given URL is linked to a phishing website using machine learning models.
- **Real-time Analysis**: Analyzes URLs in real-time and provides instant results on the legitimacy of the website.
- **User-Friendly Interface**: Offers an easy-to-use interface for users to input URLs and view detection results.

---

## **Technologies Used**
List the technologies, tools, or frameworks you used in the project.  
- [Flask](https://flask.palletsprojects.com/en/stable/) - A lightweight web framework for building web applications in Python. 
- [Scikit-Learn](https://scikit-learn.org/stable/) - A machine learning library for Python, used for building and evaluating the model.
- [Pandas](https://pandas.pydata.org/docs/getting_started/index.html) - A data manipulation and analysis library used to handle datasets.
- [Numpy](https://numpy.org/) - A library for numerical computing, used for working with arrays and matrices in the project.
- [Requests](https://requests.readthedocs.io/en/latest/) - A library for making HTTP requests, if you're fetching website data for analysis.
- [Google Colab](https://colab.research.google.com/) - A cloud-based platform for running Jupyter notebooks, used for developing and training the machine learning model.

---

## **Installation**
This section explain about how to Install or clone and run the project.

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/prmditya/phish-guard.git
   ```
2. Navigate to the project directory:
   ```bash
   cd phish-guard
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the application:
   ```bash
   python run.py
   ```

---

## **Usage**
1. Enter a URL into the input form.
2. Click the "Analyze" button.
3. The result of the identification will appear at the bottom of the page.

---

## **License**
This project is licensed under the [MIT License](LICENSE).  

---

## **Contributing**
Contributions are welcome! Follow these steps:  
1. Fork the repository.  
2. Create a new branch (`git checkout -b feature-name`).  
3. Commit your changes (`git commit -m "Add feature"`).  
4. Push to the branch (`git push origin feature-name`).  
5. Open a pull request.

---

## **Acknowledgments**
I would like to express my gratitude to the following resources and individuals who contributed to this project:

- The inspiration for the project came from this [Kaggle notebook on URL classification](https://www.kaggle.com/code/busrabetulcavusoglu/urls-classification).
- I would also like to thank my friends, [Bizzati Hanif R.F](), [M. Yusuf Ramadhan](), and [Fatyatulhaqq Diando N](), for their support and assistance throughout the development of this project.

---