# Use pyshark as an alternative to scapy for pcapng file analysis
import re
import pyshark

# Load the pcapng file using pyshark
cap = pyshark.FileCapture("monkey-see.pcapng", use_json=True, include_raw=True)

# Search for BtSCTF{...} pattern in packet layers
flag_pattern = re.compile(rb"BtSCTF\{.*?\}")
found_flags = set()

for pkt in cap:
    print(pkt)
    try:
        if hasattr(pkt, "data") and hasattr(pkt.data, "data"):
            raw_data = bytes.fromhex(pkt.data.data.replace(":", ""))
            matches = flag_pattern.findall(raw_data)
            found_flags.update(matches)
    except Exception:
        continue

cap.close()

found_flags = [flag.decode("utf-8", errors="ignore") for flag in found_flags]
found_flags
