# capstone_project

# Title: Rooted Earth 

This app was created with the intention to help users understand their plants and keep track of growth or any changes to their plants. The user can keep track of their plant growth by uploading pictures, a description and the plants watering schedule and setting a to-do task for their watering schedules.By adding the feature of logging your own personal plant, their name and needs, it adds familiarity between the user,  their specific plants and the plants needs which increases the likelihood of consitent specialized care per the individual plant by doing this, chances of survival drastically increases and the user is more likely to see increased development per the species.
To see it all come together visit my website at https://rootedearth.herokuapp.com

Home Page: 
The home page has a watering to-do list where you can choose when plants from the “My Plant” page need to be watered. Once you have selected a plant and a watering date,  it will appear right under the watering list. When the user has completed watering a plant they can press the complete button and the task disappears from the page.The name of the selected plant is linked to the detail page, so when a user clicks on the name it will send them to that specific plant with all the information.

![toDo](https://i.imgur.com/etZEbFL.png)

Plant Info Page:
The plant information page shows the user a brief description of the plant,  along with how to propagate it and if the plant is toxic to pets. 

![plantInfo](https://i.imgur.com/rmXvn9r.png)

My Plant Page:
Users will be able to upload pictures of their own plants and add a name, description and there watering schedules. Once a plant has been added, the picture and the name of the plant will be displayed on the page. 

![myPlants](https://i.imgur.com/ZuMV4fS.png)

Plant Detail Page:
When the user clicks on a plant on “My Page” they will be taken to the detail page. This page contains all of the information that was entered for the plant that was clicked on. The user will also have the ability to edit the plants' information or just delete it. 
![detailPage](https://i.imgur.com/ZYZkp6Q.png)

Technologies used:
- Python
- PSQL
- Html
- CSS Bulma
- CSS Flexbox 
# Installation 
1. fork and clone repo
2. pipenve shell
- This will launch virtual environment.
3. pipenv install
- This will install dependencies
4. python3 manage.py runserver
- Will start up server
5. http://localhost:8000
- The app should appear in th browser

Stretch Goals:
User Authentication 
- Have the user be able to see the previous watering task 
- Have the user be able to update the watering task 


Refrences:
- GA provided notation. Such as 
    - https://seir1031-materials.notion.site/Django-URLs-Views-and-Templates-9e15b3fb81e74a808b3fe0ee0cabac57
    - https://seir1031-materials.notion.site/Django-Models-01f8b23c9e82487c8e5229acb95578a5
    - https://seir1031-materials.notion.site/Django-One-to-Many-97990e65f1f14997afb1c45c87554bc3
- POD leaders 
- Form Articles 

