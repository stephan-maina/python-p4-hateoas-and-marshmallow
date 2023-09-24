from app import db
from models import Newsletter

if __name__ == '__main__':
    db.create_all()

    # Create and add sample newsletter entries
    newsletter1 = Newsletter(title='Liverpool News', body='Exciting updates about Liverpool FC.')
    newsletter2 = Newsletter(title='CR7 Fan Club', body='All the latest news about Cristiano Ronaldo.')

    db.session.add(newsletter1)
    db.session.add(newsletter2)
    
    db.session.commit()

    print("Sample newsletter entries added to the database.")
