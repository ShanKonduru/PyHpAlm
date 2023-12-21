import requests
import csv

base_url = "http://127.0.0.1:5000/alm/api/"


def get_data(endpoint):
    response = requests.get(base_url + endpoint)
    return response.json()


def extract_data_recursive(data, current_path, csv_writer):
    if isinstance(data, list):
        for item in data:
            new_path = current_path + [item]
            extract_data_recursive(item, new_path, csv_writer)
    elif isinstance(data, dict):
        for key, value in data.items():
            new_path = current_path + [key]
            extract_data_recursive(value, new_path, csv_writer)
    else:
        csv_writer.writerow(current_path + [data])


def create_csv_file(data, csv_filename):
    with open(csv_filename, "w", newline="") as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(
            ["Domain", "Project", "Module", "Submodule", "Folder", "TestCase"]
        )
        extract_data_recursive(data, [], csv_writer)


def main():

    domains = get_data("domains")
    for domain in domains:
        projects = get_data(f"projects/{domain}")
        for project in projects:
            modules = get_data(f"modules/{project}")
            for module in modules:
                submodules = get_data(f"submodules/{module}")
                for submodule in submodules:
                    folders = get_data(f"folders/{submodule}")
                    for folder in folders:
                        test_cases = get_data(f"testcases/{folder}")
                        data = {
                            "Domain": domain,
                            "Project": project,
                            "Module": module,
                            "Submodule": submodule,
                            "Folder": folder,
                            "Sub Folder": sub_folder,
                            "TestCase": test_cases,
                        }
                        # print(data)
                        create_csv_file(data, "test_plan_data.csv")
                        sub_folders = get_data(f"folders/{folder}")
                        for sub_folder in sub_folders:
                            test_cases = get_data(f"testcases/{sub_folder}")
                            data = {
                                "Domain": domain,
                                "Project": project,
                                "Module": module,
                                "Submodule": submodule,
                                "Folder": folder,
                                "Sub Folder": sub_folder,
                                "TestCase": test_cases,
                            }
                            # print(data)
                            create_csv_file(data, "test_plan_data.csv")


if __name__ == "__main__":
    main()
