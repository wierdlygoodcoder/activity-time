# Activity Booking
welcome to the activity booking here is the readme that will go throught the blood sweat and tears that i have had to go throught for you to see this. 

firstly the reason for this website is so that if a vennue/ custmer whats to book in someone to come and do an activity they can can be booked in for said activity


![Am I responsive](https://user-images.githubusercontent.com/95313496/200426518-b1622bb8-e01b-4783-85f4-a45913dddcac.jpg)



## Features
- in this web sitem you can log on and out 
- while logged in you can then book in with the booking in tab 
    - you can edit 
    - update 
    - and veiw a booking 
- you can also register for an account
- can look at news items as well 
- can not double book on the booking in



### Future Features
i would like to put in the way for admin to easliy add in a new story 
add in a away of users adding in a comment ot talk about there expeiance
have a like buttin for storys
have a map so the users can find the activity center easier
link the bookings to a calender external and then have that seperate out the the members of the team.
allow the users to use soical media logins if they would like.



## Data Model


## Testing


## Bugs


### Solved bugs
- fixed commas on settings.py on the installed app 
- fixed link to the media directory 
- fixed link to CSS and js directory
    - I'll show you in the main app urls.py I added the following!
    - in settings.py I added to line 135
    - and I removed the static lines from booking > urls.py 
- Found that when I was trying to input my date and time on the booking form I was struggling to find the right way of getting it to show on the form fixed by using date and time input types for it.
- struggling to get the form to post to the database
    - the submit button did not work
    - submit button but it gave me back a 405 error
- added functionality to have it so you can not do two bookings at the same time found that when I did the form would not submit properly.
- when deplying the website to herku the css foolders and media fileds was not working i got around this by putting the images directly on to cloudenry and setting the debut to false



### Remaining bugs
- when reduceing screen size the table on the booking page sometimes makes a white bar to the right hand side.

### Validator testing
- the website has pasted the html validator.
- using pycodestyle the project as a whole passes on pep8 apart from some "line too long" on a couple of lines.
- the websites css has passed the css validator as well 
![Screenshot 2022-11-07 064035](https://user-images.githubusercontent.com/95313496/200488091-1a868871-e57a-44ba-b1c4-997f64461987.jpg)
- using the js hint application the javascript in the project as no warnings.
- when using the wave tool there was no errors
- the light house performance accessiblity and seo hare above 96 score from lighthouse.
![Screenshot 2022-11-07 065348](https://user-images.githubusercontent.com/95313496/200489029-0ff05850-483a-41db-99fc-f8f581368c68.jpg)


## Deployment
to deploy this project i went trough these steps

1- I added the proc file and the requirements .txt.
    -I put the following code in to the procfile : 'web: gunicorn activity_time.wsgi'
2- then i whent on to herokku an added a new project to my workspace.
3- i then linked my githubaccount to the workspace and added the required repositroy.
4 i then did a git add and a git commit to then push the code to bothe the git hub and git pod.
5- i then found oput if the web site work it did not so i had to set the debug setting to faluse.
6 - then i had to put the images them self on to cloundenry.
7 then opened upo the application andit was what i was seeing before. 

## Credits
- Code institute for the base template and allow me to complete the project
- My mentor 
- Nick Lennon 
