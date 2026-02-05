# my user agent is : Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36
# print(r.html.find('title' , first= True).text) 
# requests-html==0.10.0
# lxml==4.9.1 (first install  this one)

"""Get weather for a fixed location (patna) using Google search.

This module tries to use requests_html (fast if available). If that
isn't installed or lxml wheel isn't available, it falls back to plain
requests + BeautifulSoup so the project can run without compiling lxml.
"""
from typing import Optional

import requests
from bs4 import BeautifulSoup


def _parse_with_requests(html: str) -> Optional[str]:
    soup = BeautifulSoup(html, "html.parser")
    # Google weather uses ids wob_tm (temperature) and wob_dc (description)
    temp_tag = soup.find(id="wob_tm")
    desc_tag = soup.find(id="wob_dc")
    # unit is inside div.vk_bk.wob-unit span.wob_t
    unit_tag = soup.select_one("div.vk_bk.wob-unit span.wob_t")

    if temp_tag and desc_tag:
        temp = temp_tag.get_text(strip=True)
        unit = unit_tag.get_text(strip=True) if unit_tag else "C"
        desc = desc_tag.get_text(strip=True)
        return f"{temp} {unit} {desc}"
    return None


def Weather():
    # Prefer a simple public API (wttr.in) which doesn't require lxml or JS.
    try:
        api_url = "https://wttr.in/patna?format=j1"
        resp = requests.get(api_url, timeout=10)
        if resp.status_code == 200:
            j = resp.json()
            # Structure: current_condition[0]['temp_C'], ['weatherDesc'][0]['value']
            cc = j.get('current_condition')
            if cc and isinstance(cc, list) and cc:
                temp = cc[0].get('temp_C')
                desc_list = cc[0].get('weatherDesc') or []
                desc = desc_list[0].get('value') if desc_list else ''
                unit = 'C'
                return f"{temp} {unit} {desc}"
    except Exception:
        # if wttr.in fails, fall back to the previous Google parsing code
        pass

    # Last resort: try Google parsing (requests + bs4)
    query = "patna"
    url = f"https://www.google.com/search?q=weather+{query}"
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"
        )
    }
    try:
        resp = requests.get(url, headers=headers, timeout=10)
        parsed = _parse_with_requests(resp.text)
        if parsed:
            return parsed
    except Exception:
        return "Unable to fetch weather"

    return "Unable to parse weather"


  
