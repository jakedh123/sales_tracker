import pytest
from scrapers.company_info import CompanyInfoScraper

def test_company_info_scraper_initialization():
    scraper = CompanyInfoScraper()
    assert scraper is not None

def test_extract_company_name():
    scraper = CompanyInfoScraper()
    # Add your test cases here
    pass