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

Whilst coding the site I have ensured that the site is accesible for all. This is achieve by using:

* Google Dev Tools to check contrast of items.

* Semantic HTML.

* Aria Labels to hightlight areas for users who require the use of a screen reader.

## Technologies Used

### Languages Used

* HTML5
* CSS3
* JavaScript ES6
* Python

### Frameworks, Libraries & Programs Used

* [Balsamiq](https://balsamiq.com/wireframes/) was used to create the wireframes for the website.
* [Gitpod](https://www.gitpod.io/) the vast majority of my time was spent inside GitPod's VSCode Cloud IDE.
* Google Dev Tools was used to identify and resolve problems related to responsiveness and appearance.
* [Github](https://github.com/) was used to store my project in a repository.
* [Git](https://git-scm.com/) was used for version control.
* [Google](https://google.com) for research and problem solving.
* [Stack Overflow](https://stackoverflow.com/) for research and problem solving.
* [Flask](https://flask.palletsprojects.com/en/3.0.x/) the main Python framework used throughout the project.
* [WTForms](https://flask.palletsprojects.com/en/3.0.x/patterns/wtforms/) was used to help with form validation.
* [Bcrypt](https://pypi.org/project/bcrypt/) a hash function designed for password hashing and safe storing in the backend of applications.
* [PEP8 Validator](https://pep8ci.herokuapp.com/) Used to check python code for errors
* [ElephandSQL](https://www.elephantsql.com/) Used to store PostgreSQL database.
* [Heroku](https://id.heroku.com/) Used to deploy the project
* [Am I Responsive](https://ui.dev/amiresponsive) To create the responsive banner of devices.

## Testing

Start as you mean to go on - and get used to writing a TESTING.md file from the very first project!

Testing requirements aren't massive for your first project, however if you start using a TESTING.md file from your first project you will thank yourself later when completing your later projects, which will contain much more information.
  
Use this part of the README to link to your TESTING.md file - you can view the example TESTING.md file [here](milestone1-testing.md)

## Deployment & Local Development

### Deployment

The website/application is stored using GitHub for data and version control. To do this you follow these steps:

* After each addition, change or removal of code and by utilizing the IDE's terminal commands simply type:
    * git add.

    * git commit -m and include a git commit message with a brief description of what this particular commit envolves.

    * git push.

Following the above process allows you to view the updates made to the projects repository on GitHub.    

### Local Development

#### How to Fork

Forking is the process of creating a copy of the original repository. The process allows a developer to make any changes without affecting the main repo.

To do this:

* Search for the Github repo you want to copy.

* Select the "Fork" button located in the top right corner which is located under your profile icon.

* Once completed, you will now have your own version of that repo to make changes to.

#### How to Clone

To copy a Github repository:

* First navigate to the repository you wish to copy.

* Click on the "Code" button (which has a download icon) and copy the link provided.

* In the Gitpod terminal, navigate to the directory where you want to place the clone. Then, type "git clone" and paste the link you copied earlier and press enter.

* Another way to push a cloned repository to a new Gitpod workspace can be done through the use of a Gitpod extension installed in your prefered browser, in my case Google Chrome. This browser extension will add a green Gitpod button to your Github account and will be visible on every repository created, cloned or searched for.

#### Repository Deployment via Heroku

* Login to Heroku, Open the Heroku dashboard and click on New and then select "Create New App" from the drop-down menu.

* On the next page choose a name for your app (same as the project name), choose a region then click "Create App".

* On the settings tab click on Reveal Config Vars and add the Key Port and the value 8000, Debug Key should be set to False and also include the URL address of the Postgres Database hosting platform for storing the database. 

#### Deployment of The App

* Click on the Deploy tab and select Github - "Connect to GitHub".

* Enter the name of the repository and click "Search".

* Choose the repository that contains the correct files and click "Connect".

* There is a choice of either manual or automatic deployment where the app is updated when changes are pushed to the project's GitHub repo.

* Once the deployment method has been chosen the app will then be built and can be launched by clicking the "Open App" button which should appear below the build information window, alternatively there is another button located in the top right of the page.

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
