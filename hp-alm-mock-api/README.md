   # HP ALM Mock API

   This is a simple mock implementation of an HP ALM (Application Lifecycle Management) system, created using Flask. It simulates fetching data for domains, projects, modules, sub-modules, folders, sub-folders, and test cases.

   ## Features

   - Provides mock data for domains, projects, modules, sub-modules, folders, sub-folders, and test cases.
   - Implements RESTful API endpoints for accessing the mock data.

   ## Getting Started

   ### Prerequisites

   - Python 3.x
   - [Poetry](https://python-poetry.org/)

   ### Installation

   1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/hp-alm-mock-api.git
   ```
   2. Change into the project directory:
   ```bash
   cd hp-alm-mock-api
   ```
   3. Install dependencies using Poetry:
   ```bash
   poetry install
   ```
   ### Usage:

   1. Run the Flask application:
   ```bash
   poetry run python app.py
   ```
   2. Access the mock API endpoints:

   To get a list of domains:
   ```bash
   http://127.0.0.1:5000/alm/api/domains
   ```
   To get a list of projects under a domain:
   ```bash
   http://127.0.0.1:5000/alm/api/projects/Domain1
   ```
   To get a list of modules under a project:
   ```bash
   http://127.0.0.1:5000/alm/api/modules/Project1
   ```

   ### Mock Data Structure

   The mock data structure includes domains, projects, modules, sub-modules, folders, sub-folders, and test cases. The data is stored in the mock_data dictionary in the app.py file.

   ```bash
   # Mock data structure
   mock_data = {
   "domains": [...],
   "projects": {...},
   "modules": {...},
   "sub_modules": {...},
   "folders": {...},
   "test_cases": {...},
   }
   ```

   License
   This project is licensed under the MIT License - see the LICENSE file for details.

   ```bash
   This updated template includes instructions for using Poetry to install dependencies and run the application.
   ```
