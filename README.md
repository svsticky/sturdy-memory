# Stocky

**Stocky** is an inventory management app+API+database built with Python, FastAPI, and PostgreSQL. This project is designed to be run entirely inside a Docker-based development container, so all you need is [Docker](https://www.docker.com/) and [Visual Studio Code](https://code.visualstudio.com/) with the [Dev Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers).


## Table of Contents

- [Getting Started](#getting-started)
- [Running the Application](#running-the-application)
- [Testing](#testing)
- [Deployment](#deployment)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)



## Getting Started

### Prerequisites

- [Docker](https://www.docker.com/)
- [Visual Studio Code](https://code.visualstudio.com/)
- [VS Code Dev Containers Extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)

### Setup with VS Code Dev Container

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/yourusername/stocky.git
   cd stocky
   ```

2. **Open in VS Code:**

   Open the project folder in VS Code. If you have the Dev Containers extension installed, you will be prompted to reopen the project in a container.  
   Alternatively, open the Command Palette (`Ctrl+Shift+P` or `Cmd+Shift+P`), then select **Remote-Containers: Reopen in Container**.

3. **Dev Container Initialization:**

   The provided `devcontainer.json` (inside the `.devcontainer` folder) will automatically set up your environment, installing all necessary dependencies. No local Python or PostgreSQL installation is required.



## Running the Application

1. Copy `sample.env` to `.env`. Make sure all values are properly populated. TODO: add explenation of values to populate.


2. Then, simply run:
```bash
docker compose up --build
```

The API will be accessible at [http://localhost:8000](http://localhost:8000). You can view the interactive API documentation at [http://localhost:8000/docs](http://localhost:8000/docs) or [http://localhost:8000/redoc](http://localhost:8000/redoc).
The frontend will be accessible at [http://localhost:3000](http://localhost:3000)

## Testing

### API
Inside the Dev Container, you can run tests for the API with [pytest](https://docs.pytest.org/):

THIS IS STIL VERY MUCH TO DO!!! No testing has been added yet

### Frontend
Inside the Dev Container, you can run tests for the API with [bun](https://bun.sh/docs/cli/test)

THIS IS STIL VERY MUCH TO DO!!! No testing has been added yet

## Contributing

Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a new branch: `git checkout -b feature/YourFeature`.
3. Make your changes and confirm tests pass.
4. Submit a pull request detailing your changes.

For major changes, please open an issue to discuss your ideas before proceeding.


## License

Distributed under the MIT License. See the [LICENSE](LICENSE) file for more details.



Happy hacking!
