import json

def parse_json_file_cases(file_path):

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            json_string = f.read()
            data = json.loads(json_string)
            # parsed_data = {}
            # for case_name, case_data in data.items():
            #     if isinstance(case_data, dict) and "input" in case_data and isinstance(case_data["input"], list):
            #         parsed_data[case_name] = case_data["input"]
            return data
    except FileNotFoundError:
        print(f"Error: '{file_path}' not found.")
        return None
    except json.JSONDecodeError as e:
        print(f"Error: JSON Parsing ")
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None

def demonstration_input_str_en(demonstration_input):
    return "\n".join(demonstration_input)

def read_text_file_to_lines(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = [line.strip('\n') for line in file.readlines()]
        return lines
    except FileNotFoundError:
        print(f"Error: '{file_path}' not found.")
        return []
    except Exception as e:
        print(f"Error: {e}")
        return []
