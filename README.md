# library
A library created is a simple book rating and review platform (goodreads-like) created using Django

## Features

- List books and their details
- Bookmark books
- Submit review (ratings and comments)
- Validate ratings (1 to 5)

## Setup Instructions

### Requirements

- Docker and Docker Compose
- Python 3.9

### Clone the repository:
   ```bash
   git clone https://github.com/mjpakzad/library.git
   ```

### Change directory to Project directory
```bash
cd library
```
   
## How to use
You can set up and run the project using either `make` commands or Docker commands directly.

### 1. Make commands

#### Setup
```bash
make setup
```

#### Start the project
```bash
make up
```

#### Rebuild the project
```bash
make build
```

#### Stop the project
```bash
make down
```

### Docker commands

#### Start the project
```bash
docker compose up -d
```

#### Run migrations
```bash
docker exec -it web "cd goodreads && python3 manage.py migrate"
```

#### Load fixtures
```bash
docker exec -it web "cd goodreads && python3 manage.py createsuperuser""
```

#### Stop the project
```
docker compose down
```