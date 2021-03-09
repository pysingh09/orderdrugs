# Order Drugs

## Database

    sqlite3

## Packages

    Django==3.1.7
    django-phonenumber-field==5.0.0
    djangorestframework==3.12.2
    phonenumbers==8.12.19

## Commands to execute before running project

    pip install -r requirements.txt                      --> Install all the dependencies required to run the project
    python manage.py makemigrations                      --> To generate desired migrations files of created app
    python manage.py migrate                             --> To apply generated migration to DB
    python manage.py loaddata fixtures/initial_data.json --> to load initial data in DB

## Dummy token for users in current

    'doctor':- 'a8de2605d34e99e4ddad7a042528a78b1c6e9c17'
    'patient':- '0d2aff5f4f1553b9c9515cc8a50e79811a0329cc'
    'chemist':- '428c32bbd5b95dac547ae4e6de27deaef44827c4'

### Generate Prescription

    only user with type doctor allowed to genarte prescription

### Order Drugs

    only user with type patient can order of drugs
