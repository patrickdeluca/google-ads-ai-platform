from app import create_app, db
from app.models import account, campaign, ad_group, ad, negative_keyword

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
