
# SetUp

## Repo Setup

Use the GitHub.com online interface to create a new remote project repository called something like "robo-advisor". When prompted by the GitHub.com online interface, let's get in the habit of adding a "README.md" file and a Python-flavored ".gitignore" file (and also optionally a "LICENSE") during the repo creation process. After this process is complete, you should be able to view the repo on GitHub.com at an address like https://github.com/YOUR_USERNAME/robo-advisor.

After creating the remote repo, use GitHub Desktop software or the command-line to download or "clone" it onto your computer. Choose a familiar download location like the Desktop.

After cloning the repo, navigate there from the command-line:

```sh
cd ~/Desktop/robo-advisor
```

## Environment SetUp

Create and activate a new Anaconda virtual environment:

```sh
conda create -n stocks-env python=3.7 # (first time only)
conda activate stocks-env
```

From within the virtual environment, install the required packages specified in the "requirements.txt" file you created:

```sh
pip install -r requirements.txt
```
In order to run the app, you need an API key from https://www.alphavantage.co/ After getting the API key, create a .env file in your text editor and place the API key in a variable called ALPHAVANTAGE_API_KEY.

This will allow you to run your code properly.

# Running the App


You should be able to initialize and run the app by entering this into the command line:

```sh
python app/robo-advisor.py
```

