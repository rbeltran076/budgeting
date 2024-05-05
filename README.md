
# dvis - Data Visualization Dashboard

dvis is a data visualization dashboard application that automatically generates insightful plots from any dataset .csv input. Built with Plotly and Panel.

## Usage

### Clone the Repository
Clone the dvis repository to your local machine using the following command:

```bash
git clone https://github.com/your-username/dvis.git
```

### Install Requirements
Navigate to the cloned repository directory and install the required dependencies using pip:

```bash
cd dvis
pip install -r requirements.txt
```

### Use your OpenAI API Key
Before running the app, you need to obtain your own OpenAI API key. You can sign up for an account and obtain your API key from the OpenAI website.

Once you have your API key, open the dvis.py file in a text editor, uncomment the line that reads `# openai.api_key =`, and write your API key.

### Deploy the App
Run the following command to deploy the dvis app on a local server:

```bash
panel serve dvis.py
```

Open a web browser and go to the provided URL in the terminal output to access the data visualization dashboard.
