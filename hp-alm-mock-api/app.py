from flask import Flask, jsonify

app = Flask(__name__)

# Mock data for domains, projects, modules, sub-modules, folders, sub-folders, and test cases
mock_data = {
    "domains": ["Domain1", "Domain2"],
    "projects": {"Domain1": ["Project1", "Project2"], "Domain2": ["Project3", "Project4"]},
    "modules": {"Project1": ["Module1", "Module2"], "Project2": ["Module3", "Module4"],
                "Project3": ["Module5", "Module6"], "Project4": ["Module7", "Module8"]},
    "sub_modules": {"Module1": ["SubModule1.1", "SubModule1.2"], "Module2": ["SubModule2.1", "SubModule2.2"],
                   "Module3": ["SubModule3.1", "SubModule3.2"], "Module4": ["SubModule4.1", "SubModule4.2"],
                   "Module5": ["SubModule5.1", "SubModule5.2"], "Module6": ["SubModule6.1", "SubModule6.2"],
                   "Module7": ["SubModule7.1", "SubModule7.2"], "Module8": ["SubModule8.1", "SubModule8.2"]},
    "folders": {"SubModule1.1": ["Folder1.1.1", "Folder1.1.2"], "SubModule1.2": ["Folder1.2.1", "Folder1.2.2"],
                "SubModule2.1": ["Folder2.1.1", "Folder2.1.2"], "SubModule2.2": ["Folder2.2.1", "Folder2.2.2"],
                "SubModule3.1": ["Folder3.1.1", "Folder3.1.2"], "SubModule3.2": ["Folder3.2.1", "Folder3.2.2"],
                "SubModule4.1": ["Folder4.1.1", "Folder4.1.2"], "SubModule4.2": ["Folder4.2.1", "Folder4.2.2"],
                "SubModule5.1": ["Folder5.1.1", "Folder5.1.2"], "SubModule5.2": ["Folder5.2.1", "Folder5.2.2"],
                "SubModule6.1": ["Folder6.1.1", "Folder6.1.2"], "SubModule6.2": ["Folder6.2.1", "Folder6.2.2"],
                "SubModule7.1": ["Folder7.1.1", "Folder7.1.2"], "SubModule7.2": ["Folder7.2.1", "Folder7.2.2"],
                "SubModule8.1": ["Folder8.1.1", "Folder8.1.2"], "SubModule8.2": ["Folder8.2.1", "Folder8.2.2"]},
    "test_cases": {"Folder1.1.1": ["TestCase1.1.1.1", "TestCase1.1.1.2"],
                   "Folder1.1.2": ["TestCase1.1.2.1", "TestCase1.1.2.2"],
                   "Folder1.2.1": ["TestCase1.2.1.1", "TestCase1.2.1.2"],
                   "Folder1.2.2": ["TestCase1.2.2.1", "TestCase1.2.2.2"],
                   "Folder2.1.1": ["TestCase2.1.1.1", "TestCase2.1.1.2"],
                   "Folder2.1.2": ["TestCase2.1.2.1", "TestCase2.1.2.2"],
                   "Folder2.2.1": ["TestCase2.2.1.1", "TestCase2.2.1.2"],
                   "Folder2.2.2": ["TestCase2.2.2.1", "TestCase2.2.2.2"],
                   "Folder3.1.1": ["TestCase3.1.1.1", "TestCase3.1.1.2"],
                   "Folder3.1.2": ["TestCase3.1.2.1", "TestCase3.1.2.2"],
                   "Folder3.2.1": ["TestCase3.2.1.1", "TestCase3.2.1.2"],
                   "Folder3.2.2": ["TestCase3.2.2.1", "TestCase3.2.2.2"],
                   "Folder4.1.1": ["TestCase4.1.1.1", "TestCase4.1.1.2"],
                   "Folder4.1.2": ["TestCase4.1.2.1", "TestCase4.1.2.2"],
                   "Folder4.2.1": ["TestCase4.2.1.1", "TestCase4.2.1.2"],
                   "Folder4.2.2": ["TestCase4.2.2.1", "TestCase4.2.2.2"],
                   "Folder5.1.1": ["TestCase5.1.1.1", "TestCase5.1.1.2"],
                   "Folder5.1.2": ["TestCase5.1.2.1", "TestCase5.1.2.2"],
                   "Folder5.2.1": ["TestCase5.2.1.1", "TestCase5.2.1.2"],
                   "Folder5.2.2": ["TestCase5.2.2.1", "TestCase5.2.2.2"],
                   "Folder6.1.1": ["TestCase6.1.1.1", "TestCase6.1.1.2"],
                   "Folder6.1.2": ["TestCase6.1.2.1", "TestCase6.1.2.2"],
                   "Folder6.2.1": ["TestCase6.2.1.1", "TestCase6.2.1.2"],
                   "Folder6.2.2": ["TestCase6.2.2.1", "TestCase6.2.2.2"],
                   "Folder7.1.1": ["TestCase7.1.1.1", "TestCase7.1.1.2"],
                   "Folder7.1.2": ["TestCase7.1.2.1", "TestCase7.1.2.2"],
                   "Folder7.2.1": ["TestCase7.2.1.1", "TestCase7.2.1.2"],
                   "Folder7.2.2": ["TestCase7.2.2.1", "TestCase7.2.2.2"],
                   "Folder8.1.1": ["TestCase8.1.1.1", "TestCase8.1.1.2"],
                   "Folder8.1.2": ["TestCase8.1.2.1", "TestCase8.1.2.2"],
                   "Folder8.2.1": ["TestCase8.2.1.1", "TestCase8.2.1.2"],
                   "Folder8.2.2": ["TestCase8.2.2.1", "TestCase8.2.2.2"]},
}

@app.route('/alm/api/domains', methods=['GET'])
def get_domains():
    return jsonify(mock_data["domains"])

@app.route('/alm/api/projects/<domain>', methods=['GET'])
def get_projects(domain):
    return jsonify(mock_data["projects"].get(domain, []))

@app.route('/alm/api/modules/<project>', methods=['GET'])
def get_modules(project):
    return jsonify(mock_data["modules"].get(project, []))

@app.route('/alm/api/submodules/<module>', methods=['GET'])
def get_submodules(module):
    return jsonify(mock_data["sub_modules"].get(module, []))

@app.route('/alm/api/folders/<submodule>', methods=['GET'])
def get_folders(submodule):
    return jsonify(mock_data["folders"].get(submodule, []))

@app.route('/alm/api/testcases/<folder>', methods=['GET'])
def get_test_cases(folder):
    return jsonify(mock_data["test_cases"].get(folder, []))

if __name__ == '__main__':
    app.run(debug=True)
