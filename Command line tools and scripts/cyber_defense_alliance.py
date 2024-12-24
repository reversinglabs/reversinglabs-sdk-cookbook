import json
import argparse
import configparser
import sys

from ReversingLabs.SDK.ticloud import AdvancedSearch, FileAnalysis


def parse_arguments():
	parser = argparse.ArgumentParser()
	parser.add_argument("--url", type=str, help="ReversingLabs host (e.g., https://data.reversinglabs.com)")
	parser.add_argument("-u", "--username", type=str, help="ReversingLabs account username")
	parser.add_argument("-p", "--password", type=str, help="ReversingLabs account password")
	parser.add_argument("--since", type=str, help="Start date for first seen range (e.g., 2019-01-03T04:10:00Z)")
	parser.add_argument("--until", type=str, help="End date for first seen range (e.g., 2019-01-03T04:10:00Z)")
	parser.add_argument("--family", type=str, help="Threat family name")
	parser.add_argument("--output", type=str, help="Output file name")
	parser.add_argument("--config", type=str, help="Alternate config file path (defaults to config.ini)")
	return parser.parse_args()


def load_config(args):
	config = configparser.ConfigParser()
	config.read(args.config if args.config else 'config.ini')
	return config


def get_config_value(args, config, key):
	if getattr(args, key) is not None:
		return getattr(args, key)
	elif key in config["DEFAULT"]:
		return config["DEFAULT"][key]
	elif key == "url":
		return "https://data.reversinglabs.com"
	else:
		print(f"Missing argument {key} - Try running '{sys.argv[0]} -h' for help")
		sys.exit(0)


def perform_advanced_search(advanced_search, first_seen_from, first_seen_to, family_name, file_analysis):
	more_pages = True
	next_page = 1
	output_results = []

	while more_pages:
		response = advanced_search.search(
			query_string=f"firstseen:[{first_seen_from} TO {first_seen_to}] threatname:*{family_name}",
			page_number=next_page,
			records_per_page=100
		)

		response_json = response.json()

		total_count = response_json.get("rl", {}).get("web_search_api", {}).get("total_count")
		if not total_count:
			print("No files found within range")
			sys.exit(0)

		search_entries = response_json.get("rl", {}).get("web_search_api", {}).get("entries", [])
		next_page = response_json.get("rl", {}).get("web_search_api", {}).get("next_page")
		more_pages = response_json.get("rl", {}).get("web_search_api", {}).get("more_pages")

		output_data = {}

		for entry in search_entries:
			sha1 = entry["sha1"]
			output_data[sha1] = {
				"first_seen": entry["firstseen"],
				"sha1": sha1,
				"md5": entry["md5"],
				"threat_name": entry["threatname"],
				"file_type": entry["sampletype"]
			}

			output_results.extend(fetch_sample_details(search_entries, file_analysis, sha1, output_data))

	return output_results


def fetch_sample_details(search_entries, file_analysis, sha1, output_data):
	hashes = [entry["sha256"] for entry in search_entries]
	if not hashes:
		print("Empty hashes list")
		return []

	response = file_analysis.get_analysis_results(
		hash_input=hashes
	)

	entries = response.json().get("rl", {}).get("entries", [])
	for entry in entries:
		if "dynamic_analysis" in entry:
			output_data[sha1]["dynamic_analysis"] = parse_dynamic_analysis(dynamic_analysis=entry["dynamic_analysis"])

	return list(output_data.values())

def parse_dynamic_analysis(dynamic_analysis):
	analysis_results = []
	for da in dynamic_analysis.get("entries", []):
		result = {}

		if "dynamic_analysis_report" in da:
			result["network"] = da["dynamic_analysis_report"].get("network", {})
			result["mutexes"] = da["dynamic_analysis_report"].get("summary", {}).get("mutexes", [])

		if "dynamic_analysis_report_joe_sandbox" in da:
			result["network"] = da["dynamic_analysis_report_joe_sandbox"].get("network", {})
			result["mutexes"] = da["dynamic_analysis_report_joe_sandbox"].get("summary", {}).get("mutexes", [])

		analysis_results.append(result)

	return analysis_results


def save_results(output_results, output_file):
	with open(output_file, "w") as f:
		json.dump(output_results, f, indent=4)


def main():
	args = parse_arguments()
	config = load_config(args)

	first_seen_from = get_config_value(args, config, "since")
	first_seen_to = get_config_value(args, config, "until")
	family_name = get_config_value(args, config, "family")
	url = get_config_value(args, config, "url")
	username = get_config_value(args, config, "username")
	password = get_config_value(args, config, "password")
	output_file = args.output or config["DEFAULT"].get("output", "output.json")

	advanced_search = AdvancedSearch(
		host=url,
		username=username,
		password=password
	)

	file_analysis = FileAnalysis(
		host=url,
		username=username,
		password=password
	)

	output_results = perform_advanced_search(
		advanced_search=advanced_search,
		first_seen_from=first_seen_from,
		first_seen_to=first_seen_to,
		family_name=family_name,
		file_analysis=file_analysis
	)

	print(f"Total interesting samples: {len(output_results)}")
	save_results(output_results, output_file)


if __name__ == "__main__":
	main()
