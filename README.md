# API service for MongoDB, Postgres, ClickHouse

API Service for representation information from DB: MongoDB, Postgres, ClickHouse
- Postgres: Devices and User/Auth storage.
- MongoDB: Interface for devices.
- ClickHouse: Interfaces metrics/statistics.


# Process

**Users/Auth**
- [x] Users: Endpoints, Models, Repositories, DB
- [x] JWT Auth
- [ ] Tests
- [ ] Logs 

**Devices**
- [x] Devices: Endpoints, Models, Repositories, DB
- [ ] Tests
- [ ] Logs 

**Interfaces**
- [ ] Interfaces: Endpoints, Models, Repositories, DB
- [ ] Tests
- [ ] Logs 

**Statistics**
- [ ] Interfaces:  Endpoints, Models, Repositories, DB
- [ ] Tests
- [ ] Logs 

**Infra**
- [ ] Exporter for Prometheus
- [ ] Dockerfile for App
- [ ] Docker-compose



# Run

Development env

```
git clone git@github.com:yury-nazarov/api_mpc.git
docker-compose up -d  # for start DB
cd api_mpc
python3.9 -m venv venv
pip install -r requirements.py
python main.py
```

cp and edit
```
cp .env_example .env 
```

or use default settings `src/core/config.py`

[127.0.0.1/docs]()