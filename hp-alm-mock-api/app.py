from flask import Flask, jsonify

app = Flask(__name__)

# Mock data for domains, projects, modules, sub-modules, folders, sub-folders, and test cases
mock_data = {
    "domains": ["Domain1", "Domain2", "Domain3", "Domain4", "Domain5"],
    "projects": {
        "Domain1": ["Project1.1", "Project1.2", "Project1.3"],
        "Domain2": ["Project2.1", "Project2.2", "Project2.3", "Project2.4"],
    },
    "modules": {
        "Project1": ["Module1.1", "Module1.2"],
        "Project2": ["Module2.1", "Module2.2", "Module2.3", "Module2.4", "Module2.5"],
        "Project3": ["Module3.1", "Module3.2"],
        "Project4": ["Module4.1", "Module4.2", "Module4.3", "Module4.4", "Module4.5"],
        "Project5": ["Module5.1", "Module5.2", "Module5.3", "Module5.4", "Module5.5", "Module5.6", "Module5.7"],
        "Project6": ["Module6.1", "Module6.2", "Module6.3", "Module6.4"],
        "Project7": ["Module7.1", "Module7.2", "Module7.3", "Module7.4", "Module7.5", "Module7.6", "Module7.7", "Module7.8", "Module7.9", "Module7.10"],
    },
    "folders": {
        "Module1.1": ["Folder1.1", "Folder1.2"],
        "Module2.1": ["Folder2.1", "Folder2.2""Folder2.3", "Folder2.4"],
        "Module3.1": ["Folder3.1", "Folder3.2""Folder3.3", "Folder3.4"],
        "Module4.1": ["Folder4.1", "Folder4.2""Folder4.3", "Folder4.4"],
        "Module5.1": ["Folder5.1", "Folder5.2""Folder5.3", "Folder5.4"],
    },
    "sub-folders": {
        "Folder1.1": ["Folder1.1.1", "Folder1.1.2"],
        "Folder1.2": ["Folder1.2.1", "Folder1.2.2"],
        "Folder2.1": ["Folder2.1.1", "Folder2.1.2"],
        "Folder2.2": ["Folder2.2.1", "Folder2.2.2"],
        "Folder3.1": ["Folder3.1.1", "Folder3.1.2"],
        "Folder3.2": ["Folder3.2.1", "Folder3.2.2"],
        "Folder4.1": ["Folder4.1.1", "Folder4.1.2"],
        "Folder4.2": ["Folder4.2.1", "Folder4.2.2"],
        "Folder5.1": ["Folder5.1.1", "Folder5.1.2"],
        "Folder5.2": ["Folder5.2.1", "Folder5.2.2"],
    },
    "test_cases": {
        "Folder1.1.1": [
            "TestCase1.1.1.1",
            "TestCase1.1.1.2",
            "TestCase1.1.1.3",
            "TestCase1.1.1.4",
        ],
        "Folder1.1.2": ["TestCase1.1.2.1", "TestCase1.1.2.2", "TestCase1.1.2.3"],
        "Folder1.2.1": ["TestCase1.2.1.1", "TestCase1.2.1.2", "TestCase1.2.1.3"],
        "Folder1.2.2": [
            "TestCase1.2.2.1",
            "TestCase1.2.2.2",
            "TestCase1.2.2.3",
            "TestCase1.2.2.4",
            "TestCase1.2.2.5",
        ],
        "Folder2.1.1": [
            "TestCase2.1.1.1",
            "TestCase2.1.1.2",
            "TestCase1.2.2.3",
            "TestCase1.2.2.4",
        ],
        "Folder2.1.2": ["TestCase2.1.2.1", "TestCase2.1.2.2"],
        "Folder2.2.1": ["TestCase2.2.1.1", "TestCase2.2.1.2"],
        "Folder2.2.2": [
            "TestCase2.2.2.1",
            "TestCase2.2.2.2",
            "TestCase2.2.2.3",
            "TestCase2.2.2.4",
            "TestCase2.2.2.5",
            "TestCase2.2.2.6",
            "TestCase2.2.2.7",
        ],
        "Folder3.1.1": [
            "TestCase3.1.1.1",
            "TestCase3.1.1.2",
            "TestCase3.1.1.3",
            "TestCase3.1.1.4",
            "TestCase3.1.1.5",
        ],
        "Folder3.1.2": ["TestCase3.1.2.1", "TestCase3.1.2.2"],
        "Folder3.2.1": ["TestCase3.2.1.1", "TestCase3.2.1.2"],
        "Folder3.2.2": ["TestCase3.2.2.1", "TestCase3.2.2.2"],
        "Folder4.1.1": [
            "TestCase4.1.1.1",
            "TestCase4.1.1.2",
            "TestCase4.1.1.3",
            "TestCase4.1.1.4",
            "TestCase4.1.1.5",
            "TestCase4.1.1.6",
            "TestCase4.1.1.7",
            "TestCase4.1.1.8",
        ],
        "Folder4.1.2": ["TestCase4.1.2.1", "TestCase4.1.2.2"],
        "Folder4.2.1": ["TestCase4.2.1.1", "TestCase4.2.1.2"],
        "Folder4.2.2": [
            "TestCase4.2.2.1",
            "TestCase4.2.2.2",
            "TestCase4.2.2.3",
            "TestCase4.2.2.4",
            "TestCase4.2.2.5",
            "TestCase4.2.2.6",
            "TestCase4.2.2.7",
            "TestCase4.2.2.8",
            "TestCase4.2.2.9",
        ],
        "Folder5.1.1": ["TestCase5.1.1.1", "TestCase5.1.1.2"],
        "Folder5.1.2": ["TestCase5.1.2.1", "TestCase5.1.2.2"],
        "Folder5.2.1": ["TestCase5.2.1.1", "TestCase5.2.1.2"],
        "Folder5.2.2": [
            "TestCase5.2.2.1",
            "TestCase5.2.2.2",
            "TestCase5.2.2.3",
            "TestCase5.2.2.4",
            "TestCase5.2.2.5",
            "TestCase5.2.2.6",
        ],
    },
}

@app.route("/alm/api/domains", methods=["GET"])
def get_domains():
    return jsonify(mock_data["domains"])

@app.route("/alm/api/projects/<domain>", methods=["GET"])
def get_projects(domain):
    return jsonify(mock_data["projects"].get(domain, []))

@app.route("/alm/api/modules/<project>", methods=["GET"])
def get_modules(project):
    return jsonify(mock_data["modules"].get(project, []))

@app.route("/alm/api/folders/<Folder>", methods=["GET"])
def get_folders(Folder):
    return jsonify(mock_data["folders"].get(Folder, []))

@app.route("/alm/api/subFolders/<folder>", methods=["GET"])
def get_SubFolders(folder):
    return jsonify(mock_data["sub_folders"].get(folder, []))

@app.route("/alm/api/testcases/<folder>", methods=["GET"])
def get_test_cases(folder):
    return jsonify(mock_data["test_cases"].get(folder, []))

if __name__ == "__main__":
    app.run(debug=True)
