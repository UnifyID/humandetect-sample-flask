# HumanDetect Example (Flask server)

## A. Run locally

### Prerequisites

* Python >= 3.7.0
* pip >= 20.0.0

### Setup

* Clone the repository to your system
* Run the following command to install the required libraries:

  ```
  pip install -r requirements.txt
  ```

### Add HumanDetect API Key

* Follow the [Getting Started Guide](https://developer.unify.id/docs/get-started/) to create an account on the [Developer Portal](https://dashboard.unify.id/account/sign-up).
* Generate an API key using the developer portal.
* Set the API key as an environmental variable.

  ```
  UnifyIDAPIKey=[Your API Key]
  export UnifyIDAPIKey
  ```

### Run Flask app

* `python wsgi.py` will run the Flask app locally.
* You can check that it's up and running by going to <http://localhost:5000/> in your browser.

## B. Deploy to Heroku

While running the Flask app locally might be great for trying things out, you'll have to deploy it via Heroku if you want to access it outside of your local environment.

* Create a new Heroku project
* Fork this repository, connect your GitHub account to Heroku, and deploy the forked GitHub repository
* Set your API Key as a Config var ([this guide](https://devcenter.heroku.com/articles/config-vars) can help you):
  * KEY: `UnifyIDAPIKey`
  * VALUE: Your API Key

## C. Run test

* Set the URL of your Heroku project as an environmental variable.

  ```
  UnifyIDHerokuURL=[Your Heroku project URL]
  export UnifyIDHerokuURL
  ```

* Run `python test.py`
* If everything goes according to plan, the following should be printed: `cab: 87.69%, police_van: 5.23%, racer: 1.45%, sports_car: 1.33%, car_wheel: 1.23%`

## D. Next Steps
Check out the HumanDetect Example iOS App if you want to see how HumanDetect can be implemented end-to-end, and to test the capabilities of HumanDetect in a real-world scenario.
