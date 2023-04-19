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
    + [Contact](#contact)
- [Database Design](#database-design)
  * [Models](#models)
- [Features](#features)
- [Agile Workflow](#agile-workflow)
- [Testing](#testing)
- [Deployment](#deployment)
- [Credits](#credits)

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
+ As a developer/superuser I can retrieve a single comment by ID so that I can edit or delete this comment
+ As a developer/superuser I can edit a comment that I created so that I can amend any missing or incorrect information
+ As a developer/superuser I can delete a comment which I created so that I can delete comment data from the API

### Interested

+ As a developer/superuser I can create an interested object linked to a single event so that I can show interest in an event
+ As a developer/superuser I can delete an interested object which I created so that I can delete interested data from the API
+ As a developer/superuser I can not delete an interested object which I did not create
+ As a developer/superuser I can view a list of all interested objects so that I can see all interested objects created in the API

### Going

+ As a developer/superuser I can create a going object linked to a single event so that I can show confirmed attendance to an event
+ As a developer/superuser I can delete a going object which I created so that I can delete going data from the API
+ As a developer/superuser I can not delete a going object which I did not create
+ As a developer/superuser I can view a list of all going objects so that I can see all going objects created in the API

### Followers

+ As a developer/superuser I can create a follow so that I can follow another user
+ As a developer/superuser I can view a list of follows so that I can see all the follows that have been created
+ As a developer/superuser I can delete a follow so that I can unfollow another user profile


### Search and Filter

+ As a developer/superuser I can view filtered fields so that I can see the events created count when viewing a profile
+ As a developer/superuser I can view filtered fields so that I can see the events attended count when viewing a profile
+ As a developer/superuser I can view filtered fields so that I can see the followers count when viewing a profile
+ As a developer/superuser I can view filtered fields so that I can see the following count when viewing a profile
+ As a developer/superuser I can view filtered fields so that I can easily see the interested count when viewing an event
+ As a developer/superuser I can view filtered fields so that I can easily see the going count when viewing an event
+ As a developer/superuser I can view filtered fields so that I can easily see the comments count when viewing an event
+ As a developer/superuser I can view filtered fields so that I can easily see the average rating when viewing an event
+ As a developer/superuser I can view filtered fields so that I can easily see the review counts when viewing a review
+ As a developer/superuser I can see a search field in the events list so that I can search for a specific event

### Reviews

+ As a developer/superuser I can create a review so that I can link a review and rating to an event
+ As a developer/superuser I can view a list of all reviews so that I can see all reviews created in the API
+ As a developer/superuser I can edit a review that I created so that I can amend any missing or incorrect information
+ As a developer/superuser I can delete a review which I created so that I can delete review data from the API

### Contact

+ As a developer/superuser I can create a contact so that I can see messages created
+ As a developer/superuser I can view a list of all contacts so that I can see all contacts created in the API
+ As a developer/superuser I can edit a contact that I created so that I can amend any missing or incorrect information
+ As a developer/superuser I can delete a contact which I created so that I can delete contact data from the API


# Database Designs

## Models

I have created the following models for the Happening Backend API:
 * User (slightly customized from the Django standard User model)
 * Profile (automatically created on User creation)
 * Event (A post publicising a future event)
 * Comment (To make a comment on an event while it's being promoted)
 * Interested (To indicate if a user thinks the event sounds good)
 * Going (To indicate if the user plans to attend the event)
 * Follow (For users to follow event hosts)
 * Review (For users to rate and add a review comment post event)
 * Contact (To send a message to the email address in a profile)

The relationships between all of these models is summarized in the followed entity relationship diagram:
![erd](images/events-erd.drawio.png)

# Features

# Agile Workflow

# Testing

# Deployment

# Credits