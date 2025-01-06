import os
import requests

# List of proteome IDs
proteome_ids = []
with open({UNIPROT_LIST_FILE}, "r") as f:
    for l in f:
        if l.startswith("UP"):
            proteome_ids.append(l.strip())

# Directory to save FASTA files
output_dir = {OUTPUT_DIRECTORY}
os.makedirs(output_dir, exist_ok=True)

# Base URL for the UniProt API
base_url = "https://rest.uniprot.org/uniprotkb/stream?compressed=false&format=fasta&includeIsoform=true"

for proteome_id in proteome_ids:
    # Construct the query URL
    query_url = f"{base_url}&query=(proteome:{proteome_id})"
    print(f"Downloading {proteome_id}...")
    
    # Send request
    response = requests.get(query_url)
    if response.status_code == 200:
        # Save the FASTA file
        output_path = os.path.join(output_dir, f"{proteome_id}.fasta")
        with open(output_path, "w") as f:
            f.write(response.text)
        print(f"Saved to {output_path}")
    else:
        print(f"Failed to download {proteome_id}. Status code: {response.status_code}")
