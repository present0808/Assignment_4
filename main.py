import pydivert

print("start")
with pydivert.WinDivert("tcp and tcp.PayloadLength > 0") as p:
    for packet in p:
        if(packet.is_outbound):
            data = packet.tcp.payload
            data = data.replace(B'Accept-Encoding: gzip', B'Accept-Encoding:     ')
            packet.tcp.payload = data
        if(packet.is_inbound):
            data = packet.tcp.payload
            data = data.replace(B'Michael', B'Gilbert')
            packet.tcp.payload = data
        p.send(packet, recalculate_checksum=True)

print("finish")