import sys
if __name__ == "__main__":
    filename = sys.argv[1]
    f = open(filename, 'r', encoding="utf8")
    out = open(f"{filename}out.txt", 'w')
    output = []
    print(filename)
    for line in f.readlines():
        if line.startswith("https://open.spotify.com/track/"):
            track_id = line.split('track/')[1].split('?')[0]
            out.write(f"spotify:track:{track_id},")
    f.close()
    out.close()