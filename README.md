## Running the Project

#### Create a Folder & Clone the Repository.
```
mkdir ~/Dev/search
cd ~/Dev/search
```

#### Create A Virtual Environment.
```
python3.9 -m virtualenv .
```

#### Activate the Virtual Environment.
```
source bin/activate
```

**In Windows use `.\Scripts\activate`**

#### Install Required Dependencies 
```
pip install -r requirements.txt
```

#### Make Migrations
```
python manage.py migrate
```

#### Run the Server
```
python manage.py runserver localhost:8000
```
#### you can query the API using the following endpoints
```bash
http://localhost:8000/api/search/?query={your_query}
```
#### _Example_
```bash
http://localhost:8000/api/search/?query=python
```
_Open [localhost:8000](http://localhost:8000) in Your Browser_
