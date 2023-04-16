- [Happening Backend](#happening-backend)
  * [Links to Deployed Project](#links-to-deployed-project)
- [Project Structure](#project-structure)
  * [Developer User Stories](#developer-user-stories)
    + [Profiles](#profiles)
    + [Events](#events)
    + [Comments](#comments)
    + [Interested](#interested)
    + [Going](#going)
    + [Followers](#followers)
    + [Search and Filter](#search-and-filter)
    + [Reviews](#reviews)
- [Database Design](#database-design)
  * [Models](#models)

# Happening Backend

  I live in a small town of around 15,000 people in the south of Spain, where lots of great events happen, but unlike in the big cities, there are no websites or applications dedicated to publicising the event information out to the people. 

  Happening API provides a backend database to create, view, edit and delete event information for my town. A user who wishes to share an event can upload information about the event, including the date, a description, a category for who it's ideally aimed at, an image or event poster, and keyword tags. A user who wishes to attend events can follow event hosts, show their interest in an event, mark as attending an event, comment on an event and write a review or leave a rating for an event.

  The API also includes search and filter logic to improve user experience, and make it easier for users to find events tailored to their own interests. 

  ## Links to Deployed Project
    + The project is deployed on Heroku and is available at the folowing link: [Deployed Happening API](https://events-api.herokuapp.com/)
    + The link for the GitHub repo to corresponding front end for this project is here: [Happening Front End](https://github.com/)

# Project Structure

The overall structure of the project was modelled on the [drf-api](https://github.com/Code-Institute-Solutions/drf-api) walkthrough due to time constraints and the Project 5 assessments requirements including most of what is included in the walkthrough project.

However, additional custom models have also been developed where possible such as going, and review, and I have tried to customize the walkthrough models somewhat as well to fit more closely with the scope of my own sharing platform. 

## Developer User Stories
### Profiles

+ As a developer/superuser I can view a list of all profiles so that I can see all the profiles that have been created
+ As a developer/superuser I can view the details of one profile so that I can see individual profile data
+ As a developer/superuser I can edit a profile when I am logged in so that update my personal information
+ As a developer/superuser I can delete a profile that I own so that I can delete my user account from the API

### Events

+ As a developer/superuser I can view a list of all events so that I can see all events at once
+ As a developer/superuser I can view a single event so that I can see single event details, including comments
+ As a developer/superuser I can create a new event so that this event will be displayed in the events list
+ As a developer/superuser I can edit an event that I created so that I can amend any missing or incorrect information on the event posting
+ As a developer/superuser I can delete an event which I created so that I can delete event data from the API

### Comments

+ As a developer/superuser I can create a comment so that I can link a comment to an event
+ As a developer/superuser I can view a list of all comments so that I can see all comments created in the API
+ As a developer/superuser I can edit a comment that I created so that I can amend any missing or incorrect information
+ As a developer/superuser I can delete a comment which I created so that I can delete comment data from the API

