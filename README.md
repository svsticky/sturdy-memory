# Stocky

**Stocky** is an inventory management app+API+database built with Python, FastAPI, and PostgreSQL. This project is designed to be run entirely inside a Docker-based development container, so all you need is [Docker](https://www.docker.com/) and [Visual Studio Code](https://code.visualstudio.com/) with the [Dev Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers).


## Table of Contents

- [Getting Started](#getting-started)
- [Running the Application](#running-the-application)
- [Contributing](#contributing)
- [License](#license)



## Getting Started

### Prerequisites

- [Docker](https://www.docker.com/)
- [Visual Studio Code](https://code.visualstudio.com/)
- [VS Code Dev Containers Extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)

### Setup with VS Code Dev Container

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/svsticky/sturdy-memory.git`
   cd sturdy-memory
   ```

2. **Open in VS Code:**

   Open the project folder in VS Code. If you have the Dev Containers extension installed, you will be prompted to reopen the project in a container.  
   Alternatively, open the Command Palette (`Ctrl+Shift+P` or `Cmd+Shift+P`), then select **Remote-Containers: Reopen in Container**.

3. **Dev Container Initialization:**

   The provided `devcontainer.json` (inside the `.devcontainer` folder) will automatically set up your environment, installing all necessary dependencies. No local Python or PostgreSQL installation is required.



## Running the Application

1. Copy `sample.env` to `.env`. Make sure all values are properly populated.


2. Then, simply run:
```bash
docker compose up --build
```

The API will be accessible at [http://localhost:8000](http://localhost:8000). You can view the interactive API documentation at [http://localhost:8000/docs](http://localhost:8000/docs) or [http://localhost:8000/redoc](http://localhost:8000/redoc).
The frontend will be accessible at [http://localhost:3000](http://localhost:3000)


## Contributing

Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a new branch: `git checkout -b feat/your-feature`.
3. Make your changes and confirm tests pass.
4. Submit a pull request detailing your changes.

For major changes, please open an issue to discuss your ideas before proceeding.


## LICENSE

This project is **dual-licensed** under either:

- [**The MIT License (MIT)**](#mit-license)
- [**The Apache License 2.0 (Apache-2.0)**](#apache-license-20)  

You may choose either license to govern your use of this software.

---

### MIT License

```
Copyright (c) 2025 S.V. Sticky

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
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES, OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---

### Apache License 2.0

```
Copyright 2025 S.V. Sticky

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
```

Happy hacking!
