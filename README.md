[Link to Live site](https://community-website-ogonnelloe.herokuapp.com/)

# Ogonnelloes-Community-Website
A website where people can come and find information on the lovely village of Ogonnelloe. Local clubs and businesses can register information and provide posts with updates/information and users can register to comment on these posts. Admins have control over what clubs/businesses post and they in turn have control over comments that are added to their pages in terms of comments.

# Epics

## Groups
1. CRUD their profile details
2. Add updates about their groups
3. Approve/Delete users comments
## Businesses
1. CRUD their profile details
## Users
1. Can comment and like other comments on community update posts
2. Can request to join Groups
3. When registered give a rating to a business
## Visitors
1. Can navigate the site intuitively
2. Can view all information/pages containing community updates
3. Can create a user account
4. Fill out a form to request to be a Group or Business
## Admin
1. Register Groups/Businesses
2. Approve/Delete Groups/Businesses posts
3. CRUD functionality for community updates
4. Approve/Delete Users comments on 

# User Stories

## Visitors
1. Can view each page for community information (1)
2. Can view posts of community updates (1)
3. Can register for an account (1)
5. Can delete account (1)
6. Can comment on posts (1)
7. Can like others comments (1)

## Users
1. Can sign in/out (1)
3. Can add comments to group posts (2)
4. Can like other comments (2)
5. Can add notice to notice board (4+)

## Admin
1. Can CRUD community website update posts (1)
2. Can create a draft community website update post (1)
3. Can approve User comments (1)
4. Can CRUD main page details (4)
5. Can approve users comments (2)
6. Can approve Business registration (3)
7. Can CRUD <page name> details (4+)
8. Can approve notices on notice board (4+)

## Businesses
1. Can fill out a form to register their business (3)
2. Can sign in (3)
3. Can sign out (3)
3. Can CRUD their own details (3)

## Groups
1. Can fill out a form to register their business (1)
2. Can sign in (1)
3. Can sign out (1)
4. Can CRUD their own details (1)
5. Can CRUD update posts for their club (1)
6. Can approve/delete comments on posts (2)


# Database Diagrams

## Community Update Posts

| Key          | Name           | Type             | Extra Info                   |
|--------------|----------------|------------------|------------------------------|
|              | Title (Unique) | CharField        | Max length 200               |
| ForeignKey   | Author         | User model       | Cascade on delete            |
|              | Created date   | DateTime         | auto_now_add=True            |
|              | Updated date   | DateTime         | auto_now=True                |
|              | Content        | TextField        |                              |
|              | Featured Image | Cloudinary Image |                              |
|              | Excerpt        | TextField        |                              |
| Many to Many | Likes          | User model       |                              |
|              | Slug (Unique)  | SlugField        | Max length 200               |
|              | Status         | Integer          | Draft by default (default=0) |
|              | Event          | Boolean          |                              |
|              | Location       | CharField        |                              |
|              | Time           | DateTime         |                              |

## Community Post Comments

| Key         | Name       | Type          | Extra Info        |
|-------------|------------|---------------|-------------------|
| Foreign Key | post       | Post model    | Cascade on delete |
|             | name       | CharField     | Max length 80     |
|             | email      | EmailField    |                   |
|             | body       | TextField     |                   |
|             | created_on | DateTimeField | auto_now_add=True |
|             | approved   | BooleanField  | default False     |

