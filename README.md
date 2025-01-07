# Sales Tracker

A powerful Python tool that automatically gathers and analyzes company information relevant for sales teams. This tool scrapes various data sources to provide comprehensive insights about target companies.

## Features

- **Company Information Scraping**
  - Basic company details (size, industry, locations)
  - Contact information
  - Technology stack detection
  - Company structure and hierarchy

- **News and Updates**
  - Recent company news
  - Press releases
  - Market developments
  - Sentiment analysis

- **Social Media Analysis**
  - LinkedIn presence
  - Twitter activity
  - Social media engagement metrics
  - Recent campaigns and initiatives

- **Sales Intelligence**
  - Potential opportunity identification
  - Risk factor analysis
  - Recommended approach strategies
  - Market position insights

## Installation

1. Clone the repository:
```bash
git clone https://github.com/jakedh123/sales_tracker.git
cd sales_tracker
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install required packages:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
Create a `.env` file in the root directory with the following variables:
```
LINKEDIN_API_KEY=your_linkedin_api_key
TWITTER_API_KEY=your_twitter_api_key
SERPAPI_KEY=your_serpapi_key
```

## Usage

Basic usage:
```bash
python sales_tracker.py https://company-website.com
```

This will generate a comprehensive report including:
- Company profile
- Recent developments
- Social media presence
- Potential opportunities and risks
- Recommended approaches

## Project Structure

```
sales_tracker/
├── scrapers/
│   ├── company_info.py     # Company information scraper
│   ├── news_scraper.py     # News and updates scraper
│   └── social_media.py     # Social media data scraper
├── utils/
│   ├── data_processor.py   # Data processing utilities
│   └── report_generator.py # Report generation utilities
├── config.py              # Configuration settings
├── requirements.txt       # Project dependencies
├── sales_tracker.py       # Main script
└── README.md             # This file
```

## API Keys Required

- LinkedIn API Key: For accessing company information on LinkedIn
- Twitter API Key: For social media analysis
- SerpAPI Key: For news and search results

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Disclaimer

This tool is intended for legitimate sales intelligence gathering only. Please ensure compliance with all applicable terms of service, laws, and regulations when using this tool.

## Support

For support, please open an issue in the GitHub repository.