# _Docker Projects - Build and Run Instructions_

This document provides build and run instructions for each Docker-based Python project under the `docker project` directory.
## 📝 Overview

This project demonstrates various Docker concepts through modular Python applications, including volumes, bind mounts, PostgreSQL integration, and Docker Compose.


## 📂 Project File Structure

```bash
docker project/
├── test1/
│   ├── Dockerfile              # Runs a basic Python script to add two numbers
│   └── test.py
│
├── test2_dockerVolume/
│   ├── Dockerfile              # Writes and reads usernames using Docker volume
│   ├── test2.py
│   └── userinfo.txt
│
├── test3_bindMounts/
│   ├── Dockerfile              # Reads server list using a bind-mounted file
│   ├── server.txt
│   └── test3.py
│
├── test4_API/
│   ├── Dockerfile              # Fetches and prints a random cat fact from an API
│   └── test4.py
│
├── test5_psql/
│   ├── Dockerfile              # Connects Python to PostgreSQL running on host
│   └── test5.py
│
├── test6_conn_db_container/
│   ├── Dockerfile              # Connects from Python container to Postgres container using custom network
│   └── test6.py
│
└── test7/
    ├── docker-compose.yml      # Defines Python + PostgreSQL multi-container app
    ├── Dockerfile              # Builds the Python service
    ├── server.txt              # Bind-mounted into Python container for name logging
    └── test6.py                # Reused Python DB logic (interactive CLI)
```

## 🛠️ Tech Stack

- **Docker** — Containerization platform to package and run applications in isolated environments
- **Python 3** — Primary programming language for scripting and app logic
- **PostgreSQL** — Relational database used for persistent data storage
- **Docker Compose** — Tool for defining and running multi-container Docker applications
- **Volumes & Bind Mounts** — Used for data sharing and persistence
- **psycopg2** — PostgreSQL adapter for Python



| Docker Object | Description                                  | Example Command                |
| ------------- | -------------------------------------------- | ------------------------------ |
| Image         | Read-only template for containers            | `docker build -t app .`        |
| Container     | Running instance of an image                 | `docker run -it app`           |
| Volume        | Persistent storage for containers            | `docker volume create data`    |
| Network       | Enables container-to-container communication | `docker network create webnet` |
| Tag           | Label to identify image version              | `docker tag app app:v1`        |

# TASKs

| Part | Description                     |
|------|---------------------------------|
| 1    | Containerize an application     |
| 2    | Update the application         |
| 3    | Share the application          |
| 4    | Persist the DB                 |
| 5    | Use bind mounts                |
| 6    | Multi-container apps           |
| 7    | Use Docker Compose             |


---

### 📁 test1/

#### Build

```bash
cd test1
docker build -t test1-image .
```

#### Run

```bash
docker run -it test1-image
```

---

### 📁 test2\_dockerVolume/

#### Build

```bash
cd test2_dockerVolume
docker build -t test2-image .
```

#### Run (with volume mount)

```bash
docker run -it -v user_data_vol:/app test2-image
```

---

### 📁 test3\_bindMounts/

#### Build

```bash
cd test3_bindMounts
docker build -t test3-image .
```

#### Run (with bind mount)

```bash
docker run -it -v "$(pwd)/test3_bindMounts:/app" test3-image
```

---

### 📁 test4\_API/

#### Build

```bash
cd test4_API
docker build -t test4-image .
```

#### Run

```bash
docker run -it test4-image
```

---

### 📁 test5\_psql/

#### Prerequisite: Start PostgreSQL on host

```bash
docker run --name pgsql_host -e POSTGRES_DB=database_name \
  -e POSTGRES_USER=postgres_user -e POSTGRES_PASSWORD=your_password \
  -p 5432:5432 -d postgres
```

#### Build

```bash
cd test5_psql
docker build -t test5-image .
```

#### Run (connect to host DB)

```bash
docker run -it test5-image
```

---

### 📁 test6\_conn\_db\_container/

#### Prerequisite: Setup Docker network and PostgreSQL container

```bash
docker network create mynet

docker run --name pgsql_container --network mynet \
  -e POSTGRES_DB=praveen -e POSTGRES_USER=postgres \
  -e POSTGRES_PASSWORD=Praveen1# -d postgres
```

#### Build

```bash
cd test6_conn_db_container
docker build -t test6-image .
```

#### Run (connect to DB container)

```bash
docker run -it --network mynet test6-image
```

---

### 📁 test7/ (Docker Compose)

#### Build & Run Full Stack

```bash
cd test7
docker-compose up --build
```

#### Stop the Stack

```bash
docker-compose down
```

#### Rebuild Clean

```bash
docker-compose down --volumes --remove-orphans
docker-compose up --build
```

---

