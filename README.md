# GrubSpot-Journal

## Restaurant Finder Application

**Team Name**: ScRum and Coke  
**Team Members**:  
- **Prem Jadhav**: API development and database design  
- **Deep Patidar**: Frontend UI development and wireframes  
- **Prajwal Kongalla**: Cloud deployment and system architecture  
- **Varsha Chamakura**: Scrum master and project management  

### Overview
The Restaurant Finder Application is a web-based platform, similar to Yelp, that allows users to search for restaurants, submit reviews, and access various features based on their roles (User, BusinessOwner, Admin). The application is designed with scalability, reliability, and usability in mind.

### Features

#### For All Users:
- Search restaurants by name, category, cuisine, food type (Vegetarian, Vegan), price range, and ratings.
- View detailed information, including reviews and ratings for each restaurant.
- Submit reviews and ratings for restaurants.
- Search for restaurants by location (integrated with Maps API).
- Register and log in.

#### For BusinessOwners:
- Add new restaurant listings.
- Update details like name, address, contact info, hours, descriptions, and photos.
- View and manage owned restaurant listings.
- Login manually via a provided registration process.

#### For Admins:
- Detect and handle duplicate restaurant listings.
- Remove entries for closed businesses.
- Manage user-generated content (e.g., reviews).

### Design Decisions

#### Backend Architecture:
- API-first design to ensure modularity and scalability.
- RESTful APIs designed with JSON input/output for standardization.

#### Database:
- PostgreSQL for relational data, hosted on AWS RDS.
- Schema optimized for users, roles, restaurant listings, reviews, and ratings.

#### Frontend:
- Built with React.js for a dynamic, responsive user interface.

#### External Services:
- Maps API for geolocation-based searches.

#### Backend and Database:
- Hosted on an AWS EC2 cluster with a load balancer.
- Autoscaling configured for handling traffic spikes.

#### Roles and Security:
- Role-based access control (RBAC) ensures feature segregation for Users, BusinessOwners, and Admins.
- JWT used for secure authentication.

### Diagrams

#### Component Diagram
![component2](https://github.com/user-attachments/assets/e3082e3c-fa2c-4681-b2fa-d71233d378f2)

#### Deployment Diagram
![deployment3](https://github.com/user-attachments/assets/9f035ad5-54cb-4f71-8bbd-4c04926b40b7)

#### Class Diagram
![uml](https://github.com/user-attachments/assets/a8161446-005f-4766-93b3-c9cb8f9d3330)


### Tech Stack

- **Frontend**: React.js
- **Backend**: Flask (Python), RESTful APIs
- **Database**: PostgreSQL (AWS RDS)
- **Deployment**: AWS EC2 with Auto-scaling and Load Balancer
- **Authentication**: JWT
- **Caching**: Redis
- **Monitoring**: AWS CloudWatch

### Project Setup

#### Prerequisites:
- Node.js and npm
- Python 3.7+ and Pipenv
- Docker
- AWS account for deployment

#### Installing Dependencies and Preparing Database:

1. **Install Backend Dependencies**:
    - Install Pipenv and create a virtual environment:
        ```bash
        pip install pipenv
        ```
    - Install Python dependencies:
        ```bash
        pipenv install
        ```

2. **Set Up Environment Variables**:
    - In the project root directory, create a `.env` file and add the following configurations:
        ```env
        SECRET_KEY=<<SECRET_KEY>>
        DATABASE_URL=sqlite:///dev.db
        ```
    - Customize the environment variables as needed, especially `SECRET_KEY` and `DATABASE_URL`.

3. **Activate the Pipenv Environment**:
    - Run the following command to activate the virtual environment:
        ```bash
        pipenv shell
        ```

4. **Upgrade the Database and Seed Initial Data**:
    - Run the following commands to upgrade the database and seed it with initial data (105 businesses, 315 business images, 30 users, and 270 reviews):
        ```bash
        flask db upgrade
        flask seed all
        ```

5. **Start the Backend**:
    - Run the following command to start the Flask backend:
        ```bash
        pipenv run flask run
        ```

#### Frontend Setup:

1. **Set Up Frontend Environment**:
    - Navigate to the `/Grub-spot/react-app/` folder.
    - Create a `.env` file and add the following:
        ```env
        REACT_APP_BASE_URL=http://localhost:5000
        ```

2. **Install Frontend Dependencies**:
    - Install frontend dependencies:
        ```bash
        npm install
        ```

3. **Start the Frontend**:
    - Run the following command to start the React application:
        ```bash
        npm start
        ```


### Team Collaboration

#### Scrum Process:
- **Scrum Meetings**: 3 times a week to track progress.
- **Tasks**: Managed on GoogleSheets.
- **Sprints**: Each sprint lasts 2 weeks.

### Feature Set

| Feature                     | Role            | Status        | Sprint | Priority |
|-----------------------------|-----------------|---------------|--------|----------|
| Search restaurants          | User            | Completed     | 1      | High     |
| Submit Reviews and Ratings  | User            | In Progress   | 2      | High     |
| Add New Listings            | BusinessOwner   | Completed     | 3      | High     |
| Remove Duplicate Listings   | Admin           | To Do         | 4      | Medium   |

### Contributors
- **Prem Jadhav**: API development and database design
- **Deep Patidar**: Frontend UI development and wireframes
- **Prajwal Kongalla**: Cloud deployment and system architecture
- **Varsha Chamakura**: Scrum master and project management

### Python Dependencies (from `Pipfile`)

The backend of this project uses the following Python packages, which can be installed with **Pipenv**:

- **alembic**==1.6.5
- **click**==7.1.2
- **flask-cors**==3.0.8
- **flask-login**==0.5.0
- **flask-migrate**==3.0.1
- **flask-sqlalchemy**==2.5.1
- **flask-wtf**==0.15.1
- **flask**==2.0.1
- **greenlet**==1.1.0
- **gunicorn**==20.1.0
- **itsdangerous**==2.0.1
- **jinja2**==3.0.1
- **mako**==1.1.4
- **markupsafe**==2.0.1
- **python-dateutil**==2.8.1
- **python-dotenv**==0.14.0
- **python-editor**==1.0.4
- **six**==1.15.0
- **sqlalchemy**==1.4.19
- **werkzeug**==2.0.1
- **wtforms**==2.3.3
