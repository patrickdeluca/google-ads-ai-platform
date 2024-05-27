### Google Ads AI Optimizer Platform

## Overview
The Google Ads AI Optimizer platform is designed to enhance the management and optimization of Google Ads campaigns using AI capabilities. It provides a structured backend with a Flask web application, a responsive frontend using Bootstrap, and integrates AI services for generating insights and responses. The platform allows users to manage accounts, campaigns, ad groups, ads, and negative keywords efficiently.

## Project Structure

```
gads/
├── app/
│   ├── __init__.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── account.py
│   │   ├── campaign.py
│   │   ├── ad_group.py
│   │   ├── ad.py
│   │   ├── negative_keyword.py
│   ├── routes/
│   │   ├── __init__.py
│   │   ├── account.py
│   │   ├── ai.py
│   │   ├── campaign.py
│   │   ├── ad_group.py
│   │   ├── ad.py
│   │   ├── negative_keyword.py
│   ├── schemas/
│   │   ├── __init__.py
│   │   ├── account.py
│   │   ├── ad.py
│   │   ├── campaign.py
│   │   ├── ad_group.py
│   │   ├── negative_keyword.py
│   ├── services/
│   │   ├── __init__.py
│   │   ├── data_service.py
│   │   ├── ai_service.py
│   ├── templates/
│   │   ├── index.html
│   ├── static/
│   │   ├── style.css
├── config.py
├── run.py
├── tests/
│   ├── __init__.py
│   ├── test_routes.py
│   ├── test_services.py
```

## Installation

### Prerequisites
- Python 3.6 or higher
- pip (Python package installer)

### Steps

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/gads-optimizer.git
   cd gads-optimizer
   ```

2. **Create a virtual environment and activate it:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables:**
   Create a `.env` file in the root directory and add the following:
   ```plaintext
   SECRET_KEY=your_secret_key
   OPENAI_API_KEY=your_openai_api_key
   ```

5. **Run the Flask application:**
   ```bash
   flask run
   ```

## Usage

### API Endpoints

- **Account**
  - `POST /accounts/` - Create a new account
  - `GET /accounts/` - Retrieve all accounts

- **Campaign**
  - `POST /campaigns/` - Create a new campaign
  - `GET /campaigns/` - Retrieve all campaigns

- **Ad Group**
  - `POST /ad_groups/` - Create a new ad group
  - `GET /ad_groups/` - Retrieve all ad groups

- **Ad**
  - `POST /ads/` - Create a new ad
  - `GET /ads/` - Retrieve all ads

- **Negative Keyword**
  - `POST /negative_keywords/` - Create a new negative keyword
  - `GET /negative_keywords/` - Retrieve all negative keywords

- **AI Integration**
  - `POST /ai/chat` - Generate a response using OpenAI's API

### Frontend

The frontend is a simple HTML page styled with Bootstrap. It provides a basic structure with a header, main content area, and footer.

### Running Tests

To run the tests, use the following command:

```bash
pytest
```

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit them (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a new Pull Request.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more information.
