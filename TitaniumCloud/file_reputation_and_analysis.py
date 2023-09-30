from ReversingLabs.SDK.ticloud import FileReputation, AVScanners, FileAnalysis, RHA1FunctionalSimilarity
import json


CREDENTIALS = json.load(open("ticloud_credentials.json"))
USERNAME = CREDENTIALS.get("username")
PASSWORD = CREDENTIALS.get("password")

FILE_HASH = "21841b32c6165b27dddbd4d6eb3a672defe54271"


file_reputation = FileReputation(
    host="https://data.reversinglabs.com",
    username=USERNAME,
    password=PASSWORD,
    user_agent="ReversingLabs SDK cookbook"
)

reputation = file_reputation.get_file_reputation(
    hash_input=FILE_HASH
)

reputation_text = reputation.text
print(reputation_text)


av_scanners = AVScanners(
    host="https://data.reversinglabs.com",
    username=USERNAME,
    password=PASSWORD,
    user_agent="ReversingLabs SDK cookbook"
)

scanner_results = av_scanners.get_scan_results(
    hash_input=FILE_HASH
)

results_text = scanner_results.text
print(results_text)


analysis = FileAnalysis(
    host="https://data.reversinglabs.com",
    username=USERNAME,
    password=PASSWORD,
    user_agent="ReversingLabs SDK cookbook"
)

analysis_results = analysis.get_analysis_results(
    hash_input=FILE_HASH
)

analysis_text = analysis_results.text
print(analysis_text)


similarity = RHA1FunctionalSimilarity(
    host="https://data.reversinglabs.com",
    username=USERNAME,
    password=PASSWORD,
    user_agent="ReversingLabs SDK cookbook"
)

similarity_results = similarity.get_similar_hashes(
    hash_input=FILE_HASH
)

similarity_text = similarity_results.text
print(similarity_text)


all_pages = similarity.get_similar_hashes_aggregated(
    hash_input=FILE_HASH
)

print(all_pages)


all_pages = similarity.get_similar_hashes_aggregated(
    hash_input=FILE_HASH,
    extended_results=True,
    classification="MALICIOUS",
    max_results=300,
    results_per_page=50
)

print(all_pages)