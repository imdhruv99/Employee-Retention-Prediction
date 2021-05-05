# Employee-Retention-Prediction
----
- Employee Retention Prediction using Machine Learning

### Project Abstaction
- Project's main is to predict that whether an employee will stay in the current organization or will left the organization by processing on given inputs.
- RanmForest Classification and XGBoost these algorithms are use to train the model.
- XGBoost gives the best model prediction from both algorithms.
- Model is exposed using the REST API which is constructed in Flask and Python.
- Project also process on old and failed data and it will create archive files on those datasets.
- Prediction and Training logs can be visualized using the ELK + Filebeat.
- Matrices from projects can be visualized through the Prometheus and Grafana.

### Project's Tools and Technology
- **Programing Language:** Python
- **Web Development Framework:** Flask
- **Machine Learning Libraries:** Scikit-Learn, Pandas, Numpy, Matplotlib, XGBoost
- **Machine Learning Algorithm:** KMeans, Random Forest and XGBoost
- **Container Technology:** Docker
- **Log Management System:** ElasticSearch, Logstash, Kibana, Filebeats
- **Metrics Monitoring System:** Prometheus, Grafana
- **Database:** SQLite3

### ELKStack Pipline in Brief
- Filebeat will collect the prediction and training logs from project and will transfer the logs to logstash.
- Logstash will process those logs and forward to ElasticSearch.
- At ElasticSearch, I have created index name as `logstash-*` which will give us the logs.
- Kibana is used to visualize logs from above index.

### Running the Project
- Create virtual environment
- Install dependancies from `requierments.txt`
    `pip install requirements.txt`
- Run `python main.py` inside App folder.
- You can also run project as Docker Container by building docker image.
    `docker build -t <image name as per your prefrence> .`

### Thank You!
- D H R U V &nbsp; P R A J A P A T I