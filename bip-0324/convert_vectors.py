import sys
import csv
with open('packet_encoding_test_vectors.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    quote = lambda x: "\"" + x + "\""
    for row in reader:
        args = [
            row['in_idx'],
            quote(row['in_priv_ours']),
            quote(row['in_ellswift_ours']),
            quote(row['in_ellswift_theirs']),
            "true" if int(row['in_initiating']) else "false",
            quote(row['in_contents']),
            row['in_multiply'],
            quote(row['in_aad']),
            "true" if int(row['in_ignore']) else "false",
            quote(row['mid_send_garbage_terminator']),
            quote(row['mid_recv_garbage_terminator']),
            quote(row['out_session_id']),
            quote(row['out_ciphertext']),
            quote(row['out_ciphertext_endswith'])
        ]
        print("    TestBIP324PacketVector(\n        " + ",\n        ".join(args) + ");")
