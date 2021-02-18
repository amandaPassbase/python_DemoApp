# Official Passbase Django Python Demo
This Website shows an example integration of the Passbase HTML + JS client-side library and Python server-side library. Before you try to run the website, please sign up on our [developer platform](https://app.passbase.com/signup/user) and use your own publishable and secret API keys, which you can find in the [API settings](https://app.passbase.com/settings/api) section.

## Setup
1. Clone this repository to your machine
2. Create a virtualenv with `virtualenv env` and `source env/bin/activate`. You can find [here](https://help.dreamhost.com/hc/en-us/articles/115000695551-Installing-and-using-Python-s-virtualenv-using-Python-3) how to do it if necessary.
3. Install dependencies by running `pip3 install -r requirements.txt` in the root folder
4. Create a `.env.` file for the environment variables containing the following: `PASSBASE_SECRET_KEY=` You can see an example file `.env.example`
5. Run the migrations with `python3 manage.py migrate`
6. Exchange `YOUR_PUBLISHABLE_API_KEY` with your own publishable API key in home.html file on line 32

## Run the App

You can start the App by running the following command

```
python3 manage.py runserver
```

Access the web app in browser: http://localhost:8000/


## API

You can also see the server side library in action my sending a `POST` request to `http://localhost:8000/webhooks/passbase` with a JSON body and a valid `identityAccessKey`. 

Body Payload:
```
{
  "key": "identityAccessKey" 
}
```