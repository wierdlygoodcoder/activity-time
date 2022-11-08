# [Activity Booking](https://activity-times.herokuapp.com/)
Welcome to the activity booking here is the readme that will go through the blood sweat and tears that I have had to go through for you to see this. 

Firstly the reason for this website is so that if a venue/customer whats to book someone to come and do an activity they can be booked in for said activity. the way this happens is by signing up. Once that happens the user then can log in and then use the book in form. They will enter the required data then once they have submitted the data they have been asked for. 

Once this is done the user has a choice to edit the booking or delete the booking as a whole. if they choose to update they will be taken to a different page and allowed to change any aspect of the bookings. if the user chooses to delete the booking they are shown a model and asked if they are sure they would like to delete the booking and if they do it is gone from the database. 

if the user does not what to do any thing with that they do not have to.


![Am I responsive](https://user-images.githubusercontent.com/95313496/200426518-b1622bb8-e01b-4783-85f4-a45913dddcac.jpg)



## Features
- On this website, you can log on and out 
- While logged in you can then book in with the booking tab 
    - You can edit 
    - Update 
    - And view a booking 
- You can also register for an account
- Can look at news items as well 
- Can not double book on the booking in



### Future Features
I would like to put a way for the admin to easily add a new story 
Add a way for users adding in a comment to talk about their experience
Have a like button for storeys
Have a map so the users can find the activity centre easier
Link the bookings to a calendar external and then have that separate the members of the team.
Allow the users to use social media logins if they would like.
Bookings for separate accounts and not everyone can see all of the bookings in the database.
update messaging for the forms 
do automated testing



## Testing
| Test | pass  | notes | 
|---|---|---|
| does the website open to the home page | **Pass**  |  ![Screenshot 2022-11-08 074809](https://user-images.githubusercontent.com/95313496/200505351-39a7d7f7-1faa-44b7-930c-4f9e6ccb076d.jpg)|
| can you go to any other page on the site  | **Pass** |  ![Screenshot 2022-11-08 075500](https://user-images.githubusercontent.com/95313496/200508511-5a44ca15-8752-4524-998d-fdf565f4f5f5.jpg)|  
| can you sign up | **Pass** |![Screenshot 2022-11-08 081542](https://user-images.githubusercontent.com/95313496/200510718-0946862e-ed46-46b1-9de0-5871b0e55462.jpg)|
|can you use an email already used|**pass**|![Screenshot 2022-11-08 075658](https://user-images.githubusercontent.com/95313496/200508981-4713eea3-9ccb-4d99-be26-64fd87742c93.jpg)|
|can you miss parts of the email|**pass**|![Screenshot 2022-11-08 075624](https://user-images.githubusercontent.com/95313496/200508848-3e47faa3-d038-4c60-9a94-d05bcac9ceef.jpg)|
| can you log in | **pass** | ![Screenshot 2022-11-08 075745](https://user-images.githubusercontent.com/95313496/200509057-dd5cb632-331d-4366-84cb-25c7b0b38d26.jpg)|
|  does messages show for the login| **pass** | ![Screenshot 2022-11-08 075745](https://user-images.githubusercontent.com/95313496/200509155-1bdba9b3-1130-43bc-af86-af3deecd1ab4.jpg)|
| can you book a session  | **pass** | ![screenshot 08-11-2022](https://user-images.githubusercontent.com/95313496/200509589-cb65030e-2772-424e-84a1-a405488bcdf2.jpg)|
| can you double book | **pass** | ![Screenshot 2022-11-08 081140](https://user-images.githubusercontent.com/95313496/200509862-a41c68a1-85fd-4ac8-821e-1868810812d1.jpg)|
| is there news items | **pass** | ![Screenshot 2022-11-08 075500](https://user-images.githubusercontent.com/95313496/200509913-57ddb6b0-bd18-40b5-926f-ccf13f1eee01.jpg)|
| do the social media items open in to a new tab  | **pass** | ![Screenshot 2022-11-08 081306](https://user-images.githubusercontent.com/95313496/200510131-c76ad970-3ee5-413d-bed7-b7c1a1599b2e.jpg)|


### Solved bugs
- Fixed commas on settings.py on the installed app 
- Fixed link to the media directory 
- Fixed link to CSS and js directory
    - I'll show you in the main app urls.py I added the following!
    - In settings.py I added to line 135
    - And I removed the static lines from booking > urls.py 
- Found that when I was trying to input my date and time on the booking form I was struggling to find the right way of getting it to show on the form fixed by using date and time input types for it.
- Struggling to get the form to post to the database
    - The submit button did not work
    - Submit button but it gave me back a 405 error
- Added functionality to have it so you can not do two bookings at the same time found that when I did the form would not submit properly.
- When deploying the website to Heroku the CSS folders and media fields were not working I got around this by putting the images directly onto Cloudinary and setting the debut to false



### Remaining bugs
- When reducing screen size the table on the booking page sometimes makes a white bar on the right-hand side.

### Validator testing
- The website has pasted the HTML validator.
- Using pycodestyle the project as a whole passes on pep8 apart from some "line too long" on a couple of lines.
- The website CSS has passed the CSS validator as well 
![Screenshot 2022-11-07 064035](https://user-images.githubusercontent.com/95313496/200488091-1a868871-e57a-44ba-b1c4-997f64461987.jpg)
- Using the js hint application the javascript in the project has no warnings.
- When using the wave tool there were no errors
- The lighthouse performance accessibility and SEO have above 96 scores from a lighthouse.
![Screenshot 2022-11-07 065348](https://user-images.githubusercontent.com/95313496/200489029-0ff05850-483a-41db-99fc-f8f581368c68.jpg)


## Deployment
To deploy this project I went through these steps:

1. I added the proc file and the requirements .txt.
    -I put the following code into the procfile: 'web: gunicorn activity_time.wsgi'
2. Then I went on to Heroku and added a new project to my workspace.
3. I then linked my GitHub account to the workspace and added the required repository.
4. I then did a git add and a git commits to then push the code to both the git hub and git pod.
5. I then found out that if the website worked it did not so I had to set the debug setting to false.
6. Then I had to put the images themselves on to cloundenry.
7.  then opened up the application and it was what I was seeing before. 

## Credits
- Code institute for the base template and allow me to complete the project
- My mentor 
- Nick Lennon 
