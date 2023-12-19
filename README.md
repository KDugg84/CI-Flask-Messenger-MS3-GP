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

Main colours include:

* Blue: #039be5, #428bca.

* White: #eceff1, #fafafa.

* Gray: #777777, #333.

* Green: #228b22, #66bb6a.

* Red: #ff0000, #f16c6b, #dc3545.

### Typography

The main font used throughout the project is the default style that comes with the WT-Forms Flask extension.

### Imagery

Imagery does not really feature with this application other than the default profile picture that is added to a user's account when they sigh up.

The default avatar image that a user gets when they have created an account came from here [Default Profile Images](https://stock.adobe.com/es/search?k=%22default+profile+picture%22)

### Wireframes

The wireframes were created using Balsamiq desktop for Windows 10:

* [Home Page](flaskmessenger/static/img/wireframes/Home%20Page.png)

* [About Page](flaskmessenger/static/img/wireframes/About%20Page.png)

* [Login Page](flaskmessenger/static/img/wireframes/Login%20Page.png)

* [Register Page](flaskmessenger/static/img/wireframes/Register%20Page.png)

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

### Validation

The W3C Markup Validation Service was used on all HTML pages as well as the CSS Validator.

HTML Results:

The validator flagged the lines where the Python logic is used by the jinja templating engine, the example below is just one example that was highlighted with the base template and other HTML pages

* [Base](flaskmessenger/static/img/validation/Base%20Validation%20Result.PNG)

The img tags were missing alt attributes, those have been added the below pages.

* [Home](flaskmessenger/static/img/validation/Home%20Validation%20Result.PNG)

* [Account](flaskmessenger/static/img/validation/Account%20Validation%20Result.PNG)

* [Posts](flaskmessenger/static/img/validation/Posts%20Validation%20Result.PNG)

Both Login, Register and New Posts pages were flagged for the action attribute's empty spacing.

* [Login & Register](flaskmessenger/static/img/validation/Login%20&%20Register%20Validation%20Result.PNG)

* [New Posts](flaskmessenger/static/img/validation/New%20Posts%20Validation%20Result.PNG)

CSS Result:

* [Style](flaskmessenger/static/img/validation/CSS%20Validation%20Result.PNG)

### Python Testing

Python PEP8 validation was done via Code Institue's Python Linter.

The files that were tested:

* forms.py

* models.py

* routes.py

The only errors recieved were some lines of text exceeded the character limit of 79 and some areas of trailing white space where comments are located.

### Lighthouse

Results:

* [Mobile](flaskmessenger/static/img/validation/Lighthouse%20Mobile.PNG)

* [Desktop](flaskmessenger/static/img/validation/Lighthouse%20Desktop.PNG)

### Bugs and Errors

#### Known Issues and Fixes

The login form includes a Remember Me checkbox which is linked to a variable of the same name in the forms.py file under the class LoginForm. This checkbox does not display correctly when viewed in developer tools and this issue has not been resolved due to priorities and timescale. 

The CSS classes of 'success' and 'warning' which are meant to display different colours depending on the flash messages either telling the user that they have been successful in a task 'success' or that they have encountered an error 'warning', these two classes unfortunately do not display their respective colours when triggered by a flash message and subsiquently all flash messages are displayed by a fern green #66bb6a.

#### Testing User Stories

* First Time Visitor Goals:

    * To understand how the site works and what its about.

        * Upon entering the home page the user will see the site name/logo in the top left hand corner of the navigation bar, the name indicates to the user what the website/application is and does. The navigation bar links clearly identify what page is which without ambiguity. 

    * How to navigate the site.

        * The navigation bar links are clearly visible in the top right hand corner, each link tells the user what page is which.

    * Create an account and start posting new messages.

        * The user simply clicks on the link marked 'register' and is prompted to input their details to create an account to which they are redirected back to the login page to sign-in to then start posting new messages via the 'New Posts' link in the navbar which is only visible when the user has successfully logged in. 

* Returning Visitor Goals:

    * Log in and out of accounts.

        * After a user has logged in to their account they are automatically redirected back to the home page after which the logout navigation link becomes available whereby if the user clicks on the logout navigation link they are automatically logged out and redirected back to the home page.

    * Read posts made by other users.

        * A user can read posts made by other users which are viewed on the home page. 

    * Update and delete posts made by the user.

        * The user has the option to update a post by clicking on the post's title where they are sent to another form where the user can change/update the post's title and content. The option to delete a post entirely is also available via the post's title where both options to update and delete are visible in the form of two button. The delete button once clicked will prompt a modal popup asking the user if they want to delete the post where another delete button is visible to the user to click and the post is deleted entirely.

#### Further Testing

* All pages that make up the website/application were tested using Chrome Developer Tools to check for responsivness at the various different breakpoints to see how the site would react to being viewed on different devices.

* The website was viewed on various different devices such as Desktop, Laptop, Google Nexus 7 tablet and my Blackview BV6000 Android phone.

* Friends and family members were asked to review the site to highlight any bugs or user experience issues.

#### Manual Testing

* All throughout the development process as previously mentioned each page was consistently checked to make sure that they responded correctly to the various default breakpoints built into Chrome Developer Tools.

* The logo was clicked in each page to make sure that it was correctly linked to the home page.

* Each navigation bar link on each page was clicked to verify that it not only worked but took you to the correct page.

| TEST | OUTCOME | PASS/FAIL|
|:---:|:---:|:---:|
| Create Account | Account created via register form | Pass | 
| Post Message on Home Page | Post successfully created and displated | Pass |
| Edit Message | Post title clicked and via update post button redirected to Edit Post form to update post | Pass |
| Delete User's Message | Post title clicked and via delete button shown modal to warn user and press delete | Pass |
| Login | Login successful | Pass |
| Logout | Logout successfull | Pass |
| View Other User's Posts | Created several accounts to view different posts on home page | Pass |
| View Account Details | Details such as username and email address visible in accounts page | Pass |
 
## Deployment & Local Development

### GitHub Deployment

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

### Code Used

###  Acknowledgments