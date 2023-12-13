![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

# Flask Messenger (Development Name)

Add an image of the finished site here. I like to use [amiresponsive](https://ui.dev/amiresponsive)

For my third Milestone project (MS3) I decided to create a messaging site/application that allows users to register for an account where user's can create posts which can then be viewed on the main home page. These posts can also be read by other users, also updated and or deleted but only by the user who submitted the original post.

The main focus of the project was backend development which included the use of a database such as PostreSQL to store user's information and posts and the Flask framework which is a Python based framework which allows developers to insert Python logic into the frontend.

I chose this project because messaging sites/applications are perfect examples of C.R.U.D (Create, Read, Update and Delete) functionality. The site was designed more to be viewed on small screen devices to try to mimic other messaging apps.

Add a link to the live site here.

## CONTENTS

* [User Experience](#user-experience-ux)
  * [User Stories](#user-stories)

* [Design](#design)
  * [Colour Scheme](#colour-scheme)
  * [Typography](#typography)
  * [Imagery](#imagery)
  * [Wireframes](#wireframes)

* [Features](#features)
  * [General Features on Each Page](#general-features-on-each-page)
  * [Future Implementations](#future-implementations)
  * [Accessibility](#accessibility)

* [Technologies Used](#technologies-used)
  * [Languages Used](#languages-used)
  * [Frameworks, Libraries & Programs Used](#frameworks-libraries--programs-used)

* [Deployment & Local Development](#deployment--local-development)
  * [Deployment](#deployment)
  * [Local Development](#local-development)
    * [How to Fork](#how-to-fork)
    * [How to Clone](#how-to-clone)

* [Testing](#testing)

* [Credits](#credits)
  * [Code Used](#code-used)
  * [Content](#content)
  * [Media](#media)
  * [Acknowledgments](#acknowledgments)

---

## User Experience (UX)

The best (intuitive) UX creates single-use learning.

### Main Objectives

Design and create a messaging site/application which demonstrates the use of libraries and frameworks which are available to developers.

My three main objectives were:

* I wanted to make the site easily accessible and intuitively navigated for the users.

* The use of the backend framework allows users to create an account, post messages, read other user's posts on the home page, update posts if they wish to as well as being able to delete their posts.

* I used ElephantSQL to store the PostgreSQL database for this project.

### User Stories

* First Time Visitor Goals:
    * To understand how the site works and what its about.

    * How to navigate the site.

    * Create an account and start posting new messages.

* Returning Visitor Goals:
    * Log in and out of their accounts.

    * Read posts made by other users.

    * Update and delete posts made by the user.  

## Design

### Colour Scheme

The colour scheme for this project was based somewhat on Code Institute's Task Manager walkthrough mini project which has a very neutral theme, alot of white space and light blue with the action buttons using more bright colours to help with site navigation.

### Typography

The main font used throughout the project is the default style that comes with the WT-Forms Flask extension.

### Imagery

Imagery does not really feature with this application other than the default profile picture that is added to a user's account when they sigh up.

### Wireframes

Add the images or links for your wireframes here.

## Features

### General features on each page

The general features of most of the app's pages include: 

* A navigation bar which is responsive across all device screens.

* A logo which directs the user back to the home page when clicked.

* A footer with font awesome icons for social media links.

Other features included in the 'Register' and 'Login' pages are:

* The register page includes form fields to allow the user to add their details to create an account such as their username, email address, a password and to confirm that password. A user cannot leave the form fields blank as the form will not post and the user is then prompted to fill in the required information.

* the register page includes a button which 'POSTs' the user's details to the database.

* The register page form includes a link to the login page at the bottom if they are already a user.

* After a user has created their account they are automatically redirected to the login page to sign in.

* The login page only requires a user to login with their username and password.

* As with the register page the login form includes a link at the bottom asking the user if they need an account in case they have clicked on the wrong page by accident.

After a user has successfully logged in they will see a new link in the navbar called 'New Posts':

* The new posts form has two fields one for 'Title' and for 'Content'.

* Once a user has submitted a new post they can then view that post on the home page along with other posts made by other users.

* A user then has the option to update a post by clicking on the post title where they will see two new buttons marked 'Update Post' and 'Delete Post'.

* If the user wishes to update a post they simply click on the 'Update Post' button where they are redirected back to the new post form to change or update that post's title and content and resubmit the post.

* Those changes will then be shown on the home page. 

* If a user wishes to delete a post they go through the same procedure as before by clicking on the post's title and when they click 'Delete Post' they will be prompted by a modal asking if they want to delete that post and if the user clicks 'Delete Post' on the modal that post will be deleted from the home page and the database.

### Future Implementations

* For users to be able to comment on other user's posts.

* To be able to like or subscribe to a particular user.

* For a user to be able to post links to other pages.

* for users to be able to post photos or video content not just text.

### Accessibility

## Technologies Used

### Languages Used

### Frameworks, Libraries & Programs Used

## Deployment & Local Development

👩🏻‍💻 View an example of a completed Deployment & Local Development section [here](https://github.com/kera-cudmore/TheQuizArms#Deployment)

### Deployment

Include instructions here on how to deploy your project. For your first project you will most likely be using GitHub Pages.

### Local Development

The local development section gives instructions on how someone else could make a copy of your project to play with on their local machine. This section will get more complex in the later projects, and can be a great reference to yourself if you forget how to do this.

#### How to Fork

Place instructions on how to fork your project here.

#### How to Clone

Place instructions on how to clone your project here.

## Testing

Start as you mean to go on - and get used to writing a TESTING.md file from the very first project!

Testing requirements aren't massive for your first project, however if you start using a TESTING.md file from your first project you will thank yourself later when completing your later projects, which will contain much more information.
  
Use this part of the README to link to your TESTING.md file - you can view the example TESTING.md file [here](milestone1-testing.md)

## Credits

👩🏻‍💻 View an example of a completed Credits section [here](https://github.com/kera-cudmore/BookWorm#Credits)

The Credits section is where you can credit all the people and sources you used throughout your project.

### Code Used

If you have used some code in your project that you didn't write, this is the place to make note of it. Credit the author of the code and if possible a link to where you found the code. You could also add in a brief description of what the code does, or what you are using it for here.

### Content

Who wrote the content for the website? Was it yourself - or have you made the site for someone and they specified what the site was to say? This is the best place to put this information.

###  Media

If you have used any media on your site (images, audio, video etc) you can credit them here. I like to link back to the source where I found the media, and include where on the site the image is used.
  
###  Acknowledgments

If someone helped you out during your project, you can acknowledge them here! For example someone may have taken the time to help you on slack with a problem. Pop a little thank you here with a note of what they helped you with (I like to try and link back to their GitHub or Linked In account too). This is also a great place to thank your mentor and tutor support if you used them.
