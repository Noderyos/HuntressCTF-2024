# Keyboard Junkie

## Solver : `Noderyos`

I used `tshark -r keyboard_junkie -Y 'usb.capdata && usb.data_len == 8' -T fields -e usb.capdata | sed 's/../:&/g2' > keystrokes.txt` to extract USB data from the PCAP

I then used [ctf-usb-keyboard-parser](https://github.com/TeamRocketIst/ctf-usb-keyboard-parser) to convert extracted data to text

## Flag : `flag{f7733e0093b7d281dd0a30fcf34a9634}`
