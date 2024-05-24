# fuzzy-model-finder-streamlit
The code implements a Streamlit application called "Vehicle Model Matcher." It allows users to input a vehicle model name, and it finds the best match from a predefined list of database model names using fuzzy string matching.

Here's a brief description of the code:

1. **Imports**: The code imports necessary modules, including Streamlit (`streamlit`) for creating the web application and fuzzy string matching functions (`process` and `fuzz`) from the `fuzzywuzzy` library.

2. **Database Model Names**: It defines a list called `database_names` containing various vehicle model names.

3. **Normalization Function**: The `normalize_string` function is defined to normalize the input strings by converting them to lowercase and removing non-alphanumeric characters.

4. **Matching Function**: The `match_vehicle_model` function takes a user input string and the list of database model names as input. It finds the best match for the user input using fuzzy string matching and returns the best matched database name along with the matching score.

5. **Streamlit App**: The Streamlit application is created with a title "Vehicle Model Matcher" and a horizontal line for visual separation. It includes a text input box where users can enter a vehicle model name.

6. **Submit Button**: Upon clicking the "Submit" button, the user input is processed. If a user input is provided, the best matched database name and the matching score are displayed using markdown formatting. If no input is provided, an error message prompts the user to enter a vehicle model.

Overall, this Streamlit application provides a simple and interactive interface for matching user-provided vehicle model names with a predefined list of database model names.

To Run Code :
1. open cmd, locate to location where <your_file>.py is found
2. python -m streamlit run <your_file>.py

Output Screen
![image](https://github.com/DhanyathaShree/fuzzy-model-finder-streamlit/assets/140679630/a7637ca3-2155-4689-919a-a33495630f79)
![image](https://github.com/DhanyathaShree/fuzzy-model-finder-streamlit/assets/140679630/dbeca72c-3c16-4040-904a-659caebc7685)

