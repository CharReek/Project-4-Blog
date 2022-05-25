# Damsel in Dior
Damsel in dior is a blog dedicated to all things fashion! It gives users a chance to get into 

# Table of Contents


# UX
## User stories
### Site User 
 1. As a site user i can look at a paginate list of blog posts / images so that i can choose which one i want to look at.  
 2. As a site user i can see the date that a blog post was made so that i can keep up to date on current trends and read the most up to date blog posts.
 3. As a site user i can click on a selected post so that i can read the blog post.#
 4. As a site user i can comment on a post so that i can be involved in the conversation and offer my opinion. 
 5. As a site user i can view comments on posts so that i can see other peoples opinions. 
 6. As a site user i can see what items are trending so that i can keep up with the latest trends
 7. As a site user i can register for an account so that i can leave comments on posts 
 8. As a site user i can sign in to an excisting account so that i can comment on posts 
 9. As a site user i can sign out of my account 

### Admin
1. As a admin i can approve comments so i can make the blog a safe place for all users 
2. As a admin i can draft blog posts so that i can draft a post before i want to post it 
3. As a admin i can edit, view and delete post so that i can change anything that maybe needed or delete the post.

### development plans 
### Structure
### Skeleton 
### Design


# Features 

## Navigation Bar 
The navigation bar is there to help users get around the site easily. This is always at the top so that views can always use it. The navigation bar is fully responsive and when it shriks it goes into a collapsable nav bar. This is great for moblie users. The menu also changed depending on if the user is logged in. If the user is not logged in the nav bar will show 'register' 'login'. Once the user is logged in the nav bar will change to 'logout'. 
## Footer
The footer is showed through out the entire sit, it has links to social media sites so users can keep up with whats going on on various different platform linked to the blog.

## Blog Post Cards
Blog post cards are shown on the home page, this is due to it beign the main focus of the blog. The 4 most recent posts will show if there are over 4 post the page will paginate and add a next / previous button. The user then has the option to select what post they want to view. Each post has an image on the front that is a reference to what the post is about. I chose a colourful background to add something more to the page, this will also help catching the attention of the user making them want to intereact with the post. I also added a title that on hover/ click has a line animation underline the text, this lets the user knwo where on the page they are looking at and helps highlight the post more. 

## Blog posts
All blog posts follow the same layout in order to keep the site uniformed and make it easier for the user to navigate. The title, date and creater are at the top of the page, this shows the user when and who it was posted by before they continue reading. 

## Whats hot 
This is an image slider that showcases products that are currently on trend / popular that users may be intrested in. If a user likes an item it will taken them to a website that sells the product. I decided to impliment this feature as there is nothing worse than loving a product on a blog and not being able to find where it is from! The swiper also adds an interactive feature to the page. 

## Lookbook Cards
The lookbook showcases a variety of different images of outfits, this way the user can just browse though for inspiration with out having to click anything. If the user would liek to know more they can click the image and it will take them to a blog post that has all the outfit details. Giving them the option to find where any items are from.

## Lookbook Posts
These are present for users who would like to know the outfit details for anything posted via lookbook. It follows the same structure as the blog post so that it is easy for users to navigate. 

## Comment section 
Both the blog post and lookbook post have a comments section at the bottom that those who are register can use to leave comments. This feature makes it so that other users have a way to communicate. This also opens up a disscusssion about the post and can help offer stylign tips/ hacks. The comments need to be aproved by an admin, i have done this so any comments that are no appropraite can be declined. This will help keep users on the site safe.

## Register 
This feature allows new user to register for an account so that they can leave comments on posts. 

## Login 
This allows users to log into their accoutn so that they can comment on posts 

## Logout
This allows users to sign out of their account. 

# Future Features

Going forward i would like to add in a feature so that users can upload images to the lookbook page, that way the lookbook page become a community page where people can upload images and give others feedback on an outfit that has been posted. This will be the equivilent of sending outfit pictures to your friends! This would be a great way for users to interact with each other and gain style tips and inspiration.I would then tie this into a profile page so that users can manage what images / comments they have posted and edit any information such as an email or password. This would give users the option to add and remove any images they no longer want avaliable with in the lookbook.

# Issues & Bugs

# Technoligies used 
* HTML 
* CSS
* Javascript
* Python 
* Django 
* Cloudinary 
* Font Awesome 

# Testing 

## Manual Testing 

# Deployment
I took the following steps to deploy my project to heroku, i also referenced the [Django Blog Cheatsheet](https://codeinstitute.s3.amazonaws.com/fst/Django%20Blog%20Cheat%20Sheet%20v1.pdf)
1. Create the heroku app
2. Sync up the Postgres dadabase
3. Create the settings.py file
4. Sync Cloudinary 
5. Deploy to heroku


# Credits 
* I Used [Atlantic Pacific](https://www.the-atlantic-pacific.com/) and [Hello fashion](https://www.hellofashionblog.com/) as inspitation for the style / layout of my blog
* I used code insitutes walk through for insallign all auth
* I used [Django central]( https://djangocentral.com/building-a-blog-application-with-django/) for help when it came to setting up views 
* I used bootstrap documentation to help me understand bootstrap 5 

### Image Credits 
* I created all the home page images myself using custome backgrounds and images i got from the below places 
  * The spring must have image is from [The Face](https://theface.com/style/versace-ss22-milan-fashion-week-womenswear-dua-lipa-naomi-campbell-gigi-hadid-fashion-style)
  * The what im loving now image is from [Celine](https://www.celine.com/en-int/celine-women/handbags/belt-bag/micro-belt-bag-in-grained-calfskin-189153ZVA.25VP.html) the blazer image in the article is from [Flannels](https://www.flannels.com/miu-miu-levantina-g-blazer-600409#colcode=60040906)
  * The designer gifts under £100 is from [Burberry](https://uk.burberry.com/make-up/) the images in the article are from [Dior](https://www.dior.com/en_gb/maison/objects/trinket-trays), [Flannels](https://www.flannels.com/heron-preston-embossed-heron-t-shirt-602521#colcode=60252103), [ Vivienne Westwood](https://www.viviennewestwood.com/en/men/jewellery/rings%C2%A0/westminster-ring-silver-64040016W004W004.html)
* All images on the lookbook page are my own images 
* Images for whats hot slider are from [Flannels](https://www.flannels.com)

### Acknowledgements 
* A big thanks to the front end team that i work with they have help inspired me and given me some great ideas on what features to impliment! 
