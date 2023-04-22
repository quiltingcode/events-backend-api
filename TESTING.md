# **Happening API**

# Testing

## Table of Contents

* [**Testing**](<#testing>)
    * [Code Validation](<#code-validation>)
    * [Automatic Testing](<#automatic-testing>)
    * [Manual Testing](<#manual-testing>)
    * [Known Bugs](<#known-bugs>)

## Code Validation 

### PEP8

The Happening API has been passed through the internal PEP8 validation tests which I installed into GitPod. The method I used to do this was as per the Slack Article written by kevin_ci on the 28th September 2022 in #announcements, since the PEP8online website no longer works:

1. Run the command 'pip3 install pycodestyle'
2. Press Ctrl+Shift+P
3. Type 'linter' into the search field
4. Select 'Python: Select Linter
5. Select 'pycodestyle' from the list
6. Select the 3 lines menu in the top left hand corner. Select 'View' and then 'Problems'. 
6. PEP8 errors are now displayed in a list as well as being underlined in red in the central editor window.


### Events_api files

* permissions.py - No problems or warnings found
* serializers.py - No problems or warnings found
* views.py - No problems or warnings found
* models.py - No problems or warnings found
* urls.py - No problems or warnings found

### Comments App py files

* models.py - No problems or warnings found
* serializers.py - No problems or warnings found
* tests.py - No problems or warnings found
* urls.py - No problems or warnings found
* views.py - No problems or warnings found

### Contact App py files

* models.py - No problems or warnings found
* serializers.py - No problems or warnings found
* tests.py - No problems or warnings found
* urls.py - No problems or warnings found
* views.py - No problems or warnings found

### Events App py files

* models.py - No problems or warnings found
* serializers.py - No problems or warnings found
* tests.py - No problems or warnings found
* urls.py - No problems or warnings found
* views.py - No problems or warnings found

### Followers App py files

* models.py - No problems or warnings found
* serializers.py - No problems or warnings found
* tests.py - No problems or warnings found
* urls.py - No problems or warnings found
* views.py - No problems or warnings found

### Going App py files

* models.py - No problems or warnings found
* serializers.py - No problems or warnings found
* tests.py - No problems or warnings found
* urls.py - No problems or warnings found
* views.py - No problems or warnings found

### Interested App py files

* models.py - No problems or warnings found
* serializers.py - No problems or warnings found
* tests.py - No problems or warnings found
* urls.py - No problems or warnings found
* views.py - No problems or warnings found

### Profiles App py files

* models.py - No problems or warnings found
* serializers.py - No problems or warnings found
* tests.py - No problems or warnings found
* urls.py - No problems or warnings found
* views.py - No problems or warnings found

### Reviews App py files

* models.py - No problems or warnings found
* serializers.py - No problems or warnings found
* tests.py - No problems or warnings found
* urls.py - No problems or warnings found
* views.py - No problems or warnings found

## Automatic Testing

The following automatic tests have been written into the Happening API, in order to cover all the user story scenarios. These are the tests that were created: 

| Status | **Events**
|:-------:|:--------|
| &check; | Can list events
| &check; | Logged out user can't create event
| &check; | Logged in user can create event
| &check; | Can retrieve event using valid ID
| &check; | Can't retrieve event using invalid ID
| &check; | Can update own event
| &check; | Can't update someone else's event
| &check; | Can delete own event
| &check; | Can't delete someone else's event

| Status | **Interested**
|:-------:|:--------|
| &check; | Can list interested
| &check; | Logged out user can't create interested
| &check; | Logged in user can create interested
| &check; | Can retrieve interested using valid ID
| &check; | Can't retrieve interested using invalid ID
| &check; | Can delete own interested
| &check; | Can't delete someone else's interested
| &check; | Can't post interested to the same event twice

| Status | **Going**
|:-------:|:--------|
| &check; | Can list going
| &check; | Logged out user can't create going
| &check; | Logged in user can create going
| &check; | Can retrieve going using valid ID
| &check; | Can't retrieve going using invalid ID
| &check; | Can delete own going
| &check; | Can't delete someone else's going
| &check; | Can't post going to the same event twice

| Status | **Comments**
|:-------:|:--------|
| &check; | Can list comments
| &check; | Logged out user can't create comment
| &check; | Logged in user can create comment
| &check; | Can retrieve comment using valid ID
| &check; | Can't retrieve comment using invalid ID
| &check; | Can update own comment
| &check; | Can't update someone else's comment
| &check; | Can delete own comment
| &check; | Can't delete someone else's comment

| Status | **Reviews**
|:-------:|:--------|
| &check; | Can list reviews
| &check; | Logged out user can't create review
| &check; | Logged in user can create review
| &check; | Can retrieve review using valid ID
| &check; | Can't retrieve review using invalid ID
| &check; | Can update own review
| &check; | Can't update someone else's review
| &check; | Can delete own review
| &check; | Can't delete someone else's review
| &check; | Can't review the same event twice

## Known Bugs

### Resolved

1. In my first project inception mentor meeting, I asked about what kind of field a 'Tags' model field would be, and whether it could just be a standard CharField. My mentor said that keywords should be stored in an array, so after further investigation I installed the Django Taggit Manager package to create an automatic array of words the user inputs into the events form 'tags' field. For some reason, however, despite using the blank=True attribute as per the Taggit docs, the API still requires this field to be filled in in order to sucessfully create a new event. I decided that this was not the end of the world and after a lot of research I left it as a required field. When I came to testing, my events tests were failing since I had changed over to Taggit, and so I had to amend the tests where an event is created to include a tags field as well as the title in order for the tests to pass. 

Please click [**_here_**](README.md) to return to the Happening API README file.