# **Happening API**

## Table of Contents

- [Project](#project)
  * [Objective](#objective)
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
  * [Homepage](#homepage)
  * [Profile Data](#profile-list)
  * [Events Data](#events-list)
  * [Comments Data](#comments-data)
  * [Interested Data](#interested-data)
  * [Going Data](#going-data)
  * [Followers Data](#followers-data)
  * [Reviews Data](#reviews-data)
  * [Contact Data](#contact-data)
- [Agile Workflow](#agile-workflow)
- [Testing](#testing)
- [Deployment](#deployment)
- [Credits](#credits)

# **Project**

## Objective

I live in a small town of around 15,000 people in the south of Spain, where lots of great events happen, but unlike in the big cities, there are no websites or applications dedicated to publicising the event information out to the people. 

Happening API provides a backend database to create, view, edit and delete event information for my town. A user who wishes to share an event can upload information about the event, including the date, a description, a category for who it's ideally aimed at, an image or event poster, and keyword tags. A user who wishes to attend events can follow event hosts, show their interest in an event, mark as attending an event, comment on an event and write a review or leave a rating for an event.

The API also includes search and filter logic to improve user experience, and make it easier for users to find events tailored to their own interests. 

## Links to Deployed Project

  + The project is deployed on Heroku and is available at the folowing link: [Deployed Happening API](https://happening-api-kelz.herokuapp.com/)
  + The link for the GitHub repo to corresponding front end for this project is here: [Happening Front End](https://github.com/)

## Project Structure

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

+ As a developer/superuser I can see a search field in the events list so that I can search for a specific event
+ As a developer/superuser I can filter the events list by category so that I can see only the events relating to one desired category
+ As a developer/superuser I can view a list of events by profiles I follow so that I can see only the events relating to profiles that I like
+ As a developer/superuser I can view a list of profiles followed by another profile so that I can see which profiles are following it
+ As a developer/superuser I can view a list of events I have posted an interested or going id to so that I can see only the events I am interested in attending
+ As a developer/superuser I can view a list of events relating to just one profile so that I can see only the events posted by a single user
+ As a developer/superuser I can view a list of comments linked to a particular event so that I can see see the comments relating to one single event id
+ As a developer/superuser I can view a list of reviews linked to a particular event so that I can see see the reviews relating to one single event id


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

## Homepage

When you first enter the API site, you are directed to the Root Route hompage, with a message welcoming you to the API for Happening. 

![homepage](images/homepage.png)

## Profile Data

Within the Profile List section, a user can view a list of all profiles in the API. Create functionality is not enabled, as the process is done automatically through the user registration process. 

![Profile List](images/profile-page.png)

Besides the fields created in the Profile model (as shown in the ERD Diagram), through the serializer, I also added the following fields to the JSON data:

* is_owner
* following_id
* events_count
* followers_count
* following_count
* going_count

I have set up ordering for the profile list, and selected the following parameters to sort the profiles by:

* events_count
* followers_count
* following_count
* going_count
* owner__following_created_at
* owner__followed_created_at

I have set up two field filters on the events list to filter as follows:

1. Profiles that are following the logged in user
2. Profiles that are being followed by the logged in user

If the user logs in, and views the detail of their own profile, additional Update and Delete functionality becomes available. Below the profile data, a pre-populated form is available to edit the profile model fields. At the top of the screen, a delete button is available to delete the profile from the API.

![Profile Edit Form](images/profile-edit.png)

## Events Data

Within the Events List section, a user can view a list of all events in the API. 

![Events List](images/events-page.png)

Besides the fields created in the Event model (as shown in the ERD Diagram), through the serializer, I also added the following fields to the JSON data:

* is_owner
* profile_id
* profile_image
* image_filter
* interested_id
* going_id
* comments_count
* interested_count
* going_count
* review_count
* average_rating

I have set up ordering for the events list, and selected the following parameters to sort the events by:

* comments_count
* interested_count
* going_count
* review_count
* average_rating
* interested_created_at
* going_created_at
* event_date

I have set up a search function whereby the full events list can be searched on by the event owner, title, event data, or event tags.

I have set up five field filters on the events list to filter as follows:

1. Events whose owners the logged in user is following - This will be the front end 'Feed' page
2. Events which the logged in user has posted interested in - This will combine with filter 3 to be the front end 'My Events' page 

3. Events which the logged in user has posted going to - This will combine with filter 2 to be the front end 'My Events' page

4. All events posted by user - This will be used in the 'Profile' page

5. All events in one category - This filter will be visible on all front end Event List pages

If the user logs in, a form becomes visible under the events list to create a new event. 

![Create an Event](images/create-event-form.png)

Once logged in, if the user views the details of a single event which they created additional Update and Delete functionality becomes available. Below the event data, a pre-populated form is available to edit the event. At the top of the screen, a delete button is available to delete the event from the API.

![Event Edit Form](images/event-edit.png)

## Comments Data

Within the Comments List section, a user can view a list of all comments in the API. 

![Comments List](images/comments-page.png)

Besides the fields created in the Comment model (as shown in the ERD Diagram), through the serializer, I also added the following fields to the JSON data:

* is_owner
* profile_id
* profile_image

I also set up one field filter to filter the comments by the event they are commenting on.

If the user logs in, a form becomes visible under the comments list to create a new comment. The event they want to comment on can be selected from the dropdown, and a comment text must be entered to post the comment successfully.

![Create a Comment](images/create-comment-form.png)

Once logged in, if the user views the details of a single comment which they created additional Update and Delete functionality becomes available. Below the comment data, a pre-populated form is available to edit the comment. At the top of the screen, a delete button is available to delete the comment from the API.

![Comment Edit Form](images/comment-edit.png)

## Interested Data

Within the Interested List section, a user can view a list of all interested posts in the API. 

![Interested List](images/interested-page.png)

If the user logs in, a form becomes visible under the interested list to create a new interested post. The event they want to be interested in can be selected from the dropdown, to link the interest with the event.

![Create an Interested Post](images/create-interested-form.png)

If a user tries to post interest to the same event twice, they see an error message saying that they are already interested in the selected event, and the duplicate interested post is not created.

![Create Duplicate Interested](images/interested-no-duplicates.png)

Once logged in, if the user views the details of a single interested post which they created additional Delete functionality becomes available. It is not possible to Edit an interested post.

![Delete an Interested Post](images/interested-delete.png)

## Going Data

Within the Going List section, a user can view a list of all going posts in the API. 

![Going List](images/going-page.png)

If the user logs in, a form becomes visible under the going list to create a new going post. The event they want to be going to can be selected from the dropdown, to link the going post with the event.

![Create a Going Post](images/create-going-form.png)

If a user tries to post going to the same event twice, they see an error message saying that they are already going to the selected event, and the duplicate going post is not created.

![Create Duplicate Going](images/going-no-duplicates.png)

Once logged in, if the user views the details of a single going post which they created additional Delete functionality becomes available. It is not possible to Edit a going post.

![Delete a Going Post](images/going-delete.png)

## Followers Data

Within the Follower List section, a user can view a list of all follower posts in the API. 

![Follower List](images/follower-page.png)

If the user logs in, a form becomes visible under the follower list to create a new follower post. The user they want to follow can be selected from the dropdown, to link the follower post with another user profile.

![Create a Follower Post](images/create-follower-form.png)

If a user tries to follow the same profile twice, they see an error message saying that they are already following the selected profile, and the duplicate follow post is not created.

![Create Duplicate Follower](images/follower-no-duplicates.png)

Once logged in, if the user views the details of a single follower post which they created additional Delete functionality becomes available. It is not possible to Edit a follower post.

![Delete a Follower Post](images/follower-delete.png)

## Reviews Data

Within the Review List section, a user can view a list of all reviews in the API. 

![Review List](images/reviews-page.png)

Besides the fields created in the Review model (as shown in the ERD Diagram), through the serializer, I also added the following fields to the JSON data:

* is_owner
* profile_id
* profile_image

I also set up one field filter to filter the reviews by the event they are reviewing.

If the user logs in, a form becomes visible under the reviews list to create a new review. The event they want to review can be selected from the dropdown, and a review text and rating must be entered to post the review successfully.

![Create a Review](images/create-review-form.png)

## Contact Data

# Agile Workflow

# Testing

# Deployment

# Credits