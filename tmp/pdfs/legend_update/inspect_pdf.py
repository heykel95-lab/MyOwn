import re
import sys
import zlib
from pathlib import Path


pdf = Path(sys.argv[1]).read_bytes()
for match in re.finditer(rb"(?m)^(\d+) 0 obj\s*(.*?)\s*endobj", pdf, re.S):
    object_id = int(match.group(1))
    body = match.group(2)
    stream_match = re.search(rb"stream\r?\n(.*?)\r?\nendstream", body, re.S)
    if not stream_match:
        continue
    stream = stream_match.group(1)
    decoded = stream
    if b"/FlateDecode" in body[:stream_match.start()]:
        try:
            decoded = zlib.decompress(stream)
        except zlib.error:
            continue
    bt = decoded.count(b"BT")
    tj = decoded.count(b"Tj") + decoded.count(b"TJ")
    if bt or tj or len(decoded) > 10000:
        print(object_id, len(stream), len(decoded), "BT", bt, "text", tj)
        if len(sys.argv) > 2 and object_id == int(sys.argv[2]):
            Path(sys.argv[3]).write_bytes(decoded)
