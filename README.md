## Self-replicating application
This is a web-based python application which asks user for an access to read and write his or her public repository data and, if granted, forks itself into user's profile.


## Heroku deployment
This instaction assumes that you already have registered accounts at [Heroku](https://id.heroku.com/login) and [GitHub](https://github.com/).

### 1. Prepare Heroku app
  - Go to Heroku deployment page with [![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)
  - Fill the `App name` field. Try to give it simple and meaningful name, because it will be used in an URL (`https://<your-app-name>.herokuapp.com`) to access your application.
  - Don't close this page - you'll need it later after you register a GitHub application.
 
### 2. Create GitHub application
  - To create new GitHub application go to [https://github.com/settings/applications/new].
  - Fill the `Application name` field with any name you want.
  - Fill the `Homepage URL` field with URL of heroku app (`https://<your-app-name>.herokuapp.com`) created at step 1.
  - The `Application description` field can be left empty.
  - Fill the `Authorization callback URL` with `https://<your-app-name>.herokuapp.com/callback/github`.
  - Register your GitHub app. You will be redirected to your new app's page. Don't close it yet.
  
### 3. Add GItHub app credential to Heroku app config
  - Open heroku deployment page from step 1.
  - Fill following config variables there:
    - `GIT_CLIENT_ID`: `Client ID` from you GitHub app settings.
    - `GIT_CLIENT_SECRET`: `Client Secret` from you GitHub app settings.
  - Press `Deploy app` button.

### 4. Check results
  - Go to `https://<your-app-name>.herokuapp.com`.
  - The application will ask you for an access to your GitHub account. If you authorize it, it will create a fork of itself for you.
  - Check your GitHub account for new repository with code of the self-replicating app.
    
  
