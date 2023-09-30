from ReversingLabs.SDK.ticloud import AnalyzeURL, URLThreatIntelligence, DomainThreatIntelligence, IPThreatIntelligence
import json


CREDENTIALS = json.load(open("ticloud_credentials.json"))
USERNAME = CREDENTIALS.get("username")
PASSWORD = CREDENTIALS.get("password")

DOMAIN = "kosmikband.com"


domain_ti = DomainThreatIntelligence(
    host="https://data.reversinglabs.com",
    username=USERNAME,
    password=PASSWORD,
    user_agent="ReversingLabs SDK cookbook"
)

domain_report = domain_ti.get_domain_report(domain=DOMAIN)

report_text = domain_report.text
print(report_text)


domain_to_ip = domain_ti.domain_to_ip_resolutions(domain=DOMAIN)

domain_to_ip_text = domain_to_ip.text
print(domain_to_ip_text)

resolved_ips = domain_to_ip.json()
resolutions = resolved_ips.get("rl").get("resolutions")
IP_ADDR = resolutions[0].get("ip")


ip_ti = IPThreatIntelligence(
    host="https://data.reversinglabs.com",
    username=USERNAME,
    password=PASSWORD,
    user_agent="ReversingLabs SDK cookbook"
)

ip_urls = ip_ti.urls_from_ip(ip_address=IP_ADDR)

ip_urls_text = ip_urls.text
print(ip_urls_text)

associated_urls = ip_urls.json()
url_list = associated_urls.get("rl").get("urls")
URL = url_list[0].get("url")


url_ti = URLThreatIntelligence(
    host="https://data.reversinglabs.com",
    username=USERNAME,
    password=PASSWORD,
    user_agent="ReversingLabs SDK cookbook"
)

url_report = url_ti.get_url_report(url_input=URL)

report_text = url_report.text
print(report_text)

dl_files = url_ti.get_downloaded_files(url_input=URL)

dl_files_text = dl_files.text
print(dl_files_text)


analyze = AnalyzeURL(
    host="https://data.reversinglabs.com",
    username=USERNAME,
    password=PASSWORD,
    user_agent="ReversingLabs SDK cookbook"
)

analyze_response = analyze.submit_url(url_input=URL)

analyze_response_text = analyze_response.text
print(analyze_response_text)