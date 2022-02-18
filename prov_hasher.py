import hashlib

o = open('list_of_individual_hashes.txt', 'w')
p = open('provenance_hash.txt', 'w')
provenance_hash = ''
num_nfts = 3
for i in range(num_nfts):
    #NOTE: Don't forget to add location of your nft metadata fileson local machine below
    nft_metadata_name = "/location/of/your/NFTs/" + str(i) + ".json"
    with open(nft_metadata_name, "rb") as f:
        bytes = f.read()  # read entire nft_metadata_ as bytes
        readable_hash = hashlib.sha256(bytes).hexdigest()
        print(readable_hash)
        o.write(readable_hash + "\n")
        provenance_hash = provenance_hash + readable_hash
else:
    print("Finally finished!")
    p.write(provenance_hash + "\n")
