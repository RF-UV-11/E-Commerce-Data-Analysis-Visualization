# E-Commerce Data Analysis and Visualization 📊

## 🌟 Overview
This project is an **`E-commerce data analysis and visualization tool`** built using **`Python` <a href="https://www.python.org" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40"/></a>, `Flask` <a href="https://flask.palletsprojects.com/" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/pocoo_flask/pocoo_flask-icon.svg" alt="flask" width="40" height="40"/></a>, `Plotly`** <a href="https://plotly.com/" target="_blank" rel="noreferrer"> <img src="https://avatars.githubusercontent.com/u/5997976?s=280&v=4" alt="plotly" width="40" height="40"/> </a>, and **`PostgreSQL`** <a href="https://www.postgresql.org" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/postgresql/postgresql-original-wordmark.svg" alt="postgresql" width="40" height="40"/> </a>  . It aims to provide insights into sales trends, customer behavior, and product performance through interactive visualizations and data analysis.

## 🚀 Why is it necessary ?
In the realm of E-commerce, understanding data is crucial for making informed decisions, optimizing operations, and enhancing customer satisfaction. This project leverages data analysis to:
- **Enhance Decision-Making**: Provide actionable insights based on sales trends and customer behavior.
- **Optimize Operations**: Improve inventory management and supply chain efficiencies.
- **Personalize Marketing**: Tailor marketing strategies based on customer preferences and purchase patterns.
- **Forecast Trends**: Predict future sales trends and demand fluctuations.

## 🔧 How to achieve it ?
### Components
- **Data Generation**: Uses Faker library to create synthetic E-commerce data for testing and development.
- **Database Integration**: Stores data in **`PostgreSQL`**, facilitating efficient data retrieval and management.
- **Data Analysis**: Executes **`SQL`** queries to analyze sales data, customer registrations, and product categories.
- **Visualization**: Utilizes **`Plotly`** to generate interactive charts and graphs for visualizing data insights.
- **Web Interface**: Implements **`Flask`** to host visualizations and analysis results in a user-friendly web application.

### Setup and Installation
1. **Clone Repository**
   ```bash
   git clone https://github.com/RF-UV-11/E-Commerce-Data-Analysis-Visualization.git
   cd E-Commerce-Data-Analysis-Visualization

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Database Setup**
   - Install **`PostgreSQL`** and configure database credentials in `configs.json` to use it in `postgres_connection.py` to make a connection.

4. **Run the Application**
   ```bash
   python main.py
   ```
   Access the web interface at `http://localhost:5000` to explore E-commerce data visualizations and analysis.

### Usage
- Navigate through different pages `index.html`, `graph.html`, `plot.html` to explore various visualizations and data analysis results derived from the E-commerce dataset.


### 📄 License
This project is licensed under the [Apache-2.0](https://choosealicense.com/licenses/apache-2.0/).
