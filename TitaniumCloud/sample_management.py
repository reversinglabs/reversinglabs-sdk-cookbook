from ReversingLabs.SDK.ticloud import FileUpload, FileDownload, ReanalyzeFile, DeleteFile
import json


CREDENTIALS = json.load(open("ticloud_credentials.json"))
USERNAME = CREDENTIALS.get("username")
PASSWORD = CREDENTIALS.get("password")


FILE_NAME = "file_name_placeholder"

file_upload = FileUpload(
    host="https://data.reversinglabs.com",
    username=USERNAME,
    password=PASSWORD,
    user_agent="ReversingLabs SDK cookbook"
)

upload_response = file_upload.upload_sample_from_path(file_path=FILE_NAME)

status_code = upload_response.status_code
print(status_code)


FILE_HASH = "file_hash_placeholder"

file_download = FileDownload(
    host="https://data.reversinglabs.com",
    username=USERNAME,
    password=PASSWORD,
    user_agent="ReversingLabs SDK cookbook"
)

download_response = file_download.download_sample(hash_input=FILE_HASH)

with open("downloaded_file", "wb") as file_handle:
    file_handle.write(download_response.content)


reanalyze = ReanalyzeFile(
    host="https://data.reversinglabs.com",
    username=USERNAME,
    password=PASSWORD,
    user_agent="ReversingLabs SDK cookbook"
)

reanalyze_response = reanalyze.reanalyze_samples(sample_hashes=FILE_HASH)

response_text = reanalyze_response.text
print(response_text)


delete_file = DeleteFile(
    host="https://data.reversinglabs.com",
    username=USERNAME,
    password=PASSWORD,
    user_agent="ReversingLabs SDK cookbook"
)

delete_response = delete_file.delete_samples(sample_hashes=FILE_HASH)

response_text = delete_response.text
print(response_text)